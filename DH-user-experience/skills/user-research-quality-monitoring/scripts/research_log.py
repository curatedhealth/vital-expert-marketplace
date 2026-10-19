#!/usr/bin/env python3
"""User research logs: SUS scoring, stops per session log, insight-to-decision trace.

Runs on the person's own files. Nothing is sent anywhere. The script counts and
computes; it never sets a threshold, a target, a severity or a verdict.

Subcommands

  sus FILE.csv [--by user_group|round|user_group,round]
      System Usability Scale per respondent and per group. Scoring as restated by
      Hyzy et al. 2022 (research row UX-M-07): odd items minus 1, 5 minus even
      items, sum times 2.5, range 0 to 100. Brooke's original text was not read.
      Columns: respondent_id, q1 ... q10 (each 1 to 5). Optional: user_group, round.
      A response with a missing or out-of-range item is excluded and counted; the
      handling of missing items is not in the sources, so nothing is imputed.

  stops FILE.csv [--plan "patient=8,clinician=5"] [--min-participants N]
                 [--study-type formative|validation]
      Session log, one row per participant per task.
      Columns: participant_id, user_group, task_id, outcome (completed, stopped,
      assisted, or the person's own labels). Optional: stop_id, quote, critical
      (yes/no, as the person flagged it), employee (yes/no), think_aloud (yes/no).
      Prints participants per user group (against the person's plan if given), each
      stop with the number of distinct participants who hit it, by user group, and
      their words. "Repeated" is applied only if the person gives --min-participants.
      Flags employees and think-aloud sessions; with --study-type validation it
      notes FDA's statements on both (UX-US-38, UX-US-40) for the regulatory owner.

  trace INSIGHTS.csv --as-of YYYY-MM-DD [--changes CHANGES.csv]
      Insight log columns: insight_id, raised_on (YYYY-MM-DD), decision (action,
      refusal, open or blank). Optional: study_id, stop_id, participants_hit,
      decided_on, decision_ref, owner, release, shipped_on.
      Changes columns: change_id, release, shipped_on. Optional: insight_id,
      description. Prints decision status, open insights with age as of the date,
      actions not yet shipped, time from raised to decided, and every shipped change
      with no insight behind it ("not traced to this research").

Identifiable data guard: every subcommand refuses a file whose header names an
identifier (name, email, phone, address, date of birth, record or insurance
numbers, postcode) or whose cells hold an email address or a long digit string.
Use pseudonymous codes such as P01.

Usage: python3 research_log.py SUBCOMMAND FILE [options]
"""
import argparse
import csv
import re
import statistics
import sys
from collections import OrderedDict, defaultdict
from datetime import date

ID_HEADERS = {
    "name", "first_name", "last_name", "full_name", "surname", "email", "e_mail",
    "phone", "telephone", "mobile", "address", "street", "dob", "date_of_birth",
    "birth_date", "mrn", "medical_record_number", "nhs_number", "ssn",
    "insurance_number", "member_id", "postcode", "zip", "zip_code", "ip_address",
}
EMAIL = re.compile(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}")
LONG_DIGITS = re.compile(r"\d[\d\s\-]{8,}\d")
ISO_DATE = re.compile(r"\d{4}-\d{2}-\d{2}")


def norm(h):
    return re.sub(r"[^a-z0-9]+", "_", (h or "").strip().lower()).strip("_")


