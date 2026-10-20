#!/usr/bin/env python3
"""Helper for analytics-adoption-and-impact-monitoring (dh-technology).

Reads the person's own files and prints facts against the person's own rules.
It never sets a target, an adoption threshold, a pass rule, an owner, a recheck
date or a keep, change or stop call.

  funnel      python3 adoption_check.py funnel --roster ROSTER.csv --events EVENTS.csv
                  --since 2026-09-01 --as-of 2026-09-30 [--by role|site]
              Roster columns: person_id, role, site, in_scope (yes/no), invited_on,
              trained_on, practice_task_done (yes/no), practice_task_on,
              stopped_step, champion (yes/no).
              Events columns: person_id, date, event (view, task_completed, export,
              question). A "task_completed" event is the decision recorded in the
              product (the trained task done in production).
              Stages, each over the valid denominator of people in scope
              (RE-AIM, CS27, CS28): invited, trained (attended), practice task
              done (proof, not attendance), active in the window (any event),
              task completed in production in the window. Penetration is
              computed both ways Proctor gives (CS39): completers / in scope,
              and completers / trained.
  champions   python3 adoption_check.py champions --roster ROSTER.csv --events EVENTS.csv
                  --since ... --as-of ...
              Questions taken per champion in the window ("question" events
              logged against the champion's person_id); a champion with no
              record is "unmeasured", never "inactive".
  cadence     python3 adoption_check.py cadence --log ISSUES.csv
              Columns: report, period_end, due_on, sent_on, data_timestamp,
              refresh_finished_on, recipients, withheld_metrics, status
              (sent/missed), missed_reason, who_told, next_issue_on.
  outcome     python3 adoption_check.py outcome --file OUTCOME.csv [--bet-metric NAME]
              Columns: group (product or comparison), metric, window_start,
              window_end, n_users, n_units, outcome_count, comparison_type
              (before-after or concurrent).
  agreement   python3 adoption_check.py agreement --file CASES.csv
              Columns: case_id, user, shown_on, recommendation, action, agreed
              (yes/no), override_reason. User agreement and reasons for
              variation (DECIDE-AI item, DA-82).
  governance  python3 adoption_check.py governance --metrics REGISTER.csv
                  [--publishers PUBLISHERS.csv] --as-of 2026-10-20
                  [--review-every-days N]
              Metrics columns: metric_id, status, certified_on, certifier, owner,
              version_certified, version_current, formula_changed_on,
              dashboards, dashboards_show_status (yes/no).
              Publishers columns: user, role_at_grant, role_now, granted_on,
              last_reviewed_on.
  words       python3 adoption_check.py words ANSWER.md

Flags are facts, never verdicts:
  Funnel     A1 no one marked in scope (no valid denominator); A2 trained with no
             practice proof (attendance is not enablement); A3 event dated
             outside the window or after the read date (left out); A4 event for a
             person not on the roster (left out, counted); A5 export-only user
             (activity without the task in the product); A6 practice task not
             done, with the step stopped on
  Cadence    C1 no data timestamp; C2 sent before the source refresh finished;
             C3 same data timestamp as the previous issue; C4 sent after the
             due date; C5 missed with no reason; C6 missed with no one told;
             C7 missed with no next issue date
  Outcome    O1 no comparison group; O2 windows differ between groups; O3 number
             of users not given; O4 outcome is a page view or click count; O5
             metric differs from the bet metric
  Governance G1 certified with no owner; G2 formula changed after certification
             and still certified; G3 dashboards use a draft or changed metric
             without showing its status; G4 certified with no certifier or date;
             P1 role changed since grant and publish rights kept; P2 never
             reviewed; P3 last review older than your interval (only if given)
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
    return f"{x.day} {x.strftime('%B')} {x.year}" if x else "not given"


def rows(path):
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def g(r, k):
    return (r.get(k) or "").strip()


def yes(r, k):
    return g(r, k).lower() in ("yes", "y", "true", "1")


def pct(n, den):
    return f"{n}/{den} ({100 * n / den:.1f}%)" if den else f"{n}/0 (not computable)"


def load_events(path, since, as_of, roster_ids):
    kept, outside, unknown = [], 0, set()
    for e in rows(path):
        ed = d(e.get("date"))
        if ed is None or ed < since or ed > as_of:
            outside += 1
            continue
        if g(e, "person_id") not in roster_ids:
            unknown.add(g(e, "person_id"))
            continue
        kept.append(e)
    return kept, outside, unknown


def cmd_funnel(a):
    since, as_of = d(a.since), d(a.as_of)
    roster = rows(a.roster)
    ids = {g(r, "person_id") for r in roster}
    ev, outside, unknown = load_events(a.events, since, as_of, ids)
    by_person = {}
    for e in ev:
        by_person.setdefault(g(e, "person_id"), []).append(g(e, "event").lower())
    print(f"Window: {full(since)} to {full(as_of)} (yours). Denominator: people marked in scope on your roster "
          "(valid denominator, RE-AIM, re-aim.org, read 19 October 2026, CS27, CS28).")
    groups = {}
    for r in roster:
        key = g(r, a.by) or "not given" if a.by else "all in scope"
        groups.setdefault(key, []).append(r)
    flags = set()
    print("| Group | In scope | Invited | Trained (attended) | Practice task done | Active in window | "
          "Task completed in product (penetration 1: completers / in scope) | Penetration 2: completers / trained | Export only |")
    print("|---|---|---|---|---|---|---|---|---|")
    tot = {"scope": 0}
    for key in sorted(groups):
        rs = [r for r in groups[key] if yes(r, "in_scope")]
        n = len(rs)
        inv = sum(1 for r in rs if d(r.get("invited_on")))
        tr = [r for r in rs if d(r.get("trained_on"))]
        pr = sum(1 for r in rs if yes(r, "practice_task_done"))
        act = sum(1 for r in rs if by_person.get(g(r, "person_id")))
        comp = [r for r in rs if "task_completed" in by_person.get(g(r, "person_id"), [])]
        comp_tr = sum(1 for r in comp if d(r.get("trained_on")))
        exp_only = sum(1 for r in rs if by_person.get(g(r, "person_id"))
                       and "task_completed" not in by_person[g(r, "person_id")]
                       and "export" in by_person[g(r, "person_id")])
        if any(d(r.get("trained_on")) and not yes(r, "practice_task_done") for r in rs):
            flags.add("A2")
        if exp_only:
            flags.add("A5")
        tot["scope"] += n
        print(f"| {key} | {n} | {pct(inv, n)} | {pct(len(tr), n)} | {pct(pr, n)} | {pct(act, n)} | "
              f"{pct(len(comp), n)} | {pct(comp_tr, len(tr))} | {exp_only} |")
    if tot["scope"] == 0:
        flags.add("A1")
    if outside:
        flags.add("A3")
    if unknown:
        flags.add("A4")
    stopped = [(g(r, "person_id"), g(r, "stopped_step")) for r in roster
               if yes(r, "in_scope") and d(r.get("trained_on")) and not yes(r, "practice_task_done")]
    if stopped:
        flags.add("A6")
        print("\nTrained but practice task not done (step stopped on, from your roster): "
              + "; ".join(f"{p}: {s or 'step not given'}" for p, s in stopped) + ".")
    print(f"\nEvents left out: {outside} outside the window or after the read date; "
          f"{len(unknown)} person ids not on the roster ({', '.join(sorted(unknown)) or 'none'}).")
    print("Flags: " + (", ".join(sorted(flags)) or "none") + ".")
    print("Attendance is not enablement: 'trained' counts sessions attended; 'practice task done' is the proof "
          "your curriculum names. Whether these figures meet your adoption rule is yours; no source sets one.")
    return 0


def cmd_champions(a):
    since, as_of = d(a.since), d(a.as_of)
    roster = rows(a.roster)
    ids = {g(r, "person_id") for r in roster}
    ev, _, _ = load_events(a.events, since, as_of, ids)
    q = {}
    for e in ev:
        if g(e, "event").lower() == "question":
            q[g(e, "person_id")] = q.get(g(e, "person_id"), 0) + 1
    champs = [r for r in roster if yes(r, "champion")]
    print(f"Window: {full(since)} to {full(as_of)} (yours).")
    print("| Champion | Role | Site | Questions logged in window |")
    print("|---|---|---|---|")
    for r in champs:
        n = q.get(g(r, "person_id"))
        print(f"| {g(r, 'person_id')} | {g(r, 'role')} | {g(r, 'site')} | {n if n else 'unmeasured (no record)'} |")
    sites = {g(r, "site") for r in roster if yes(r, "in_scope")}
    without = sorted(s for s in sites if s not in {g(r, 'site') for r in champs})
    print("\nSites in scope with no champion on the roster: " + (", ".join(without) or "none") + ".")
    print("A named champion with no record is unmeasured, not inactive.")
    return 0


def cmd_cadence(a):
    log = rows(a.log)
    print("| Report | Period end | Due | Sent | Data timestamp | Status | Flags |")
    print("|---|---|---|---|---|---|---|")
    prev = {}
    counts = {}
    for r in sorted(log, key=lambda x: (g(x, "report"), g(x, "period_end"))):
        fl = []
        rep = g(r, "report")
        ts, sent, due = d(r.get("data_timestamp")), d(r.get("sent_on")), d(r.get("due_on"))
        ref = d(r.get("refresh_finished_on"))
        status = g(r, "status").lower() or "not given"
        if status == "sent":
            if not ts:
                fl.append("C1")
            if ref and sent and sent < ref:
                fl.append("C2")
            if ts and prev.get(rep) and ts == prev[rep]:
                fl.append("C3")
            if sent and due and sent > due:
                fl.append("C4")
            if ts:
                prev[rep] = ts
        elif status == "missed":
            if not g(r, "missed_reason"):
                fl.append("C5")
            if not g(r, "who_told"):
                fl.append("C6")
            if not d(r.get("next_issue_on")):
                fl.append("C7")
        for f in fl:
            counts[f] = counts.get(f, 0) + 1
        print(f"| {rep} | {full(d(r.get('period_end')))} | {full(due)} | {full(sent) if sent else 'not sent'} | "
              f"{full(ts)} | {status} | {', '.join(fl) or 'none'} |")
    print("\nFlag counts: " + (", ".join(f"{k} {v}" for k, v in sorted(counts.items())) or "none") + ".")
    print("Facts from your issue log; whether a late or missed issue breaks your cadence rule is yours.")
    return 0


def num(s):
    try:
        return float(str(s).replace(",", ""))
    except (ValueError, TypeError):
        return None


def cmd_outcome(a):
    data = rows(a.file)
    fl = set()
    groups = {g(r, "group").lower(): r for r in data}
    print("| Group | Metric | Window | Users | Units | Outcome count | Rate per unit |")
    print("|---|---|---|---|---|---|---|")
    rates = {}
    for r in data:
        nu, oc = num(r.get("n_units")), num(r.get("outcome_count"))
        rate = oc / nu if nu and oc is not None else None
        rates[g(r, "group").lower()] = rate
        if not g(r, "n_users"):
            fl.add("O3")
        if re.search(r"view|click|open|visit", g(r, "metric"), re.I):
            fl.add("O4")
        if a.bet_metric and g(r, "metric").lower() != a.bet_metric.lower():
            fl.add("O5")
        print(f"| {g(r, 'group')} | {g(r, 'metric')} | {full(d(r.get('window_start')))} to {full(d(r.get('window_end')))} | "
              f"{g(r, 'n_users') or 'not given'} | {g(r, 'n_units') or 'not given'} | {g(r, 'outcome_count') or 'not given'} | "
              + (f"{rate:.4f}" if rate is not None else "not computable") + " |")
    comp = [k for k in groups if k != "product"]
    if "product" not in groups or not comp:
        fl.add("O1")
    else:
        p, c = groups["product"], groups[comp[0]]
        ctype = g(p, "comparison_type") or g(c, "comparison_type") or "not given"
        if ctype != "before-after" and (g(p, "window_start"), g(p, "window_end")) != (g(c, "window_start"), g(c, "window_end")):
            fl.add("O2")
        if rates.get("product") is not None and rates.get(comp[0]) is not None:
            diff = rates["product"] - rates[comp[0]]
            print(f"\nDifference in rate (product minus {comp[0]}): {diff:+.4f}; comparison type: {ctype}. "
                  "A difference is arithmetic on your file, not evidence that the product caused it.")
    print("Flags: " + (", ".join(sorted(fl)) or "none") + ".")
    print("A missing metric is a gap, never a zero; a metric never instrumented is not a product failure "
          "(Proctor 2011, CS32, DOI 10.1007/s10488-010-0319-7).")
    return 0


def cmd_agreement(a):
    data = rows(a.file)
    n = len(data)
    agreed = sum(1 for r in data if yes(r, "agreed"))
    over = [r for r in data if g(r, "agreed").lower() in ("no", "n", "false", "0")]
    blank = n - agreed - len(over)
    with_reason = sum(1 for r in over if g(r, "override_reason"))
    print(f"Cases: {n}. Agreed with the recommendation: {pct(agreed, n)}. "
          f"Varied from it: {pct(len(over), n)}. Agreement not recorded: {blank}.")
    print(f"Variations with a reason recorded: {pct(with_reason, len(over))}.")
    reasons = {}
    for r in over:
        k = g(r, "override_reason") or "reason not recorded"
        reasons[k] = reasons.get(k, 0) + 1
    print("| Reason for variation (as recorded) | Cases |")
    print("|---|---|")
    for k, v in sorted(reasons.items(), key=lambda x: -x[1]):
        print(f"| {k} | {v} |")
    print("DECIDE-AI asks for user agreement and reasons for variation (Vasey 2022, DA-82, "
          "DOI 10.1136/bmj-2022-070904). High agreement is not accuracy and low agreement is not error: "
          "neither says whether the recommendation or the user was right.")
    return 0


def cmd_governance(a):
    as_of = d(a.as_of)
    print(f"Read date: {full(as_of)}.")
    print("| Metric | Status | Certified | Version certified, current | Formula changed | Dashboards | Flags |")
    print("|---|---|---|---|---|---|---|")
    for r in rows(a.metrics):
        fl = []
        st = g(r, "status").lower()
        cd, ch = d(r.get("certified_on")), d(r.get("formula_changed_on"))
        changed = (ch and cd and ch > cd) or (g(r, "version_current") and g(r, "version_certified")
                                              and g(r, "version_current") != g(r, "version_certified"))
        if st == "certified":
            if not g(r, "owner"):
                fl.append("G1")
            if changed:
                fl.append("G2")
            if not g(r, "certifier") or not cd:
                fl.append("G4")
        if (st != "certified" or changed) and g(r, "dashboards") and not yes(r, "dashboards_show_status"):
            fl.append("G3")
        print(f"| {g(r, 'metric_id')} | {st or 'not given'} | {full(cd)} | {g(r, 'version_certified') or 'not given'}, "
              f"{g(r, 'version_current') or 'not given'} | {full(ch)} | {g(r, 'dashboards') or 'none listed'} | "
              f"{', '.join(fl) or 'none'} |")
    if a.publishers:
        print("\n| Publisher | Role at grant | Role now | Granted | Last reviewed | Flags |")
        print("|---|---|---|---|---|---|")
        for r in rows(a.publishers):
            fl = []
            if g(r, "role_now") and g(r, "role_now") != g(r, "role_at_grant"):
                fl.append("P1")
            lr = d(r.get("last_reviewed_on"))
            if not lr:
                fl.append("P2")
            elif a.review_every_days and as_of and (as_of - lr).days > a.review_every_days:
                fl.append("P3")
            print(f"| {g(r, 'user')} | {g(r, 'role_at_grant')} | {g(r, 'role_now') or 'not given'} | "
                  f"{full(d(r.get('granted_on')))} | {full(lr)} | {', '.join(fl) or 'none'} |")
        if not a.review_every_days:
            print("Review interval: not given (P3 not checked).")
    print("\nWhether a metric is decertified, and whether a right is removed, is the owner's decision; "
          "the flags are facts from your register.")
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
          "rows not tied to the question; never a gap, a stop or the record line")
    return 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("funnel")
    for k in ("--roster", "--events", "--since", "--as-of"):
        f.add_argument(k, required=True)
    f.add_argument("--by")
    c = sub.add_parser("champions")
    for k in ("--roster", "--events", "--since", "--as-of"):
        c.add_argument(k, required=True)
    k = sub.add_parser("cadence")
    k.add_argument("--log", required=True)
    o = sub.add_parser("outcome")
    o.add_argument("--file", required=True)
    o.add_argument("--bet-metric")
    ag = sub.add_parser("agreement")
    ag.add_argument("--file", required=True)
    gv = sub.add_parser("governance")
    gv.add_argument("--metrics", required=True)
    gv.add_argument("--publishers")
    gv.add_argument("--as-of", required=True)
    gv.add_argument("--review-every-days", type=int)
    w = sub.add_parser("words")
    w.add_argument("answer")
    a = ap.parse_args()
    return {"funnel": cmd_funnel, "champions": cmd_champions, "cadence": cmd_cadence, "outcome": cmd_outcome,
            "agreement": cmd_agreement, "governance": cmd_governance, "words": cmd_words}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
