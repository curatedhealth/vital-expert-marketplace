#!/usr/bin/env python3
"""Engagement and retention read of one cohort on one version (mechanism-validation-monitoring A3).

Usage:
  python3 engagement_read.py --definitions DEFS.json --data USAGE.csv [--version V] [--as-of YYYY-MM-DD] [--json]

USAGE.csv has one row per user per day of use: user_id, version, date (YYYY-MM-DD),
minutes, sessions, period_days (the prescribed or intended period for that user).
Days without a row are days without use.

DEFS.json (shape: evals/files/engagement_definitions_illustrative.json) holds the
person's definitions: "rule" is "digav" (DiGAV section 23c, SE70 to SE73) or "custom"
with "gap_days"; "window_cap_days" (90 under the DiGAV); "set_before_data" and "set_on";
optional "thresholds" on discontinued_share, completed_share or mean_weekly_minutes,
each with "direction" (">=" or "<=") and "value".

What it does: keeps one version; per user, takes the window from first use for the
period (capped); finds the first run of days without use that meets the person's
discontinuation rule; reports the SE73 items (number and share discontinuing, weekly
distribution, number and share completing, mean days to discontinuation) and weekly
usage volume and frequency with discontinued users included (SE71). It compares with a
threshold only if the definitions were set before the data were read. Without --as-of
it prints "data cut not given": gaps after a user's last recorded use cannot be judged,
so those users are "not determinable" and weekly means use observed weeks only. It
never imputes, never supplies a benchmark or a threshold, and never reads usage as the
outcome. Every [PAPER] row it prints carries its DOI.
"""
import argparse
import csv
import json
import math
from collections import defaultdict
from datetime import date, timedelta

DOI = {"SE71": None, "SE72": None, "SE73": None, "SE82": "10.1007/s13142-016-0453-1",
       "SE92": "10.2196/jmir.8578", "SE26": None}


def row(r):
    return f"{r}, DOI {DOI[r]}" if DOI.get(r) else r


def d(s):
    return date.fromisoformat(s.strip())


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def gap_rule(defs, period_days):
    if defs.get("rule") == "digav":
        if period_days >= 90:
            return 21.0, "three consecutive weeks without use (period of 90 days or more), " + row("SE72")
        return 0.25 * period_days, f"25 percent of the {period_days}-day period without use, " + row("SE72")
    g = defs.get("custom", {}).get("gap_days")
    if g is None:
        return None, "no discontinuation rule given"
    return float(g), f"{g} consecutive days without use (the person's rule)"


