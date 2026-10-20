#!/usr/bin/env python3
"""Helpers for funding-and-portfolio-comparison. Standard library only.

compare FILE            Turn a saved diligence-dh.compare_portfolio output (the raw
                        response, or the examples/live wrapper with "calls") into a
                        markdown table, one row per company, with the resolution basis,
                        record counts, the evidence maturity score with its points and
                        components, and the notes the person must see (brand resolved to
                        its maker, combined filing names, unresolved, field absent,
                        not assessable, none found).
funding FILE            Turn a saved diligence-dh.get_funding_signals output, or a
                        build_company_profile output holding funding_and_filings, into
                        a table of public filings by type. Amounts are shown only per
                        filing row, by type; sum_of_stated_amounts is reported as present
                        and not used.
crosscheck CMP FUND     Check that the funding signal counts in a compare_portfolio row
                        match the source counts of a get_funding_signals output for the
                        same company.
swap FILE               Read an analytics.mcda input (alternatives + criteria_weights,
                        the person's own scores) and, if present, its results. Recompute
                        the EVIDEM weighted sum (value = 25 x sum(weight x score), 0 to 4
                        scale), check it against the tool, flag ties, and give for each
                        adjacent pair and criterion the weight at which the pair would
                        swap, the other weights kept in proportion.
words ANSWER.md         Count the words of a drafted answer, without the calls list
                        (the "Calls made" block, up to the record line) and table columns headed
                        Source or Retrieved. Short mode limit 450; prints the cut order
                        if over.

Missing fields stay missing: an absent field or sub-field is printed "field absent",
never 0, none or a country. Company status (exists, bankrupt, delisted, deregistered,
acquired) is never in the library record: each output names the status step in
references/company-status.md.

Nothing is scored, valued or recommended. The script reads only what the files hold.
"""
import json
import sys


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def cell(v):
    if v is None:
        return "null"
    if isinstance(v, dict):
        return "; ".join(f"{k} {cell(x)}" for k, x in v.items())
    if isinstance(v, list):
        return "; ".join(cell(x) for x in v)
    return str(v).replace("|", "/")


def compare_calls(d):
    if isinstance(d, dict) and "calls" in d:
        return d["calls"]
    if isinstance(d, dict) and "response" in d:
        r = d["response"]
        r.setdefault("arguments", d.get("call", {}).get("arguments"))
        return [r]
    return [d]


STUDY_KEYS = ("total", "linked_by_brand", "linked_by_indication_only", "unlinked")


def studies_cell(v):
    if not isinstance(v, dict):
        return cell(v) if v is not None else "field absent", list(STUDY_KEYS)
    absent = [k for k in STUDY_KEYS if k not in v]
    parts = [f"{k} {cell(v[k])}" if k in v else f"{k} field absent" for k in STUDY_KEYS]
    parts += [f"{k} {cell(x)}" for k, x in v.items() if k not in STUDY_KEYS]
    return "; ".join(parts), absent


