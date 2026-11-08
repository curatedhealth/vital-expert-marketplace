#!/usr/bin/env python3
"""Integrated diligence report assembler (plugin level). Deterministic, offline, standard library only.

Usage: assemble_report.py manifest.json [--thresholds t.json] [--lines extra.json] [--out report.json] [--md report.md] [--pretty]
Exit 0 ok, 1 hard error (E_*), 2 usage or file error. Soft issues are reported as flags, not failures.

What it does. It reads the outputs of the nine skills for one asset (company mode: one set per asset, then a
roll-up) and assembles a report in which every line points to a register row ("pointer"). It adds no finding
of its own: it counts, lists and compares what the registers already say. It recommends nothing and certifies
nothing; the deal lead (BD head or investment lead) signs, a human-only gate.

Manifest: {"mode": "asset"|"company", "as_of": "YYYY-MM-DD", "prepared_by": str|null, "reviewed_by": str|null,
           "version": str, "release_state": str,
           "company_outputs": {"E": path|null},                      # company mode only; shared financial register
           "assets": [{"name": str, "outputs": {"F","A","B","C","D","E","G","R","H": path|null}}]}
A null or absent path is a missing workstream output: a GAP with its consequence, not an error.

Each output is a JSON register (see templates/integrated-diligence-report.schema.json for the fields read):
  common: failure_mode_screen [{id|mode_id, state, register_ref?}], gaps [{field, missing, why_it_matters}],
          reviewer {name, date} (null = UNSIGNED), and any field whose value is exactly "HUMAN ONLY".
  A: rows [{id, ...}]    B: timeline {range {low_months, mid_months, high_months}}, assumptions {route, review_months}?
  C: dates (the exclusivity_dates.py output)    D: routes [{market, route, disposition, clock}]
  E: licensor_obligations [{licensor, ...}]     F: any list of rows with ids    G: differentiation [{claim, state, basis}]
  R: countries [{country, state, launch_year {early, mid, late}, exclusivity_end_year, loe_applied}]  (revenue and price register)
  H: conditions [{id, state, owner}], options

Pointer: "<code>:<path>" or "<asset>/<code>:<path>"; code in F A B C D E G R H; path as in a.b[0].c or rows[R1]
(an element of a list is found by position or by its id). "MANIFEST:<code>" points at a missing output.
A line whose pointer does not resolve fails the check (E_POINTER); an added line with no pointer fails (E_UNSUPPORTED).

RULES (all team-set defaults, not facts; override with --thresholds):
  R-STATUS  ENGINEERING RULE. Proposed status per workstream from register counts: RED if the output is missing, or
            triggered failure modes >= red_triggered (default 2), or open GAPs >= red_gaps (default 5), or [CHECK]
            items >= red_checks (default 8); GREEN if there is no triggered failure mode, no open GAP, no [CHECK] item
            and the register sign-off (reviewer name and date) is closed; YELLOW otherwise. The deal lead confirms or
            changes it. Reason: no published standard sets a traffic-light threshold; a practitioner guide (Seimetz
            2020, VP-A-142) reports findings with traffic-light style severity but gives no thresholds.
  R-CONF-1  B vs C. Approval date = as_of + B months (CONVENTION: 30.4375 days a month) at low, mid and high; shown beside
            each C effective-exclusivity date (all patents; composition only) per market. Conflict if the date is on or
            before the high approval date; optional min_years_remaining (default none) flags a shorter remainder at mid.
  R-CONF-2  D vs B. B states the route and review months its timeline assumes (assumptions). Conflict if D lists no such
            route, lists it with a disposition other than candidate, or states a longer verified clock. If B states none,
            the pair is "not comparable".
  R-CONF-3  G vs A/F. A differentiation claim marked supported whose basis does not resolve to a row of A or F (or has no
            basis, or A and F are absent) is a conflict.
  R-CONF-4  H vs other workstreams. An H condition marked met whose owner workstream is missing or has an open sign-off is
            a conflict; one marked met whose owner has open GAPs is a conflict; any other condition whose owner has open
            GAPs is listed as a dependency.
  R-CONF-5  E vs C. A licensor named in E that does not appear in the C ownership and licence chain is a conflict.
  R-CONF-6  R vs B. Launch year per computed country in R (early, mid, late) against the approval year implied by B at
            low, mid and high (as_of + B months, same convention as R-CONF-1). Conflict if a launch year falls before the
            approval year it is paired with (launch cannot precede approval). Added 7 November 2026 (nine-workstream version).
  R-CONF-7  R vs C. R's exclusivity end year per computed country (where erosion starts the year after) against the
            effective exclusivity years in C (all patents; composition only) for the same market (US; DE FR IT ES map to EU;
            other markets are not comparable). Conflict if R's year equals neither C year. Added 7 November 2026.
  R-RANK    Top risks: cross-workstream conflicts first (3), then triggered failure modes and H conditions marked not met
            (2), then failure modes marked cannot tell (1); ties by workstream order F A B C D E G R H; top_n default 10.
"""
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

ORDER = ["F", "A", "B", "C", "D", "E", "G", "R", "H"]
NAMES = {"F": "Scientific validity and mechanism", "A": "Clinical data quality", "B": "Development risk and timeline",
         "C": "IP portfolio and exclusivity", "D": "Regulatory pathway and legal risk", "E": "Financial statements and tax",
         "G": "Market opportunity and competitive position", "R": "Revenue and price ranges", "H": "Commercial viability"}
SKILLS = {"F": "assess-scientific-validity-and-moa", "A": "review-clinical-data-quality",
          "B": "estimate-development-risk-and-timeline", "C": "assess-ip-portfolio-and-freedom-to-operate",
          "D": "evaluate-regulatory-pathway-and-legal-risk", "E": "analyze-financial-statements-and-tax",
          "G": "evaluate-market-opportunity-and-competitive-position", "R": "forecast-revenue-and-price-ranges", "H": "determine-commercial-viability"}