def read_user(days, period_days, cap, rule_days, as_of):
    first = min(days)
    length = min(period_days, cap) if cap else period_days
    end = first + timedelta(days=length - 1)
    uses = sorted(x for x in days if x <= end)
    gaps = []  # (last use before gap, first day without use, gap length)
    for a, b in zip(uses, uses[1:]):
        k = (b - a).days - 1
        if k > 0:
            gaps.append((a, a + timedelta(days=1), k))
    observed_to = None
    if as_of is not None:
        observed_to = min(as_of, end)
        k = (observed_to - uses[-1]).days
        if k > 0:
            gaps.append((uses[-1], uses[-1] + timedelta(days=1), k))
    disc = None
    if rule_days is not None:
        for last, start, k in gaps:
            if k >= rule_days:
                disc = (last, start)
                break
    if disc:
        status = "discontinued"
    elif as_of is None:
        status = "not determinable"
    elif as_of >= end:
        status = "completed"
    else:
        status = "in progress"
    return {"first": first, "end": end, "status": status, "disc": disc,
            "weeks_window": math.ceil(length / 7), "observed_to": observed_to or uses[-1]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--definitions", required=True)
    ap.add_argument("--data", required=True)
    ap.add_argument("--version")
    ap.add_argument("--as-of")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    defs = json.load(open(a.definitions))
    as_of = d(a.as_of) if a.as_of else None
    cap = defs.get("window_cap_days")

    per_user = defaultdict(dict)
    period = {}
    excluded = 0
    versions = set()
    for r in csv.DictReader(open(a.data)):
        versions.add(r["version"])
        if a.version and r["version"] != a.version:
            excluded += 1
            continue
        day = d(r["date"])
        if as_of and day > as_of:
            excluded += 1
            continue
        m = per_user[r["user_id"]].setdefault(day, [0.0, 0.0])
        m[0] += num(r.get("minutes")) or 0.0
        m[1] += num(r.get("sessions")) or 0.0
        period[r["user_id"]] = int(float(r["period_days"]))

    out = {"version": a.version or "not given", "data_cut": a.as_of or "data cut not given; ask the person",
           "rows_excluded_other_version_or_after_cut": excluded,
           "versions_in_file": sorted(versions), "users": len(per_user)}
    if not a.version and len(versions) > 1:
        out["warning_versions"] = "more than one version in the file and no --version given: results pool versions; ask the person"

    results = {}
    rules = set()
    for u, days in per_user.items():
        rd, rtext = gap_rule(defs, period[u])
        rules.add(rtext)
        results[u] = read_user(days, period[u], cap, rd, as_of)
    out["discontinuation_rule"] = sorted(rules)

    n = len(results)
    disc = [u for u, x in results.items() if x["status"] == "discontinued"]
    comp = [u for u, x in results.items() if x["status"] == "completed"]
    out["items_SE73"] = {
        "discontinued_n": len(disc),
        "discontinued_share": round(len(disc) / n, 3) if n else None,
        "completed_n": len(comp),
        "completed_share": round(len(comp) / n, 3) if n else None,
        "in_progress_n": sum(1 for x in results.values() if x["status"] == "in progress"),
        "not_determinable_n": sum(1 for x in results.values() if x["status"] == "not determinable"),
        "discontinuations_by_week": {},
        "mean_days_to_discontinuation": None,
        "days_to_discontinuation_reading": "days from first use to the last use before the qualifying gap; the DiGAV text does not say which day counts, so the person confirms or replaces this reading",
    }
    byweek = defaultdict(int)
    days_to = []
    for u in disc:
        x = results[u]
        last, start = x["disc"]
        byweek[(start - x["first"]).days // 7 + 1] += 1
        days_to.append((last - x["first"]).days)
    out["items_SE73"]["discontinuations_by_week"] = {f"week {k}": v for k, v in sorted(byweek.items())}
    if days_to:
        out["items_SE73"]["mean_days_to_discontinuation"] = round(sum(days_to) / len(days_to), 1)

    # weekly usage volume and frequency, discontinued users included (SE71)
    weeks = defaultdict(lambda: [0, 0.0, 0.0])
    user_mean = {}
    for u, x in results.items():
        utot = uw = 0
        for w in range(1, x["weeks_window"] + 1):
            wstart = x["first"] + timedelta(days=7 * (w - 1))
            if wstart > x["observed_to"]:
                break
            mins = sess = 0.0
            for k in range(7):
                v = per_user[u].get(wstart + timedelta(days=k))
                if v and wstart + timedelta(days=k) <= x["end"]:
                    mins += v[0]
                    sess += v[1]
            weeks[w][0] += 1
            weeks[w][1] += mins
            weeks[w][2] += sess
            utot += mins
            uw += 1
        user_mean[u] = utot / uw if uw else 0.0
    out["weekly_usage_SE71"] = {f"week {w}": {"users": c, "mean_minutes": round(m / c, 1), "mean_sessions": round(s / c, 2)}
                                for w, (c, m, s) in sorted(weeks.items())}
    tot_c = sum(v[0] for v in weeks.values())
    out["mean_weekly_minutes"] = round(sum(v[1] for v in weeks.values()) / tot_c, 1) if tot_c else None
    out["mean_weekly_sessions"] = round(sum(v[2] for v in weeks.values()) / tot_c, 2) if tot_c else None
    um = sorted(user_mean.values())
    if um:
        mid = len(um) // 2
        med = um[mid] if len(um) % 2 else (um[mid - 1] + um[mid]) / 2
        top = max(user_mean, key=user_mean.get)
        out["per_user_weekly_minutes"] = {"median": round(med, 1), "highest_user": top, "highest_value": round(user_mean[top], 1),
                                          "note": "one heavy user can carry the mean; the median is shown beside it. A very high level is reported as a level and handed to A4 only if the design named an overuse or screen-time risk."}
    if as_of is None:
        out["weekly_note"] = "data cut not given: weeks after each user's last recorded use are not counted, so weekly means cover observed weeks only and are provisional"

    comps = []
    th = defs.get("thresholds", {})
    vals = {"discontinued_share": out["items_SE73"]["discontinued_share"],
            "completed_share": out["items_SE73"]["completed_share"],
            "mean_weekly_minutes": out["mean_weekly_minutes"]}
    for k, t in th.items():
        v = vals.get(k)
        if as_of is None:
            comps.append({"measure": k, "value": v, "threshold": t, "result": "not compared: data cut not given"})
        elif not defs.get("set_before_data"):
            comps.append({"measure": k, "value": v, "threshold": t, "result": "not compared: definitions not set before the data were read"})
        elif v is None:
            comps.append({"measure": k, "value": v, "threshold": t, "result": "not compared: no value"})
        else:
            ok = v >= t["value"] if t["direction"] == ">=" else v <= t["value"]
            comps.append({"measure": k, "value": v, "threshold": t, "result": "within the person's threshold" if ok else "outside the person's threshold"})
    out["threshold_comparisons"] = comps or "no thresholds given; values reported without a verdict"
    out["notes"] = [
        "Usage is the 'used' link, never the outcome (" + row("SE26") + "; " + row("SE82") + ").",
        "Called 'usage', not adherence, unless the person gives an intended use with its justification (" + row("SE92") + ").",
        "No benchmark or retention target is sourced; none is applied.",
    ]

    if a.json:
        print(json.dumps(out, indent=1, default=str))
        return
    print(f"Version: {out['version']} | Data cut: {out['data_cut']} | Users: {n} | Rows excluded (other version or after cut): {excluded}")
    if "warning_versions" in out:
        print("WARNING:", out["warning_versions"])
    print("Discontinuation rule:", "; ".join(out["discontinuation_rule"]))
    i = out["items_SE73"]
    print(f"Discontinued: {i['discontinued_n']} of {n} ({i['discontinued_share']}) | Completed: {i['completed_n']} ({i['completed_share']}) | In progress: {i['in_progress_n']} | Not determinable: {i['not_determinable_n']}")
    print("Discontinuations by week (first day without use):", i["discontinuations_by_week"] or "none")
    print("Mean days to discontinuation:", i["mean_days_to_discontinuation"], "(" + i["days_to_discontinuation_reading"] + ")")
    print("Weekly usage, discontinued users included (SE71):")
    for w, v in out["weekly_usage_SE71"].items():
        print(f"  {w}: users {v['users']}, mean minutes {v['mean_minutes']}, mean sessions {v['mean_sessions']}")
    print("Mean weekly minutes:", out["mean_weekly_minutes"], "| Mean weekly sessions:", out["mean_weekly_sessions"])
    if "per_user_weekly_minutes" in out:
        pu = out["per_user_weekly_minutes"]
        print(f"Per-user mean weekly minutes: median {pu['median']}; highest {pu['highest_user']} at {pu['highest_value']} ({pu['note']})")
    if "weekly_note" in out:
        print("Note:", out["weekly_note"])
    print("Threshold comparisons:")
    if isinstance(comps, list) and comps:
        for c in comps:
            print(f"  {c['measure']}: {c['value']} vs {c['threshold']['direction']} {c['threshold']['value']}: {c['result']}")
    else:
        print("  ", out["threshold_comparisons"])
    for x in out["notes"]:
        print("Note:", x)


if __name__ == "__main__":
    main()
