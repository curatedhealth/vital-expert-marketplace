#!/usr/bin/env python3
"""Session record and coverage from the person's own training log (task A2).

No connector call. The person's data stays local. Roles and pseudonymous ids only,
never names (references/governance.md).

Input CSV (header row required), one row per person in the role at the site:
  user_id, role, site, session_date, completed_task_once, trains_others
  session_date          YYYY-MM-DD of the session attended; blank if not attended
  completed_task_once   yes/no: the person did the task on the task card once, observed,
                        during or after the session (blank = not recorded)
  trains_others         yes/no: designated to train others (train-the-trainer, CS45)

What it reports per group (site, role, or both):
  in role, attended, completed the task once, attended but not completed,
  completion not recorded, not attended, designated trainers.
  Attendance is never counted as completion (old register rule; CS80 for devices:
  training that users actually get should match the training that was validated).

Usage:
  python3 session_coverage.py SESSIONS.csv [--by site|role|site,role] [--as-of YYYY-MM-DD]
"""
import argparse
import csv
from collections import defaultdict


def yes(v):
    return (v or "").strip().lower() in ("yes", "y", "true", "1")


def pct(n, dnm):
    return f"{n}/{dnm} ({100.0 * n / dnm:.0f}%)" if dnm else f"{n}/0"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sessions")
    ap.add_argument("--by", default="site,role")
    ap.add_argument("--as-of")
    a = ap.parse_args()
    by = [x.strip() for x in a.by.split(",") if x.strip()]

    groups = defaultdict(list)
    checks = []
    with open(a.sessions, newline="") as f:
        for i, r in enumerate(csv.DictReader(f), start=2):
            key = " / ".join((r.get(k) or "").strip() or f"[GAP] {k}" for k in by) if by else "all"
            att = bool((r.get("session_date") or "").strip())
            comp_raw = (r.get("completed_task_once") or "").strip().lower()
            if a.as_of and att and r["session_date"].strip() > a.as_of:
                checks.append(f"line {i}: session date after as-of date")
            if comp_raw in ("yes", "y", "true", "1") and not att:
                checks.append(f"line {i}: completion recorded without a session date (check whether trained elsewhere)")
            groups[key].append({"att": att, "comp": comp_raw, "trainer": yes(r.get("trains_others"))})

    print("Session coverage. Attendance is not completion. Rates show numerator/denominator.\n")
    hdr = f"{'Group':<28}{'In role':>8}{'Attended':>16}{'Completed once':>18}{'Attended, not completed':>26}{'Not recorded':>14}{'Not attended':>14}{'Trainers':>10}"
    print(hdr)
    tot = defaultdict(int)
    for g in sorted(groups):
        rows = groups[g]
        n = len(rows)
        att = sum(r["att"] for r in rows)
        comp = sum(1 for r in rows if r["comp"] in ("yes", "y", "true", "1"))
        att_not = sum(1 for r in rows if r["att"] and r["comp"] in ("no", "n", "false", "0"))
        unrec = sum(1 for r in rows if r["att"] and r["comp"] == "")
        not_att = n - att
        tr = sum(r["trainer"] for r in rows)
        for k, v in (("n", n), ("att", att), ("comp", comp), ("att_not", att_not), ("unrec", unrec), ("not_att", not_att), ("tr", tr)):
            tot[k] += v
        print(f"{g:<28}{n:>8}{pct(att, n):>16}{pct(comp, n):>18}{att_not:>26}{unrec:>14}{not_att:>14}{tr:>10}")
    print(f"{'All':<28}{tot['n']:>8}{pct(tot['att'], tot['n']):>16}{pct(tot['comp'], tot['n']):>18}{tot['att_not']:>26}{tot['unrec']:>14}{tot['not_att']:>14}{tot['tr']:>10}")
    if checks:
        print("\nData checks (confirm with the person):")
        for c in checks:
            print("  - " + c)


if __name__ == "__main__":
    main()
