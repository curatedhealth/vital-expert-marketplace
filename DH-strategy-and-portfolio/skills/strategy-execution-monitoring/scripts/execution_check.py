#!/usr/bin/env python3
"""Helper for strategy-execution-monitoring (dh-strategy-and-portfolio).

Reads the person's own benefits register, milestone log and experiment log
(CSV) and prints facts against the person's own rules. It never sets a target,
a pass rule, an owner, a reread date or a kill-or-continue call.

  benefits     python3 execution_check.py benefits --register REG.csv --as-of 2026-10-20
               Columns: id, benefit, objective, owner, measure, direction (up|down),
               baseline, baseline_date, target, target_date, actual, actual_date,
               pass_rule (the person's, as a share of the planned change, e.g. ">=0.5"),
               reread_date, source.
               Share of planned change = (actual - baseline) / (target - baseline).
  milestones   python3 execution_check.py milestones --log LOG.csv --as-of 2026-10-20
               Columns: id, milestone, objective, owner, due, completed_on, evidence,
               depends_on, pass_rule_elements (the person's; any of owner, evidence,
               on_time, separated by ";"), recheck_date.
  experiments  python3 execution_check.py experiments --log LOG.csv
               Columns: id, option, question, prespecified_endpoint, success_criterion,
               decision_rule, rule_written_on, started_on, sample_planned,
               sample_actual, result, status.
  words        python3 execution_check.py words ANSWER.md
               Leaves out the "Calls made" block (up to the record block, which is
               counted) and the Source and Rows columns.

Flags are facts, never verdicts:
  Benefits    E1 owner not named; E2 baseline not given; E3 target not given;
              E4 no actual measured; E5 reread date earlier than the read date;
              E6 pass rule not given; E7 actual dated after the read date or before
              the baseline date (the reading does not belong to this period)
  Milestones  M1 owner not named; M2 no evidence of completion (completed or past due); M3 completed after due;
              M4 due date passed, not completed; M5 completed before a dependency;
              M6 recheck date not given for a failed element
  Experiments X1 no prespecified endpoint (SP-115); X2 success criterion or decision
              rule not given; X3 decision rule written after the start; X4 sample below
              plan; X5 result not reported; X6 question not given
"""
import argparse
import csv
import re
import sys
from datetime import date

CAP = 450


def d(s):
    s = (s or "").strip()
    if not s:
        return None
    try:
        return date.fromisoformat(s[:10])
    except ValueError:
        return None


def full(x):
    if x is None:
        return "not given"
    return f"{x.day} {x.strftime('%B')} {x.year}"


def num(s):
    s = (s or "").strip().replace(",", "")
    if not s:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def rows(path):
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def rule_met(rule, value):
    rule = (rule or "").strip()
    m = re.fullmatch(r"(>=|<=|>|<)\s*(-?[0-9.]+)", rule)
    if not m or value is None:
        return None
    op, n = m.group(1), float(m.group(2))
    return {">=": value >= n, "<=": value <= n, ">": value > n, "<": value < n}[op]


