#!/usr/bin/env python3
"""Helpers for investment-portfolio-monitoring. Standard library only.

deltas HOLDINGS.csv DELTAS.json [DELTAS.json ...] --as-of YYYY-MM-DD
    Read the person's holdings list and one or more saved diligence-dh.get_deltas
    outputs. HOLDINGS.csv columns (one row per holding):
      holding, library_reference, since, owner, reread_date
    library_reference is the name exactly as sent to get_deltas; since is the date
    the person asked from (YYYY-MM-DD). Prints, per holding: what the library
    recorded, the window the answer actually covers (the log's first entry and last
    sweep), and flags:
      W1 the requested window starts before the change log began: events between
         since and the log start may be missing
      W2 the holding was not in any deltas file read (not read)
      W3 owner not named
      W4 reread date not given
      W5 reread date on or before the as-of date
      W6 the deltas call used a different since date from the holding's row
    It does not judge a change, score a holding, or say anything about value.

diff EARLIER.json LATER.json
    Compare two saved diligence-dh.compare_portfolio outputs (raw response or the
    examples/live wrapper) company by company and field by field. Companies present
    in only one file are listed as not comparable. Values are printed as returned.

words ANSWER.md
    Count the words of a drafted answer, without the calls list (from the "Calls
    made" line on) and table columns headed Source or Retrieved. Short mode limit
    450; prints the cut order if over.

Company status (exists, bankrupt, delisted, deregistered, acquired) is never in the
change log: deltas prints the status step from references/company-status.md for
every holding. A W1 window is never reported as "no change" for the span before
the log began.
"""
import csv
import json
import sys
from datetime import date


def d(s):
    try:
        y, m, dd = (int(x) for x in str(s).strip()[:10].split("-"))
        return date(y, m, dd)
    except Exception:
        return None


def long(dt):
    return f"{dt.day} {dt.strftime('%B')} {dt.year}" if dt else "not given"


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def deltas_blocks(path):
    raw = load(path)
    call = raw.get("call", {})
    args = call.get("args") or call.get("arguments") or {}
    body = raw.get("response", raw)
    return {"file": path, "since": args.get("since"), "companies": body.get("companies", []),
            "log": body.get("log", {}), "retrieved": raw.get("retrieved") or raw.get("_note", "")}


