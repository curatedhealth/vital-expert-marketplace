#!/usr/bin/env python3
"""Summarize an accessibility issue log against the WCAG version and level the person targets.

Usage:
  python3 a11y_issue_log.py LOG.csv --version 2.2 --level AA --as-of 2026-10-19 [--json]

LOG.csv columns (header names, case-insensitive; extra columns are ignored):
  id, screen, task, day_one (yes/no), criterion (for example 1.4.3), level (as the person
  recorded it), severity (the person's own label), status (open, closed, or the person's
  own words), opened (YYYY-MM-DD), closed (YYYY-MM-DD or empty), found_by (automated,
  manual, assistive_tech, user_research, or the person's words)

The script never assigns severity, never decides a pass, and never says the product conforms.
It reports the person's log against the criteria table in references/data/wcag_criteria.csv,
which was extracted from the W3C WCAG 2.1 and 2.2 Recommendations (see
references/wcag-criteria-additions.md, rows WX1 to WX6).
"""
import argparse
import csv
import json
import os
import statistics
import sys
from collections import Counter, defaultdict
from datetime import date

LEVEL_RANK = {"A": 1, "AA": 2, "AAA": 3}
CLOSED_WORDS = {"closed", "fixed", "resolved", "done", "verified"}


def load_criteria(path):
    crit = {}
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            crit[r["sc"]] = r
    return crit


def parse_date(s):
    s = (s or "").strip()
    if not s:
        return None
    try:
        return date.fromisoformat(s)
    except ValueError:
        return "bad"


