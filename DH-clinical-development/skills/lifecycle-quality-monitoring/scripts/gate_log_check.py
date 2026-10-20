#!/usr/bin/env python3
"""Read a product's stage-gate log and report, stage by stage, what the log shows.

Input: a CSV gate log the person keeps (one row per owed work product), columns:
  stage, owed_work_product, status, evidence_ref, decided_by, decision_date,
  opened_on, owner, reread_date, next_stage_started_on
status is the person's word: accepted, missing, in progress, waived.
Dates are YYYY-MM-DD. Empty cells are allowed.

Options:
  --as-of YYYY-MM-DD   the read date for "days open" (required)
  --events FILE.json   saved regulatory-dh.search_safety_events output (or the
                       examples/live wrapper); events dated after a stage's last
                       decision are listed against that stage as post-market inputs
  --product NAME       filter events by product name

It counts and flags against the log's own content only. It does not score a
stage, set a threshold, or decide whether a stage passed. Flags:
  F1 accepted with no evidence_ref       (a status with no work product behind it)
  F2 accepted with no decided_by or date (no named decision)
  F3 missing with no owner               (owner not named)
  F4 next stage started while an item of this stage is missing or in progress
  F5 missing or in progress with no reread_date
"""
import csv
import json
import sys
from collections import OrderedDict
from datetime import date


def d(s):
    try:
        y, m, dd = (int(x) for x in s.strip()[:10].split("-"))
        return date(y, m, dd)
    except Exception:
        return None


def load_events(path, product):
    with open(path) as f:
        data = json.load(f)
    calls = data["calls"] if isinstance(data, dict) and "calls" in data else [data]
    out = []
    for c in calls:
        for r in c.get("results") or []:
            if "event_date" not in r:
                continue
            if product and product.lower() not in (r.get("title", "") + r.get("manufacturer", "")).lower():
                continue
            out.append(r)
    seen, uniq = set(), []
    for r in out:
        k = (r.get("title"), r.get("event_date"))
        if k not in seen:
            seen.add(k)
            uniq.append(r)
    return sorted(uniq, key=lambda r: r["event_date"])


def main(argv):
    args = {"--as-of": None, "--events": None, "--product": None}
    files = []
    i = 0
    while i < len(argv):
        if argv[i] in args:
            args[argv[i]] = argv[i + 1]
            i += 2
        else:
            files.append(argv[i])
            i += 1
    asof = d(args["--as-of"] or "")
    if not asof or not (files or args["--events"]):
        print(__doc__)
        return 2
    stages = OrderedDict()
    if not files:
        print("No gate log given: stage table skipped; post-market inputs only.")
    for path in files[:1]:
      with open(path, newline="") as f:
        lines = [ln for ln in f if not ln.startswith("#")]
        for row in csv.DictReader(lines):
            row = {k: (v or "").strip() for k, v in row.items()}
            stages.setdefault(row["stage"], []).append(row)
    print(f"Gate log read as of {asof.isoformat()}. Counts and flags from the log only; the pass rule is the person's.\n")
    if stages:
      print("| Stage | Owed items | Accepted | Missing | In progress | Waived | Days open | Flags |")
      print("|---|---|---|---|---|---|---|---|")
    details, last_decision = [], {}
    for st, rows in stages.items():
        c = {"accepted": 0, "missing": 0, "in progress": 0, "waived": 0}
        flags = []
        opened = [d(r["opened_on"]) for r in rows if d(r["opened_on"])]
        decided = [d(r["decision_date"]) for r in rows if d(r["decision_date"])]
        for r in rows:
            s = r["status"].lower()
            c[s] = c.get(s, 0) + 1
            item = r["owed_work_product"]
            if s == "accepted" and not r["evidence_ref"]:
                flags.append("F1"); details.append(f"{st} / {item}: F1 accepted with no evidence reference")
            if s == "accepted" and (not r["decided_by"] or not d(r["decision_date"])):
                flags.append("F2"); details.append(f"{st} / {item}: F2 accepted with no named decider or decision date")
            if s in ("missing", "in progress"):
                if s == "missing" and not r["owner"]:
                    flags.append("F3"); details.append(f"{st} / {item}: F3 missing, owner not named")
                if d(r["next_stage_started_on"]):
                    flags.append("F4"); details.append(f"{st} / {item}: F4 next stage started on {r['next_stage_started_on']} while this item is {s}")
                if not d(r["reread_date"]):
                    flags.append("F5"); details.append(f"{st} / {item}: F5 {s} with no reread date")
        open_days = ""
        if opened:
            end = max(decided) if decided and c["missing"] == 0 and c["in progress"] == 0 else asof
            open_days = str((end - min(opened)).days) + ("" if end == asof else " (closed)")
        if decided:
            last_decision[st] = max(decided)
        print(f"| {st} | {len(rows)} | {c['accepted']} | {c['missing']} | {c['in progress']} | {c['waived']} | {open_days or 'not stored'} | {', '.join(sorted(set(flags))) or 'none'} |")
    if details:
        print("\nFlags by item:")
        for x in details:
            print(f"- {x}")
    if args["--events"]:
        ev = load_events(args["--events"], args["--product"])
        print("\nPost-market inputs from the saved record (records only; a missing record is a gap, not evidence of no event):")
        if not ev:
            print("- none in the saved output")
        latest = max(last_decision.values()) if last_decision else None
        for r in ev:
            after = d(r["event_date"]) and latest and d(r["event_date"]) > latest
            if latest is None:
                tag = "no gate log given"
            else:
                tag = "after the last gate decision in the log" if after else "on or before the last gate decision in the log"
            print(f"- {r['event_date']} {r.get('source_type','')} {r.get('severity','')}: {r.get('title','').split(',')[0]} ({tag}). Source {r.get('source_url','')}, retrieved {r.get('retrieved_at','')[:10]}.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
