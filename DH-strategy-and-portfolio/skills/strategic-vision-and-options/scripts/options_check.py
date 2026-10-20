#!/usr/bin/env python3
"""Helper for strategic-vision-and-options (dh-strategy-and-portfolio).

Four subcommands. None of them sets a score, a weight, a range or a decision:
every number comes from the person or from a saved library output.

  rank     Check the person's option scores and weights, reproduce the
           analytics.mcda weighted sum (EVIDEM, 0 to 4 scale), and print the
           swap points: the weight on one criterion at which two adjacent
           options tie (the library returns no robustness view, register C17).
           For each option not scored on every criterion it prints the sum on
           the criteria scored and the score on the missing criterion at which
           it would tie each ranked option (the missing score is never filled).
             python3 options_check.py rank --input SCORES.json [--mcda MCDA.json]
           SCORES.json: {"scored_by": "...", "proposed": false,
                         "criteria_weights": {"c1": 0.4, ...},
                         "alternatives": [{"id": "...", "scores": {"c1": 3, ...}}]}
           A saved analytics.mcda response file (call plus response) also works
           as --input.

  tornado  Read a saved analytics.risk-tornado result and print the swings with
           flags R1 to R4 (facts about the run, never verdicts).
             python3 options_check.py tornado --file analytics_calls.json [--n 1]

  facts    Turn a saved diligence-dh.build_company_profile output into an
           authorization table (pathways in words), Form D rows with their
           caveats, the library's evidence maturity with its rubric, and the
           company status line: quoted from the research pass rows for the
           companies it read (Akili, Pear, Big Health, Aidoc; SP-148 to
           SP-169), with current FDA listing holders, otherwise the filings to
           open.
             python3 options_check.py facts --profile PROFILE.json [--funding FUNDING.json]

  words    Count a short answer against the 450-word cap. Leaves out the
           "Calls made" block (up to the record block, which is counted) and the
           Source and Rows columns.
             python3 options_check.py words ANSWER.md
"""
import argparse
import json
import re
import sys
from datetime import date

CAP = 450


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def full_date(s):
    if not s:
        return "not given"
    try:
        d = date.fromisoformat(str(s)[:10])
    except ValueError:
        return str(s)
    return f"{d.day} {d.strftime('%B')} {d.year}"


# ---------------------------------------------------------------- rank

def read_scores(path):
    d = load(path)
    if "call" in d and "arguments" in d.get("call", {}):
        args = d["call"]["arguments"]
        return {"scored_by": "illustrative inputs in a saved library call",
                "proposed": False,
                "criteria_weights": args["criteria_weights"],
                "alternatives": args["alternatives"],
                "_response": d.get("response")}
    return d


def mcda_value(scores, weights):
    contrib = {c: round(w * scores[c] / 4 * 100, 6) for c, w in weights.items()}
    return round(sum(contrib.values()), 6), contrib


def swap_point(a, b, weights, c):
    """Weight on criterion c at which a and b tie, other weights rescaled
    proportionally. Returns None when no tie exists inside 0..1."""
    wc = weights[c]
    if wc >= 1:
        return None
    d = {k: a[k] - b[k] for k in weights}
    rest = sum(weights[k] * d[k] for k in weights if k != c) / (1 - wc)
    denom = rest - d[c]
    if abs(denom) < 1e-12:
        return None
    x = rest / denom
    if 0.001 < x < 0.999:
        return round(x, 3)
    return None


