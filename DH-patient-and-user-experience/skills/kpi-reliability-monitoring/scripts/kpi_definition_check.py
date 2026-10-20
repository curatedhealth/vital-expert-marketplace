#!/usr/bin/env python3
"""KPI definition quality, formula drift and event-data missingness checks.

Nothing is sent anywhere. The checks say whether a KPI card is complete and computable;
they never judge whether a KPI value is good. Thresholds are the person's.

Card format (JSON, {"kpis": [card, ...]}), the same as engagement_kpis.py reads:
  id, name, decision, grain, source, missing_data_rule, definition_source (text)
  period: {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"} or {"window_days": N, "anchor": "..."}
  numerator: {"event": "...", "min_count": N, "within_days_of_start": N}
  denominator: {"population": "eligible" | "enrolled" | "enrolled_in_period" |
                "enrolled_before_period" | free text, "start_event": "...",
                "min_days_observed": N}
  optional: attrition_type ("dropout" or "nonusage"), stopped_rule (text),
            instrument (for example "PAM-13"), measurement_properties (text naming the
            evidence), threshold: {"value": ..., "set_by": "..."}

Subcommands
  cards    python3 kpi_definition_check.py cards kpis.json [--json out.json]
           One line per check per card: pass, fail or check, with the rule's source.
  drift    python3 kpi_definition_check.py drift cards.json dashboard.json
           Compares each KPI card with the definition the dashboard actually uses
           (same format). Reports match, drift (field by field) and renamed KPIs.
  missing  python3 kpi_definition_check.py missing events.csv --as-of YYYY-MM-DD
                   [--start-event enrolled]
           Missing and inconsistent event data: blanks, invalid dates, duplicates,
           events after the as-of date, events before a person's start event, people
           with events but no start event, and event counts per month (a month with no
           events can mean a feed outage, not a behavior change).

Rule sources (row ids from the copied research files in references/):
  REG   the register method for KPI definition (decision, formula, grain, source table)
  CS27  RE-AIM: reach on a valid denominator, not volunteers who indicate interest
  CS39  Proctor: penetration = eligible persons who use / all eligible
  CS-CC research "Changes and conflicts": pick one definition per metric and name it
  PE-21 FDA: avoid missing data; collect reasons for missing data
  PE-102 Eysenbach: dropout attrition and nonusage attrition are different things
  PE-104 effective engagement: enough engagement to achieve intended outcomes
  PE-93 to PE-96 COSMIN measurement properties and criteria for an instrument
"""
import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date

ATTRITION_WORDS = re.compile(r"retention|retain|attrition|churn|dropout|drop-out|stopped|persist", re.I)
REACH_WORDS = re.compile(r"\breach\b|penetration|uptake", re.I)
VOLUNTEER_WORDS = re.compile(r"interest|signed up|sign-up|download|volunteer|registered on the app|opt-in", re.I)


def pd(s):
    try:
        return date.fromisoformat((s or "").strip())
    except ValueError:
        return None


def load_cards(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh).get("kpis", [])


