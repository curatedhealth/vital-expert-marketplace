#!/usr/bin/env python3
"""Risk feedback: compare observed post-market events with the person's risk file.

Two modes.

1. Prepare an events table from saved library output
     python3 risk_feedback.py --from-connector out.json [more.json ...] > events.csv
   Reads saved regulatory-dh.search_safety_events responses, folds rows that repeat the same
   event (same date and same summary text, one row per app line or model in the source) into
   one event, and writes events.csv with hazard_id left blank. The person (or the model, with
   each mapping marked "proposed" until the person confirms) fills hazard_id from their own
   risk file. The script never maps an event to a hazard.

2. Compare events with the risk file
     python3 risk_feedback.py --risk risk_file.csv --events events.csv [--scale scale.json] [--json]

   risk_file.csv   the person's hazard list. Columns: hazard_id, hazard, harm, severity,
                   probability, controls. Severity and probability are the person's own
                   words or numbers, copied as written.
   events.csv      columns: event_id, origin, source, date, description, hazard_id,
                   harm_observed, severity_observed. origin is "own" (the person's complaints,
                   vigilance or MDR files) or "comparable" (another product's recall or alert).
                   Comparable events show whether a hazard was foreseeable; they are never
                   counted as occurrences of the person's product. Complaints, the person's own vigilance or MDR files, and
                   comparable products' recalls can sit in one file; the source column keeps
                   them apart. hazard_id may hold several ids separated by ";".
   scale.json      optional. The person's ordered severity scale, lowest first:
                   {"severity": ["negligible", "minor", "serious", "critical", "catastrophic"]}
                   Only with a scale does the script compare observed severity with the file.

Output
  Per hazard: own events and comparable events mapped (counted apart), highest observed severity, the file's severity, and a
  flag when observed severity is above the file's estimate on the person's scale. Then the
  events not mapped to any hazard (candidates for "not foreseen", for the person to decide),
  and events naming a hazard id the file does not hold. No verdict on whether a control is
  effective or a risk acceptable: those are the owner's decisions.
"""
import argparse
import csv
import json
import sys
from collections import defaultdict, OrderedDict


def from_connector(paths):
    events = OrderedDict()
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            data = json.load(fh)
        for r in data.get("results", []):
            key = (r.get("event_date"), " ".join((r.get("summary") or "").split()))
            if key not in events:
                events[key] = {"rows": [], "r": r}
            if r.get("title") not in [x.get("title") for x in events[key]["rows"]]:
                events[key]["rows"].append(r)
    w = csv.writer(sys.stdout)
    w.writerow(["event_id", "origin", "source", "date", "description", "hazard_id", "harm_observed", "severity_observed", "source_url", "lines_affected"])
    for n, ((date, summary), v) in enumerate(events.items(), 1):
        r = v["r"]
        src = f"{r.get('source_type')} {r.get('jurisdiction')} {r.get('severity') or ''} {r.get('manufacturer') or ''}".strip()
        titles = " | ".join((x.get("title") or "")[:90] for x in v["rows"])
        w.writerow([f"EV-{n:02d}", "comparable", src, date, summary, "", "", "", r.get("source_url"), f"{len(v['rows'])}: {titles}"])


def read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        rd = csv.DictReader(fh)
        return [{(k or "").strip().lower(): (v or "").strip() for k, v in row.items()} for row in rd]


def compare(risk_path, events_path, scale_path):
    hazards = OrderedDict((h["hazard_id"], h) for h in read_csv(risk_path) if h.get("hazard_id"))
    events = read_csv(events_path)
    scale = None
    if scale_path:
        with open(scale_path, encoding="utf-8") as fh:
            scale = [s.strip().lower() for s in json.load(fh).get("severity", [])]

    def rank(label):
        if scale is None:
            return None
        label = (label or "").strip().lower()
        return scale.index(label) if label in scale else None

    mapped = defaultdict(list)
    unmapped, unknown = [], []
    for e in events:
        ids = [x.strip() for x in (e.get("hazard_id") or "").replace(",", ";").split(";") if x.strip()]
        if not ids:
            unmapped.append(e)
            continue
        for i in ids:
            (mapped[i] if i in hazards else unknown).append(e if i in hazards else dict(e, _bad=i))

    rows = []
    for hid, h in hazards.items():
        evs = mapped.get(hid, [])
        obs = [e.get("severity_observed", "") for e in evs if e.get("severity_observed")]
        top = None
        if obs:
            if scale:
                ranked = [(rank(o), o) for o in obs if rank(o) is not None]
                top = max(ranked)[1] if ranked else obs[0]
            else:
                top = "; ".join(sorted(set(obs)))
        flag = ""
        if scale and top and rank(top) is not None and rank(h.get("severity")) is not None:
            if rank(top) > rank(h.get("severity")):
                flag = "observed above file estimate"
        elif scale and top and rank(h.get("severity")) is None:
            flag = "file severity not on the scale given"
        own = [e for e in evs if (e.get("origin") or "own").lower() != "comparable"]
        comp = [e for e in evs if (e.get("origin") or "").lower() == "comparable"]
        rows.append({
            "own_events": len(own), "comparable_events": len(comp),
            "hazard_id": hid, "hazard": h.get("hazard", ""), "file_severity": h.get("severity", ""),
            "file_probability": h.get("probability", ""), "controls": h.get("controls", ""),
            "events": len(evs), "sources": "; ".join(sorted({e.get("source", "") for e in evs})),
            "event_ids": "; ".join(e.get("event_id", "") for e in evs),
            "highest_observed": top or "", "flag": flag,
        })
    return rows, unmapped, unknown, scale


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--from-connector", nargs="+")
    ap.add_argument("--risk")
    ap.add_argument("--events")
    ap.add_argument("--scale")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.from_connector:
        from_connector(a.from_connector)
        return
    if not (a.risk and a.events):
        sys.exit("give --from-connector, or both --risk and --events")
    rows, unmapped, unknown, scale = compare(a.risk, a.events, a.scale)
    if a.json:
        print(json.dumps({"hazards": rows, "unmapped_events": unmapped, "unknown_hazard_ids": unknown}, indent=1, ensure_ascii=False))
        return
    print("Observed events against the risk file. Mapping, severity and probability are the person's; "
          "whether a control worked and whether a risk stays acceptable are the owner's decisions.\n")
    if not scale:
        print("No severity scale given: observed and file severity are listed side by side, not compared.\n")
    print("| Hazard | File severity | File probability | Controls | Own events | Comparable events | Event ids | Highest observed | Flag |")
    print("|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        print(f"| {r['hazard_id']} {r['hazard']} | {r['file_severity']} | {r['file_probability']} | {r['controls']} | "
              f"{r['own_events']} | {r['comparable_events']} | {r['event_ids']} | {r['highest_observed']} | {r['flag']} |")
    print(f"\nEvents not mapped to any hazard in the file: {len(unmapped)} (candidates for 'not foreseen'; the person decides)")
    for e in unmapped:
        print(f"- {e.get('event_id')} ({e.get('origin') or 'own'}; {e.get('source')}, {e.get('date')}): {e.get('description', '')[:160]}")
    if unknown:
        print(f"\nEvents naming a hazard id the file does not hold: {len(unknown)}")
        for e in unknown:
            print(f"- {e.get('event_id')} names {e.get('_bad')}")


if __name__ == "__main__":
    main()