def cmd_rank(args):
    d = read_scores(args.input)
    if d.get("proposed"):
        print("Not ranked: these scores are labeled proposed. Proposed scores are never "
              "sent to analytics.mcda; the person confirms or replaces them first.")
        return 1
    w = d.get("criteria_weights") or {}
    alts = d.get("alternatives") or []
    print(f"Scored by: {d.get('scored_by') or 'not given'}")
    total = round(sum(w.values()), 6)
    problems = []
    if not w:
        problems.append("weights not given: nothing is ranked")
    elif abs(total - 1) > 0.001:
        problems.append(f"weights sum to {total}, not 1: ask the person to fix them; nothing is rescaled")
    for c, v in w.items():
        if v < 0:
            problems.append(f"negative weight on {c}")
    ranked, not_ranked = [], []
    for a in alts:
        s = a.get("scores", {})
        missing = [c for c in w if c not in s or s[c] is None]
        bad = [c for c in w if c in s and s[c] is not None and not (0 <= s[c] <= 4)]
        if missing:
            not_ranked.append((a["id"], "not scored on " + ", ".join(missing), s, missing))
        elif bad:
            not_ranked.append((a["id"], "score outside 0 to 4 on " + ", ".join(bad), s, []))
        else:
            v, contrib = mcda_value(s, w)
            ranked.append((a["id"], v, contrib, s))
    if problems:
        for p in problems:
            print("STOP: " + p)
        return 1
    ranked.sort(key=lambda r: -r[1])
    print("\nArithmetic on the person's scores, not a decision (EVIDEM weighted sum, 0 to 4).")
    print("| Option | Value | Contributions |")
    print("|---|---|---|")
    for oid, v, contrib, _ in ranked:
        cs = "; ".join(f"{k} {contrib[k]:g}" for k in sorted(contrib))
        print(f"| {oid} | {v:g} | {cs} |")
    for oid, why, _, _ in not_ranked:
        print(f"| {oid} | not ranked | {why} |")
    ties = [(ranked[i][0], ranked[i + 1][0]) for i in range(len(ranked) - 1)
            if abs(ranked[i][1] - ranked[i + 1][1]) < 1e-9]
    for a, b in ties:
        print(f"TIE: {a} and {b} have the same value; the arithmetic does not separate them.")
    resp = d.get("_response")
    if args.mcda:
        resp = load(args.mcda).get("response", resp)
    if resp:
        lib = {r["id"]: r["value_estimate"] for r in resp.get("results", [])}
        diffs = [oid for oid, v, _, _ in ranked if oid in lib and abs(lib[oid] - v) > 0.01]
        print("\nLibrary check: " + ("analytics.mcda values match this arithmetic."
                                     if not diffs else "MISMATCH for " + ", ".join(diffs)))
    print("\nSwap points (weight on one criterion at which two adjacent options tie; other "
          "weights rescaled in proportion). Facts about the person's weights, not advice:")
    any_swap = False
    for i in range(len(ranked) - 1):
        a, b = ranked[i], ranked[i + 1]
        for c in sorted(w):
            x = swap_point(a[3], b[3], w, c)
            if x is not None and abs(x - w[c]) > 1e-9:
                any_swap = True
                print(f"- {a[0]} and {b[0]} tie when the weight on {c} is {x:g} (yours: {w[c]:g}).")
    if not any_swap:
        print("- No single-criterion weight change inside 0 to 1 makes adjacent options tie.")
    decides_top = False
    for oid, why, sc, missing in not_ranked:
        if not missing:
            continue
        part = round(sum(w[c] * sc[c] / 4 * 100 for c in w if c not in missing), 6)
        print(f"\nTie scores for {oid} (not ranked; {why}). Sum on the criteria scored: {part:g}. "
              "Arithmetic on the person's scores; the missing score is the person's and is never filled in.")
        if len(missing) == 1:
            c = missing[0]
            per_point = w[c] * 100 / 4
            for rid, v, _, _ in ranked:
                x = (v - part) / per_point if per_point else None
                if x is None:
                    line = "weight on the missing criterion is 0: the value stays " + f"{part:g}"
                elif x <= 0:
                    line = f"already at or above {rid} ({v:g}) with any score from 0"
                    if ranked and rid == ranked[0][0]:
                        decides_top = True
                elif x > 4:
                    line = f"cannot reach {rid} ({v:g}) even with 4"
                else:
                    line = f"ties {rid} ({v:g}) at a {c} score of {x:.4g} (0 to 4); any higher score puts it above"
                    if ranked and rid == ranked[0][0]:
                        decides_top = True
                print(f"- {line}.")
        else:
            for rid, v, _, _ in ranked:
                need = v - part
                print(f"- needs {need:g} weighted points across {', '.join(missing)} to tie {rid} ({v:g}).")
            if ranked and ranked[0][1] - part <= sum(w[c] for c in missing) * 100:
                decides_top = True
    if decides_top:
        print("TOP NOT SETTLED: an unranked option's tie score with first place lies inside the 0 to 4 scale. "
              "Do not say first place holds; say which empty cell decides the top.")
    print("\nEvery criterion is read as higher-is-better (register C17): name criteria so a "
          "higher score is better.")
    return 0


