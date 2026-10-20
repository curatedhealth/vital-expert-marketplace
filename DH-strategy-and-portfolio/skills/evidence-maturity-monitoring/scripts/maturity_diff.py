#!/usr/bin/env python3
"""Compare two saved evidence-maturity snapshots and say what kind of change each is.

Reads two JSON files saved from diligence-dh.get_evidence_maturity (or
compare_portfolio, or build_company_profile) on two dates, as in examples/live/.
Matches companies by the reference the person asked for (the call argument) and,
failing that, by the resolved company name. For each company it prints the score
and points on both dates and classifies every difference:

  RESOLUTION  the reference resolved to a different company: not comparable.
  METHOD      rubric version changed, or the assessable maximum changed, or a
              component moved between assessable and excluded. The score moved
              because the convention or the loaded sources changed, not the evidence.
  INPUT       a component input changed (authorizations, studies, results posted,
              active studies, products). This is a change in what the records hold;
              read the record before calling it new evidence.
  POINTS      a component's points moved; read it with the INPUT or METHOD line
              beside it, which says why.
  NONE        nothing differs.

It also compares the source coverage blocks when both files carry one (COVERAGE:
loaded record counts and sources not loaded; a change in the perimeter, not evidence).
Risk flags from either run (resolution, recall, terminated studies) are carried
forward verbatim; a resolution flag ("combined", "proposal") stays classed RESOLUTION
until the person validates it. Safety events are printed as stored; a field one run
lacks is "not in that run", never 0 or none. Company status is not in any run: the
script reminds the reader to run the status step (references/company-status.md).

It never rates a company, proposes a framework level, or says a change matters.

Usage: python3 maturity_diff.py EARLIER.json LATER.json [--company NAME]
       python3 maturity_diff.py --count ANSWER.md
         counts a short answer's words without the "Calls made" list and without
         table columns whose header starts with "Source"; flags anything over 450.
"""
import json
import re
import sys

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


def full_date(s):
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", str(s or ""))
    if not m:
        return "date not stored"
    y, mo, d = (int(x) for x in m.groups())
    return f"{d} {MONTHS[mo - 1]} {y}"


def pts(text):
    m = re.search(r"(\d+)\s*(?:of|/)\s*(\d+)", str(text or ""))
    return (int(m.group(1)), int(m.group(2))) if m else (None, None)


def snapshot(path):
    with open(path) as f:
        data = json.load(f)
    out = {}
    calls = data["calls"] if isinstance(data, dict) and "calls" in data else [data]
    for c in calls:
        items = []
        if isinstance(c.get("companies"), list):
            for co in c["companies"]:
                items.append((co.get("query"), co, c.get("retrieved_at")))
        elif "response" in c:
            r = c["response"]
            ref = ((c.get("call") or {}).get("arguments") or {}).get("company")
            items.append((ref, dict(r.get("evidence_maturity") or {}, resolution=r.get("resolution"),
                                    company=ref), (r.get("provenance") or {}).get("retrieved_at")))
        else:
            items.append(((c.get("arguments") or {}).get("company"), c, c.get("retrieved_at")))
        for ref, rec, when in items:
            em = rec.get("evidence_maturity") if isinstance(rec.get("evidence_maturity"), dict) else rec
            comps = {}
            raw = em.get("components") or []
            if isinstance(raw, dict):
                for k, v in raw.items():
                    e, mx = pts(v)
                    comps[k] = {"points": e, "max": mx, "inputs": {}}
            else:
                for x in raw:
                    comps[x.get("component")] = {"points": x.get("points"), "max": x.get("max_points"),
                                                 "inputs": x.get("inputs") or {}}
            exl = em.get("not_assessable") or em.get("excluded_dimensions")
            excluded = None if exl is None else sorted([x.get("component") if isinstance(x, dict) else x for x in exl])
            ap = em.get("assessable_points") or {}
            earned, maximum = ap.get("earned"), ap.get("maximum")
            if earned is None:
                earned, maximum = pts(em.get("score_scale"))
            res = rec.get("resolution")
            if isinstance(res, dict):
                res = res.get("status")
            company = rec.get("company") or (str(res).split(":")[-1].split(";")[0].strip() if res else None)
            key = (ref or company or "unknown").lower()
            flags = list(rec.get("risk_flags") or em.get("risk_flags") or [])
            safety = rec.get("safety_events", "not in this run")
            out[key] = {"ref": ref, "company": company, "resolution": str(res), "score": em.get("score"),
                        "flags": flags, "safety": safety,
                        "earned": earned, "max": maximum, "rubric": em.get("rubric_version"),
                        "components": comps, "excluded": excluded, "when": when}
    cov = (data.get("source_coverage_excerpt") or {}) if isinstance(data, dict) else {}
    return out, cov