CODE_OF_SKILL = {v: k for k, v in SKILLS.items()}
BLOCKS = {  # what a missing or open item holds up, from the relations in the capability map
    "F": "G differentiation claims that rest on mechanism rows cannot be checked; a clinical row whose mechanism rationale is a GAP stays a GAP",
    "A": "B (probability and timeline), D (routes), G (differentiation) and H (conditions) rest on this register",
    "B": "D refines B's timeline; H reads it; the launch-versus-exclusivity check needs it",
    "C": "D requires it; H's exclusivity condition and the launch-versus-exclusivity check need it; the licence cross-check with E needs it",
    "D": "H reads the pathway map; route and review-clock statements and the inspection and statement-versus-record risks depend on it",
    "E": "runway, financing, licensor obligations and tax flags are not covered; the licensor cross-check with C needs it",
    "G": "H requires it; population, competitors and differentiation are not covered",
    "R": "H's price and revenue condition and the launch-versus-timeline and erosion-versus-exclusivity checks need it",
    "H": "the commercial conditions and analog range are absent; decision options rest on the other workstreams only",
}
MISSING_TEXT = {
    "F": "no mechanism register: target, human evidence, reproduction and class precedent are not shown",
    "A": "no clinical evidence register: no row of clinical evidence can be pointed to",
    "B": "no probability or timeline range",
    "C": "no exclusivity register: no exclusivity date can be pointed to",
    "D": "no pathway map or legal-and-regulatory risk register",
    "E": "no financial register: runway, financing and tax flags are absent",
    "G": "no market register: no population, competitor or differentiation row",
    "R": "no revenue and price ranges: no country revenue, list price or sensitivity row",
    "H": "no commercial option set or analog range",
}
DEFAULTS = {"red_triggered": 2, "red_gaps": 5, "red_checks": 8, "top_n": 10, "min_years_remaining": None}
RECOMMEND = [
    r"\b(we|i)\s+(strongly\s+)?(recommend|advise|suggest)\b", r"\bis\s+recommended\b", r"\bshould\s+(sign|proceed|bid|walk away|pass)\b",
    r"\b(recommend|advise)(ed|s)?\s+(to\s+|that\s+)?(sign|proceed|bid|pass)\b", r"\b(safe|ready|good)\s+to\s+sign\b",
    r"\bgo\s+ahead\s+(and\s+)?(sign|with the deal)\b", r"\b(certif(y|ies|ied)|attest(s|ed)?)\b", r"\bnothing\s+blocks\s+signing\b",
    r"\bthe\s+asset\s+is\s+(not\s+)?(viable|worth)\b", r"\bpreferred\s+option\b", r"\bbest\s+option\b",
]
OPTION_NAMES = ["sign", "sign with conditions", "do not sign"]


class ReportError(Exception):
    def __init__(self, code, message):
        super().__init__(f"{code}: {message}")
        self.code, self.message = code, message


# ---------------------------------------------------------------- pointers
TOKEN = re.compile(r"([A-Za-z_][\w\-]*)|\[([^\]]+)\]")
ANATOMY_PTR = re.compile(r"^([A-Za-z0-9._-]+/)?[A-Za-z0-9._-]+:[A-Za-z0-9_.\[\]-]+$")   # anatomy v1.2 section 11 pointer_regex
PTR = re.compile(r"^(?:(?P<asset>[^/:]+)/)?(?P<code>[FABCDEGRH]|MANIFEST):(?P<path>.*)$")
ID_KEYS = ("id", "mode_id", "finding_id", "family", "name", "agent", "claim", "country")


def walk_path(root, path):
    cur = root
    pos = 0
    path = path.strip().lstrip(".")
    while pos < len(path):
        if path[pos] == ".":
            pos += 1
            continue
        m = TOKEN.match(path, pos)
        if not m:
            return False, None
        pos = m.end()
        key, idx = m.group(1), m.group(2)
        if key is not None:
            if not isinstance(cur, dict) or key not in cur:
                return False, None
            cur = cur[key]
        else:
            if not isinstance(cur, list):
                return False, None
            if idx.isdigit():
                i = int(idx)
                if i >= len(cur):
                    return False, None
                cur = cur[i]
            else:
                hit = [x for x in cur if isinstance(x, dict) and any(str(x.get(k)) == idx for k in ID_KEYS)]
                if len(hit) != 1:
                    return False, None
                cur = hit[0]
    return True, cur


class Store:
    """The loaded outputs of one report (one asset)."""

    def __init__(self, name, bundles, missing):
        self.name, self.bundles, self.missing = name, bundles, missing

    def resolve(self, ptr, others=None):
        m = PTR.match(ptr or "")
        if not m:
            return False, None
        if m.group("path") and not ANATOMY_PTR.match(ptr):
            return False, None   # a pointer with a path must also follow the anatomy pointer syntax <skill-code>:<path>
        asset, code, path = m.group("asset"), m.group("code"), m.group("path")
        store = self
        if asset and asset != self.name:
            store = (others or {}).get(asset)
            if store is None:
                return False, None
        if code == "MANIFEST":
            return (path in store.missing, {"missing": path}) if path in store.missing else (False, None)
        if code not in store.bundles:
            return False, None
        return walk_path(store.bundles[code], path)


def row_text(v):
    if isinstance(v, str):
        return v
    if isinstance(v, dict):
        for k in ("text", "finding", "description", "claim", "detail", "missing", "note", "condition", "field", "target", "agent", "type"):
            if isinstance(v.get(k), str) and v[k].strip():
                return v[k].strip()
        s = json.dumps(v, ensure_ascii=False)
        return s if len(s) <= 140 else s[:137] + "..."
    return json.dumps(v)


# ---------------------------------------------------------------- loading
def load_json(path):
    try:
        return json.loads(Path(path).read_text())
    except FileNotFoundError:
        raise ReportError("E_MANIFEST", f"file not found: {path}")
    except json.JSONDecodeError as ex:
        raise ReportError("E_MANIFEST", f"{path}: not valid JSON ({ex})")


def parse_date(v, field):
    try:
        y, m, d = (int(x) for x in str(v).split("-"))
        return date(y, m, d)
    except Exception:
        raise ReportError("E_DATE", f"{field}: expected YYYY-MM-DD, got {v!r}")


def check_unknown(o, where):
    if isinstance(o, str) and o.strip().lower() == "unknown":
        raise ReportError("E_UNKNOWN", f"{where}: the value 'unknown' is rejected; absence is a GAP with a consequence")
    if isinstance(o, dict):
        for k, v in o.items():
            check_unknown(v, f"{where}.{k}")
    if isinstance(o, list):
        for i, v in enumerate(o):
            check_unknown(v, f"{where}[{i}]")