def check_card(c):
    out = []

    def add(check, status, note, rule):
        out.append({"kpi": c.get("id", "?"), "check": check, "status": status, "note": note, "rule": rule})

    num, den, per = c.get("numerator") or {}, c.get("denominator") or {}, c.get("period") or {}
    add("Decision named", "pass" if c.get("decision") else "fail",
        c.get("decision") or "no decision named", "REG")
    add("Numerator stated", "pass" if num.get("event") or num.get("formula") else "fail",
        num.get("event") or num.get("formula") or "no numerator", "REG")
    pop = den.get("population") or den.get("formula")
    add("Denominator stated", "pass" if pop else "fail", pop or "no denominator: a count is not a rate", "REG, CS27")
    if pop:
        text = " ".join(str(v) for v in den.values())
        if VOLUNTEER_WORDS.search(text):
            add("Denominator valid", "check",
                "denominator reads as people who showed interest or signed up; RE-AIM reach uses all eligible people",
                "CS27")
        elif REACH_WORDS.search(c.get("name", "")) and pop != "eligible":
            add("Denominator valid", "check",
                f"a reach or penetration KPI on population '{pop}'; the published formulas divide by all eligible people",
                "CS27, CS39")
        elif pop in ("enrolled", "enrolled_in_period", "enrolled_before_period") and not den.get("start_event"):
            add("Denominator valid", "fail", "enrollment population without the event that marks enrollment", "REG")
        else:
            add("Denominator valid", "pass", pop, "CS27")
    ps, pe = pd(per.get("start")), pd(per.get("end"))
    if ps and pe:
        add("Period stated", "pass" if ps <= pe else "fail",
            f"{ps.isoformat()} to {pe.isoformat()}" if ps <= pe else "period end before start", "REG")
    elif per.get("window_days"):
        add("Period stated", "pass", f"rolling {per['window_days']} days, anchor {per.get('anchor') or 'not stated'}", "REG")
    else:
        add("Period stated", "fail", "no period: the value cannot be recomputed", "REG")
    add("Grain stated", "pass" if c.get("grain") else "fail", c.get("grain") or "no grain", "REG")
    add("Source table stated", "pass" if c.get("source") else "fail", c.get("source") or "no source table", "REG")
    add("Missing-data rule stated", "pass" if c.get("missing_data_rule") else "fail",
        c.get("missing_data_rule") or "not stated: blanks may be counted as zero, excluded or imputed without anyone knowing",
        "PE-21")
    add("Definition source named", "pass" if c.get("definition_source") else "check",
        c.get("definition_source") or "no framework named; adoption, reach and penetration carry different published definitions",
        "CS-CC")
    if num.get("within_days_of_start") is not None:
        mdo = den.get("min_days_observed")
        ok = mdo is not None and int(mdo) >= int(num["within_days_of_start"])
        add("Window matches denominator", "pass" if ok else "check",
            "denominator keeps only people observed for the full window" if ok else
            f"numerator window {num['within_days_of_start']} days but the denominator includes people observed for less",
            "CS27 (valid denominator), PE-104")
    if ATTRITION_WORDS.search(c.get("name", "")):
        at = c.get("attrition_type")
        add("Attrition type named", "pass" if at in ("dropout", "nonusage") else "check",
            at or "dropout (lost to follow-up) and nonusage (stopped using) are different measures", "PE-102")
        add("Stopped rule stated", "pass" if c.get("stopped_rule") else "check",
            c.get("stopped_rule") or "how many days without use mean 'stopped' is not stated", "PE-101 to PE-103")
    if c.get("instrument"):
        add("Instrument measurement properties", "pass" if c.get("measurement_properties") else "check",
            c.get("measurement_properties") or f"{c['instrument']}: no evidence named for reliability, validity or measurement error",
            "PE-93 to PE-96")
    thr = c.get("threshold")
    if thr:
        add("Threshold owner named", "pass" if thr.get("set_by") else "check",
            thr.get("set_by") or "owner not named", "people decide")
    return out


def cmd_cards(args):
    cards = load_cards(args.file)
    allres = []
    for c in cards:
        res = check_card(c)
        allres += res
        n = Counter(r["status"] for r in res)
        print(f"\nKPI {c.get('id', '?')}: {c.get('name', '')}  (pass {n['pass']}, fail {n['fail']}, check {n['check']})")
        for r in res:
            if r["status"] != "pass" or args.all:
                print(f"  {r['status'].upper():5} {r['check']}: {r['note']} [{r['rule']}]")
    tot = Counter(r["status"] for r in allres)
    print(f"\nCards: {len(cards)}. Checks: pass {tot['pass']}, fail {tot['fail']}, check {tot['check']}.")
    print("A fail means the card cannot be recomputed as written. A check needs the person's reading. Neither is a verdict on the KPI value.")
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(allres, fh, indent=2)


FIELDS = ("numerator", "denominator", "period", "grain", "source", "missing_data_rule")


def norm(v):
    return json.dumps(v, sort_keys=True) if isinstance(v, (dict, list)) else str(v or "").strip().lower()