def shown(v):
    return "not in output" if v is None else v


CUT_ORDER = ("context paragraphs, repeated row ids in prose, secondary rules, rows not tied to "
             "the person's question, the 'Full version on request' line. Never cut a gap, a stop or the record line.")


def count_words(path, cap=450):
    """Count an answer's words without the calls list and source columns."""
    with open(path) as f:
        lines = f.read().splitlines()
    words, drop = 0, set()
    _skip_calls = False  # the calls list sits before the record block; skip it, then count the record
    for line in lines:
        s = line.strip()
        if _skip_calls:
            if re.search(r"Clears it|^\W*(#+\s*)?(\*\*)?(\d+\.\s*)?(\*\*)?Record\b", s.strip()):
                _skip_calls = False
            else:
                continue
        if re.match(r"^(#+\s*|\d+\.\s*)?(\*\*)?calls made", s, re.I):
            _skip_calls = True
            continue
        if s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            if not drop and any(c.lower().startswith("source") for c in cells):
                drop = {i for i, c in enumerate(cells) if c.lower().startswith("source")}
            words += sum(len(c.split()) for i, c in enumerate(cells) if i not in drop)
            continue
        drop = set()
        words += len([w for w in s.split() if re.search(r"\w", w)])
    ok = words <= cap
    print(f"Words (without calls list and source columns): {words}; cap {cap}: {'OK' if ok else 'OVER'}")
    if not ok:
        print("Cut in this order until under: " + CUT_ORDER)
    return 0 if ok else 1


