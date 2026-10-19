#!/usr/bin/env python3
"""Engagement KPIs and attrition curves from the person's own event file.

Nothing is sent anywhere. No subcommand sets a target, a threshold or a definition of
"engaged": every rule (which event counts, the period, the denominator, how many days
without use mean "stopped") comes from the person and is passed as an argument.

Input files
  events.csv    one row per event. Columns: user_id, event_date (YYYY-MM-DD), event_type.
                Extra columns are allowed (for example site, segment) and can be used
                with --group.
  eligible.csv  optional. One row per person eligible for the program (column user_id,
                optional group column). This is the valid denominator for reach
                (RE-AIM: "based on valid denominator (not of volunteers who indicate
                interest)", research row CS27).
  kpis.json     the KPI cards: {"kpis": [ {card}, ... ]}. A card:
                  id, name, decision, grain, source, missing_data_rule  (text)
                  period: {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"}
                  numerator: {"event": "session", "min_count": 1,
                              "within_days_of_start": null}
                  denominator: {"population": "eligible" | "enrolled" |
                                "enrolled_in_period" | "enrolled_before_period",
                                "start_event": "enrolled",
                                "min_days_observed": 56}
                min_days_observed keeps only people enrolled at least that many days
                before the period end, so everyone in the denominator had the full
                window to reach the numerator (a valid denominator).
                The same card format is read by kpi_definition_check.py
                (kpi-reliability-monitoring skill).

Subcommands
  kpis       Computes each card: numerator count, denominator count, value, and
             people who meet the numerator but sit outside the denominator.
             python3 engagement_kpis.py kpis events.csv --defs kpis.json
                     [--eligible eligible.csv | --eligible-count N]
  attrition  Nonusage attrition curve (Kaplan-Meier, as Eysenbach suggests, rows PE-101
             to PE-103 and KX1 to KX3), raw attrition proportions with a valid
             denominator per time point, usage half-life t50 and the t25 and t10 points,
             and optional dropout attrition for follow-up waves.
             python3 engagement_kpis.py attrition events.csv --start-event enrolled
                     --use-event session --inactive-days 14 --as-of 2026-10-19
                     [--interval-days 7] [--horizon-days 84] [--group site]
                     [--followup "followup_w4:28,followup_w12:84"] [--csv-out curve.csv]
             "Stopped" means: last use event more than --inactive-days before --as-of.
             People still inside that window are censored at --as-of. --inactive-days
             has no default because it is the person's definition.
             --interval-days only sets the display points.

Usage: python3 engagement_kpis.py SUBCOMMAND FILE [options]
"""
import argparse
import csv
import json
import sys
from collections import defaultdict
from datetime import date


def parse_date(s):
    s = (s or "").strip()
    if not s:
        return None
    try:
        return date.fromisoformat(s)
    except ValueError:
        return None


