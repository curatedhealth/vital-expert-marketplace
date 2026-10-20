#!/usr/bin/env python3
"""Two checks on a review: search currency against a named rule, and the AMSTAR 2 overall rating.

Usage:
  python3 review_check.py currency --last-search YYYY-MM-DD --target YYYY-MM-DD [--rule cochrane|jca|all]
                                   [--new-studies FILE.csv]
  python3 review_check.py amstar2 RATINGS.csv [--critical 2,4,7,9,11,13,15]

currency
  --last-search  date the last search was run (the person's or the review's own statement)
  --target       planned publication date (Cochrane) or dossier submission date (EU JCA)
  Rules, quoted in references/currency-rules.md:
    cochrane  MECIR C37: searches rerun within 12 months, preferably six, before publication (ES-52)
    jca       search cut-off at most 3 months before dossier submission, medicines and devices (ES-152, ES-156)
  --new-studies  optional CSV with columns id,date_or_year,design: candidate studies the person or the
                 library found; rows dated after the last search are listed as new-study signals (ES-103).
  A date check is not a judgment that a review is out of date: the question, its quality and new
  evidence decide that (ES-103), and the person decides.

amstar2
  RATINGS.csv has columns item (1 to 16) and rating (Yes, Partial yes, No, Not applicable),
  as the person's appraisers rated them. The critical items default to the seven AMSTAR 2 names
  (2, 4, 7, 9, 11, 13, 15; ES-106); the appraisers may change the list (ES-109).
  Overall confidence follows Shea et al. 2017 (ES-105 [PAPER] doi 10.1136/bmj.j4008, ES-107): High, Moderate, Low, Critically low.
  A "No" on a critical item is a critical flaw; a "No" on a non-critical item is a non-critical weakness.
  How a "Partial yes" counts is the appraisers' call; the script lists them and does not count them.
  Item ratings are never summed into a score (ES-108).
"""
import csv
import sys
from datetime import date


def parse_date(s):
    s = s.strip()
    if len(s) == 4:
        return date(int(s), 12, 31), "year only"
    if len(s) == 7:
        y, m = s.split("-")
        return date(int(y), int(m), 28), "month only"
    y, m, d = s.split("-")
    return date(int(y), int(m), int(d)), "full"


def minus_months(d, n):
    y, m = d.year, d.month - n
    while m <= 0:
        m += 12
        y -= 1
    day = min(d.day, [31, 29 if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1])
    return date(y, m, day)


def fmt(d):
    return f"{d.day} {d.strftime('%B')} {d.year}"


def currency(args):
    def arg(name, default=None):
        return args[args.index(name) + 1] if name in args else default
    last, _ = parse_date(arg("--last-search"))
    target, _ = parse_date(arg("--target"))
    rule = (arg("--rule", "all") or "all").lower()
    days = (target - last).days
    print(f"Last search {fmt(last)}; target date {fmt(target)}; {days} days apart.")
    if days < 0:
        print("  The last search is after the target date; check the dates.")
    if rule in ("cochrane", "all"):
        limit12, limit6 = minus_months(target, 12), minus_months(target, 6)
        ok12, ok6 = last >= limit12, last >= limit6
        print(f"Cochrane MECIR C37 (ES-52): last search must be on or after {fmt(limit12)} (12 months), preferably on or after {fmt(limit6)} (six months).")
        print(f"  12 months: {'within' if ok12 else 'OUTSIDE'}; six months: {'within' if ok6 else 'outside'}.")
    if rule in ("jca", "all"):
        limit3 = minus_months(target, 3)
        ok3 = last >= limit3
        print(f"EU JCA cut-off (ES-152, ES-156): last search must be on or after {fmt(limit3)} (at most 3 months before submission).")
        print(f"  {'within' if ok3 else 'OUTSIDE'}; for submission on {fmt(target)}, a search run on or after {fmt(limit3)} meets the cut-off.")
    path = arg("--new-studies")
    if path:
        newer, unclear = [], []
        with open(path, newline="", encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                r = {k.strip().lower(): (v or "").strip() for k, v in r.items()}
                d, precision = parse_date(r.get("date_or_year", "")) if r.get("date_or_year") else (None, None)
                if d is None:
                    unclear.append(r)
                elif precision == "year only" and d.year == last.year:
                    unclear.append(r)
                elif d > last:
                    newer.append(r)
        print(f"\nCandidate new studies after the last search: {len(newer)}")
        for r in newer:
            print(f"  - {r.get('id')} ({r.get('date_or_year')}, {r.get('design') or 'design not given'})")
        if unclear:
            print(f"Dates too coarse to place against the last search: {len(unclear)}")
            for r in unclear:
                print(f"  - {r.get('id')} ({r.get('date_or_year') or 'no date'})")
        print("These are signals for the update decision, not included studies: each needs screening (ES-103).")
    return 0


def amstar2(args):
    path = args[0]
    crit = [2, 4, 7, 9, 11, 13, 15]
    if "--critical" in args:
        crit = [int(x) for x in args[args.index("--critical") + 1].split(",") if x.strip()]
    ratings = {}
    with open(path, newline="", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            r = {k.strip().lower(): (v or "").strip() for k, v in r.items()}
            ratings[int(r["item"])] = r.get("rating", "").lower()
    missing = [i for i in range(1, 17) if i not in ratings or not ratings[i]]
    flaws = [i for i in crit if ratings.get(i) == "no"]
    weak = [i for i in range(1, 17) if i not in crit and ratings.get(i) == "no"]
    partial = [i for i in range(1, 17) if ratings.get(i) == "partial yes"]
    print(f"Critical items used: {crit}{' (default AMSTAR 2 list, ES-106)' if crit == [2, 4, 7, 9, 11, 13, 15] else ' (appraisers changed the list, ES-109)'}")
    print(f"Critical flaws (No on a critical item): {flaws or 'none'}")
    print(f"Non-critical weaknesses (No on another item): {weak or 'none'}")
    print(f"Partial yes (appraisers decide how these count): {partial or 'none'}")
    if missing:
        print(f"Items not rated: {missing} [GAP]; the overall rating below assumes they are not flaws.")
    if len(flaws) > 1:
        overall = "Critically low: more than one critical flaw; the review should not be relied on (ES-107)"
    elif len(flaws) == 1:
        overall = "Low: one critical flaw (ES-107)"
    elif len(weak) > 1:
        overall = "Moderate: more than one non-critical weakness (ES-107)"
    else:
        overall = "High: no or one non-critical weakness (ES-107)"
    print(f"Overall confidence by the AMSTAR 2 rule (Shea et al. 2017, ES-105 [PAPER] doi 10.1136/bmj.j4008): {overall}")
    print("No total score is computed (ES-108). The ratings and the final call are the appraisers'.")
    return 0


def main(argv):
    if len(argv) < 2 or argv[1] not in ("currency", "amstar2"):
        print(__doc__)
        return 2
    return currency(argv[2:]) if argv[1] == "currency" else amstar2(argv[2:])


if __name__ == "__main__":
    sys.exit(main(sys.argv))