def read(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        header = [norm(h) for h in (reader.fieldnames or [])]
        rows = [{norm(k): (v or "").strip() for k, v in r.items()} for r in reader]
    bad = [h for h in header if h in ID_HEADERS]
    if bad:
        sys.exit(f"Refused: {path} has identifying columns {bad}. Remove them and use pseudonymous codes (for example P01).")
    for i, r in enumerate(rows, start=2):
        for k, v in r.items():
            if ISO_DATE.fullmatch(v):
                continue
            if EMAIL.search(v) or LONG_DIGITS.search(v):
                sys.exit(f"Refused: {path} line {i}, column '{k}' looks like contact or record data. Remove it and rerun.")
    return header, rows


def yes(v):
    return str(v or "").strip().lower() in ("yes", "y", "true", "1")


def d(s):
    s = (s or "").strip()
    return date.fromisoformat(s) if s else None


def fmt(x):
    return f"{x:.1f}" if isinstance(x, float) else str(x)


# ---------------------------------------------------------------- sus
def sus_score(r):
    items = []
    for i in range(1, 11):
        v = r.get(f"q{i}", "")
        try:
            n = int(float(v))
        except ValueError:
            return None, f"q{i} missing or not a number"
        if n < 1 or n > 5 or float(v) != n:
            return None, f"q{i} out of range 1 to 5"
        items.append(n)
    total = sum((x - 1) if i % 2 == 0 else (5 - x) for i, x in enumerate(items))
    return total * 2.5, None


def cmd_sus(a):
    header, rows = read(a.file)
    missing = [f"q{i}" for i in range(1, 11) if f"q{i}" not in header]
    if "respondent_id" not in header or missing:
        sys.exit(f"Needs respondent_id and q1 to q10; missing {missing or ['respondent_id']}.")
    keys = [k.strip() for k in a.by.split(",")] if a.by else []
    for k in keys:
        if k not in header:
            sys.exit(f"--by column '{k}' not in the file.")
    scored, excluded = [], []
    for r in rows:
        s, why = sus_score(r)
        (excluded.append((r["respondent_id"], why)) if s is None else scored.append((r, s)))
    print(f"SUS file: {a.file}; responses {len(rows)}; scored {len(scored)}; excluded {len(excluded)}")
    print("Scoring: odd items minus 1, 5 minus even items, sum x 2.5 (Hyzy et al. 2022 restating Brooke; UX-M-07).")
    for rid, why in excluded:
        print(f"  excluded {rid}: {why} (no imputation; missing-item rule not sourced)")
    print("\nPer respondent")
    for r, s in scored:
        tag = " ".join(f"{k}={r.get(k, '')}" for k in keys)
        print(f"  {r['respondent_id']} {tag} SUS {s:g}")
    groups = OrderedDict()
    for r, s in scored:
        groups.setdefault(tuple(r.get(k, "") for k in keys), []).append(s)
    print("\nSummary" + (f" by {', '.join(keys)}" if keys else ""))
    print("  group | n | mean | median | SD | min | max")
    for g, ss in groups.items():
        sd = statistics.stdev(ss) if len(ss) > 1 else float("nan")
        label = " / ".join(g) if keys else "all"
        print(f"  {label} | {len(ss)} | {statistics.mean(ss):.1f} | {statistics.median(ss):g} | "
              f"{'n/a' if sd != sd else f'{sd:.1f}'} | {min(ss):g} | {max(ss):g}")
    if "round" in keys and len(keys) == 1 and len(groups) > 1:
        names = list(groups)
        print("\nDifference of means between consecutive rounds (descriptive only; no test run)")
        for a1, b1 in zip(names, names[1:]):
            print(f"  {a1[0]} to {b1[0]}: {statistics.mean(groups[b1]) - statistics.mean(groups[a1]):+.1f}")
    print("\nReport n beside every mean; respondents differ between rounds unless your file says otherwise.")
    print("\nNo pass mark is applied. Published means are context only, never targets (see references).")
    return 0


# ---------------------------------------------------------------- stops
def parse_plan(s):
    plan = OrderedDict()
    for part in (s or "").split(","):
        if part.strip():
            k, _, v = part.partition("=")
            plan[k.strip()] = int(v)
    return plan


def cmd_stops(a):
    header, rows = read(a.file)
    need = ["participant_id", "user_group", "task_id", "outcome"]
    miss = [c for c in need if c not in header]
    if miss:
        sys.exit(f"Needs columns {need}; missing {miss}.")
    by_group = defaultdict(set)
    for r in rows:
        by_group[r["user_group"]].add(r["participant_id"])
    plan = parse_plan(a.plan)
    print(f"Session log: {a.file}; rows {len(rows)}; participants {len({r['participant_id'] for r in rows})}")
    print("\nParticipants per user group" + (" (against your plan)" if plan else ""))
    for g in list(plan) + [g for g in by_group if g not in plan]:
        n = len(by_group.get(g, ()))
        p = plan.get(g)
        print(f"  {g}: {n}" + (f" of {p} planned{' (short by ' + str(p - n) + ')' if n < p else ''}" if p is not None else ""))

    tasks = OrderedDict()
    for r in rows:
        tasks.setdefault(r["task_id"], []).append(r)
    print("\nOutcomes by task (labels as you coded them)")
    for t, rs in tasks.items():
        oc = defaultdict(int)
        for r in rs:
            oc[r["outcome"] or "(blank)"] += 1
        crit = "critical (your flag)" if any(yes(r.get("critical")) for r in rs) else ""
        print(f"  {t} {crit}: " + ", ".join(f"{k} {v}" for k, v in oc.items()))

    stops = OrderedDict()
    for r in rows:
        sid = r.get("stop_id", "")
        if sid:
            stops.setdefault(sid, []).append(r)
    print("\nStops (distinct participants who hit each stop)")
    if not stops:
        print("  none coded (add stop_id per row where a participant stopped)")
    order = sorted(stops.items(), key=lambda kv: -len({r["participant_id"] for r in kv[1]}))
    for sid, rs in order:
        parts = {r["participant_id"] for r in rs}
        grp = defaultdict(set)
        for r in rs:
            grp[r["user_group"]].add(r["participant_id"])
        crit = any(yes(r.get("critical")) for r in rs)
        label = ""
        if a.min_participants is not None:
            label = " REPEATED (your rule)" if len(parts) >= a.min_participants else " below your rule"
        print(f"  {sid}: {len(parts)} participant{'s' if len(parts) != 1 else ''} ({', '.join(f'{g} {len(p)}' for g, p in grp.items())})"
              f"; tasks {sorted({r['task_id'] for r in rs})}{'; on a task you flagged critical' if crit else ''}{label}")
        for r in rs:
            if r.get("quote"):
                print(f"      {r['participant_id']} ({r['user_group']}): \"{r['quote']}\"")

    emp = sorted({r["participant_id"] for r in rows if yes(r.get("employee"))})
    ta = sorted({r["participant_id"] for r in rows if yes(r.get("think_aloud"))})
    print("\nFlags")
    print(f"  employee participants: {', '.join(emp) or 'none'}")
    print(f"  think-aloud sessions: {', '.join(ta) or 'none'}")
    if a.study_type == "validation" and (emp or ta):
        print("  For the regulatory owner: FDA says employees should not be HF validation participants except in rare "
              "cases (UX-US-38) and think-aloud is not acceptable in validation (UX-US-40).")
    elif emp:
        print("  Formative work may include employees, with caution about bias (UX-US-45).")
    if any(yes(r.get("critical")) for r in rows):
        print("  Stops on tasks you flagged critical go to the human factors or regulatory owner as recorded; "
              "the script does not judge use error or severity.")
    return 0


# ---------------------------------------------------------------- trace
def cmd_trace(a):
    header, ins = read(a.file)
    need = ["insight_id", "raised_on", "decision"]
    miss = [c for c in need if c not in header]
    if miss:
        sys.exit(f"Needs columns {need}; missing {miss}.")
    as_of = d(a.as_of)
    status = defaultdict(list)
    for r in ins:
        dec = (r["decision"] or "open").lower()
        status[dec if dec in ("action", "refusal", "open") else f"other: {dec}"].append(r)
    n = len(ins)
    print(f"Insight log: {a.file}; insights {n}; as of {as_of.isoformat()}")
    for k in ("action", "refusal", "open"):
        print(f"  {k}: {len(status.get(k, []))} of {n}")
    for k in [k for k in status if k.startswith("other")]:
        print(f"  {k}: {len(status[k])} (label not recognized; counted apart)")

    opened = status.get("open", [])
    if opened:
        print("\nOpen insights (no action or refusal written), oldest first")
        for r in sorted(opened, key=lambda r: r["raised_on"]):
            age = (as_of - d(r["raised_on"])).days
            print(f"  {r['insight_id']}: raised {r['raised_on']}, {age} days open; owner: "
                  f"{r.get('owner') or 'owner not named'}; participants hit {r.get('participants_hit') or 'not recorded'}")
    days = [(d(r["decided_on"]) - d(r["raised_on"])).days for r in ins
            if r.get("decided_on") and (r["decision"] or "").lower() in ("action", "refusal")]
    if days:
        print(f"\nDays from raised to decided (action or refusal): n {len(days)}, median {statistics.median(days):g}, "
              f"longest {max(days)}")
    refusals_no_reason = [r["insight_id"] for r in status.get("refusal", []) if not r.get("decision_ref")]
    if refusals_no_reason:
        print(f"Refusals with no reason or reference recorded: {', '.join(refusals_no_reason)}")
    no_owner = [r["insight_id"] for r in ins if not r.get("owner")]
    if no_owner:
        print(f"No owner recorded: {', '.join(no_owner)}")

    if a.changes:
        _, ch = read(a.changes)
        ids = {r["insight_id"] for r in ins}
        actions = {r["insight_id"]: r for r in status.get("action", [])}
        shipped_for = defaultdict(list)
        print(f"\nChanges: {a.changes}; {len(ch)} rows")
        untraced, unknown = [], []
        for c in ch:
            iid = c.get("insight_id", "")
            if not iid:
                untraced.append(c)
            elif iid not in ids:
                unknown.append(c)
            else:
                shipped_for[iid].append(c)
        print(f"  traced to an insight in the log: {sum(len(v) for v in shipped_for.values())}")
        print(f"  not traced to this research (no insight id): {len(untraced)}"
              + (f" ({', '.join(c['change_id'] for c in untraced)})" if untraced else ""))
        if unknown:
            print(f"  insight id not found in the log: {', '.join(c['change_id'] + ' -> ' + c['insight_id'] for c in unknown)}")
        not_shipped = [i for i in actions if not any(c.get("shipped_on") and d(c["shipped_on"]) <= as_of
                                                      for c in shipped_for.get(i, []))]
        print(f"  actions with no shipped change as of {as_of.isoformat()}: {len(not_shipped)} of {len(actions)}"
              + (f" ({', '.join(not_shipped)})" if not_shipped else ""))
        traced_to_open = [i for i in shipped_for if (actions.get(i) is None)]
        if traced_to_open:
            print(f"  changes cite insights not marked action (check the log): {', '.join(traced_to_open)}")
    print("\nNo threshold applied. How long an insight may stay open is your rule.")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("sus")
    s.add_argument("file")
    s.add_argument("--by", default="")
    s.set_defaults(fn=cmd_sus)
    s = sp.add_parser("stops")
    s.add_argument("file")
    s.add_argument("--plan", default="")
    s.add_argument("--min-participants", type=int)
    s.add_argument("--study-type", choices=["formative", "validation"], default="formative")
    s.set_defaults(fn=cmd_stops)
    s = sp.add_parser("trace")
    s.add_argument("file")
    s.add_argument("--as-of", required=True)
    s.add_argument("--changes")
    s.set_defaults(fn=cmd_trace)
    a = p.parse_args()
    sys.exit(a.fn(a))


if __name__ == "__main__":
    main()
