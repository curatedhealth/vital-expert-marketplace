#!/usr/bin/env python3
"""Adoption and penetration over time from the person's own usage file.

No connector call. The person's data stays local. Every rate is printed with its
numerator and denominator. No threshold is applied unless the person passes one.

Inputs (CSV, header row required):
  roster:  user_id, role, site, eligible, trained_date
           eligible = yes/no (the person's own eligibility list: users expected to do the task)
           trained_date = YYYY-MM-DD, blank if not trained
  usage:   user_id, date, kind
           kind = task      (the trained task done in production, per the person's task card)
                  old_step  (the old step or workaround the person wants to stop)
  Use pseudonymous ids and roles, never names (references/governance.md).

Definitions (references/adoption-metrics.md; rows in references/customer-success-research.md):
  Adoption (staff or user level)  adopted / trained: trained users with at least one task
                                  event on or after their training date, up to period end
                                  (Proctor adoption as action, CS34; RE-AIM percent of
                                  staff invited that participate, CS28, with trained as the
                                  invited denominator; say which one you report).
  Penetration                     active in period / eligible, and active / trained
                                  (Proctor's second calculation, CS39: providers who deliver
                                  divided by providers trained in or expected to deliver).
  Window adoption (optional)      trained users with a task event within W days of training /
                                  trained users whose window has fully elapsed. W is the
                                  person's (--window). Users whose window has not elapsed
                                  are counted separately, never as misses.
  After-training activity         for adopters, share with a task event in month k after
                                  training (descriptive only; CS78 states that training
                                  knowledge decays, this table does not measure knowledge).
  Maintenance (optional)          adopters trained at least M months before as-of who still
                                  had a task event in the last 30 days before as-of. M is the
                                  person's (--maintenance-months); RE-AIM uses 6 or more
                                  months at individual level (CS26) for outcomes, not usage.

Usage:
  python3 adoption_over_time.py ROSTER.csv USAGE.csv --as-of 2026-10-19
        [--period month|week] [--by site|role|site,role]
        [--window DAYS] [--rule-share 0.70] [--maintenance-months 6] [--json OUT.json]

--rule-share applies only with --window and only if the person set that share.
"""
import argparse
import csv
import json
import sys
from collections import defaultdict
from datetime import date, timedelta


def d(s):
    s = (s or "").strip()
    if not s:
        return None
    y, m, dd = s.split("-")
    return date(int(y), int(m), int(dd))


def month_start(x):
    return date(x.year, x.month, 1)