def cmd_drift(args):
    cards = {c.get("id"): c for c in load_cards(args.cards)}
    dash = {c.get("id"): c for c in load_cards(args.dashboard)}
    formula = lambda c: (norm(c.get("numerator")), norm(c.get("denominator")), norm(c.get("period")))
    for cid, card in cards.items():
        d = dash.get(cid)
        if d is None:
            same = [k for k, v in dash.items() if formula(v) == formula(card)]
            if same:
                print(f"{cid}: not on the dashboard under this id; dashboard KPI {', '.join(same)} has the same formula under "
                      f"the name '{dash[same[0]].get('name', '')}'. Renamed: confirm with the card owner before treating them as one.")
            else:
                print(f"{cid}: on the card list, not on the dashboard.")
            continue
        diffs = [f for f in FIELDS if norm(card.get(f)) != norm(d.get(f))]
        renamed = norm(card.get("name")) != norm(d.get("name"))
        if not diffs and not renamed:
            print(f"{cid}: match.")
            continue
        if not diffs:
            print(f"{cid}: same formula, name differs (card '{card.get('name')}', dashboard '{d.get('name')}').")
            continue
        print(f"{cid}: DRIFT in {', '.join(diffs)}{' (and renamed)' if renamed else ''}.")
        for f in diffs:
            print(f"    {f}: card {json.dumps(card.get(f))} | dashboard {json.dumps(d.get(f))}")
        if "grain" in diffs:
            print("    The grain differs: the two numbers count different units and cannot be compared directly.")
    for cid in dash:
        if cid not in cards:
            print(f"{cid}: on the dashboard with no KPI card ('{dash[cid].get('name', '')}'). No card, no agreed definition.")


def cmd_missing(args):
    as_of = date.fromisoformat(args.as_of)
    blanks, invalid, after, seen, dups = Counter(), 0, 0, set(), 0
    rows = []
    with open(args.file, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        for raw in reader:
            r = {k.strip(): (v or "").strip() for k, v in raw.items() if k}
            for col in ("user_id", "event_date", "event_type"):
                if not r.get(col):
                    blanks[col] += 1
            d = pd(r.get("event_date")) if r.get("event_date") else None
            if r.get("event_date") and d is None:
                invalid += 1
            key = (r.get("user_id"), r.get("event_date"), r.get("event_type"))
            if key in seen:
                dups += 1
            seen.add(key)
            if d and d > as_of:
                after += 1
            if d and r.get("user_id") and r.get("event_type"):
                rows.append((r["user_id"], d, r["event_type"]))
    total = len(seen) + dups
    print(f"Rows: {total}. As of {as_of.isoformat()}.")
    for col in ("user_id", "event_date", "event_type"):
        print(f"  Blank {col}: {blanks[col]}")
    print(f"  Invalid dates: {invalid}")
    print(f"  Exact duplicate rows (same person, date, event): {dups}")
    print(f"  Events dated after the as-of date: {after}")
    if args.start_event:
        starts = {}
        for u, d, t in rows:
            if t == args.start_event and (u not in starts or d < starts[u]):
                starts[u] = d
        before = sum(1 for u, d, t in rows if u in starts and d < starts[u])
        orphans = {u for u, _, _ in rows} - set(starts)
        print(f"  Events before the person's '{args.start_event}' event: {before}")
        print(f"  People with events but no '{args.start_event}' event: {len(orphans)}")
    types = Counter(t for _, _, t in rows)
    print("Event types: " + "; ".join(f"{t} {n}" for t, n in sorted(types.items())))
    months = Counter(d.strftime("%Y-%m") for _, d, _ in rows if d <= as_of)
    if months:
        first, last = min(months), max(months)
        y, m = map(int, first.split("-"))
        print("Events per month (a month with 0 may be a feed outage, not behavior):")
        while f"{y:04d}-{m:02d}" <= last:
            k = f"{y:04d}-{m:02d}"
            print(f"  {k}: {months.get(k, 0)}")
            m += 1
            if m == 13:
                y, m = y + 1, 1
    print("Missing data is reported, never imputed. Reasons for missing data come from the person (PE-21).")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("cards")
    c.add_argument("file")
    c.add_argument("--json")
    c.add_argument("--all", action="store_true", help="print passing checks too")
    d = sub.add_parser("drift")
    d.add_argument("cards")
    d.add_argument("dashboard")
    m = sub.add_parser("missing")
    m.add_argument("file")
    m.add_argument("--as-of", required=True)
    m.add_argument("--start-event")
    args = ap.parse_args()
    {"cards": cmd_cards, "drift": cmd_drift, "missing": cmd_missing}[args.cmd](args)


if __name__ == "__main__":
    main()
