#!/usr/bin/env python3
"""Build a dated lifecycle timeline for named products from saved connector output.

Reads one or more JSON files saved from regulatory-dh calls (get_authorization,
search_devices, find_predicates, search_safety_events). A file may hold one call
output (with "results") or a wrapper {"calls": [...]} as in examples/live/.
Prints a markdown table, oldest first: date, product, event, reference, pathway,
days from submission to decision (where both dates are stored), predicate as the
record states it, source URL. Then MAUDE report counts by year, labeled as reports.

It only re-arranges what the records state. It does not infer a stage, a reason
for a change, or whether a product is still marketed.

Usage: python3 lifecycle_timeline.py FILE.json [FILE.json ...] [--product NAME]
"""
import json
import sys
from datetime import date


def load_calls(path):
    with open(path) as f:
        data = json.load(f)
    if isinstance(data, dict) and "calls" in data:
        return data["calls"]
    return [data]


def parse(d):
    try:
        y, m, dd = (int(x) for x in d[:10].split("-"))
        return date(y, m, dd)
    except Exception:
        return None


def main(argv):
    files, product = [], None
    i = 0
    while i < len(argv):
        if argv[i] == "--product":
            product = argv[i + 1].lower()
            i += 2
            continue
        files.append(argv[i])
        i += 1
    if not files:
        print(__doc__)
        return 2
    rows, seen, maude, codes = [], set(), {}, set()
    for path in files:
        for call in load_calls(path):
            for r in call.get("results") or []:
                name = r.get("product") or r.get("device") or r.get("title", "").split(",")[0]
                if product and product not in name.lower():
                    continue
                if "event_date" in r:
                    key = ("event", r.get("title"), r["event_date"])
                    if key in seen:
                        continue
                    seen.add(key)
                    rows.append((r["event_date"], name, f"{r.get('source_type','event')} {r.get('severity','')}".strip(),
                                 "", "", "", "", r.get("source_url", "")))
                    continue
                ref = r.get("reference") or ";".join(sum((r.get("identifiers") or {}).values(), []))
                if not ref:
                    url = r.get("source_url", "")
                    ref = url.split("=")[-1] if "=" in url else ""
                if not r.get("decision_date"):
                    continue
                key = ("auth", ref.upper(), r["decision_date"])
                if key in seen:
                    continue
                seen.add(key)
                if r.get("product_code"):
                    codes.add(r["product_code"])
                sub, dec = parse(r.get("submission_date") or ""), parse(r["decision_date"])
                days = str((dec - sub).days) if sub and dec else "not stored"
                pred = r.get("predicate_references") or r.get("predicates")
                pred = ", ".join(pred) if isinstance(pred, list) else (pred or "none stated")
                rows.append((r["decision_date"], name, "authorization" + (f" ({r['status']})" if r.get("status") else ""), ref,
                             r.get("pathway", ""), days, pred, r.get("source_url", "")))
            for m in call.get("maude_counts") or []:
                maude[m["product_code"]] = m
    rows.sort(key=lambda x: x[0])
    print("| Date | Product | Event | Reference | Pathway | Days submission to decision | Predicate (as stored) | Source |")
    print("|---|---|---|---|---|---|---|---|")
    for r in rows:
        print("| " + " | ".join(r) + " |")
    auth = [r for r in rows if r[2].startswith("authorization")]
    for a, b in zip(auth, auth[1:]):
        da, db = parse(a[0]), parse(b[0])
        print(f"\nInterval: {a[3]} to {b[3]}: {(db - da).days} days between decision dates.")
    for code, m in maude.items():
        if product and code not in codes:
            continue
        years = ", ".join(f"{y['year']}: {y['count']}" for y in m.get("by_year", []))
        print(f"\nMAUDE reports, product code {code}: {m.get('total_reports')} ({years}). {m.get('basis')}. Retrieved {m.get('retrieved_at','')[:10]}.")
    print("\nRecords only. A missing record is a gap in the store, not evidence that nothing happened.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
