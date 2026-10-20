#!/usr/bin/env python3
"""Turn saved diligence-dh output into the tables a company and evidence read needs.

Reads JSON saved from diligence-dh.build_company_profile, get_evidence_maturity or
compare_portfolio (a single response, a {"call":..., "response":...} wrapper, or a
{"calls": [...]} wrapper, as in examples/live/). Prints, per company:

  1. Products and authorizations as stored, with the pathway in words
     ("DENG" is FDA's raw code for a granted De Novo, register C3).
  2. Filings stored in the profile, by form type, with what each form does and does
     not show (Form D rows DL-002, DL-006, DL-015, DL-018).
  3. The library's evidence maturity convention: each component, the points, the
     excluded components, and a recomputation of the stated formula
     (score = round(100 x earned / assessable maximum)).
  4. Safety events and recall flags as stored (compare_portfolio carries them;
     build_company_profile does not, and its silence is never printed as 0 or none),
     and a reminder that company status is not in the library (status step,
     references/company-status.md, DL-135 to DL-168).
  5. Contradictions inside the same response (a "[GAP]" field beside data that fills
     it; "US sources only" beside non-US authorizations that earned points).

It only re-arranges and re-checks what the records state. It does not rate the
company, propose a framework level, or infer revenue, runway, valuation or intent.

Usage: python3 profile_table.py FILE.json [FILE.json ...]
       python3 profile_table.py --count ANSWER.md
         counts a short answer's words without the "Calls made" list and without
         table columns whose header starts with "Source"; flags anything over 450
         and prints the house cut order.
"""
import json
import re
import sys
from datetime import date

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


def full_date(s):
    if not s:
        return "not stored"
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", str(s))
    if not m:
        return str(s)
    y, mo, d = (int(x) for x in m.groups())
    return f"{d} {MONTHS[mo - 1]} {y}"


def pathway_words(pathway, status):
    p = (pathway or "").upper()
    s = (status or "")
    if "DE_NOVO" in p or s == "DENG":
        return "FDA De Novo" + (", granted (raw code DENG)" if s == "DENG" else f", {s}")
    if "510K" in p:
        return f"FDA 510(k), {s or 'status not stored'} (clearance, not approval, DL-128)"
    if "PMA" in p:
        return f"FDA PMA, {s or 'status not stored'}"
    return f"{pathway or 'pathway not stored'}, {s or 'status not stored'}"


def records(path):
    with open(path) as f:
        data = json.load(f)
    out = []
    if isinstance(data, dict) and "calls" in data:
        for c in data["calls"]:
            if "companies" in c and isinstance(c["companies"], list):
                for co in c["companies"]:
                    co = dict(co)
                    co.setdefault("retrieved_at", c.get("retrieved_at"))
                    out.append(("compare_portfolio", co, data))
            else:
                out.append(("get_evidence_maturity", c, data))
    elif isinstance(data, dict) and "response" in data:
        out.append(((data.get("call") or {}).get("tool", "build_company_profile"), data["response"], data))
    else:
        out.append(("unknown", data, data))
    return out


def parse_points(text):
    m = re.search(r"(\d+)\s*(?:of|/)\s*(\d+)", str(text or ""))
    return (int(m.group(1)), int(m.group(2))) if m else (None, None)


def maturity_block(tool, rec):
    em = rec.get("evidence_maturity") if tool != "get_evidence_maturity" else rec
    if not em:
        return None
    if isinstance(em, str):
        return {"score": em, "lines": [f"stated as text: {em}"], "flags": []}
    score = em.get("score")
    comps, earned, maximum = [], 0, 0
    raw = em.get("components") or []
    if isinstance(raw, dict):
        for k, v in raw.items():
            e, mx = parse_points(v)
            comps.append((k, e, mx, None))
    else:
        for c in raw:
            comps.append((c.get("component"), c.get("points"), c.get("max_points"), c.get("inputs")))
    ap = em.get("assessable_points") or {}
    se, sm = ap.get("earned"), ap.get("maximum")
    if se is None:
        se, sm = parse_points(em.get("score_scale"))
    if comps and all(c[1] is not None for c in comps):
        earned = sum(c[1] for c in comps)
    else:
        earned = se
    if all(c[2] is not None for c in comps) and comps:
        maximum = sum(c[2] for c in comps)
    else:
        maximum = sm
    lines, flags = [], []
    for name, e, mx, inputs in comps:
        inp = ""
        if inputs:
            inp = "; inputs " + ", ".join(f"{k} {v}" for k, v in inputs.items())
        lines.append(f"{name}: {e if e is not None else '?'} of {mx if mx is not None else 'max not in this output'}{inp}")
    for x in em.get("not_assessable") or []:
        lines.append(f"excluded (not counted as zero): {x.get('component')}: {x.get('reason')}")
    for x in em.get("excluded_dimensions") or []:
        lines.append(f"excluded (not counted as zero): {x}")
    if earned is not None and maximum:
        recomputed = round(100 * earned / maximum)
        ok = "matches" if recomputed == score else f"DOES NOT MATCH stated {score}"
        lines.append(f"formula check: round(100 x {earned} / {maximum}) = {recomputed}, {ok}")
    if comps and se is not None and earned is not None and se != earned:
        flags.append(f"component points sum to {earned} but the response states {se} earned")
    return {"score": score, "rubric": em.get("rubric_version"), "lines": lines, "flags": flags,
            "limits": (em.get("interpretation_limits") or [])
            + ([em["interpretation_limits_excerpt"]] if em.get("interpretation_limits_excerpt") else []),
            "risk_flags": em.get("risk_flags") or rec.get("risk_flags") or []}


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