def cmd_benefits(a):
    as_of = d(a.as_of)
    print(f"Read date: {full(as_of)}. Share of planned change = (actual - baseline) / (target - baseline).")
    print("| Id | Benefit | Owner | Baseline | Target | Actual (date) | Share of planned change | Your rule | Rule met | Reread | Flags |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    counts = {"met": 0, "not met": 0, "not measurable": 0}
    for r in rows(a.register):
        fl = []
        owner = (r.get("owner") or "").strip()
        if not owner:
            fl.append("E1")
        b, t, act = num(r.get("baseline")), num(r.get("target")), num(r.get("actual"))
        if b is None:
            fl.append("E2")
        if t is None:
            fl.append("E3")
        if act is None:
            fl.append("E4")
        rr = d(r.get("reread_date"))
        if rr and as_of and rr < as_of:
            fl.append("E5")
        if not (r.get("pass_rule") or "").strip():
            fl.append("E6")
        ad = d(r.get("actual_date"))
        bd = d(r.get("baseline_date"))
        if ad and ((as_of and ad > as_of) or (bd and ad < bd)):
            fl.append("E7")
        share = None
        if None not in (b, t, act) and t != b:
            share = (act - b) / (t - b)
        met = rule_met(r.get("pass_rule"), share)
        if met is None:
            counts["not measurable"] += 1
            met_s = "not measurable"
        elif met:
            counts["met"] += 1
            met_s = "met"
        else:
            counts["not met"] += 1
            met_s = "not met"
        share_s = f"{share:.2f}" if share is not None else "n/a"
        act_s = f"{r.get('actual')} ({full(ad)})" if act is not None else "not measured"
        print(f"| {r['id']} | {r['benefit']} | {owner or 'owner not named'} | "
              f"{r.get('baseline') or 'not given'} | {r.get('target') or 'not given'} | {act_s} | "
              f"{share_s} | {r.get('pass_rule') or 'not given'} | {met_s} | {full(rr)} | "
              f"{', '.join(fl) or 'none'} |")
    print(f"\nCounts against your rules: met {counts['met']}, not met {counts['not met']}, "
          f"not measurable {counts['not measurable']}.")
    print("A share of planned change is arithmetic on your numbers; whether a benefit is on track, "
          "and what follows, is yours.")
    return 0


def cmd_milestones(a):
    as_of = d(a.as_of)
    log = rows(a.log)
    by_id = {r["id"]: r for r in log}
    print(f"Read date: {full(as_of)}. Elements checked are only those in your pass rule.")
    print("| Id | Milestone | Owner | Due | Completed | Elements failed | Recheck | Flags |")
    print("|---|---|---|---|---|---|---|---|")
    failed_total = 0
    failed_units = []
    for r in log:
        fl, failed = [], []
        elements = [e.strip() for e in (r.get("pass_rule_elements") or "").split(";") if e.strip()]
        owner = (r.get("owner") or "").strip()
        due, done = d(r.get("due")), d(r.get("completed_on"))
        assess = bool(done) or bool(due and as_of and due < as_of)
        if not owner:
            fl.append("M1")
        if assess and not (r.get("evidence") or "").strip():
            fl.append("M2")
        if done and due and done > due:
            fl.append("M3")
        if not done and due and as_of and due < as_of:
            fl.append("M4")
        for dep in [x.strip() for x in (r.get("depends_on") or "").split(";") if x.strip()]:
            dd = d(by_id.get(dep, {}).get("completed_on"))
            if done and (dd is None or dd > done):
                fl.append(f"M5 ({dep})")
        if not assess:
            elements_note = "not yet due"
        else:
            elements_note = None
        if assess and "owner" in elements and not owner:
            failed.append("owner")
        if assess and "evidence" in elements and not (r.get("evidence") or "").strip():
            failed.append("evidence")
        if "on_time" in elements and (("M3" in fl) or ("M4" in fl)):
            failed.append("on_time")
        rc = d(r.get("recheck_date"))
        if failed and rc is None:
            fl.append("M6")
        if not elements:
            failed_s = "pass rule not given"
        elif elements_note:
            failed_s = elements_note
        else:
            failed_s = ", ".join(failed) or "none"
        failed_total += len(failed)
        if failed:
            failed_units.append(r)
        print(f"| {r['id']} | {r['milestone']} | {owner or 'owner not named'} | {full(due)} | "
              f"{full(done) if done else 'not completed'} | {failed_s} | {full(rc)} | {', '.join(fl) or 'none'} |")
    print(f"\nFailed elements: {failed_total}. Each goes to the owner you name, with a recheck date "
          "you set or 'stopped' if you stop the unit; the model assigns neither.")
    if failed_units:
        print("Objective served and milestones that depend on each milestone with a failed element "
              "(from your objective and depends_on columns; facts, not verdicts):")
        for r in failed_units:
            dependents = [x["id"] for x in log
                          if r["id"] in [y.strip() for y in (x.get("depends_on") or "").split(";")]]
            print(f"- {r['id']} serves {(r.get('objective') or '').strip() or 'objective not given'}; "
                  f"depended on by: {', '.join(dependents) or 'none in the log'}.")
    return 0


def cmd_experiments(a):
    print("| Id | Option | Endpoint | Rule | Sample (planned, actual) | Result | Status | Flags |")
    print("|---|---|---|---|---|---|---|---|")
    inconclusive = []
    for r in rows(a.log):
        fl = []
        if not (r.get("question") or "").strip():
            fl.append("X6")
        if not (r.get("prespecified_endpoint") or "").strip():
            fl.append("X1")
        if not (r.get("success_criterion") or "").strip() or not (r.get("decision_rule") or "").strip():
            fl.append("X2")
        w, s = d(r.get("rule_written_on")), d(r.get("started_on"))
        if w and s and w > s:
            fl.append("X3")
        sp, sa = num(r.get("sample_planned")), num(r.get("sample_actual"))
        if sp is not None and sa is not None and sa < sp:
            fl.append("X4")
        res = (r.get("result") or "").strip()
        if not res or res.lower() == "not reported":
            fl.append("X5")
        if {"X1", "X2", "X3", "X5", "X6"} & set(fl):
            inconclusive.append(r["id"])
        rule = r.get("decision_rule") or "not given"
        print(f"| {r['id']} | {r.get('option')} | {r.get('prespecified_endpoint') or 'not given'} | {rule} | "
              f"{r.get('sample_planned') or 'not given'}, {r.get('sample_actual') or 'not given'} | "
              f"{res or 'not reported'} | {r.get('status') or 'not given'} | {', '.join(fl) or 'none'} |")
    print("\nCannot be read against a rule written before the start (X1, X2, X3, X5 or X6): "
          + (", ".join(inconclusive) or "none") + ".")
    print("Whether a test taught something usable, and whether the option continues, is the person's call.")
    return 0


def count_words(path):
    text = open(path, encoding="utf-8").read()
    m = re.search(r"^#*\s*\**Calls made", text, flags=re.M | re.I)
    if m:
        rest = text[m.start():]
        r = re.search(r"^(#+\s*|\**)?Record\b|^.*Clears it:", rest, flags=re.M)
        text = text[:m.start()] + (rest[r.start():] if r else "")
    out, drop = [], set()
    names = ("source", "rows", "source and date", "source and rows", "source and rows (doi for [paper])")
    for line in text.splitlines():
        if line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            low = [c.lower() for c in cells]
            if any(c in names for c in low):
                drop = {i for i, c in enumerate(low) if c in names}
            out.append(" ".join(c for i, c in enumerate(cells) if i not in drop))
        else:
            if not line.strip():
                drop = set()
            out.append(line)
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9.,'%()/-]*", "\n".join(out)))


def cmd_words(a):
    n = count_words(a.answer)
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
    b = sub.add_parser("benefits")
    b.add_argument("--register", required=True)
    b.add_argument("--as-of", required=True)
    m = sub.add_parser("milestones")
    m.add_argument("--log", required=True)
    m.add_argument("--as-of", required=True)
    x = sub.add_parser("experiments")
    x.add_argument("--log", required=True)
    w = sub.add_parser("words")
    w.add_argument("answer")
    a = ap.parse_args()
    return {"benefits": cmd_benefits, "milestones": cmd_milestones,
            "experiments": cmd_experiments, "words": cmd_words}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
