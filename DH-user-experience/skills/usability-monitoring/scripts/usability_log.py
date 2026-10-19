#!/usr/bin/env python3
"""Summarize a usability test log by task and by the severity the person assigned.

Subcommands
  log FILE.csv [--min-per-group N] [--outcomes-ok success,...]
      Per task: participants, outcome counts (labels as the person coded them),
      use errors, participants who returned to the old step, severity as assigned.
      Per user group: participant count, against the person's own minimum if given.
      Flags: rows with no severity assigned, employees, think-aloud sessions.
  sus FILE.csv
      System Usability Scale per participant and per group, scored as restated by
      Hyzy et al. 2022 (UX-M-07): odd items minus 1, 5 minus even items, sum x 2.5.

Expected log columns: participant_id, user_group, task_id, task_name, critical,
severity, outcome, returned_to_old_step. Optional: employee, think_aloud, note.
The script never assigns a severity, a pass or a fail. It counts what is in the file.
"""
import csv
import statistics
import sys
from collections import Counter, OrderedDict, defaultdict

USE_ERROR = "use_error"


def yes(v):
    return str(v or "").strip().lower() in ("yes", "y", "true", "1")


def read(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def cmd_log(path, min_per_group=None, ok_labels=("success",)):
    rows = read(path)
    if not rows:
        print("No rows.")
        return 1
    tasks = OrderedDict()
    for r in rows:
        tasks.setdefault(r["task_id"], []).append(r)

    print(f"Log: {path} ({len(rows)} rows)")
    print("\nBy task (severity and critical flag as the person assigned them)")
    print("task | name | critical | participants | outcomes | use errors | returned to old step | severity assigned")
    for tid, rs in tasks.items():
        parts = {r["participant_id"] for r in rs}
        oc = Counter(r["outcome"].strip() for r in rs)
        ue = oc.get(USE_ERROR, 0)
        ret = sum(1 for r in rs if yes(r.get("returned_to_old_step")))
        crit = sorted({r.get("critical", "").strip() or "not stated" for r in rs})
        sev = Counter((r.get("severity") or "").strip() or "NOT ASSIGNED" for r in rs if r["outcome"].strip() not in ok_labels)
        oc_s = ", ".join(f"{k} {v}" for k, v in sorted(oc.items()))
        sev_s = ", ".join(f"{k} {v}" for k, v in sorted(sev.items())) or "no non-success rows"
        print(f"{tid} | {rs[0]['task_name']} | {'/'.join(crit)} | {len(parts)} | {oc_s} | {ue} of {len(rs)} | {ret} | {sev_s}")

    print("\nUse errors and other non-success rows by severity (as assigned)")
    by_sev = defaultdict(list)
    for r in rows:
        if r["outcome"].strip() in ok_labels:
            continue
        s = (r.get("severity") or "").strip() or "NOT ASSIGNED"
        by_sev[s].append(r)
    for s, rs in sorted(by_sev.items()):
        oc = Counter(r["outcome"].strip() for r in rs)
        print(f"{s}: {len(rs)} rows ({', '.join(f'{k} {v}' for k, v in sorted(oc.items()))})")
        for r in rs:
            note = (r.get("note") or "").strip()
            print(f"  {r['task_id']} {r['participant_id']} ({r['user_group']}): {r['outcome']}" + (f"; {note}" if note else ""))

    print("\nBy user group")
    groups = defaultdict(set)
    for r in rows:
        groups[r["user_group"]].add(r["participant_id"])
    for g, ps in sorted(groups.items()):
        line = f"{g}: {len(ps)} participants"
        if min_per_group is not None:
            line += f" (your minimum {min_per_group}: {'met' if len(ps) >= min_per_group else 'not met'})"
        print(line)

    flags = []
    unassigned = [r for r in rows if r["outcome"].strip() not in ok_labels and not (r.get("severity") or "").strip()]
    if unassigned:
        flags.append(f"{len(unassigned)} non-success row(s) have no severity assigned: " + ", ".join(f"{r['task_id']}/{r['participant_id']}" for r in unassigned))
    if rows and "employee" in rows[0]:
        emp = sorted({r["participant_id"] for r in rows if yes(r.get("employee"))})
        if emp:
            flags.append("employees among participants: " + ", ".join(emp))
    if rows and "think_aloud" in rows[0]:
        ta = sorted({r["participant_id"] for r in rows if yes(r.get("think_aloud"))})
        if ta:
            flags.append("think-aloud sessions: " + ", ".join(ta))
    print("\nFlags")
    print("\n".join(f"- {f}" for f in flags) if flags else "- none")
    return 0


def sus_score(answers):
    total = 0
    for i, a in enumerate(answers, start=1):
        a = int(a)
        if not 1 <= a <= 5:
            raise ValueError(f"answer {a} outside 1 to 5")
        total += (a - 1) if i % 2 == 1 else (5 - a)
    return total * 2.5


def cmd_sus(path):
    rows = read(path)
    items = [f"q{i}" for i in range(1, 11)]
    per = []
    for r in rows:
        try:
            s = sus_score([r[q] for q in items])
        except (KeyError, ValueError) as e:
            print(f"{r.get('participant_id')}: not scored ({e})")
            continue
        per.append((r["participant_id"], r.get("user_group", ""), s))
    print(f"SUS: {path} ({len(per)} scored)")
    for p, g, s in per:
        print(f"{p} ({g}): {s:g}")
    groups = defaultdict(list)
    for _, g, s in per:
        groups[g].append(s)
    groups["all"] = [s for _, _, s in per]
    print("\ngroup | n | mean | SD | min | max")
    for g, ss in groups.items():
        sd = statistics.stdev(ss) if len(ss) > 1 else float("nan")
        print(f"{g} | {len(ss)} | {statistics.mean(ss):.2f} | {sd:.2f} | {min(ss):g} | {max(ss):g}")
    return 0


def main(argv):
    if len(argv) < 3 or argv[1] not in ("log", "sus"):
        print(__doc__)
        return 2
    if argv[1] == "sus":
        return cmd_sus(argv[2])
    mpg = None
    ok = ("success",)
    if "--min-per-group" in argv:
        mpg = int(argv[argv.index("--min-per-group") + 1])
    if "--outcomes-ok" in argv:
        ok = tuple(x.strip() for x in argv[argv.index("--outcomes-ok") + 1].split(","))
    return cmd_log(argv[2], mpg, ok)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