def compare(path):
    d = load(path)
    notes = []
    status_names = []
    print("| Query | Company as resolved | Resolution | Authorizations | Studies | Safety events | Funding signal counts | Evidence maturity (rubric) | Reimbursement |")
    print("|---|---|---|---|---|---|---|---|---|")
    for c in compare_calls(d):
        when = c.get("retrieved_at", "date not in file")
        for r in c.get("companies", []):
            q = r.get("query", "")
            res = r.get("resolution", "")
            if res.startswith("unresolved"):
                print(f"| {q} | lookup missed | {cell(res)} | not assessable | not assessable | not assessable | not assessable | not assessable | not assessable |")
                notes.append(f"{q}: unresolved ({when}); every metric not assessable. Write 'lookup missed', never zero or absent.")
                continue
            comp = r.get("company", "")
            em = r.get("evidence_maturity", {})
            ap = em.get("assessable_points", {})
            emtxt = f"{em.get('score')} ({ap.get('earned')} of {ap.get('maximum')} assessable points; {cell(em.get('components', {}))})" if em else "field absent"
            fund = r.get("funding_signal_counts")
            fundtxt = cell(fund) if fund is not None else "field absent"
            stxt, sabsent = studies_cell(r.get("studies"))
            if sabsent:
                notes.append(f"{comp}: studies sub-field(s) absent in the response: {', '.join(sabsent)}. Write 'field absent', never 0.")
            status_names.append(comp)
            print(f"| {q} | {comp} | {cell(res)} | {cell(r.get('authorizations_by_jurisdiction', 'field absent'))} | "
                  f"{stxt} | {cell(r.get('safety_events', 'field absent'))} | {fundtxt} | {emtxt} | "
                  f"{cell(r.get('reimbursement_listings', 'field absent'))} |")
            if q.strip().lower() != comp.strip().lower():
                notes.append(f"{q}: resolved to the company {comp}; the row is company level and covers all its products, not the product queried.")
            if fund is None:
                notes.append(f"{comp}: no funding_signal_counts field in the response. Not a zero; call get_funding_signals for this company to see what the store holds.")
            for f in r.get("risk_flags", []):
                notes.append(f"{comp}: risk flag as returned: {f}")
            if r.get("safety_events") == "none_found":
                notes.append(f"{comp}: safety events none_found means the loaded sources hold no row; not evidence that nothing happened.")
        print()
        print(f"Call retrieved {when}: arguments {cell(c.get('arguments'))}.")
    rg = None
    for c in compare_calls(d):
        rg = rg or c.get("reading_guide")
    if rg:
        print(f"Reading guide as returned: {rg}")
    cov = d.get("source_coverage_excerpt") if isinstance(d, dict) else None
    if cov:
        print("Not loaded as returned: " + "; ".join(cov.get("not_loaded", [])))
    print()
    print("Notes for the person:")
    for n in notes:
        print(f"- {n}")
    print("- The evidence maturity score is the library's stated convention for documented evidence, not a valuation or a prediction. It is never a rank of the companies.")
    print("- Authorizations by jurisdiction say where products are authorized, not where a company is incorporated; incorporation is not in the record. Never write 'US company' from them.")
    print()
    print("Status (references/company-status.md): the library record does not show whether a company exists, is in bankruptcy, was delisted, deregistered or acquired.")
    for n in status_names:
        print(f"- {n}: status [GAP]: not read. Open its EDGAR filing list for each CIK (8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15) or its register; a Form 15 or 25 is not dissolution (DL-144, DL-149).")


def funding_block(d):
    if isinstance(d, dict) and "response" in d:
        d = d["response"]
    if "funding_and_filings" in d:
        return {"sources": d["funding_and_filings"], "private_rounds": d.get("funding", "[GAP]"),
                "gap_reason": d.get("funding_gap_reason"), "profile": True}
    return {"sources": d.get("sources", {}), "private_rounds": d.get("private_rounds", "[GAP]"),
            "total": d.get("total_public_signals"), "cik": d.get("sec_cik"), "profile": False}