def main(argv):
    if argv and argv[0] == "--count":
        return count_words(argv[1]) if len(argv) > 1 else 2
    args = [a for a in argv if not a.startswith("--")]
    company = None
    if "--company" in argv:
        company = argv[argv.index("--company") + 1].lower()
        args = [a for a in args if a.lower() != company]
    if len(args) != 2:
        print(__doc__)
        return 2
    a, cov_a = snapshot(args[0])
    b, cov_b = snapshot(args[1])
    pairs = [(k, k) for k in a if k in b]
    by_co_b = {(v["company"] or "").lower(): k for k, v in b.items()}
    for k, v in a.items():
        if k in b:
            continue
        kb = by_co_b.get((v["company"] or "").lower())
        if kb and kb not in a and v["company"]:
            pairs.append((k, kb))
    used_a, used_b = {p[0] for p in pairs}, {p[1] for p in pairs}
    if company:
        pairs = [p for p in pairs if company in p[0] or company in p[1]
                 or company in (a[p[0]]["company"] or "").lower()]
    only = [k for k in a if k not in used_a] + [k for k in b if k not in used_b]
    if company:
        only = [k for k in only if company in k]
    for ka, kb in pairs:
        x, y = a[ka], b[kb]
        k = ka
        print(f"## {x['ref'] or k}: {full_date(x['when'])} to {full_date(y['when'])}")
        print(f"Score {shown(x['score'])} ({shown(x['earned'])} of {shown(x['max'])}) to "
              f"{shown(y['score'])} ({shown(y['earned'])} of {shown(y['max'])}); "
              f"rubric {x['rubric'] or 'not in output'} to {y['rubric'] or 'not in output'}")
        changes = []
        if (x["company"] or "").lower() != (y["company"] or "").lower():
            changes.append(("RESOLUTION", f"resolved to '{x['company']}' then '{y['company']}': not comparable"))
        if (x["ref"] or "") != (y["ref"] or ""):
            print(f"- note: matched by resolved company; the references differ ('{x['ref']}' and '{y['ref']}'), "
                  "so the two runs may cover different products of the same company")
        if x["rubric"] and y["rubric"] and x["rubric"] != y["rubric"]:
            changes.append(("METHOD", f"rubric version {x['rubric']} to {y['rubric']}"))
        if x["max"] != y["max"] and x["max"] and y["max"]:
            changes.append(("METHOD", f"assessable maximum {x['max']} to {y['max']}"))
        if x["excluded"] is None or y["excluded"] is None:
            print("- note: the excluded-component list is not in one of the outputs (trimmed or a different tool); not compared")
        else:
            for comp in sorted(set(x["excluded"]) ^ set(y["excluded"])):
                where = "became assessable" if comp in x["excluded"] else "became excluded"
                changes.append(("METHOD", f"component {comp} {where}"))
        if x["components"] and y["components"]:
            for comp in sorted(set(x["components"]) ^ set(y["components"])):
                where = "added to the assessed components" if comp in y["components"] else "no longer among the assessed components"
                changes.append(("METHOD", f"component {comp} {where}"))
        for comp in sorted(set(x["components"]) | set(y["components"])):
            cx, cy = x["components"].get(comp), y["components"].get(comp)
            if not cx or not cy:
                continue
            if cx["points"] != cy["points"]:
                changes.append(("POINTS", f"{comp} points {cx['points']} to {cy['points']}"))
            if not cx["inputs"] or not cy["inputs"]:
                if cx["inputs"] or cy["inputs"]:
                    print(f"- note: {comp} inputs are in one output only; inputs not compared")
                continue
            for inp in sorted(set(cx["inputs"]) | set(cy["inputs"])):
                vx, vy = cx["inputs"].get(inp), cy["inputs"].get(inp)
                if vx != vy:
                    changes.append(("INPUT", f"{comp}.{inp} {vx} to {vy}"))
        kinds = {c[0] for c in changes}
        if not changes:
            print("- NONE: no difference in score, points, inputs, rubric or excluded components")
        for kind, text in changes:
            print(f"- {kind}: {text}")
        if x["score"] != y["score"]:
            if "INPUT" not in kinds and kinds & {"METHOD", "RESOLUTION"}:
                print("- Reading: the score moved with no change in evidence inputs; it reflects the convention or the loaded sources")
            elif "INPUT" in kinds and "METHOD" in kinds:
                print("- Reading: inputs and method both changed; the score difference cannot be assigned to evidence alone")
            elif "INPUT" in kinds:
                print("- Reading: the score moved with an input change; open the record behind that input before treating it as new evidence")
        elif "POINTS" in kinds or "INPUT" in kinds or "METHOD" in kinds:
            print("- Reading: the score is unchanged but its parts changed; report the parts, not only the score")
        print("Risk flags carried forward (verbatim, from either run):")
        allflags = list(dict.fromkeys(x["flags"] + y["flags"]))
        if not allflags:
            print("- none stored in either run (a run that lacks the field says nothing)")
        for fl in allflags:
            where = "both runs" if fl in x["flags"] and fl in y["flags"] else ("earlier run only" if fl in x["flags"] else "later run only")
            cls = "RESOLUTION (until the person validates it)" if re.search(r"combined|proposal|normaliz", fl, re.I) else "flag as stored"
            print(f"- {cls}; {where}: {fl}")
        print(f"Safety events as stored: earlier {x['safety']}; later {y['safety']} "
              "(none_found is none found in the loaded enforcement source, not proof of none)")
        print("Company status: not in either run. Run the status step (references/company-status.md) "
              "or write 'Status: [GAP]: not read' with the filings to open.")
        print()
    for k in sorted(set(only)):
        side = "earlier" if k in a else "later"
        print(f"## {k}: in the {side} snapshot only; no comparison")
    if cov_a and cov_b:
        la, lb = cov_a.get("loaded_includes") or {}, cov_b.get("loaded_includes") or {}
        diffs = [f"{s} {la.get(s, 'not in this excerpt')} to {lb.get(s, 'not in this excerpt')}"
                 for s in sorted(set(la) | set(lb)) if la.get(s) != lb.get(s)]
        na, nb = set(cov_a.get("not_loaded") or []), set(cov_b.get("not_loaded") or [])
        print("## Source coverage (COVERAGE change, not evidence)")
        for d in diffs or ["loaded record counts: no difference"]:
            print(f"- loaded: {d}")
        for s in sorted(na - nb):
            print(f"- no longer listed as not loaded: {s}")
        for s in sorted(nb - na):
            print(f"- newly listed as not loaded: {s}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
