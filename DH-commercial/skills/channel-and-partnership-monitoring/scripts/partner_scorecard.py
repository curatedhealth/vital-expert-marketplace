#!/usr/bin/env python3
"""Score each partner for a period against the measures the person set.

Inputs
  LOG.csv       the person's handoff record, one row per event, columns:
                period, partner, partner_type, buyer_id, event, event_date, source, note
                event:  qualified_handoff | implementation_started | claim_breach | partner_reported_lead
                source: handoff_record | partner_report
  MEASURES.json the person's measure sheet:
                {"period": "...", "partner_types": {TYPE: {"measures": [
                  {"name": "...", "event": EVENT, "op": ">=" | "<=", "threshold": N,
                   "forces_hold": true|false}]}}}

Rules applied (register method for DH-02.01.4.2):
  - counts come from the handoff record; a partner report is counted only when the
    same buyer and event are in the handoff record (then it is the record that counts)
  - a partner report that cannot be tied to a buyer in the record is listed, not counted
  - an implementation is counted only for a buyer this partner handed off
  - claim breaches are listed with their note, as evidence
The script never sets a threshold: a partner type without measures gets counts only.

Usage: python3 partner_scorecard.py LOG.csv MEASURES.json [--period P]
"""
import csv
import json
import sys
from collections import defaultdict

OPS = {">=": lambda v, t: v >= t, "<=": lambda v, t: v <= t, ">": lambda v, t: v > t,
       "<": lambda v, t: v < t, "==": lambda v, t: v == t}


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    log_path, measures_path = sys.argv[1], sys.argv[2]
    with open(measures_path, encoding="utf-8") as fh:
        sheet = json.load(fh)
    period = sheet.get("period")
    if "--period" in sys.argv:
        period = sys.argv[sys.argv.index("--period") + 1]
    with open(log_path, encoding="utf-8", newline="") as fh:
        rows = [r for r in csv.DictReader(fh) if not period or r["period"] == period]
    if not rows:
        print(f"No rows for period {period}.")
        return 2

    ptype = {}
    record = defaultdict(set)          # (partner, event) -> buyer ids from the record
    handed = defaultdict(set)          # partner -> buyers handed off (record)
    reports = defaultdict(list)        # partner -> partner-reported rows
    breaches = defaultdict(list)
    problems = []
    for r in rows:
        p = r["partner"].strip()
        ptype[p] = r["partner_type"].strip()
        ev, src, buyer = r["event"].strip(), r["source"].strip(), r["buyer_id"].strip()
        if src == "handoff_record":
            if ev == "claim_breach":
                breaches[p].append(r)
                continue
            if not buyer:
                problems.append(f"{p}: record row without buyer_id ({ev}, {r['event_date']})")
                continue
            record[(p, ev)].add(buyer)
            if ev == "qualified_handoff":
                handed[p].add(buyer)
        elif src == "partner_report":
            reports[p].append(r)
        else:
            problems.append(f"{p}: unknown source '{src}'")

    print(f"Period: {period}")
    print()
    for p in sorted(ptype):
        counts = {
            "qualified_handoff": len(record[(p, "qualified_handoff")]),
            "implementation_started": len(record[(p, "implementation_started")] & handed[p]),
            "claim_breach": len(breaches[p]),
        }
        untied_impl = record[(p, "implementation_started")] - handed[p]
        tied, untied = [], []
        for r in reports[p]:
            b = r["buyer_id"].strip()
            ev = "qualified_handoff" if r["event"] == "partner_reported_lead" else r["event"]
            (tied if b and b in record[(p, ev)] else untied).append(r)
        print(f"## {p} ({ptype[p]})")
        print("| Measure | Count (handoff record) | Rule (yours) | Result |")
        print("|---|---|---|---|")
        measures = sheet.get("partner_types", {}).get(ptype[p], {}).get("measures", [])
        hold = []
        if not measures:
            for ev, n in counts.items():
                print(f"| {ev} | {n} | no rule set [GAP] | not judged |")
        for m in measures:
            n = counts.get(m["event"])
            if n is None:
                print(f"| {m['name']} | not counted [GAP] | {m['op']} {m['threshold']} | not measurable |")
                continue
            ok = OPS[m["op"]](n, m["threshold"])
            res = "met" if ok else "missed"
            if not ok and m.get("forces_hold"):
                res += " (your hold rule)"
                hold.append(m["name"])
            print(f"| {m['name']} | {n} | {m['op']} {m['threshold']} | {res} |")
        print()
        print(f"Partner reports tied to a buyer in the record: {len(tied)} (already counted from the record)")
        print(f"Partner reports not tied to a buyer: {len(untied)} (not counted)"
              + (": " + ", ".join(f"{r['event_date']} {r['buyer_id'] or 'no buyer id'}" for r in untied) if untied else ""))
        if untied_impl:
            print(f"Implementations for buyers this partner did not hand off: {len(untied_impl)} (not counted): {', '.join(sorted(untied_impl))}")
        for b in breaches[p]:
            print(f"Claim breach {b['event_date']}: {b['note']}")
        if breaches[p]:
            print("Open claim breach: the register rule says do not continue this partner while a breach is open; the action stops for your owner.")
        print(f"Hold rules triggered: {', '.join(hold) if hold else 'none'}")
        print()
    if problems:
        print("Data problems:")
        for x in problems:
            print(" -", x)
    return 0


if __name__ == "__main__":
    sys.exit(main())