def funding(path):
    d = load(path)
    company = (d.get("call", {}).get("arguments") or d.get("call", {}).get("args") or {}).get("company", "company not in file")
    b = funding_block(d)
    src = b["sources"]
    print(f"Company queried: {company}. SEC CIK as returned: {cell(b.get('cik')) if b.get('cik') is not None else 'field absent'}. Total public signals as returned: {cell(b.get('total'))}.")
    print()
    sec = src.get("sec_edgar", {})
    print("| SEC form type | Filings in the store |")
    print("|---|---|")
    for t, n in (sec.get("by_type") or {}).items():
        print(f"| {t} | {n} |")
    print()
    if sec.get("date_range"):
        print(f"SEC filing dates in the store: {sec['date_range'][0]} to {sec['date_range'][1]} (latest filing in the store, not a statement about the company today).")
    rows = sec.get("rows") or sec.get("latest") or []
    if rows:
        print()
        print("| Type | Date | Amount as stored | Counterparty | Reference |")
        print("|---|---|---|---|---|")
        for r in rows:
            amt = r.get("amount")
            amt = "not stated" if amt is None else f"{amt:,} {r.get('currency', '')}".strip()
            print(f"| {r.get('type')} | {r.get('date')} | {amt} | {cell(r.get('counterparty', 'field absent'))} | {r.get('reference', 'field absent')} |")
        print(f"\nRows shown: {len(rows)} of {sec.get('count', '?')} SEC filings (the saved file may be trimmed).")
    if "sum_of_stated_amounts" in sec:
        print("sum_of_stated_amounts is present and not used: it adds amounts across filing types (the tool's own caveat). Quote amounts per filing, by type.")
    for k, v in src.items():
        if k == "sec_edgar":
            continue
        print(f"{k}: {cell(v)}")
    print(f"Private rounds: {cell(b['private_rounds'])}" + (f" ({b['gap_reason']})" if b.get("gap_reason") else ""))
    if b.get("profile"):
        print("Note: build_company_profile says funding [GAP] while funding_and_filings lists Form D rows in the same response. Read Form D as an offering notice the company filed; which Item 13 field the amount is (total offering or amount sold) is not stated by the tool.")
    if any(r.get("type") in ("D", "D/A") for r in rows) or "D" in (sec.get("by_type") or {}):
        print("Form D: no valuation, price per share, lead investor or investor names (DL-018); amount sold may be stale (DL-006).")
    bt = sec.get("by_type") or {}
    seen = [t for t in ("25", "25-NSE", "15-12G", "15-12B", "15-15D") if t in bt]
    print()
    print(f"Status forms in the store: {', '.join(seen) if seen else 'none of Form 25 or Form 15'}. "
          "The store holds the CIKs above and selected form types only; a parent, listed or successor registrant may file under another CIK. "
          "Status [GAP]: not read unless the filings are opened: 8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15 (references/company-status.md). "
          "A Form 15 or 25 is not dissolution (DL-144, DL-149).")


def crosscheck(cmp_path, fund_path):
    d = load(cmp_path)
    f = load(fund_path)
    company = (f.get("call", {}).get("arguments") or {}).get("company", "")
    b = funding_block(f)
    found = False
    for c in compare_calls(d):
        for r in c.get("companies", []):
            if r.get("company", "").lower() == company.lower():
                found = True
                counts = r.get("funding_signal_counts")
                if counts is None:
                    print(f"{company}: compare_portfolio row has no funding_signal_counts field.")
                    continue
                for k, n in counts.items():
                    m = (b["sources"].get(k) or {}).get("count")
                    status = "match" if m == n else f"DIFFERENT (get_funding_signals {m})"
                    print(f"{company} {k}: compare_portfolio {n}; get_funding_signals {m}: {status}")
    if not found:
        print(f"{company}: not in the compare_portfolio file; nothing to check.")


def value(scores, weights):
    return 25.0 * sum(weights[c] * scores.get(c, 0) for c in weights)