# ---------------------------------------------------------------- tornado

def tornado_runs(path):
    d = load(path)
    runs = []
    if isinstance(d, dict) and "calls" in d:
        for c in d["calls"]:
            if c.get("call") == "analytics.risk-tornado" and isinstance(c.get("result"), dict):
                runs.append((c.get("arguments", {}), c["result"]))
    elif isinstance(d, dict) and "result" in d:
        runs.append((d.get("arguments", {}), d["result"]))
    return runs


def cmd_tornado(args):
    runs = tornado_runs(args.file)
    if not runs:
        print("No analytics.risk-tornado result in the file.")
        return 1
    idx = (args.n or 1) - 1
    arguments, res = runs[idx]
    ranges = arguments.get("parameter_ranges", {}) or {}
    formula = arguments.get("formula", "")
    base = res.get("base_value")
    print(f"Formula: {formula}")
    print(f"Base value: {base:g}  (variation used where no range was given: "
          f"plus or minus {res.get('variation_pct', 0.2) * 100:g} percent)")
    print("| Parameter | Low to high input | Output low to high | Swing | Flags |")
    print("|---|---|---|---|---|")
    for r in res.get("results", []):
        flags = []
        if r["parameter"] not in ranges:
            flags.append("R1 default range, not the person's")
        lo, hi = r["low_output"], r["high_output"]
        if base is not None and ((lo < 0) != (base < 0) or (hi < 0) != (base < 0)):
            flags.append("R3 output changes sign")
        print(f"| {r['parameter']} | {r['low_value']:g} to {r['high_value']:g} | "
              f"{lo:g} to {hi:g} | {r['swing']:g} | {'; '.join(flags) or 'none'} |")
    for p in res.get("skipped_parameters", []):
        print(f"| {p} | skipped | not varied | n/a | R2 list parameter skipped by the tool |")
    if re.search(r"/\s*\(\s*\w+\s*-\s*\w+\s*\)", formula):
        print("R4 the formula divides by a difference: a ratio can flip sign inside the range "
              "and the swing order then misleads. Run the tornado on a difference instead.")
    print("Sensitivity on the person's inputs; the ranges marked R1 must be replaced by the "
          "person's own before the result is used.")
    return 0


# ---------------------------------------------------------------- facts