def next_month(x):
    return date(x.year + (x.month // 12), x.month % 12 + 1, 1)


def periods(start, end, kind):
    out = []
    if kind == "week":
        cur = start - timedelta(days=start.weekday())
        while cur <= end:
            out.append((cur, min(cur + timedelta(days=6), end)))
            cur += timedelta(days=7)
    else:
        cur = month_start(start)
        while cur <= end:
            out.append((cur, min(next_month(cur) - timedelta(days=1), end)))
            cur = next_month(cur)
    return out


def months_between(a, b):
    return (b.year - a.year) * 12 + (b.month - a.month) - (1 if b.day < a.day else 0)


def rate(n, dnm):
    return f"{n}/{dnm} ({100.0 * n / dnm:.0f}%)" if dnm else f"{n}/0 (no denominator)"


def load(roster_path, usage_path):
    roster, problems = {}, []
    with open(roster_path, newline="") as f:
        for i, r in enumerate(csv.DictReader(f), start=2):
            uid = r["user_id"].strip()
            if uid in roster:
                problems.append(f"roster line {i}: duplicate user_id {uid}")
            roster[uid] = {
                "role": r.get("role", "").strip() or "[GAP] role",
                "site": r.get("site", "").strip() or "[GAP] site",
                "eligible": r.get("eligible", "").strip().lower() in ("yes", "y", "true", "1"),
                "trained": d(r.get("trained_date")),
            }
    usage = defaultdict(lambda: {"task": [], "old_step": []})
    with open(usage_path, newline="") as f:
        for i, r in enumerate(csv.DictReader(f), start=2):
            uid = r["user_id"].strip()
            kind = r.get("kind", "").strip()
            when = d(r.get("date"))
            if uid not in roster:
                problems.append(f"usage line {i}: user_id {uid} not in roster (excluded)")
                continue
            if kind not in ("task", "old_step") or when is None:
                problems.append(f"usage line {i}: kind or date not readable (excluded)")
                continue
            usage[uid][kind].append(when)
    for uid, ev in usage.items():
        t = roster[uid]["trained"]
        if roster[uid]["trained"] is None and ev["task"]:
            problems.append(f"user {uid}: task events but no training date (counted as active, not as adopted)")
        if t and ev["task"] and min(ev["task"]) < t:
            problems.append(f"user {uid}: task events before training date (pre-training events not counted for adoption)")
    return roster, usage, problems


def group_key(u, by):
    if not by:
        return "all"
    return " / ".join(u[k] for k in by)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roster")
    ap.add_argument("usage")
    ap.add_argument("--as-of", required=True)
    ap.add_argument("--period", choices=["month", "week"], default="month")
    ap.add_argument("--by", default="")
    ap.add_argument("--window", type=int)
    ap.add_argument("--rule-share", type=float)
    ap.add_argument("--maintenance-months", type=int)
    ap.add_argument("--json")
    a = ap.parse_args()
    as_of = d(a.as_of)
    by = [x.strip() for x in a.by.split(",") if x.strip()]
    if a.rule_share is not None and a.window is None:
        sys.exit("--rule-share needs --window: a share without a window is not a rule.")

    roster, usage, problems = load(a.roster, a.usage)
    trained_dates = [u["trained"] for u in roster.values() if u["trained"]]
    task_dates = [x for ev in usage.values() for x in ev["task"]]
    if not trained_dates and not task_dates:
        sys.exit("No training dates and no task events: nothing to compute.")
    start = min(trained_dates + task_dates)
    result = {"as_of": a.as_of, "period": a.period, "by": by or ["all"], "groups": {}, "data_checks": problems}

    groups = defaultdict(list)
    for uid, u in roster.items():
        groups[group_key(u, by)].append(uid)

    print(f"Adoption and penetration over time, as of {a.as_of} (period: {a.period}).")
    print("Every rate shows numerator/denominator. No verdict unless the person set a rule.\n")
    for g in sorted(groups):
        uids = groups[g]
        rows = []
        for p0, p1 in periods(start, as_of, a.period):
            elig = [x for x in uids if roster[x]["eligible"]]
            trained = [x for x in uids if roster[x]["trained"] and roster[x]["trained"] <= p1]
            adopted = [x for x in trained if any(roster[x]["trained"] <= t <= p1 for t in usage[x]["task"])]
            active = [x for x in uids if any(p0 <= t <= p1 for t in usage[x]["task"])]
            active_elig = [x for x in active if roster[x]["eligible"]]
            active_tr = [x for x in active if x in trained]
            old = [x for x in uids if any(p0 <= t <= p1 for t in usage[x]["old_step"])]
            old_and_task = [x for x in old if x in active]
            rows.append({
                "period": f"{p0.isoformat()} to {p1.isoformat()}",
                "eligible": len(elig), "trained": len(trained), "adopted": len(adopted),
                "active": len(active), "active_eligible": len(active_elig), "active_trained": len(active_tr),
                "old_step_users": len(old),
                "old_step_and_task": len(old_and_task),
            })
        gr = {"periods": rows}
        print(f"== {g}")
        print(f"{'Period':<26}{'Eligible':>9}{'Trained':>9}{'Adoption (adopted/trained)':>30}"
              f"{'Penetration (active/eligible)':>32}  {'Active/trained':>22}{'Old step users':>16}{'Old step, also task':>21}")
        for r in rows:
            print(f"{r['period']:<26}{r['eligible']:>9}{r['trained']:>9}{rate(r['adopted'], r['trained']):>30}"
                  f"{rate(r['active_eligible'], r['eligible']):>32}  {rate(r['active_trained'], r['trained']):>22}"
                  f"{r['old_step_users']:>16}{r['old_step_and_task']:>21}")

        trained_all = [x for x in uids if roster[x]["trained"]]
        if a.window is not None:
            elapsed = [x for x in trained_all if roster[x]["trained"] + timedelta(days=a.window) <= as_of]
            pending = [x for x in trained_all if x not in elapsed]
            hit = [x for x in elapsed if any(roster[x]["trained"] <= t <= roster[x]["trained"] + timedelta(days=a.window)
                                             for t in usage[x]["task"])]
            line = f"Window adoption ({a.window} days, the person's window): {rate(len(hit), len(elapsed))}; window not yet elapsed: {len(pending)}"
            w = {"window_days": a.window, "hit": len(hit), "elapsed": len(elapsed), "not_elapsed": len(pending)}
            if a.rule_share is not None:
                if not elapsed:
                    verdict = "no verdict (no user has completed the window)"
                else:
                    verdict = "met" if len(hit) / len(elapsed) >= a.rule_share else "missed"
                line += f"; the person's rule {a.rule_share:.0%}: {verdict}"
                w["rule_share"] = a.rule_share
                w["verdict"] = verdict
            print(line)
            gr["window"] = w

        adopters = [x for x in trained_all if any(t >= roster[x]["trained"] for t in usage[x]["task"])]
        if adopters:
            maxk = max(months_between(roster[x]["trained"], as_of) for x in adopters)
            decay = []
            for k in range(0, maxk + 1):
                base = [x for x in adopters if months_between(roster[x]["trained"], as_of) >= k + 1]
                act = [x for x in base if any(months_between(roster[x]["trained"], t) == k and t >= roster[x]["trained"]
                                              for t in usage[x]["task"])]
                decay.append({"month_after_training": k, "active": len(act), "adopters_observed": len(base)})
            print("After-training activity (adopters with a task event in month k after training; only full months observed):")
            print("  " + "; ".join(f"m{r['month_after_training']}: {rate(r['active'], r['adopters_observed'])}"
                                   for r in decay if r["adopters_observed"]))
            gr["after_training_activity"] = decay

        if a.maintenance_months is not None:
            cutoff = as_of - timedelta(days=30)
            base = [x for x in adopters if months_between(roster[x]["trained"], as_of) >= a.maintenance_months]
            still = [x for x in base if any(cutoff < t <= as_of for t in usage[x]["task"])]
            print(f"Maintenance (adopters trained {a.maintenance_months}+ months ago with a task event in the last 30 days): "
                  f"{rate(len(still), len(base))}")
            gr["maintenance"] = {"months": a.maintenance_months, "still_active": len(still), "base": len(base)}

        not_trained_elig = [x for x in uids if roster[x]["eligible"] and not roster[x]["trained"]]
        print(f"Eligible but not trained: {len(not_trained_elig)}\n")
        gr["eligible_not_trained"] = len(not_trained_elig)
        result["groups"][g] = gr

    if problems:
        print("Data checks (fix or confirm with the person):")
        for p in problems:
            print("  - " + p)
    if a.json:
        with open(a.json, "w") as f:
            json.dump(result, f, indent=1)


if __name__ == "__main__":
    main()