def read_events(path, group_col=None):
    """Return (events, problems). events: list of (user, date, type, group)."""
    events, problems = [], defaultdict(int)
    with open(path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        cols = [c.strip() for c in (reader.fieldnames or [])]
        for need in ("user_id", "event_date", "event_type"):
            if need not in cols:
                sys.exit(f"events file lacks column '{need}' (has: {', '.join(cols)})")
        if group_col and group_col not in cols:
            sys.exit(f"events file lacks group column '{group_col}'")
        for raw in reader:
            r = {k.strip(): (v or "").strip() for k, v in raw.items() if k}
            if not r.get("user_id"):
                problems["blank user_id"] += 1
                continue
            if not r.get("event_type"):
                problems["blank event_type"] += 1
                continue
            d = parse_date(r.get("event_date"))
            if d is None:
                problems["blank or invalid event_date"] += 1
                continue
            events.append((r["user_id"], d, r["event_type"], r.get(group_col, "") if group_col else ""))
    return events, problems


def pct(n, base):
    return f"{100 * n / base:.1f} percent" if base else "n/a (denominator 0)"


def print_problems(problems, n_ok):
    if problems:
        print("Rows excluded before computing (missing data; report them, do not impute):")
        for k, v in problems.items():
            print(f"  {k}: {v}")
    print(f"Rows used: {n_ok}")


def first_event(events, etype):
    first = {}
    for u, d, t, _ in events:
        if t == etype and (u not in first or d < first[u]):
            first[u] = d
    return first


# ---------------------------------------------------------------- kpis

def cmd_kpis(args):
    events, problems = read_events(args.file)
    print_problems(problems, len(events))
    with open(args.defs, encoding="utf-8") as fh:
        cards = json.load(fh).get("kpis", [])
    eligible = None
    if args.eligible:
        with open(args.eligible, newline="", encoding="utf-8-sig") as fh:
            eligible = {(r.get("user_id") or "").strip() for r in csv.DictReader(fh)} - {""}
    for c in cards:
        cid = c.get("id", "?")
        print(f"\nKPI {cid}: {c.get('name', '')}")
        per = c.get("period") or {}
        ps, pe = parse_date(per.get("start")), parse_date(per.get("end"))
        num = c.get("numerator") or {}
        den = c.get("denominator") or {}
        missing = [k for k, ok in (("period start and end", ps and pe),
                                    ("numerator event", num.get("event")),
                                    ("denominator population", den.get("population"))) if not ok]
        if missing:
            print(f"  Not computed: the card has no {', '.join(missing)} [GAP]")
            continue
        pop = den["population"]
        start_event = den.get("start_event")
        starts = first_event(events, start_event) if start_event else {}
        if pop == "eligible":
            if eligible is None and args.eligible_count is None:
                print("  Not computed: denominator 'eligible' needs --eligible or --eligible-count [GAP]")
                continue
            den_set = eligible
            den_n = len(eligible) if eligible is not None else args.eligible_count
        elif pop in ("enrolled", "enrolled_in_period", "enrolled_before_period"):
            if not start_event:
                print("  Not computed: the denominator needs a start_event (which event marks enrollment) [GAP]")
                continue
            if pop == "enrolled":
                den_set = {u for u, d in starts.items() if d <= pe}
            elif pop == "enrolled_in_period":
                den_set = {u for u, d in starts.items() if ps <= d <= pe}
            else:
                den_set = {u for u, d in starts.items() if d < ps}
            mdo = den.get("min_days_observed")
            if mdo is not None:
                den_set = {u for u in den_set if (pe - starts[u]).days >= int(mdo)}
            den_n = len(den_set)
        else:
            print(f"  Not computed: unknown denominator population '{pop}'")
            continue
        etype = num["event"]
        min_count = int(num.get("min_count") or 1)
        within = num.get("within_days_of_start")
        counts = defaultdict(int)
        for u, d, t, _ in events:
            if t != etype or not (ps <= d <= pe):
                continue
            if within is not None:
                s = starts.get(u)
                if s is None or not (0 <= (d - s).days <= int(within)):
                    continue
            counts[u] += 1
        meets = {u for u, n in counts.items() if n >= min_count}
        if den_set is not None:
            in_den = meets & den_set
            outside = meets - den_set
        else:
            in_den, outside = meets, set()
        print(f"  Period: {ps.isoformat()} to {pe.isoformat()}")
        rule = f"at least {min_count} '{etype}' event(s) in the period"
        if within is not None:
            rule += f", within {within} days of '{start_event}'"
        print(f"  Numerator: {len(in_den)} people with {rule}")
        extra = f", observed at least {den['min_days_observed']} days" if den.get("min_days_observed") is not None else ""
        print(f"  Denominator: {den_n} ({pop}{', start event ' + repr(start_event) if start_event else ''}{extra})")
        print(f"  Value: {pct(len(in_den), den_n)}")
        if den_set is None:
            print("  Numerator-in-denominator check not possible: only a count of eligible people was given")
        elif outside:
            print(f"  Check: {len(outside)} people meet the numerator but are not in the denominator "
                  f"(excluded from the value; check this is intended, for example people not yet observed for the full window, or a denominator that does not match the numerator)")
        thr = c.get("threshold")
        if thr and thr.get("value") is not None:
            print(f"  Threshold (the person's, set by {thr.get('set_by') or 'owner not named'}): {thr['value']}")
        else:
            print("  Threshold: none set; no verdict")


# ---------------------------------------------------------------- attrition

def km_curve(durations):
    """durations: list of (time_days, stopped_bool, days_observed). Returns sorted [(t, S(t), at_risk, stopped_at_t)]."""
    times = sorted({t for t, e, _ in durations if e})
    s, out = 1.0, []
    for t in times:
        at_risk = sum(1 for d, _, _ in durations if d >= t)
        d_t = sum(1 for d, e, _ in durations if e and d == t)
        if at_risk:
            s *= 1 - d_t / at_risk
        out.append((t, s, at_risk, d_t))
    return out


def s_at(curve, t):
    s = 1.0
    for ti, si, _, _ in curve:
        if ti <= t:
            s = si
        else:
            break
    return s


def t_point(curve, level):
    for ti, si, _, _ in curve:
        if si <= level:
            return ti
    return None


def attrition_for(users, args):
    """users: dict user -> (start, last_use or None, use_count). Returns durations and raw table."""
    durations = []
    for u, (start, last_use, _) in users.items():
        obs_end = (args.as_of - start).days
        if obs_end < 0:
            continue
        last = last_use if last_use is not None else start
        if (args.as_of - last).days > args.inactive_days:
            durations.append(((last - start).days, True, obs_end))
        else:
            durations.append((obs_end, False, obs_end))
    return durations


def cmd_attrition(args):
    args.as_of = date.fromisoformat(args.as_of)
    events, problems = read_events(args.file, args.group)
    print_problems(problems, len(events))
    after = sum(1 for _, d, _, _ in events if d > args.as_of)
    if after:
        print(f"Events dated after the as-of date, ignored: {after}")
    events = [e for e in events if e[1] <= args.as_of]
    starts, groups = {}, {}
    for u, d, t, g in events:
        if t == args.start_event and (u not in starts or d < starts[u]):
            starts[u] = d
            groups[u] = g
    if not starts:
        sys.exit(f"No '{args.start_event}' events found; nothing to compute")
    last_use, n_use, before_start = {}, defaultdict(int), 0
    for u, d, t, _ in events:
        if t != args.use_event or u not in starts:
            continue
        if d < starts[u]:
            before_start += 1
            continue
        n_use[u] += 1
        if u not in last_use or d > last_use[u]:
            last_use[u] = d
    orphans = {u for u, _, t, _ in events if t == args.use_event} - set(starts)
    print(f"As of {args.as_of.isoformat()}. Start event '{args.start_event}', use event '{args.use_event}', "
          f"stopped = no '{args.use_event}' for more than {args.inactive_days} days (the person's rule).")
    print(f"People with a start event: {len(starts)}; never used after start: "
          f"{sum(1 for u in starts if u not in last_use)}")
    if before_start:
        print(f"Use events dated before the person's start event, ignored: {before_start}")
    if orphans:
        print(f"People with use events but no start event, excluded: {len(orphans)}")
    by_group = defaultdict(dict)
    for u, s in starts.items():
        key = groups[u] if args.group else "all"
        by_group[key][u] = (s, last_use.get(u), n_use.get(u, 0))
    horizon = args.horizon_days or max((args.as_of - s).days for s in starts.values())
    points = list(range(0, horizon + 1, args.interval_days))
    rows_out, summary = [], {}
    for g in sorted(by_group):
        users = by_group[g]
        durs = attrition_for(users, args)
        curve = km_curve(durs)
        print(f"\nNonusage attrition, group: {g} (n = {len(durs)}; stopped {sum(e for _, e, _ in durs)}, "
              f"still using at the as-of date (censored) {sum(1 for _, e, _ in durs if not e)})")
        print("  Day | Enrolled at least this many days before the as-of date | Of those, stopped before this day | Raw stopped proportion | Kaplan-Meier still using")
        for t in points:
            valid = [(d, e) for d, e, o in durs if o >= t]
            stopped = sum(1 for d, e in valid if e and d < t)
            km = s_at(curve, t)
            print(f"  {t:>3} | {len(valid):>5} | {stopped:>5} | {pct(stopped, len(valid)):>22} | {100 * km:.1f} percent")
            rows_out.append({"group": g, "day": t, "valid_denominator": len(valid), "stopped": stopped,
                             "raw_stopped_proportion": round(stopped / len(valid), 4) if valid else "",
                             "km_still_using": round(km, 4)})
        tp = {lvl: t_point(curve, 1 - lvl) for lvl in (0.10, 0.25, 0.50)}
        print("  Usage half-life and earlier points (days from start until the share still using falls to):")
        for lvl, label in ((0.10, "t10 (10 percent stopped)"), (0.25, "t25 (25 percent stopped)"),
                           (0.50, "t50, usage half-life (50 percent stopped)")):
            v = tp[lvl]
            print(f"    {label}: {v if v is not None else 'not reached within the data'}")
        summary[g] = (durs, curve)
    if args.group and len(summary) > 1 and args.horizon_days:
        ref = args.ref or sorted(summary)[0]
        print(f"\nRelative risk of having stopped by day {args.horizon_days} (raw proportions, valid denominators; reference group {ref}):")
        def prop(durs):
            valid = [(d, e) for d, e, o in durs if o >= args.horizon_days]
            return sum(1 for d, e in valid if e and d < args.horizon_days), len(valid)
        rn, rd = prop(summary[ref][0])
        for g in sorted(summary):
            n, dn = prop(summary[g][0])
            rr = (n / dn) / (rn / rd) if dn and rd and rn else None
            print(f"  {g}: {n} of {dn} ({pct(n, dn)}); relative risk {rr:.2f}" if rr is not None
                  else f"  {g}: {n} of {dn}; relative risk not computable")
        print("  A descriptive comparison of the person's groups; not a cause and not a test of significance.")
    if args.followup:
        print("\nDropout attrition for follow-up waves (denominator: people whose wave was due by the as-of date):")
        done = defaultdict(set)
        for u, d, t, _ in events:
            done[t].add(u)
        for spec in args.followup.split(","):
            name, day = spec.split(":")
            day = int(day)
            due = {u for u, s in starts.items() if (args.as_of - s).days >= day}
            comp = due & done[name.strip()]
            print(f"  {name.strip()} (due day {day}): due {len(due)}, completed {len(comp)} "
                  f"({pct(len(comp), len(due))}), dropout {pct(len(due) - len(comp), len(due))}")
    if args.csv_out:
        with open(args.csv_out, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows_out[0].keys()))
            w.writeheader()
            w.writerows(rows_out)
        print(f"\nCurve table written to {args.csv_out} (for the dashboard chart)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    k = sub.add_parser("kpis")
    k.add_argument("file")
    k.add_argument("--defs", required=True)
    k.add_argument("--eligible")
    k.add_argument("--eligible-count", type=int)
    a = sub.add_parser("attrition")
    a.add_argument("file")
    a.add_argument("--start-event", required=True)
    a.add_argument("--use-event", required=True)
    a.add_argument("--inactive-days", type=int, required=True)
    a.add_argument("--as-of", required=True)
    a.add_argument("--interval-days", type=int, default=7)
    a.add_argument("--horizon-days", type=int)
    a.add_argument("--group")
    a.add_argument("--ref")
    a.add_argument("--followup")
    a.add_argument("--csv-out")
    args = ap.parse_args()
    {"kpis": cmd_kpis, "attrition": cmd_attrition}[args.cmd](args)


if __name__ == "__main__":
    main()