def load_manifest(path):
    base = Path(path).resolve().parent
    m = load_json(path)
    if m.get("mode") not in ("asset", "company"):
        raise ReportError("E_MODE", "mode must be asset or company")
    parse_date(m.get("as_of"), "as_of")
    assets = m.get("assets")
    if not isinstance(assets, list) or not assets:
        raise ReportError("E_MANIFEST", "assets: at least one asset is required")
    if m["mode"] == "asset" and len(assets) != 1:
        raise ReportError("E_MODE", "asset mode takes exactly one asset; use company mode for several")
    names = [a.get("name") for a in assets]
    if any(not n or "/" in n or ":" in n for n in names) or len(set(names)) != len(names):
        raise ReportError("E_MANIFEST", "asset names must be unique, non-empty and free of '/' and ':'")
    shared = m.get("company_outputs") or {}
    stores = []
    for a in assets:
        outs = dict(a.get("outputs") or {})
        for k in outs:
            if k not in ORDER:
                raise ReportError("E_MANIFEST", f"{a['name']}: unknown workstream code {k!r}")
        if m["mode"] == "company" and not outs.get("E") and shared.get("E"):
            outs["E"] = shared["E"]
        bundles, missing = {}, []
        for c in ORDER:
            p = outs.get(c)
            if not p:
                missing.append(c)
                continue
            b = load_json(base / p)
            if not isinstance(b, dict):
                raise ReportError("E_MANIFEST", f"{a['name']}/{c}: output must be a JSON object")
            check_unknown(b, f"{a['name']}/{c}")
            bundles[c] = b
        stores.append(Store(a["name"], bundles, missing))
    return m, stores


