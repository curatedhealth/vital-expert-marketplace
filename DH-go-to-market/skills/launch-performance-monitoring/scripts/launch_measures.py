#!/usr/bin/env python3
"""Compute launch measures from the person's own field records and check them
against the thresholds the person set.

Nothing here sets a threshold, fills a missing count or judges a cause. A
measure with no data is reported "not measured". Briefing misses and customer
meeting misses are kept apart.

Inputs (CSV, UTF-8, header row):
  --activity  date,role,person,account,activity,claim_ids,outcome
              activity: briefing | meeting | leave_behind | demo | training | other
              claim_ids: semicolon-separated approved claim ids used (may be empty)
              outcome: held | cancelled | no_show | delivered (free text allowed)
  --roster    role,person,briefer,briefing_due        (dates YYYY-MM-DD; due may be empty)
  --claims    id,claim[,status]                       (status 'approved' marks approval;
                                                       all rows approved if no status column)
  --measures  JSON list: [{"id": "M1", "label": "...", "metric": "<metric name>",
                           "comparison": ">=" | "<=", "threshold": number}]
              metric names: accounts_reached, meetings_held, meetings_cancelled,
              leave_behinds, briefings_delivered, roster_briefed_share,
              roster_overdue, unapproved_claim_uses, claim_uses
  --start / --end   the period (inclusive, YYYY-MM-DD); --as-of for overdue briefings
  --json      machine-readable output
"""
import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from datetime import date


def d(s):
    return date.fromisoformat(s.strip()) if s and s.strip() else None


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return [{k.strip(): (v or "").strip() for k, v in r.items()} for r in csv.DictReader(f)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--activity", required=True)
    ap.add_argument("--roster")
    ap.add_argument("--claims")
    ap.add_argument("--measures")
    ap.add_argument("--start", required=True)
    ap.add_argument("--end", required=True)
    ap.add_argument("--as-of")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    start, end = d(a.start), d(a.end)
    as_of = d(a.as_of) if a.as_of else end

    acts = [r for r in read_csv(a.activity) if r.get("date") and start <= d(r["date"]) <= end]
    out = {"period": {"start": a.start, "end": a.end, "as_of": as_of.isoformat()},
           "rows_in_period": len(acts), "metrics": {}, "detail": {}, "measures": [],
           "note": "Computed from the person's records only. Thresholds are the person's. No cause is inferred."}
    m = out["metrics"]

    meetings = [r for r in acts if r["activity"] == "meeting"]
    held = [r for r in meetings if r["outcome"] == "held"]
    m["meetings_held"] = len(held)
    m["meetings_cancelled"] = sum(1 for r in meetings if r["outcome"] in ("cancelled", "no_show"))
    m["accounts_reached"] = len({r["account"] for r in held if r["account"]})
    m["leave_behinds"] = sum(1 for r in acts if r["activity"] == "leave_behind")
    briefings = [r for r in acts if r["activity"] == "briefing" and r["outcome"] in ("held", "delivered")]
    m["briefings_delivered"] = len(briefings)

    # claims used in the field
    approved = None
    if a.claims:
        rows = read_csv(a.claims)
        has_status = any(r.get("status") for r in rows)
        approved = {r["id"] for r in rows if (r.get("status", "").lower() == "approved" or not has_status)}
    uses = Counter()
    unapproved = []
    for r in acts:
        for cid in [c.strip() for c in r.get("claim_ids", "").split(";") if c.strip()]:
            uses[cid] += 1
            if approved is not None and cid not in approved:
                unapproved.append({"date": r["date"], "person": r["person"], "account": r["account"], "claim_id": cid})
    m["claim_uses"] = sum(uses.values())
    out["detail"]["claim_uses_by_id"] = dict(sorted(uses.items()))
    if approved is not None:
        m["unapproved_claim_uses"] = len(unapproved)
        out["detail"]["unapproved_claim_uses"] = unapproved
    else:
        out["detail"]["unapproved_claim_uses"] = "not measured: no approved claim list supplied"

    # roster coverage
    if a.roster:
        roster = read_csv(a.roster)
        briefed_people = {r["person"] for r in read_csv(a.activity)
                          if r["activity"] == "briefing" and r["outcome"] in ("held", "delivered")
                          and d(r["date"]) and d(r["date"]) <= as_of}
        lines, overdue = [], 0
        for p in roster:
            due = d(p.get("briefing_due"))
            done = p["person"] in briefed_people
            if done:
                status = "briefed"
            elif due is None:
                status = "not briefed; no due date set"
            elif due < as_of:
                status = "not briefed; past the person's due date"
                overdue += 1
            else:
                status = "not briefed; due date not reached"
            lines.append({"role": p["role"], "person": p["person"], "briefer": p.get("briefer") or "owner not named",
                          "briefing_due": p.get("briefing_due") or None, "status": status})
        m["roster_size"] = len(roster)
        m["roster_briefed"] = sum(1 for l in lines if l["status"] == "briefed")
        m["roster_briefed_share"] = round(m["roster_briefed"] / len(roster), 3) if roster else None
        m["roster_overdue"] = overdue
        out["detail"]["roster"] = lines

    # per-person meeting outcome, kept apart from briefing status
    per = defaultdict(lambda: {"held": 0, "cancelled_or_no_show": 0})
    for r in meetings:
        per[r["person"]]["held" if r["outcome"] == "held" else "cancelled_or_no_show"] += 1
    out["detail"]["meetings_by_person"] = dict(per)

    # check the person's thresholds
    if a.measures:
        for ms in json.load(open(a.measures, encoding="utf-8")):
            val = m.get(ms["metric"])
            if val is None:
                res = "not measured"
            elif ms.get("threshold") is None:
                res = "no threshold set"
            elif ms["comparison"] == ">=":
                res = "met" if val >= ms["threshold"] else "missed"
            elif ms["comparison"] == "<=":
                res = "met" if val <= ms["threshold"] else "missed"
            else:
                res = "comparison not understood"
            out["measures"].append({**ms, "value": val, "result": res})

    if a.json:
        json.dump(out, sys.stdout, indent=1, ensure_ascii=False)
        print()
        return
    print(f"Launch measures, {a.start} to {a.end} (as of {as_of.isoformat()}); {len(acts)} activity rows")
    for k, v in m.items():
        print(f"  {k}: {v}")
    if out["measures"]:
        print("Your measures:")
        for x in out["measures"]:
            print(f"  {x['id']} {x['label']}: {x['value']} vs {x['comparison']} {x['threshold']} -> {x['result']}")
    if isinstance(out["detail"]["unapproved_claim_uses"], list) and out["detail"]["unapproved_claim_uses"]:
        print("Unapproved claim ids used in the field:")
        for u in out["detail"]["unapproved_claim_uses"]:
            print(f"  {u['date']} {u['person']} at {u['account']}: {u['claim_id']}")
    if "roster" in out["detail"]:
        print("Roster:")
        for l in out["detail"]["roster"]:
            print(f"  {l['role']} {l['person']} (briefer {l['briefer']}, due {l['briefing_due']}): {l['status']}")
    print("Meetings by person (kept apart from briefing status):")
    for p, v in out["detail"]["meetings_by_person"].items():
        print(f"  {p}: held {v['held']}, cancelled or no-show {v['cancelled_or_no_show']}")


if __name__ == "__main__":
    main()