def deltas(holdings_path, files, as_of):
    blocks = [deltas_blocks(f) for f in files]
    asof = d(as_of)
    with open(holdings_path, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    print(f"As of {long(asof)}. Holdings read: {len(rows)}. Deltas files read: {len(blocks)}.")
    print()
    print("| Holding | Library reference | Window asked | Library answer | Covered by the log | Owner | Reread date | Flags |")
    print("|---|---|---|---|---|---|---|---|")
    counts = {}
    for r in rows:
        ref = (r.get("library_reference") or "").strip()
        since = d(r.get("since"))
        hit, blk = None, None
        for b in blocks:
            for c in b["companies"]:
                if c.get("company", "").strip().lower() == ref.lower():
                    same = since and d(b.get("since")) == since
                    if hit is None or same:
                        hit, blk = c, b
        flags = []
        if hit is None:
            answer, cover = "not read", "-"
            flags.append("W2")
        else:
            n = hit.get("change_count")
            answer = hit.get("changes") if n == 0 else f"{n} changes recorded"
            first = d(blk["log"].get("first_entry_at"))
            sweep = d(blk["log"].get("last_sweep_at"))
            cover = f"log from {long(first)}, last sweep {long(sweep)}"
            if since and first and since < first:
                flags.append("W1")
            if blk.get("since") and since and d(blk["since"]) != since:
                flags.append("W6")
        owner = (r.get("owner") or "").strip()
        if not owner:
            flags.append("W3")
            owner = "owner not named"
        rr = d(r.get("reread_date"))
        if rr is None:
            flags.append("W4")
        elif asof and rr <= asof:
            flags.append("W5")
        for f in flags:
            counts[f] = counts.get(f, 0) + 1
        print(f"| {r.get('holding')} | {ref} | from {long(since)} | {answer} | {cover} | {owner} | {long(rr)} | {', '.join(flags) or '-'} |")
    print()
    print("Flag counts: " + (", ".join(f"{k} {v}" for k, v in sorted(counts.items())) or "none"))
    for b in blocks:
        lim = b["log"].get("limits", [])
        if lim:
            print(f"\nLimits as returned ({b['file']}):")
            for x in lim:
                print(f"- {x}")
    print("\n'No change recorded' is a statement about the library's event-dated log rows in the window up to the last sweep, not that nothing happened.")
    if counts.get("W1"):
        firsts = sorted({long(d(b["log"].get("first_entry_at"))) for b in blocks if b["log"].get("first_entry_at")})
        print(f"W1: the change log began on {', '.join(firsts)}. For each W1 holding say so first, never report 'no change' for the span before it, "
              "and offer the holding's dated primary filings and authorization records for that span instead "
              "(saved get_funding_signals output in references/tools.md, the EDGAR filing list per CIK, FDA and DiGA records).")
    print("Status (references/company-status.md): the change log does not show whether a holding exists, is in bankruptcy, was delisted, deregistered or acquired. "
          "For each holding: status [GAP]: not read, unless its 8-K Items 1.03, 2.01, 3.01, 5.01, Form 25, Form 15 or its register were opened. "
          "A Form 15 or 25 is not dissolution (DL-144, DL-149).")


def compare_rows(path):
    raw = load(path)
    calls = raw["calls"] if "calls" in raw else [raw.get("response", raw)]
    out = {}
    for c in calls:
        for r in c.get("companies", []):
            key = (r.get("company") or r.get("query") or "").strip()
            out[key] = (r, c.get("retrieved_at", "date not in file"))
    return out


def flat(prefix, v, acc):
    if isinstance(v, dict):
        for k, x in v.items():
            flat(f"{prefix}.{k}" if prefix else k, x, acc)
    elif isinstance(v, list):
        acc[prefix] = "; ".join(json.dumps(x) if not isinstance(x, str) else x for x in v)
    else:
        acc[prefix] = v
    return acc


def diff(a, b):
    A, B = compare_rows(a), compare_rows(b)
    print("| Company | Field | Earlier | Later |")
    print("|---|---|---|---|")
    changed = 0
    for k in sorted(set(A) & set(B)):
        fa, fb = flat("", A[k][0], {}), flat("", B[k][0], {})
        for f in sorted(set(fa) | set(fb)):
            va, vb = fa.get(f, "field absent"), fb.get(f, "field absent")
            if va != vb:
                changed += 1
                print(f"| {k} | {f} | {va} | {vb} |")
    print()
    for k in sorted(set(A) ^ set(B)):
        side = "earlier only" if k in A else "later only"
        print(f"Not comparable: {k} ({side}).")
    same = sorted(set(A) & set(B))
    print(f"Companies in both runs: {len(same)}. Field changes: {changed}.")
    for k in same:
        print(f"- {k}: earlier retrieved {A[k][1]}, later retrieved {B[k][1]}")
    print("A changed field is a change in the library's record or rubric between runs, not a judgment of the company. Check the rubric version before reading a score change.")


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
    args = sys.argv[1:]
    if args[:1] == ["deltas"] and "--as-of" in args:
        i = args.index("--as-of")
        as_of = args[i + 1]
        rest = args[1:i] + args[i + 2:]
        if len(rest) >= 2:
            deltas(rest[0], rest[1:], as_of)
            sys.exit(0)
    if args[:1] == ["words"] and len(args) == 2:
        words(args[1])
        sys.exit(0)
    if args[:1] == ["diff"] and len(args) == 3:
        diff(args[1], args[2])
        sys.exit(0)
    print(__doc__)
    sys.exit(2)
