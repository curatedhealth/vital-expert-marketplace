#!/usr/bin/env python3
"""Tally a stakeholder reception log against the person's own measure.

Usage:
    python3 reception_log.py LOG.csv [--by line_id|claim_id|audience|use]
                             [--numerator CODE[,CODE...]] [--min-n N] [--flag-at SHARE]

LOG.csv columns (required): date, audience, organization, use, line_id,
claim_id, response_code. Optional: note.

The response codes, the measure and the flag rule are the person's:
  --numerator  the codes the person counts as a miss (for example
               "rejected,questioned"). Without it the script only counts
               responses per code and says the measure is not chosen.
  --min-n      the smallest number of responses the person accepts before
               a share is reported (default 1).
  --flag-at    the share at or above which the person wants a line flagged
               for review (no default: without it nothing is flagged).
"no_response" rows are counted but kept out of the denominator unless the
person lists "no_response" in --numerator. The script reports what the log
says; it does not judge the narrative or name an owner.
"""
import csv
import sys
from collections import Counter, defaultdict

REQUIRED = ["date", "audience", "organization", "use", "line_id", "claim_id", "response_code"]


def arg(argv, name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


def main(argv):
    if len(argv) < 2:
        raise SystemExit(__doc__)
    by = arg(argv, "--by", "line_id")
    num = arg(argv, "--numerator")
    numerator = {c.strip() for c in num.split(",")} if num else None
    min_n = int(arg(argv, "--min-n", "1"))
    flag_at = arg(argv, "--flag-at")
    flag_at = float(flag_at) if flag_at is not None else None

    with open(argv[1], newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise SystemExit("The log is empty.")
    missing = [c for c in REQUIRED if c not in rows[0]]
    if missing:
        raise SystemExit("Missing columns: " + ", ".join(missing))
    if by not in REQUIRED:
        raise SystemExit("--by must be one of line_id, claim_id, audience, use")
    blank = [i + 2 for i, r in enumerate(rows) if not r["response_code"].strip() or not r[by].strip()]
    if blank:
        raise SystemExit(f"Rows with an empty response_code or {by}: lines {blank}")

    groups = defaultdict(list)
    for r in rows:
        groups[r[by].strip()].append(r)
    codes = sorted({r["response_code"].strip() for r in rows})
    dates = sorted(r["date"] for r in rows)

    print(f"Log: {len(rows)} responses, {dates[0]} to {dates[-1]}, grouped by {by}.")
    print("Codes found: " + ", ".join(codes))
    if numerator is None:
        print("Measure not chosen by the person [GAP]: counts only, no share, no flag.")
    else:
        print("Person's measure: share of responses coded " + ", ".join(sorted(numerator))
              + " (no_response kept out of the denominator unless listed).")
    if flag_at is None and numerator is not None:
        print("Flag rule not set by the person [GAP]: shares shown, nothing flagged.")
    print()
    header = "| " + by + " | n | " + " | ".join(codes) + " | Share (person's measure) | Flag |"
    print(header)
    print("|" + "---|" * (len(codes) + 4))
    for key in sorted(groups):
        g = groups[key]
        cnt = Counter(r["response_code"].strip() for r in g)
        share_txt, flag = "n/a", ""
        if numerator is not None:
            denom = [r for r in g if r["response_code"].strip() != "no_response" or "no_response" in numerator]
            if len(denom) < min_n:
                share_txt = f"below min-n ({len(denom)} < {min_n})"
            else:
                hits = sum(1 for r in denom if r["response_code"].strip() in numerator)
                share = hits / len(denom) if denom else 0.0
                share_txt = f"{hits}/{len(denom)} = {share:.2f}"
                if flag_at is not None and share >= flag_at:
                    flag = f"flagged (at or above {flag_at:.2f})"
        print(f"| {key} | {len(g)} | " + " | ".join(str(cnt.get(c, 0)) for c in codes) + f" | {share_txt} | {flag} |")
    print()
    print("Notes per group (verbatim from the log):")
    for key in sorted(groups):
        notes = [f"{r['date']} {r['organization']}: {r.get('note', '').strip()}" for r in groups[key] if r.get("note", "").strip()]
        for n in notes:
            print(f"- {key}: {n}")


if __name__ == "__main__":
    main(sys.argv)