def norm(row):
    return {k.strip().lower(): (v or "").strip() for k, v in row.items() if k}


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser()
    ap.add_argument("log")
    ap.add_argument("--version", required=True, choices=["2.0", "2.1", "2.2"])
    ap.add_argument("--level", required=True, choices=["A", "AA", "AAA"])
    ap.add_argument("--as-of", required=True, help="YYYY-MM-DD; ages count to this date")
    ap.add_argument("--criteria", default=os.path.join(here, "..", "references", "data", "wcag_criteria.csv"))
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    as_of = date.fromisoformat(a.as_of)
    crit = load_criteria(a.criteria)
    vcol = "level_" + a.version.replace(".", "_")
    target_rank = LEVEL_RANK[a.level]
    in_target_set = {sc for sc, r in crit.items() if r[vcol] and LEVEL_RANK[r[vcol]] <= target_rank}

    with open(a.log, newline="", encoding="utf-8-sig") as f:
        rows = [norm(r) for r in csv.DictReader(f)]

    issues, data_problems = [], []
    for r in rows:
        iid = r.get("id") or "(no id)"
        sc = r.get("criterion", "")
        c = crit.get(sc)
        st = r.get("status", "").lower()
        is_closed = st in CLOSED_WORDS
        opened, closed = parse_date(r.get("opened")), parse_date(r.get("closed"))
        rec = {
            "id": iid, "screen": r.get("screen", ""), "task": r.get("task", ""),
            "day_one": r.get("day_one", "").lower() in {"yes", "y", "true", "1"},
            "criterion": sc, "logged_level": r.get("level", "").upper(),
            "severity": r.get("severity", "") or "(none given)", "status": r.get("status", ""),
            "closed": is_closed, "found_by": r.get("found_by", "") or "(not recorded)",
        }
        if c is None:
            rec["scope"] = "criterion not in WCAG 2.0, 2.1 or 2.2 table"
            data_problems.append(f"{iid}: criterion '{sc}' not found in the WCAG table")
        elif not c[vcol]:
            if sc == "4.1.1":
                rec["scope"] = f"not in WCAG {a.version} (4.1.1 Parsing removed in 2.2; test and report only if a 2.0 or 2.1 policy applies)"
            else:
                first = "2.1" if c["level_2_1"] else "2.2"
                rec["scope"] = f"not in WCAG {a.version} (first appears in WCAG {first})"
        elif LEVEL_RANK[c[vcol]] > target_rank:
            rec["scope"] = f"above target (Level {c[vcol]} in WCAG {a.version}; target {a.level})"
        else:
            rec["scope"] = "in target"
        rec["w3c_level"] = c[vcol] if c else ""
        rec["name"] = c["name"] if c else ""
        if c and c[vcol] and rec["logged_level"] and rec["logged_level"] != c[vcol]:
            data_problems.append(f"{iid}: logged level {rec['logged_level']} but W3C level for {sc} in WCAG {a.version} is {c[vcol]}")
        if opened in (None, "bad"):
            data_problems.append(f"{iid}: opened date missing or not YYYY-MM-DD")
            rec["age_days"] = None
        else:
            end = closed if (is_closed and isinstance(closed, date)) else as_of
            rec["age_days"] = (end - opened).days
            if opened > as_of:
                data_problems.append(f"{iid}: opened after the as-of date")
        if is_closed and closed in (None, "bad"):
            data_problems.append(f"{iid}: status '{r.get('status', '').strip()}' counted as closed but no valid closed date; whether it is closed is the person's call")
        if isinstance(closed, date) and isinstance(opened, date) and closed < opened:
            data_problems.append(f"{iid}: closed before opened")
        if not is_closed and isinstance(closed, date):
            data_problems.append(f"{iid}: closed date given but status is '{rec['status']}'")
        issues.append(rec)

    open_in = [i for i in issues if not i["closed"] and i["scope"] == "in target"]
    ages = [i["age_days"] for i in open_in if i["age_days"] is not None]
    sev_age = defaultdict(list)
    for i in open_in:
        if i["age_days"] is not None:
            sev_age[i["severity"]].append(i["age_days"])

    out = {
        "target": f"WCAG {a.version} Level {a.level}",
        "as_of": a.as_of,
        "criteria_in_target": len(in_target_set),
        "issues_total": len(issues),
        "status_counts": dict(Counter(i["status"] or "(blank)" for i in issues)),
        "scope_counts": dict(Counter(i["scope"] for i in issues)),
        "open_in_target": len(open_in),
        "open_in_target_day_one": sum(1 for i in open_in if i["day_one"]),
        "open_in_target_by_severity_as_logged": dict(Counter(i["severity"] for i in open_in)),
        "open_in_target_by_level": dict(Counter(i["w3c_level"] for i in open_in)),
        "open_in_target_by_screen": dict(Counter(i["screen"] for i in open_in)),
        "open_age_days": {
            "n": len(ages),
            "median": statistics.median(ages) if ages else None,
            "oldest": max(ages) if ages else None,
            "by_severity_as_logged": {k: {"n": len(v), "median": statistics.median(v), "oldest": max(v)} for k, v in sev_age.items()},
        },
        "criteria_with_open_in_target_issues": sorted({i["criterion"] for i in open_in}, key=lambda s: tuple(int(x) for x in s.split("."))),
        "criteria_in_target_with_no_issue_logged": len(in_target_set - {i["criterion"] for i in issues}),
        "found_by_counts": dict(Counter(i["found_by"] for i in issues)),
        "open_in_target_list": sorted(open_in, key=lambda i: (not i["day_one"], -(i["age_days"] or 0))),
        "out_of_target_list": [i for i in issues if i["scope"] != "in target"],
        "data_problems": data_problems,
        "notes": [
            "Severity is the person's label, counted as logged; the script does not judge it.",
            "A criterion with no issue logged is not a pass: the log records issues found, not tests run.",
            "Automated tests check only part of what needs testing (references UX-UK-24, UX-US-78); counts by found_by show how the log was built.",
            "No conformance statement: WCAG conformance is for full pages and complete processes (UX-STD-21, UX-STD-22) and needs a test record, not an issue log.",
        ],
    }

    if a.json:
        json.dump(out, sys.stdout, indent=2, default=str)
        print()
        return

    p = print
    p(f"# Issue log summary: target {out['target']}, as of {a.as_of}")
    p(f"Criteria in target: {out['criteria_in_target']}. Issues in log: {out['issues_total']}.")
    p(f"Open and in target: {out['open_in_target']} ({out['open_in_target_day_one']} on day-one tasks).")
    oa = out["open_age_days"]
    if oa["n"]:
        p(f"Open in-target age (days to {a.as_of}): median {oa['median']}, oldest {oa['oldest']}.")
    p("\n## Status (as logged)")
    for k, v in out["status_counts"].items():
        p(f"- {k}: {v}")
    p("\n## Scope against the target")
    for k, v in out["scope_counts"].items():
        p(f"- {k}: {v}")
    p("\n## Open in target by severity (the person's labels)")
    for k, v in oa["by_severity_as_logged"].items():
        p(f"- {k}: {v['n']} open, median age {v['median']} days, oldest {v['oldest']}")
    p("\n## Open in target by W3C level")
    for k, v in sorted(out["open_in_target_by_level"].items(), key=lambda kv: LEVEL_RANK.get(kv[0], 9)):
        p(f"- Level {k}: {v}")
    p("\n## Open in-target issues (day-one first, then oldest)")
    p("| id | screen | task | day one | criterion | W3C level | severity (logged) | age days | found by |")
    p("|---|---|---|---|---|---|---|---|---|")
    for i in out["open_in_target_list"]:
        p(f"| {i['id']} | {i['screen']} | {i['task']} | {'yes' if i['day_one'] else 'no'} | {i['criterion']} {i['name']} | {i['w3c_level']} | {i['severity']} | {i['age_days']} | {i['found_by']} |")
    if out["out_of_target_list"]:
        p("\n## Outside the target (kept, not counted above)")
        for i in out["out_of_target_list"]:
            p(f"- {i['id']} {i['criterion']} {i['name']}: {i['scope']}; status {i['status']}")
    p("\n## How the log was built (found_by)")
    for k, v in out["found_by_counts"].items():
        p(f"- {k}: {v}")
    p(f"\nCriteria in target with no issue logged: {out['criteria_in_target_with_no_issue_logged']} (not passes; not tested unless a test record says so).")
    if data_problems:
        p("\n## Data problems in the log")
        for d in data_problems:
            p(f"- {d}")
    p("\n## Notes")
    for n in out["notes"]:
        p(f"- {n}")


if __name__ == "__main__":
    main()