# Company status read in the research pass of 20 October 2026 (rows in
# references/strategy-and-portfolio-research.md, section 8). SEC rows are [WF].
STATUS_READ = {
    "akili": {
        "match": ("akili",),
        "ciks": ("1850266",),
        "lines": [
            "Akili, Inc. (EDGAR CIK 1850266; Akili Interactive Labs, Inc. is its wholly owned subsidiary, "
            "not a former name) (Akili, Inc. EDGAR submissions record, read 20 October 2026, SP-148 [WF]).",
            "Akili 8-K, 29 May 2024: Item 1.01 merger agreement with Virtual Therapeutics Corporation, "
            "tender offer at $0.4340 per share (SP-150 [WF]). Signing, not closing (SEC Form 8-K instructions, DL-138).",
            "Akili 8-K, 2 July 2024: Item 2.01 offer completed 2 July 2024; Item 5.01 change in control, Akili "
            "became a wholly owned subsidiary of Virtual Therapeutics Corporation; Item 3.01 Nasdaq asked to "
            "file Form 25 (SP-151, SP-152 [WF]).",
            "Akili Form 25-NSE, 2 July 2024, filed by Nasdaq; body not readable (SP-153 [WF]). Form 25 concerns "
            "the listing only (SEC Rule 12d2-2, DL-144); after a merger it signals converted shares, not failure "
            "(DL-142, inference).",
            "Akili Form 15-12G, 12 July 2024 (SP-154 [WF]): SEC reporting stopped; not dissolution (SEC Rule "
            "12h-3, DL-149, inference). No later Akili filing will disclose a license or deal.",
            "EndeavorRx: De Novo DEN200026 requester akili interactive labs, inc. (FDA De Novo record, SP-166); "
            "listed now by \"AKILIINTERACTIVE Labs, Inc. C/O Virtual Therapeutics\", Kirkland, WA, registration "
            "year 2026 (FDA registration and listing database, read 20 October 2026, SP-168). The listing holder "
            "is not proof of who can grant a license.",
            "Virtual Therapeutics Corporation: Company status [GAP]: not read (no row).",
        ],
    },
    "pear": {
        "match": ("pear therapeutics",),
        "ciks": ("1835567",),
        "lines": [
            "Pear Therapeutics, Inc. (EDGAR CIK 1835567) (Pear EDGAR submissions record, read 20 October 2026, SP-155 [WF]).",
            "Pear 8-K, 7 April 2023: Item 1.03 chapter 11 filed 7 April 2023, US Bankruptcy Court, District of "
            "Delaware, case 23-10429; Item 2.05 about 170 employees (92%) terminated; Item 7.01 section 363 sale "
            "process, little or no equity recovery expected (SP-156, SP-158, SP-159 [WF]).",
            "Pear 8-K, 10 April 2023: Item 3.01 Nasdaq delisting notice, trading suspended 19 April 2023, no appeal (SP-160 [WF]).",
            "Pear Form 25-NSE, 2 May 2023: the last filing; no Form 15 and no 8-K after 10 April 2023 (SP-155 [WF]). "
            "No Item 1.03(b) plan confirmation appears: the outcome is open on EDGAR (DL-137, inference).",
            "No Pear filing names a buyer of Somryst, reSET or reSET-O (SP-161 [WF]); court sale orders not read.",
            "Somryst: 510(k) K191716 to Pear, 23 March 2020 (FDA 510(k) record, SP-165); listed now by Nox Medical, "
            "Reykjavik, from 18 December 2024 (FDA registration and listing database, read 20 October 2026, SP-167). "
            "reSET and reSET-O: listed now by Harvest Bio LLC, Middletown, CT, from 14 November 2024 (SP-169). "
            "A listing holder is not the sale record.",
        ],
    },
    "big health": {
        "match": ("big health",),
        "ciks": (),
        "lines": [
            "Big Health: no SEC registrant found (EDGAR company lookup and full-text search, 20 October 2026, SP-162 [WF]); "
            "no 8-K, Form 25 or Form 15 exists to read.",
            "FDA establishment BIG HEALTH INC, registration 3024442350, Newport Beach, active, registration year 2026; "
            "listings SleepioRx (K233577) and DaylightRx (K233872) (FDA registration and listing database, read "
            "20 October 2026, SP-163). An FDA registration is not corporate status.",
            "Corporate status: [GAP]: not read (state register of its legal entity; ask the legal entity).",
        ],
    },
    "aidoc": {
        "match": ("aidoc",),
        "ciks": (),
        "lines": [
            "Aidoc: no SEC registrant found (EDGAR company lookup, 20 October 2026, SP-162 [WF]).",
            "FDA establishment AIDOC MEDICAL LTD., registration 3014938447, Tel Aviv-Yafo, active, registration year 2026, "
            "25 device listings (FDA registration and listing database, read 20 October 2026, SP-164). "
            "An FDA registration is not corporate status.",
            "Corporate status: [GAP]: not read (Israeli company register; no row).",
        ],
    },
}