def safety_lines(tool, rec):
    out = []
    if "safety_events" in rec:
        se = rec["safety_events"]
        if se == "none_found":
            out.append("safety_events: none_found: none found in the loaded enforcement source; not proof of none")
        else:
            out.append(f"safety_events as stored: {se}")
    else:
        out.append(f"safety_events: field not in this {tool} response; not 0 and not none. "
                   "Read the saved compare_portfolio result or mark 'not read [GAP]'")
    for fl in rec.get("risk_flags") or []:
        if "recall" in str(fl).lower():
            out.append(f"recall flag as stored (quote verbatim; truncation is the saved file's): {fl}")
    return out


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == "--count":
        return count_words(argv[1]) if len(argv) > 1 else 2
    for path in argv:
        for tool, rec, wrapper in records(path):
            name = rec.get("company") or (rec.get("arguments") or {}).get("company") \
                or ((wrapper.get("call") or {}).get("arguments") or {}).get("company") or rec.get("query")
            res = rec.get("resolution")
            if isinstance(res, dict):
                res = f"{res.get('status')}, {res.get('basis')}"
            when = rec.get("retrieved_at") or (rec.get("provenance") or {}).get("retrieved_at") \
                or wrapper.get("retrieved") or ""
            print(f"## {name}  ({tool}; file {path.split('/')[-1]}; retrieved {full_date(when)})")
            print(f"Resolution as stated: {res or 'not stated'}. A brand or number resolves to the company, not one product.")
            ids = rec.get("identifiers")
            if ids:
                print("Identifiers: " + "; ".join(f"{k} {v}" for k, v in ids.items()))
            prods = rec.get("products") or []
            if prods and isinstance(prods[0], dict):
                print("\n| Product | Record | Pathway as stored | Product code | Regulation | Decision date | Source |")
                print("|---|---|---|---|---|---|---|")
                for p in sorted(prods, key=lambda x: x.get("decision_date") or ""):
                    print(f"| {p.get('product')} | {p.get('fda_submission')} | {pathway_words(p.get('pathway'), p.get('status'))} | "
                          f"{p.get('product_code')} | {p.get('regulation_number')} | {full_date(p.get('decision_date'))} | {p.get('source_url', 'not stored')} |")
            abj = rec.get("authorizations_by_jurisdiction")
            if abj:
                print("Authorizations by jurisdiction as stored: " + ", ".join(f"{k} {v}" for k, v in abj.items()))
            st = rec.get("clinical_evidence") or rec.get("studies")
            if st:
                print("Registered studies as linked by the library: " + ", ".join(f"{k} {v}" for k, v in st.items())
                      + " (registry rows, not publications; indication-only links are weaker)")
            ff = (rec.get("funding_and_filings") or {}).get("sec_edgar")
            if ff:
                print(f"\nSEC filings stored: {ff.get('count')} ({', '.join(f'{k} {v}' for k, v in (ff.get('by_type') or {}).items())})")
                print("| Form | Filed | Amount as stated | What the form does not show |")
                print("|---|---|---|---|")
                for r in ff.get("latest") or []:
                    note = ("Form D: amount sold as of filing, may be stale (DL-006, DL-015); date tracks first sale "
                            "(DL-002); no valuation, price per share or investor names (DL-018 (inference))") \
                        if r.get("type", "").startswith("D") else "read the filing at its URL"
                    amt = f"USD {r['amount']:,}" if isinstance(r.get("amount"), (int, float)) else "not stated"
                    print(f"| {r.get('type')} | {full_date(r.get('date'))} | {amt} | {note} |")
            print("\nSafety events and recall flags:")
            for l in safety_lines(tool, rec):
                print(f"- {l}")
            print("Company status: not in the library. Run the status step (references/company-status.md, "
                  "DL-135 to DL-168) or write 'Status: [GAP]: not read' with the filings to open.")
            if abj and not ids:
                print("Note: authorizations by jurisdiction say where products are authorized, not where the company "
                      "is incorporated; country of incorporation not in this response.")
            flags = []
            for field in ("funding", "reimbursement"):
                if str(rec.get(field, "")).startswith("[GAP]"):
                    reason = rec.get(field + "_gap_reason", "")
                    if field == "funding" and ff and ff.get("count"):
                        flags.append(f"funding says [GAP] ('{reason}') while the same response stores {ff.get('count')} SEC filing(s): "
                                     "read filings as what the company filed; private rounds stay [GAP]")
                    else:
                        flags.append(f"{field} [GAP]: {reason or 'reason not stated'}")
            mb = maturity_block(tool, rec)
            if mb:
                print(f"\nLibrary evidence maturity convention (rubric {mb.get('rubric') or 'version not in this output'}): "
                      f"score {mb['score']}. A stated convention, not a framework level, a rating or a valuation.")
                for l in mb["lines"]:
                    print(f"- {l}")
                for l in mb.get("limits") or []:
                    print(f"- limit stated by the tool: {l}")
                for l in mb.get("risk_flags") or []:
                    print(f"- risk flag as stated: {l}")
                flags += mb["flags"]
                limits = " ".join(mb.get("limits") or []).lower()
                nonus = (abj and any(k != "US" for k in abj)) or bool(re.search(r"deutschland|gmbh|\bag\b", str(res).lower()))
                if "us sources only" in limits and nonus:
                    flags.append("the tool says 'US sources only' but this company resolves to a non-US filer or holds non-US "
                                 "authorizations; name the register behind each authorization before relying on the score")
            print("\nContradictions and gaps inside the response:")
            for fl in flags or ["none found by this script"]:
                print(f"- {fl}")
            print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