# ---------------------------------------------------------------- metrics
def strings_with(o, needle, path=""):
    out = []
    if isinstance(o, str):
        if needle in o:
            out.append(path)
    elif isinstance(o, dict):
        for k, v in o.items():
            out += strings_with(v, needle, f"{path}.{k}" if path else k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            out += strings_with(v, needle, f"{path}[{i}]")
    return out


def human_only_fields(b):
    out = []
    for k, v in b.items():
        if v == "HUMAN ONLY":
            out.append(k)
        elif isinstance(v, dict):
            out += [f"{k}.{kk}" for kk, vv in v.items() if vv == "HUMAN ONLY"]
    return out


def signed(b):
    r = b.get("reviewer")
    return isinstance(r, dict) and bool(r.get("name")) and bool(r.get("date"))


def metrics(code, b, T):
    fms = b.get("failure_mode_screen") or []
    trig = [(i, f) for i, f in enumerate(fms) if isinstance(f, dict) and f.get("state") == "triggered"]
    cant = [(i, f) for i, f in enumerate(fms) if isinstance(f, dict) and f.get("state") == "cannot tell"]
    gaps = b.get("gaps") or []
    checks = strings_with(b, "[CHECK]")
    sg = signed(b)
    if len(trig) >= T["red_triggered"] or len(gaps) >= T["red_gaps"] or len(checks) >= T["red_checks"]:
        st = "red"
    elif not trig and not gaps and not checks and sg:
        st = "green"
    else:
        st = "yellow"
    return {"triggered": trig, "cannot_tell": cant, "gaps": gaps, "checks": checks, "signed": sg, "status": st,
            "human_only": human_only_fields(b), "screen_present": "failure_mode_screen" in b}


def ptr(code, path):
    return f"{code}:{path}"


# ---------------------------------------------------------------- conflicts
def add_months(d, months):
    return d + timedelta(days=round(months * 30.4375))


def conf(rid, status, left, right, detail, kind="conflict"):
    return {"rule": rid, "status": status, "type": kind, "left": left, "right": right, "detail": detail}


def side(code, pointer, text):
    return {"workstream": code, "pointer": pointer, "text": text}


def conflicts_for(store, M, T, as_of):
    B, out, checks = store.bundles, [], []
    # R-CONF-1 launch timing (B) vs effective exclusivity (C)
    r1 = []
    rng = (B.get("B", {}).get("timeline") or {}).get("range") if "B" in B else None
    cd = (B.get("C", {}).get("dates") or {}).get("markets") if "C" in B else None
    if not rng or not cd:
        miss = [x for x, ok in (("B timeline range", bool(rng)), ("C dates", bool(cd))) if not ok]
        r1.append(conf("R-CONF-1", "not comparable", side("B", ptr("B", "timeline.range") if rng else "MANIFEST:B" if "B" in store.missing else "B:", "timeline range" if rng else "absent"),
                       side("C", ptr("C", "dates.markets") if cd else "MANIFEST:C" if "C" in store.missing else "C:", "exclusivity dates" if cd else "absent"),
                       "cannot compare: " + ", ".join(miss) + " missing", "gap"))
    else:
        dates = {k: add_months(as_of, float(rng[f"{k}_months"])) for k in ("low", "mid", "high")}
        for mk, mv in cd.items():
            eff = (mv or {}).get("effective") or {}
            for view in ("effective_all_patents", "effective_composition_only"):
                if not eff.get(view):
                    continue
                end = parse_date(eff[view], f"C dates {mk} {view}")
                rem = {k: round((end - d).days / 365.25, 2) for k, d in dates.items()}
                bad = end <= dates["high"]
                low_t = T.get("min_years_remaining")
                short = low_t is not None and rem["mid"] < float(low_t)
                st = "conflict" if (bad or short) else "no conflict"
                why = []
                if end <= dates["low"]:
                    why.append("exclusivity ends on or before the earliest approval date")
                elif bad:
                    why.append("exclusivity ends inside the approval window (low to high)")
                if short:
                    why.append(f"years remaining at mid ({rem['mid']}) are below the team threshold {low_t}")
                r1.append(conf("R-CONF-1", st,
                               side("B", ptr("B", "timeline.range"), f"approval dates from as_of {as_of}: low {dates['low']}, mid {dates['mid']}, high {dates['high']} ({rng['low_months']}/{rng['mid_months']}/{rng['high_months']} months)"),
                               side("C", ptr("C", f"dates.markets.{mk}.effective"), f"{mk} {view.replace('effective_', '').replace('_', ' ')} ends {end}; years remaining after approval low/mid/high {rem['low']}/{rem['mid']}/{rem['high']}"),
                               "; ".join(why) or "exclusivity ends after the high approval date"))
    # R-CONF-2 regulatory route and timing (D) vs development timeline (B)
    r2 = []
    asm = (B.get("B", {}).get("assumptions") if "B" in B else None) or {}
    routes = (B.get("D", {}).get("routes") if "D" in B else None)
    if "B" not in B or "D" not in B or not asm.get("route"):
        why = "B output missing" if "B" not in B else "D output missing" if "D" not in B else "B states no assumed route"
        r2.append(conf("R-CONF-2", "not comparable", side("B", "MANIFEST:B" if "B" not in B else ptr("B", "assumptions") if "assumptions" in B["B"] else "B:", "no assumed route" if "B" in B else "absent"),
                       side("D", "MANIFEST:D" if "D" not in B else "D:", "routes" if "D" in B else "absent"), "cannot compare: " + why, "gap"))
    else:
        hits = [(i, r) for i, r in enumerate(routes or []) if isinstance(r, dict) and r.get("route") == asm["route"]]
        left = side("B", ptr("B", "assumptions"), f"timeline assumes route {asm['route']}" + (f" with {asm['review_months']} months of review" if asm.get("review_months") is not None else ""))
        if not hits:
            r2.append(conf("R-CONF-2", "conflict", left, side("D", ptr("D", "routes"), "route not listed in the pathway map"), "B assumes a route that D does not map"))
        else:
            i, r = hits[0]
            right = side("D", ptr("D", f"routes[{i}]"), f"route {r.get('route')} disposition {r.get('disposition')}" + (f", clock {json.dumps(r.get('clock'))}" if r.get("clock") else ""))
            why = []
            if r.get("disposition") != "candidate":
                why.append(f"D's disposition is {r.get('disposition')!r}, not candidate")
            ck = r.get("clock") or {}
            dm = ck.get("months") if ck.get("months") is not None else (ck["days"] / 30.4375 if ck.get("days") is not None else None)
            if dm is not None and asm.get("review_months") is not None and float(asm["review_months"]) < float(dm) - 0.05:
                why.append(f"B assumes {asm['review_months']} months of review; D's verified clock is {round(dm, 2)} months")
            r2.append(conf("R-CONF-2", "conflict" if why else "no conflict", left, right, "; ".join(why) or "assumed route is a candidate in D and its clock is not shorter than B assumes"))
    # R-CONF-3 differentiation claims (G) without support in A or F
    r3 = []
    G = B.get("G")
    if G is None:
        r3.append(conf("R-CONF-3", "not comparable", side("G", "MANIFEST:G", "absent"), side("A", "A:", "-"), "cannot compare: G output missing", "gap"))
    else:
        for i, c in enumerate(G.get("differentiation") or []):
            if not isinstance(c, dict) or c.get("state") != "supported":
                continue
            basis, bad = c.get("basis") or [], []
            for b in basis:
                ref = str(b.get("ref", "")) if isinstance(b, dict) else str(b)
                m = re.match(r"^([AF])-(.+)$", ref)
                if not m:
                    bad.append(f"{ref or '(empty)'}: not an A or F reference")
                    continue
                code, rid = m.group(1), m.group(2)
                if code not in B:
                    bad.append(f"{ref}: workstream {code} output missing")
                    continue
                found = False
                for lst in ([v for v in B[code].values() if isinstance(v, list)]):
                    for x in lst:
                        if isinstance(x, dict) and any(str(x.get(k)) in (rid, ref) for k in ("id", "finding_id", "mode_id")):
                            found = True
                if not found:
                    bad.append(f"{ref}: no such row in {code}")
            if not basis:
                bad.append("no basis stated")
            st = "conflict" if bad else "no conflict"
            r3.append(conf("R-CONF-3", st, side("G", ptr("G", f"differentiation[{i}]"), row_text(c)),
                           side("A" if any(str((b or {}).get('ref', '')).startswith('A') for b in basis if isinstance(b, dict)) else "F", "A:" if "A" in B else "MANIFEST:A", "; ".join(bad) or "basis resolves"),
                           "supported claim without support in the evidence or mechanism registers: " + "; ".join(bad) if bad else "basis resolves to a register row"))
        if not (G.get("differentiation") or []):
            r3.append(conf("R-CONF-3", "no conflict", side("G", "G:", "no differentiation claims"), side("A", "A:", "-"), "no claim to check"))
    # R-CONF-4 commercial conditions (H) that depend on rows still GAP elsewhere
    r4 = []
    H = B.get("H")
    if H is None:
        r4.append(conf("R-CONF-4", "not comparable", side("H", "MANIFEST:H", "absent"), side("-", "H:", "-"), "cannot compare: H output missing", "gap"))
    else:
        for i, c in enumerate(H.get("conditions") or []):
            code = CODE_OF_SKILL.get((c or {}).get("owner"))
            if not code or code == "H":
                continue
            left = side("H", ptr("H", f"conditions[{i}]"), f"{c.get('id')} {c.get('state')}: {c.get('detail', '')}".strip())
            if code not in B:
                bad = c.get("state") == "met"
                r4.append(conf("R-CONF-4", "conflict" if bad else "no conflict", left, side(code, f"MANIFEST:{code}", "owner workstream output missing"),
                               "condition marked met while its owner's output is missing" if bad else "owner output missing; condition is not marked met"))
                continue
            om = store_metrics_cache[(store.name, code)]
            right = side(code, ptr(code, "gaps[0]") if om["gaps"] else ptr(code, ""), f"{len(om['gaps'])} open GAP(s); sign-off {'closed' if om['signed'] else 'open'}")
            if c.get("state") == "met" and (not om["signed"] or om["gaps"]):
                r4.append(conf("R-CONF-4", "conflict", left, right, "condition marked met while its owner's register is unsigned or has open GAPs"))
            elif om["gaps"] and c.get("state") != "met":
                r4.append(conf("R-CONF-4", "dependency", left, right, "condition depends on a register that still has open GAPs", "dependency"))
            else:
                r4.append(conf("R-CONF-4", "no conflict", left, right, "owner register signed with no open GAP" if om["signed"] else "owner register has no open GAP"))
    # R-CONF-5 licensor obligations (E) vs the licence chain (C)
    r5 = []
    if "E" not in B or "C" not in B:
        r5.append(conf("R-CONF-5", "not comparable", side("E", "MANIFEST:E" if "E" not in B else "E:", "absent" if "E" not in B else "-"), side("C", "MANIFEST:C" if "C" not in B else "C:", "absent" if "C" not in B else "-"),
                       "cannot compare: " + ("E" if "E" not in B else "C") + " output missing", "gap"))
    else:
        chain = [re.sub(r"\s*\(.*?\)\s*", " ", str(((o or {}).get("license_in") or {}).get("licensor", ""))).strip().lower() for o in (B["C"].get("ownership") or [])]
        for i, lo in enumerate(B["E"].get("licensor_obligations") or []):
            name = re.sub(r"\s*\(.*?\)\s*", " ", str((lo or {}).get("licensor", ""))).strip().lower()
            ok = bool(name) and any(name in c or c in name for c in chain if c)
            r5.append(conf("R-CONF-5", "no conflict" if ok else "conflict", side("E", ptr("E", f"licensor_obligations[{i}]"), f"{lo.get('licensor')}: {lo.get('type', '')} {lo.get('trigger', '')}".strip()),
                           side("C", ptr("C", "ownership"), "licensors in the chain: " + (", ".join(c for c in chain if c) or "none")),
                           "licensor appears in the ownership and licence chain" if ok else "E lists a licensor that the C ownership and licence chain does not name"))
    # R-CONF-6 revenue launch years (R) vs approval years implied by the timeline (B)
    r6 = []
    Rr = B.get("R")
    if not rng or Rr is None:
        miss = [x for x, ok in (("B timeline range", bool(rng)), ("R output", Rr is not None)) if not ok]
        r6.append(conf("R-CONF-6", "not comparable", side("R", "MANIFEST:R" if Rr is None else "R:", "absent" if Rr is None else "revenue register"),
                       side("B", ptr("B", "timeline.range") if rng else "MANIFEST:B" if "B" in store.missing else "B:", "timeline range" if rng else "absent"),
                       "cannot compare: " + ", ".join(miss) + " missing", "gap"))
    else:
        appr = {k: add_months(as_of, float(rng[f"{k}_months"])).year for k in ("low", "mid", "high")}
        pair = (("early", "low"), ("mid", "mid"), ("late", "high"))
        for i, c in enumerate(Rr.get("countries") or []):
            ly = (c or {}).get("launch_year") if isinstance(c, dict) else None
            if not isinstance(c, dict) or c.get("state") != "computed" or not isinstance(ly, dict):
                continue
            bad = [f"{a} launch {ly[a]} is before the {b} approval year {appr[b]}" for a, b in pair if ly.get(a) is not None and int(ly[a]) < appr[b]]
            r6.append(conf("R-CONF-6", "conflict" if bad else "no conflict",
                           side("R", ptr("R", f"countries[{c.get('country')}].launch_year"), f"{c.get('country')} launch years early/mid/late {ly.get('early')}/{ly.get('mid')}/{ly.get('late')}"),
                           side("B", ptr("B", "timeline.range"), f"approval years from as_of {as_of}: low {appr['low']}, mid {appr['mid']}, high {appr['high']}"),
                           "; ".join(bad) or "no launch year precedes the paired approval year"))
    # R-CONF-7 erosion start (R) vs effective exclusivity end (C)
    r7 = []
    if Rr is None or "C" not in B or not cd:
        miss = [x for x, ok in (("R output", Rr is not None), ("C dates", bool(cd))) if not ok]
        r7.append(conf("R-CONF-7", "not comparable", side("R", "MANIFEST:R" if Rr is None else "R:", "absent" if Rr is None else "revenue register"),
                       side("C", ptr("C", "dates.markets") if cd else "MANIFEST:C" if "C" in store.missing else "C:", "exclusivity dates" if cd else "absent"),
                       "cannot compare: " + ", ".join(miss) + " missing", "gap"))
    else:
        for i, c in enumerate(Rr.get("countries") or []):
            if not isinstance(c, dict) or c.get("state") != "computed" or c.get("exclusivity_end_year") is None:
                continue
            ctry = c.get("country")
            mk = "US" if ctry == "US" else "EU" if ctry in ("DE", "FR", "IT", "ES") else None
            left = side("R", ptr("R", f"countries[{ctry}].exclusivity_end_year"), f"{ctry} exclusivity end year {c['exclusivity_end_year']}; erosion {'starts ' + str(int(c['exclusivity_end_year']) + 1) if c.get('loe_applied') else 'not applied'}")
            eff = ((cd.get(mk) or {}).get("effective") or {}) if mk else {}
            ys = {v: parse_date(eff[v], f"C dates {mk} {v}").year for v in ("effective_all_patents", "effective_composition_only") if eff.get(v)}
            if not ys:
                r7.append(conf("R-CONF-7", "not comparable", left, side("C", ptr("C", "dates.markets"), f"no effective dates for {mk or ctry}"), f"C holds no effective exclusivity date for {ctry}", "gap"))
                continue
            ok = int(c["exclusivity_end_year"]) in ys.values()
            r7.append(conf("R-CONF-7", "no conflict" if ok else "conflict", left,
                           side("C", ptr("C", f"dates.markets.{mk}.effective"), "; ".join(f"{k.replace('effective_', '').replace('_', ' ')} ends {y}" for k, y in ys.items())),
                           "R's exclusivity end year matches an effective exclusivity year in C" if ok else "R places the exclusivity end in a year that neither C view gives; erosion would start at the wrong time"))
    for grp in (r1, r2, r3, r4, r5, r6, r7):
        out += grp
    return out


store_metrics_cache = {}


# ---------------------------------------------------------------- assembly
def counts_line(ws):
    return tuple(sum(1 for w in ws if w["proposed_status"] == k) for k in ("green", "yellow", "red"))


def build_asset(store, M, T, as_of):
    for c in ORDER:
        if c in store.bundles:
            store_metrics_cache[(store.name, c)] = metrics(c, store.bundles[c], T)
    ws, gaps_out, risks = [], [], []
    for c in ORDER:
        if c in store.missing:
            ws.append({"code": c, "name": NAMES[c], "skill": SKILLS[c], "present": False, "proposed_status": "red", "counts": None,
                       "rule_applied": "R-STATUS: output missing is red", "pointer": f"MANIFEST:{c}", "route_to": SKILLS[c],
                       "consequence": MISSING_TEXT[c] + "; " + BLOCKS[c], "deal_lead_confirmation": "PENDING", "deal_lead_status": None})
            gaps_out.append({"workstream": c, "kind": "missing output", "pointer": f"MANIFEST:{c}", "missing": f"{SKILLS[c]} output", "why_it_matters": MISSING_TEXT[c], "blocks": BLOCKS[c], "route_to": SKILLS[c]})
            continue
        m = store_metrics_cache[(store.name, c)]
        why = []
        if m["triggered"]:
            why.append(f"{len(m['triggered'])} triggered failure mode(s)")
        if m["gaps"]:
            why.append(f"{len(m['gaps'])} open GAP(s)")
        if m["checks"]:
            why.append(f"{len(m['checks'])} [CHECK] item(s)")
        if not m["signed"]:
            why.append("register sign-off open")
        ws.append({"code": c, "name": NAMES[c], "skill": SKILLS[c], "present": True, "proposed_status": m["status"],
                   "counts": {"triggered_failure_modes": len(m["triggered"]), "open_gaps": len(m["gaps"]), "check_items": len(m["checks"]), "signoff_open": 0 if m["signed"] else 1,
                              "cannot_tell": len(m["cannot_tell"]), "human_only_fields": m["human_only"]},
                   "rule_applied": "R-STATUS: " + ("; ".join(why) if why else "no triggered failure mode, no open GAP, no [CHECK] item, sign-off closed") + f" -> {m['status']}",
                   "pointer": f"{c}:", "route_to": None, "consequence": None, "deal_lead_confirmation": "PENDING", "deal_lead_status": None})
        for i, g in enumerate(m["gaps"]):
            gaps_out.append({"workstream": c, "kind": "open gap", "pointer": ptr(c, f"gaps[{i}]"), "missing": (g or {}).get("missing") or row_text(g),
                             "why_it_matters": (g or {}).get("why_it_matters") or "(not stated in the register)", "blocks": BLOCKS[c], "route_to": None})
        for i, f in m["triggered"]:
            ref = f.get("register_ref")
            ok, val = (store.resolve(ptr(c, ref)) if ref else (False, None))
            risks.append({"score": 2, "order": ORDER.index(c), "workstream": c, "kind": "triggered failure mode", "text": f"{f.get('id') or f.get('mode_id')} triggered" + (f": {row_text(val)}" if ok else ""),
                          "pointers": [ptr(c, f"failure_mode_screen[{i}]")] + ([ptr(c, ref)] if ok else [])})
        for i, f in m["cannot_tell"]:
            risks.append({"score": 1, "order": ORDER.index(c), "workstream": c, "kind": "failure mode cannot tell", "text": f"{f.get('id') or f.get('mode_id')} cannot tell" + (f" (gap {f.get('gap')})" if f.get("gap") else ""),
                          "pointers": [ptr(c, f"failure_mode_screen[{i}]")]})
        if c == "H":
            for i, k in enumerate(store.bundles["H"].get("conditions") or []):
                if isinstance(k, dict) and k.get("state") == "not met":
                    risks.append({"score": 2, "order": ORDER.index(c), "workstream": c, "kind": "commercial condition not met", "text": f"{k.get('id')} not met: {k.get('detail', '')}".strip(),
                                  "pointers": [ptr(c, f"conditions[{i}]")]})
    confl = conflicts_for(store, M, T, as_of)
    for k in confl:
        if k["status"] == "conflict":
            risks.append({"score": 3, "order": ORDER.index(k["left"]["workstream"]) if k["left"]["workstream"] in ORDER else 9, "workstream": "cross", "kind": f"conflict {k['rule']}",
                          "text": f"{k['rule']}: {k['detail']}", "pointers": [k["left"]["pointer"], k["right"]["pointer"]]})
    risks.sort(key=lambda r: (-r["score"], r["order"]))
    top = risks[: int(T["top_n"])]
    for n, r in enumerate(top, 1):
        r["rank"] = n
        r.pop("score"), r.pop("order")
    n_g, n_y, n_r = counts_line(ws)
    n_gaps = sum(1 for g in gaps_out if g["kind"] == "open gap")
    n_chk = sum(w["counts"]["check_items"] for w in ws if w["counts"])
    n_trg = sum(w["counts"]["triggered_failure_modes"] for w in ws if w["counts"])
    n_con = sum(1 for k in confl if k["status"] == "conflict")
    n_mis = len(store.missing)
    all_ptr = [g["pointer"] for g in gaps_out] + [p for r in risks for p in r["pointers"]] + [f"{w['code']}:" for w in ws if w["present"]]
    answer = [
        {"text": f"Workstreams (proposed, the deal lead confirms): {n_g} green, {n_y} yellow, {n_r} red of {len(ws)}.", "pointers": [w["pointer"] for w in ws]},
        {"text": f"Open: {n_gaps} GAP(s), {n_chk} [CHECK] item(s), {n_trg} triggered failure mode(s), {n_con} cross-workstream conflict(s), {n_mis} workstream output(s) missing.",
         "pointers": sorted(set(all_ptr), key=all_ptr.index) or [w["pointer"] for w in ws]},
        {"text": "Largest open items: " + ("; ".join(f"[{r['rank']}] {r['text']}" for r in top[:3]) if top else ("no ranked risk; open GAP(s): " + "; ".join(f"{g['workstream']}: {g['missing']}" for g in gaps_out[:3]) if gaps_out else "none recorded")) + ". Nothing is recommended or certified; the deal lead decides.",
         "pointers": [p for r in top[:3] for p in r["pointers"]] or [g["pointer"] for g in gaps_out[:3]] or [w["pointer"] for w in ws]},
    ]
    # decision options
    unmet = lambda ptrs, label: {"condition": label, "pointers": ptrs}
    trig_p = [p for r in risks if r["kind"] == "triggered failure mode" for p in r["pointers"][:1]]
    gap_p = [g["pointer"] for g in gaps_out]
    con_p = [k["left"]["pointer"] for k in confl if k["status"] == "conflict"]
    roots = [w["pointer"] for w in ws]
    chk_p = []
    for c in ORDER:
        if c in store.bundles:
            chk_p += [ptr(c, p) for p in store_metrics_cache[(store.name, c)]["checks"]]
    red_p = [w["pointer"] for w in ws if w["proposed_status"] == "red"]
    unsig_p = [f"{w['code']}:" for w in ws if w["present"] and w["counts"]["signoff_open"]]
    options = [
        {"option": "sign", "recommended": False, "conditions_that_would_have_to_hold": [
            {"condition": "every workstream is green (the deal lead confirms)", "met": n_g == len(ws), "pointers": [w["pointer"] for w in ws if w["proposed_status"] != "green"] or roots},
            {"condition": "no cross-workstream conflict is open", "met": n_con == 0, "pointers": con_p or roots},
            {"condition": "no GAP is open and no output is missing", "met": not gap_p, "pointers": gap_p or roots},
            {"condition": "no failure mode is triggered", "met": not trig_p, "pointers": trig_p or roots},
            {"condition": "every register sign-off is closed", "met": not unsig_p, "pointers": unsig_p or roots}]},
        {"option": "sign with conditions", "recommended": False, "conditions_precedent": (
            [unmet([g["pointer"]], f"close GAP: {g['missing']} ({g['workstream']})") for g in gaps_out]
            + [unmet([k["left"]["pointer"], k["right"]["pointer"]], f"resolve conflict {k['rule']}: {k['detail']}") for k in confl if k["status"] == "conflict"]
            + [unmet([p], f"close [CHECK] item at {p}") for p in chk_p[:15]]
            + [unmet([p], f"close the register sign-off at {p}") for p in unsig_p]) or [unmet(roots, "none open")]},
        {"option": "do not sign", "recommended": False, "conditions_present": (
            [unmet([w["pointer"]], f"workstream {w['code']} is red (proposed)") for w in ws if w["proposed_status"] == "red"]
            + [unmet(r["pointers"], r["text"]) for r in risks if r["kind"] in ("triggered failure mode", "commercial condition not met")]
            + [unmet([k["left"]["pointer"], k["right"]["pointer"]], f"conflict {k['rule']}: {k['detail']}") for k in confl if k["status"] == "conflict"]) or [unmet(roots, "none recorded")]},
    ]
    return {"asset": store.name, "answer": answer, "workstreams": ws, "top_risks": top, "conflicts": [k for k in confl if k["status"] != "no conflict"],
            "conflict_checks": [{"rule": k["rule"], "status": k["status"], "pointers": [k["left"]["pointer"], k["right"]["pointer"]]} for k in confl],
            "open_gaps": gaps_out, "decision_options": options, "recommended_option": None, "deal_lead_decision": "PENDING (HUMAN ONLY)",
            "human_only_fields": {c: store_metrics_cache[(store.name, c)]["human_only"] for c in ORDER if c in store.bundles}}


def extra_lines_check(lines, stores):
    out = []
    for n, ln in enumerate(lines):
        t = (ln or {}).get("text", "")
        if not isinstance(t, str) or not t.strip():
            raise ReportError("E_UNSUPPORTED", f"added line {n}: empty text")
        for pat in RECOMMEND:
            if re.search(pat, t, re.I):
                raise ReportError("E_RECOMMEND", f"added line {n}: recommends or certifies ({pat!r}); the deal lead decides")
        ptrs = ln.get("pointers") or []
        if not ptrs:
            raise ReportError("E_UNSUPPORTED", f"added line {n} has no register pointer; the report adds no finding of its own: {t[:80]!r}")
        pool = []
        for p in ptrs:
            ok, val = False, None
            for s in stores:
                ok, val = s.resolve(p, {x.name: x for x in stores})
                if ok:
                    break
            if not ok:
                raise ReportError("E_POINTER", f"added line {n}: pointer {p!r} does not resolve to a register row")
            pool.append(json.dumps(val, ensure_ascii=False))
        blob = " ".join(pool)
        for num in re.findall(r"\d+(?:\.\d+)?", t):
            if num not in blob:
                raise ReportError("E_UNSUPPORTED", f"added line {n}: figure {num} is not in the pointed rows; the report adds no finding of its own")
        out.append({"text": t.strip(), "pointers": ptrs})
    return out


def verify_pointers(report, stores):
    by = {s.name: s for s in stores}
    def chk(p, where):
        for s in stores:
            ok, _ = s.resolve(p, by)
            if ok:
                return
        raise ReportError("E_POINTER", f"{where}: pointer {p!r} does not resolve")
    for a in report["assets"]:
        s = by[a["asset"]]
        def chk_a(p, where):
            ok, _ = s.resolve(p, by)
            if not ok:
                raise ReportError("E_POINTER", f"{a['asset']} {where}: pointer {p!r} does not resolve")
        for ln in a["answer"]:
            if not ln["pointers"]:
                raise ReportError("E_UNSUPPORTED", f"{a['asset']}: answer line without pointer")
            for p in ln["pointers"]:
                chk_a(p, "answer")
        for r in a["top_risks"]:
            for p in r["pointers"]:
                chk_a(p, "top risk")
        for k in a["conflicts"]:
            for p in (k["left"]["pointer"], k["right"]["pointer"]):
                chk_a(p, "conflict")
        for g in a["open_gaps"]:
            chk_a(g["pointer"], "gap")
        for o in a["decision_options"]:
            for key in ("conditions_that_would_have_to_hold", "conditions_precedent", "conditions_present"):
                for c in o.get(key, []):
                    if not c["pointers"]:
                        raise ReportError("E_UNSUPPORTED", f"{a['asset']}: option condition without pointer")
                    for p in c["pointers"]:
                        chk_a(p, "option")
        for w in a["workstreams"]:
            chk_a(w["pointer"], "workstream")
    for ln in report.get("added_lines", []):
        for p in ln["pointers"]:
            chk(p, "added line")


def validate_schema(o, sch, path="report"):
    t = sch.get("type")
    tmap = {"object": dict, "array": list, "string": str, "boolean": bool, "integer": int, "number": (int, float), "null": type(None)}
    if t:
        ts = t if isinstance(t, list) else [t]
        if not any(isinstance(o, tmap[x]) and not (x in ("integer", "number") and isinstance(o, bool)) for x in ts):
            raise ReportError("E_SCHEMA", f"{path}: expected {t}")
    if "enum" in sch and o not in sch["enum"]:
        raise ReportError("E_SCHEMA", f"{path}: {o!r} not in {sch['enum']}")
    if isinstance(o, dict):
        for k in sch.get("required", []):
            if k not in o:
                raise ReportError("E_SCHEMA", f"{path}: missing {k}")
        for k, sub in sch.get("properties", {}).items():
            if k in o:
                validate_schema(o[k], sub, f"{path}.{k}")
    if isinstance(o, list):
        if "minItems" in sch and len(o) < sch["minItems"]:
            raise ReportError("E_SCHEMA", f"{path}: fewer than {sch['minItems']} items")
        if "maxItems" in sch and len(o) > sch["maxItems"]:
            raise ReportError("E_SCHEMA", f"{path}: more than {sch['maxItems']} items")
    if isinstance(o, list) and "items" in sch:
        for i, x in enumerate(o):
            validate_schema(x, sch["items"], f"{path}[{i}]")


def render_md(rep):
    L = []
    for a in rep["assets"]:
        L.append(f"# Integrated diligence report: {a['asset']} ({rep['mode']} mode, as of {rep['as_of']})\n")
        L.append(f"Prepared by: {rep['sign_off']['prepared_by']}    Reviewed by: {rep['sign_off']['reviewed_by']}    Version: {rep['sign_off']['version']}    Release state: {rep['sign_off']['release_state']}    Status: {rep['sign_off']['status']}\n")
        L.append("## 1. The answer in three lines\n")
        for ln in a["answer"]:
            L.append(f"- {ln['text']}  `{', '.join(ln['pointers'][:6])}{' ...' if len(ln['pointers']) > 6 else ''}`")
        L.append("\n## 2. Workstream status (proposed)\n")
        L.append("| Workstream | Proposed status | Rule applied | Register | Deal-lead confirmation |\n|---|---|---|---|---|")
        for w in a["workstreams"]:
            L.append(f"| {w['code']} {w['name']} | {w['proposed_status'].upper()} | {w['rule_applied']} | `{w['pointer']}` | {w['deal_lead_confirmation']} (status: ____) |")
        L.append("\nThe status is PROPOSED by the stated rule R-STATUS (ENGINEERING RULE; practitioner practice, not a standard). The deal lead confirms or changes it.\n")
        L.append("## 3. Top risks across workstreams\n")
        L.append("| Rank | Risk | Kind | Register pointers |\n|---|---|---|---|")
        for r in a["top_risks"]:
            L.append(f"| {r['rank']} | {r['text']} | {r['kind']} | `{', '.join(r['pointers'])}` |")
        if not a["top_risks"]:
            L.append("| - | none recorded | - | - |")
        L.append("\n## 4. Conflicts between workstreams (side by side, not reconciled)\n")
        L.append("| Rule | Result | Left | Right | Detail |\n|---|---|---|---|---|")
        for k in a["conflicts"]:
            L.append(f"| {k['rule']} | {k['status']} | {k['left']['workstream']}: {k['left']['text']} `{k['left']['pointer']}` | {k['right']['workstream']}: {k['right']['text']} `{k['right']['pointer']}` | {k['detail']} |")
        if not a["conflicts"]:
            L.append("| - | none | - | - | - |")
        L.append("\nChecks run: " + "; ".join(f"{r}: {n} comparison(s)" for r, n in sorted({(c['rule']): sum(1 for x in a['conflict_checks'] if x['rule'] == c['rule']) for c in a['conflict_checks']}.items())) + "\n")
        L.append("## 5. Open gaps and what each blocks\n")
        L.append("| Workstream | Gap | Why it matters | Blocks | Pointer |\n|---|---|---|---|---|")
        for g in a["open_gaps"]:
            L.append(f"| {g['workstream']} | {g['missing']} | {g['why_it_matters']} | {g['blocks']}{' (run ' + g['route_to'] + ')' if g.get('route_to') else ''} | `{g['pointer']}` |")
        if not a["open_gaps"]:
            L.append("| - | none | - | - | - |")
        L.append("\n## 6. Decision options (none recommended)\n")
        for o in a["decision_options"]:
            L.append(f"### {o['option'].capitalize()}\n")
            for key in ("conditions_that_would_have_to_hold", "conditions_precedent", "conditions_present"):
                for c in o.get(key, []):
                    mark = "" if "met" not in c else ("[met] " if c["met"] else "[not met] ")
                    L.append(f"- {mark}{c['condition']}  `{', '.join(c['pointers'][:4])}{' ...' if len(c['pointers']) > 4 else ''}`")
            L.append("")
        L.append("## 7. Sign-off\n")
        s = rep["sign_off"]
        L.append(f"Prepared by: {s['prepared_by']}    Reviewed by: {s['reviewed_by']}    Deal lead decision: {s['deal_lead_decision']}    Version: {s['version']}    Release state: {s['release_state']}    Status: {s['status']}\n")
        L.append("## 8. Rules applied\n")
        L.append("Thresholds in force (team-set defaults, client may override): " + json.dumps(rep["thresholds"]) + "\n")
        L.append("R-STATUS, R-CONF-1 to R-CONF-7 and R-RANK are ENGINEERING RULES of this tool (see the tool docstring and templates/integrated-diligence-report.md). The report adds no finding of its own; every line points to a register row.\n")
    if rep.get("rollup"):
        L.append("## Roll-up across assets (company mode)\n")
        hdr = ["Asset"] + ORDER
        L.append("| " + " | ".join(hdr) + " |\n|" + "---|" * len(hdr))
        for r in rep["rollup"]["matrix"]:
            L.append("| " + " | ".join([r["asset"]] + [r["statuses"].get(c, "-").upper() for c in ORDER]) + " |")
        L.append("\nDates and ranges are never merged across assets.\n")
    if rep.get("added_lines"):
        L.append("## Added lines (each points to register rows)\n")
        for ln in rep["added_lines"]:
            L.append(f"- {ln['text']}  `{', '.join(ln['pointers'])}`")
    return "\n".join(L) + "\n"


def run(manifest_path, thresholds=None, lines=None):
    M, stores = load_manifest(manifest_path)
    T = dict(DEFAULTS)
    T.update(thresholds or {})
    as_of = parse_date(M["as_of"], "as_of")
    store_metrics_cache.clear()
    assets = [build_asset(s, M, T, as_of) for s in stores]
    reviewed = M.get("reviewed_by")
    rep = {"tool": "assemble_report.py", "mode": M["mode"], "as_of": M["as_of"], "thresholds": T, "assets": assets,
           "sign_off": {"prepared_by": M.get("prepared_by") or "UNSIGNED", "reviewed_by": reviewed or "UNSIGNED", "deal_lead_decision": "PENDING (HUMAN ONLY)",
                        "version": str(M.get("version") or "1"), "release_state": M.get("release_state") or "Draft", "status": "UNSIGNED" if not reviewed else "REVIEWED, DEAL-LEAD DECISION PENDING"},
           "recommended_option": None}
    if M["mode"] == "company":
        rep["rollup"] = {"matrix": [{"asset": a["asset"], "statuses": {w["code"]: w["proposed_status"] for w in a["workstreams"]},
                                      "pointers": [w["pointer"] for w in a["workstreams"]]} for a in assets]}
    if lines:
        rep["added_lines"] = extra_lines_check(lines, stores)
    verify_pointers(rep, stores)
    return rep


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    opts = {}
    for k in ("--thresholds", "--lines", "--out", "--md"):
        if k in argv:
            i = argv.index(k)
            if i + 1 >= len(argv):
                print(f"E_USAGE: {k} needs a value", file=sys.stderr)
                return 2
            opts[k] = argv[i + 1]
            args = [a for a in args if a != argv[i + 1]]
    if len(args) != 1:
        print(__doc__.split("\n")[1], file=sys.stderr)
        return 2
    try:
        th = load_json(opts["--thresholds"]) if "--thresholds" in opts else None
        ln = load_json(opts["--lines"]) if "--lines" in opts else None
        rep = run(args[0], th, ln)
        sch = Path(__file__).resolve().parent.parent / "templates" / "integrated-diligence-report.schema.json"
        if sch.is_file():
            validate_schema(rep, json.loads(sch.read_text()))
    except ReportError as ex:
        print(json.dumps({"ok": False, "error": ex.code, "message": ex.message}), file=sys.stderr)
        return 1
    except OSError as ex:
        print(f"E_FILE: {ex}", file=sys.stderr)
        return 2
    if "--out" in opts:
        Path(opts["--out"]).write_text(json.dumps(rep, indent=1, ensure_ascii=False) + "\n")
    if "--md" in opts:
        Path(opts["--md"]).write_text(render_md(rep))
    if "--out" not in opts and "--md" not in opts:
        print(json.dumps(rep, indent=2 if "--pretty" in argv else None, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