def status_read(company, ids):
    name = (company or "").lower()
    cik = str((ids or {}).get("SEC_CIK", "")).lstrip("0")
    for key, rec in STATUS_READ.items():
        if any(m in name for m in rec["match"]) or (cik and cik in rec["ciks"]):
            return key, rec
    return None, None


PATHWAY = {
    "FDA_510K": "510(k) cleared",
    "FDA_DE_NOVO": "De Novo granted",
    "FDA_PMA": "PMA approved",
}


def cmd_facts(args):
    p = load(args.profile)
    resp = p.get("response", p)
    company = p.get("call", {}).get("arguments", {}).get("company", "the company")
    retrieved = resp.get("provenance", {}).get("retrieved_at", "")
    print(f"Company: {company} (library, retrieved {full_date(retrieved)})")
    ids = resp.get("identifiers", {})
    if ids:
        print("Identifiers: " + "; ".join(f"{k} {v}" for k, v in ids.items()))
    print("\n| Product | Reference | Pathway in words | Product code | Decision date | Source |")
    print("|---|---|---|---|---|---|")
    for pr in resp.get("products", []):
        words = PATHWAY.get(pr.get("pathway"), pr.get("pathway") or "not stored")
        print(f"| {pr.get('product')} | {pr.get('fda_submission')} | {words} | "
              f"{pr.get('product_code') or 'not stored'} | {full_date(pr.get('decision_date'))} | "
              f"{pr.get('source_url') or 'not stored'} |")
    ce = resp.get("clinical_evidence")
    if ce:
        print(f"\nRegistered studies: {ce.get('studies_total')} in total, "
              f"{ce.get('studies_linked_by_brand')} linked by brand, "
              f"{ce.get('studies_linked_by_indication_only')} by indication only (registry records, not results).")
    em = resp.get("evidence_maturity")
    if em:
        pts = em.get("assessable_points", {})
        print(f"Evidence maturity (library convention, not an evidence verdict): {em.get('score')} "
              f"({pts.get('earned')} of {pts.get('maximum')} assessable points), rubric "
              f"{em.get('rubric_version')}, excluded: {', '.join(em.get('excluded_dimensions', [])) or 'none'}.")
    ff = resp.get("funding_and_filings", {}).get("sec_edgar", {})
    for row in ff.get("latest", []):
        if row.get("type") == "D":
            print(f"Form D filed {full_date(row.get('date'))}: amount as stored {row.get('currency')} "
                  f"{row.get('amount'):,}. A Form D shows no valuation or investor names "
                  f"(DL-016; DL-018, an inference); the amount may be stale (DL-006).")
    if resp.get("funding") == "[GAP]":
        print("Private rounds: [GAP] (no funding source licensed; register C2).")
    if resp.get("reimbursement") == "[GAP]":
        print("Reimbursement: [GAP] in this call; reimbursement status is dh-access-and-value "
              "coverage-pathway-and-access-strategy.")
    # company status
    eight_k, other = [], []
    if args.funding:
        f = load(args.funding).get("response", {})
        for row in f.get("sources", {}).get("sec_edgar", {}).get("rows", []):
            if row.get("type") in ("8-K", "8-K/A"):
                eight_k.append(row)
            if row.get("type") in ("25", "25-NSE", "15", "15-12B", "15-12G", "15-15D"):
                other.append(row)
    key, rec = status_read(company, ids)
    cik = ids.get("SEC_CIK")
    if rec:
        print("\nCompany status as read in the research pass (20 October 2026; the library stores no status field):")
        for line in rec["lines"]:
            print("- " + line)
        if cik and rec["ciks"] and cik.lstrip("0") not in rec["ciks"]:
            print(f"- The library profile carries CIK {cik}; the status above is for the listed entity, "
                  f"CIK {rec['ciks'][0]}. Say which entity each fact belongs to.")
        print("- Status is as of 20 October 2026; a later filing can change it. In the answer, name the option "
              "this status blocks and what would unblock it (option-frameworks.md section 5).")
        return 0
    print("\nCompany status [GAP]: not read. The library stores no status field.")
    if eight_k:
        for row in sorted(eight_k, key=lambda r: r.get("date", ""), reverse=True)[:2]:
            print(f"- Open the 8-K of {full_date(row.get('date'))} ({row.get('reference')}, "
                  f"{row.get('source_url') or 'URL not stored'}) for Items 1.03, 2.01, 3.01 and 5.01 (DL-136 to DL-141).")
    elif cik:
        print(f"- No 8-K row is stored for SEC CIK {cik}. On EDGAR, list the filings for CIK {cik} and open any "
              f"8-K for Items 1.03, 2.01, 3.01 and 5.01 (DL-136 to DL-141), and any Form 25 or Form 15 (DL-142 to DL-149).")
    else:
        print("- No SEC identifier stored: ask for the legal entity and its register (Companies House "
              "company_status, DL-157 to DL-164; German insolvency notices, DL-165 to DL-168).")
    for row in other:
        print(f"- {row.get('type')} of {full_date(row.get('date'))} is stored: open it.")
    print("- Form 25 concerns the listing only (DL-144); Form 15 is not dissolution (DL-149, inference). Never take status from press, "
          "memory or the date filings stopped. EDGAR asks automated clients for a declared contact "
          "(DL-153): ask which contact the person's organization uses; never invent one.")
    return 0