def swap(path):
    d = load(path)
    args = d.get("call", {}).get("arguments") or d.get("call", {}).get("args") or d
    alts = args["alternatives"]
    w = args["criteria_weights"]
    missing = [(a["id"], k) for a in alts for k in w if k not in a["scores"]]
    if missing:
        print("Missing scores (analytics.mcda refuses the whole call with HTTP 400): " + "; ".join(f"{i} {k}" for i, k in missing))
        print("Drop the unscored option before the call and list it as not ranked, or ask the person for the score.")
        return
    bad = [(a["id"], k, v) for a in alts for k, v in a["scores"].items() if not 0 <= v <= 4]
    if bad:
        print("Scores outside 0 to 4: " + "; ".join(f"{i} {k}={v}" for i, k, v in bad))
    total = sum(w.values())
    if abs(total - 1) > 1e-6:
        print(f"Weights sum to {total:.3f}, not 1. Ask the person to confirm before ranking.")
    ranked = sorted(alts, key=lambda a: value(a["scores"], w), reverse=True)
    print("| Order | Option | Value (recomputed) |")
    print("|---|---|---|")
    for i, a in enumerate(ranked, 1):
        print(f"| {i} | {a['id']} | {value(a['scores'], w):.2f} |")
    res = d.get("response", d).get("results", []) if isinstance(d.get("response", d), dict) else []
    tool = {r["id"]: r.get("value_estimate") for r in res}
    if tool:
        mism = [a["id"] for a in alts if abs((tool.get(a["id"]) or -1) - value(a["scores"], w)) > 0.01]
        print("\nCheck against analytics.mcda: " + ("all values match." if not mism else f"MISMATCH for {mism}"))
    for x, y in zip(ranked, ranked[1:]):
        if abs(value(x["scores"], w) - value(y["scores"], w)) < 1e-9:
            print(f"Tie: {x['id']} and {y['id']} have the same value; the tool does not flag ties.")
    print("\nWhere adjacent options would swap (one weight moved, the others kept in proportion):\n")
    print("| Pair | Criterion | Current weight | Swap at weight | Direction |")
    print("|---|---|---|---|---|")
    for hi, lo in zip(ranked, ranked[1:]):
        for k in w:
            a = hi["scores"].get(k, 0) - lo["scores"].get(k, 0)
            rest = sum(w[c] * (hi["scores"].get(c, 0) - lo["scores"].get(c, 0)) for c in w if c != k)
            if w[k] >= 1:
                continue
            B = rest / (1 - w[k])
            if abs(B - a) < 1e-12:
                continue
            t = B / (B - a)
            if 1e-6 < t < 1 - 1e-6 and abs(t - w[k]) > 1e-9:
                direction = "if raised above" if t > w[k] else "if lowered below"
                print(f"| {hi['id']} over {lo['id']} | {k} | {w[k]:.2f} | {t:.2f} | {direction} |")
    for x in alts:
        for y in alts:
            if x is not y and all(x["scores"][k] >= y["scores"][k] for k in w) and any(x["scores"][k] > y["scores"][k] for k in w):
                print(f"Dominance: {x['id']} scores at least as high as {y['id']} on every criterion; that order holds at any weights.")
    print("\nCriteria not listed for a pair cannot swap that pair at any weight strictly between 0 and 1.")
    print("The order is the person's scores and weights, computed. It is not a recommendation to invest, pass or price.")


CUT_ORDER = ("context paragraphs, repeated row ids in prose, secondary rules, rows not tied to "
             "the person's question. Never cut a gap, a stop or the record line.")


def words(path, limit=450):
    """Count the answer's words without the calls list and table source columns."""
    import re
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    seps = [i for i, x in enumerate(lines) if x.strip() == "---"]
    if len(seps) >= 2:
        lines = lines[seps[0] + 1:seps[1]]
    lines = [x for x in lines if not re.match(r"^\s*Sources?:", x)]
    kept, drop_cols, in_table = [], set(), False
    _skip_calls = False  # the calls list sits before the record block; skip it, then count the record
    for ln in lines:
        if _skip_calls:
            if re.search(r"Clears it|^\W*(#+\s*)?(\*\*)?(\d+\.\s*)?(\*\*)?Record\b", ln.strip()):
                _skip_calls = False
            else:
                continue
        if re.match(r"^\s*(#+\s*|\*\*|\d+\.\s*\*\*)?\s*Calls made", ln, re.I):
            _skip_calls = True
            continue
        s = ln.strip()
        if s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if not in_table:
                drop_cols = {i for i, c in enumerate(cells) if re.search(r"source|retriev", c, re.I)}
                in_table = True
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            ln = " ".join(c for i, c in enumerate(cells) if i not in drop_cols)
        else:
            in_table = False
        kept.append(ln)
    n = len(re.findall(r"\S+", "\n".join(kept)))
    print(f"Words (without the calls list and table source columns): {n}. Limit: {limit}.")
    if n > limit:
        print(f"Over by {n - limit}. Cut in this order until under: " + CUT_ORDER)
    else:
        print("Within the limit.")


if __name__ == "__main__":
    cmds = {"compare": (compare, 1), "funding": (funding, 1), "crosscheck": (crosscheck, 2), "swap": (swap, 1), "words": (words, 1)}
    if len(sys.argv) < 3 or sys.argv[1] not in cmds or len(sys.argv) - 2 != cmds[sys.argv[1]][1]:
        print(__doc__)
        sys.exit(2)
    cmds[sys.argv[1]][0](*sys.argv[2:])
