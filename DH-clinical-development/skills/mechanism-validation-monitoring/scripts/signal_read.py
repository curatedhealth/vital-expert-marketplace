#!/usr/bin/env python3
"""Safety and efficacy signal read against thresholds set before launch (mechanism-validation-monitoring A4).

Usage:
  python3 signal_read.py --thresholds THRESHOLDS.json --events EVENTS.csv --exposure EXPOSURE.csv [--version V] [--json]

EVENTS.csv: event_id, date (YYYY-MM-DD), version, category (as the person or the owner
they name assigned it), seriousness (as assigned, or "not assessed").
EXPOSURE.csv: period, start, end (YYYY-MM-DD), version, active_users, plus any efficacy
measure columns the person tracks per period (for example responder_share).
THRESHOLDS.json (shape: evals/files/signal_thresholds_illustrative.json): "set_on",
"set_before_launch", and "signals", each with "id", "kind" ("event_count",
"event_rate_per_1000" or "measure"), "category" or "measure", "alert_when" (">" or "<")
and "value".

What it does: keeps one version; per period, counts events by the person's category
(events outside every period are listed, not dropped), computes rates on the person's
active-user denominator, reads each measure column, and marks each signal "crossed" or
"not crossed" only when its threshold was set before launch (MDCG 2025-10 asks for
indicators and thresholds in the premarket phase, SE63); otherwise "not compared".
Categories without a threshold are counted without a verdict. It never reclassifies an
event, never judges seriousness, causality or reportability (that is the call of the
owner the person names for vigilance reporting, routed to dh-regulatory-and-quality
audit-capa-and-complaints), never imputes, and never supplies a threshold.
"""
import argparse
import csv
import json
from collections import defaultdict
from datetime import date


def d(s):
    return date.fromisoformat(s.strip())


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--thresholds", required=True)
    ap.add_argument("--events", required=True)
    ap.add_argument("--exposure", required=True)
    ap.add_argument("--version")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    th = json.load(open(a.thresholds))

    periods = []
    for r in csv.DictReader(open(a.exposure)):
        if a.version and r["version"] != a.version:
            continue
        periods.append(r)
    out = {"version": a.version or "not given", "thresholds_set_on": th.get("set_on", "not given"),
           "set_before_launch": bool(th.get("set_before_launch")), "periods": [], "events_outside_periods": [],
           "events_other_version": 0}
    counts = defaultdict(lambda: defaultdict(int))
    serious = defaultdict(lambda: defaultdict(int))
    for e in csv.DictReader(open(a.events)):
        if a.version and e["version"] != a.version:
            out["events_other_version"] += 1
            continue
        day = d(e["date"])
        hit = None
        for p in periods:
            if d(p["start"]) <= day <= d(p["end"]):
                hit = p["period"]
                break
        if hit is None:
            out["events_outside_periods"].append(e["event_id"])
            continue
        counts[hit][e["category"].strip()] += 1
        serious[hit][(e["category"].strip(), (e.get("seriousness") or "not assessed").strip())] += 1

    covered = {s.get("category") for s in th.get("signals", []) if s.get("category")}
    for p in periods:
        pid = p["period"]
        users = num(p.get("active_users"))
        rows = []
        for s in th.get("signals", []):
            if s["kind"] == "measure":
                v = num(p.get(s["measure"]))
                label = s["measure"]
                denom = "per the person's measure definition"
            else:
                c = counts[pid].get(s["category"], 0)
                label = s["category"]
                if s["kind"] == "event_count":
                    v, denom = c, "count"
                else:
                    v = round(c / users * 1000, 2) if users else None
                    denom = f"{c} events / {int(users) if users else 'no active users given'} active users x 1000"
            if not th.get("set_before_launch"):
                res = "not compared: threshold not set before launch"
            elif v is None:
                res = "not compared: no value for this period"
            else:
                crossed = v > s["value"] if s["alert_when"] == ">" else v < s["value"]
                res = "crossed the person's threshold" if crossed else "not crossed"
            rows.append({"signal": s["id"], "what": label, "kind": s["kind"], "value": v, "basis": denom,
                         "alert_when": f"{s['alert_when']} {s['value']}", "result": res})
        uncovered = {k: v for k, v in counts[pid].items() if k not in covered}
        out["periods"].append({"period": pid, "start": p["start"], "end": p["end"], "active_users": p.get("active_users"),
                               "signals": rows, "categories_without_threshold": uncovered,
                               "seriousness_as_assigned": {f"{k[0]} / {k[1]}": v for k, v in sorted(serious[pid].items())}})
    out["notes"] = [
        "Categories and seriousness are as the person assigned them; none is reclassified here.",
        "Whether any event is reportable under 21 CFR 803 or 806 or MDR Articles 87 to 89, and by when, is the call of the owner the person names for vigilance reporting (route: dh-regulatory-and-quality audit-capa-and-complaints).",
        "A crossed threshold is a signal for the miss review (B1), not a finding that the product is unsafe or ineffective; a threshold not crossed is not a finding that it is safe or effective.",
    ]

    if a.json:
        print(json.dumps(out, indent=1))
        return
    print(f"Version: {out['version']} | Thresholds set on: {out['thresholds_set_on']} | Set before launch: {out['set_before_launch']}")
    print(f"Events of other versions excluded: {out['events_other_version']} | Events outside every period: {out['events_outside_periods'] or 'none'}")
    for p in out["periods"]:
        print(f"\nPeriod {p['period']} ({p['start']} to {p['end']}), active users {p['active_users']}:")
        for r in p["signals"]:
            print(f"  {r['signal']} {r['what']} ({r['kind']}): {r['value']} [{r['basis']}] alert when {r['alert_when']}: {r['result']}")
        print("  Categories without a threshold (counted, no verdict):", p["categories_without_threshold"] or "none")
        print("  Seriousness as assigned:", p["seriousness_as_assigned"] or "none")
    print()
    for x in out["notes"]:
        print("Note:", x)


if __name__ == "__main__":
    main()