# ---------------------------------------------------------------- words

def count_words(path):
    text = open(path, encoding="utf-8").read()
    m = re.search(r"^#*\s*\**Calls made", text, flags=re.M | re.I)
    if m:
        rest = text[m.start():]
        r = re.search(r"^(#+\s*|\**)?Record\b|^.*Clears it:", rest, flags=re.M)
        text = text[:m.start()] + (rest[r.start():] if r else "")
    out = []
    drop = set()
    for line in text.splitlines():
        if line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            low = [c.lower() for c in cells]
            heads = ("source", "rows", "source and date", "rows (doi for [paper])", "source and rows",
                     "source and rows (doi for [paper])")
            if any(c in heads for c in low):
                drop = {i for i, c in enumerate(low) if c in heads}
            cells = [c for i, c in enumerate(cells) if i not in drop]
            out.append(" ".join(cells))
        else:
            drop = set() if not line.strip() else drop
            out.append(line)
    words = re.findall(r"[A-Za-z0-9][A-Za-z0-9.,'%()/-]*", "\n".join(out))
    return len(words)


def cmd_words(args):
    n = count_words(args.answer)
    print(f"{n} words")
    if n <= CAP:
        print("within the short-mode cap")
        return 0
    print("over the cap: cut context paragraphs, repeated row ids in prose, secondary rules, "
          "rows not tied to the question; never a gap, a stop, the company status line or the record line")
    return 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("rank")
    r.add_argument("--input", required=True)
    r.add_argument("--mcda")
    t = sub.add_parser("tornado")
    t.add_argument("--file", required=True)
    t.add_argument("--n", type=int)
    f = sub.add_parser("facts")
    f.add_argument("--profile", required=True)
    f.add_argument("--funding")
    w = sub.add_parser("words")
    w.add_argument("answer")
    a = ap.parse_args()
    return {"rank": cmd_rank, "tornado": cmd_tornado, "facts": cmd_facts, "words": cmd_words}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
