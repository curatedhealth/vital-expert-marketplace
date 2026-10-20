#!/usr/bin/env python3
"""Build a decision evidence log from saved library rows and the person's decision notes.

Usage:
  python3 decision_evidence_log.py --rows rows1.json [rows2.json ...]
                                   [--notes notes.json] [--as-of 2026-10-19]
                                   [--only HTG624 HTG675 ...] [--share]

--rows   Saved output of market-access-dh.find_scheme_precedents (the tool's JSON,
         or a trimmed copy with a "results" list).
--notes  The decision text as read on the body's page, per reference: read_on, url,
         category, economic (verbatim), uncertainties, evidence_asked (list),
         stated_period_years and stated_period_source (if the guidance states its own
         period), collected (list of asked outcomes the person's records show).
--share  Print collected / asked per decision. Use only when the person has chosen
         that formula; it is their score, not the body's.

What the script does that the library does not:
  * merges renumbered NICE guidance (HTE8 -> HTG675) using the row's own passage;
  * flags early-use titles stored with a status other than conditional;
  * reads "Last updated" dates from the stored passage;
  * counts evidence windows: the guidance's stated period if the notes give one,
    else the PMG48 default of 3 years from publication (HE-072), labeled as such;
  * tallies evidence asks and, if the person supplies them, outcomes collected.
A decision with no notes prints "[GAP] decision text not read".
"""
import argparse
import datetime as dt
import json
import re
import sys

MOVED = re.compile(r"moved health technology evaluation (\d+) to become HealthTech guidance (\d+)", re.I)
UPDATED = re.compile(r"Last updated: (\d{1,2} \w+ \d{4})")
EARLY = re.compile(r"early value assessment|early-use", re.I)


def load_rows(paths):
    rows = []
    for p in paths:
        d = json.load(open(p))
        rows.extend(d.get("results", d if isinstance(d, list) else []))
    return rows


def add_years(d, years):
    try:
        return d.replace(year=d.year + years)
    except ValueError:  # 29 February
        return d.replace(year=d.year + years, day=28)


def fmt(d):
    return f"{d.day} {d.strftime('%B %Y')}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rows", nargs="+", required=True)
    ap.add_argument("--notes")
    ap.add_argument("--as-of", default="2026-10-19")
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--share", action="store_true")
    a = ap.parse_args()
    as_of = dt.date.fromisoformat(a.as_of)
    notes = json.load(open(a.notes)) if a.notes else {}

    rows = load_rows(a.rows)
    alias = {}
    for r in rows:
        m = MOVED.search(r.get("evidence_passage") or "")
        if m:
            alias[f"HTE{m.group(1)}"] = f"HTG{m.group(2)}"
    merged, seen = [], set()
    for r in rows:
        ref = r.get("scheme_identifier") or r.get("decision_reference")
        canon = alias.get(ref, ref)
        if canon in seen:
            continue
        seen.add(canon)
        r = dict(r)
        r["_ref"] = canon
        r["_aliases"] = sorted(k for k, v in alias.items() if v == canon)
        merged.append(r)
    if a.only:
        merged = [r for r in merged if r["_ref"] in a.only]

    print(f"Decision evidence log as of {fmt(as_of)}. Rows: {len(rows)} stored, {len(merged)} after merging renumbered guidance"
          f"{' and filtering' if a.only else ''}.")
    if alias:
        print("Merged: " + "; ".join(f"{k} is {v}" for k, v in sorted(alias.items())) + " (the stored passage says the guidance has not changed).")
    print("\n| Ref | Title | Scheme, stored status | Published | Last updated (passage) | Flags | Retrieved |")
    print("|---|---|---|---|---|---|---|")
    for r in merged:
        flags = []
        title = r.get("product", "")
        if EARLY.search(title) and r.get("status") != "conditional":
            flags.append(f"early-use title stored as {r.get('status')}; check the guidance (HE-071)")
        if r["_aliases"]:
            flags.append("also stored as " + ", ".join(r["_aliases"]))
        m = UPDATED.search(r.get("evidence_passage") or "")
        lu = m.group(1) if m else "not in passage"
        ret = (r.get("retrieved_at") or "")[:10]
        print(f"| {r['_ref']} | {title} | {r.get('scheme')}, {r.get('status')} ({r.get('status_raw')}) | {r.get('listed_on')} | {lu} | {'; '.join(flags) or 'none'} | {ret} |")

    print("\n## What each decision said about the evidence")
    for r in merged:
        ref = r["_ref"]
        n = notes.get(ref)
        print(f"\n### {ref}")
        if not n:
            print("[GAP] decision text not read; the library holds the page header only. Read " + (r.get("source_url") or "the guidance page") + ".")
            continue
        print(f"Read {n.get('read_on', '[GAP] read date')} at {n.get('url', r.get('source_url'))}")
        print(f"- Category: {n.get('category', '[GAP]')}")
        if n.get("economic"):
            print(f"- Economic evidence (verbatim): \"{n['economic']}\"")
        for u in n.get("uncertainties", []):
            print(f"- Uncertainty or limitation (verbatim): \"{u}\"")
        asked = n.get("evidence_asked", [])
        if asked:
            print(f"- Evidence asked ({len(asked)} item{"s" if len(asked) != 1 else ""}): " + "; ".join(asked))
        early = bool(EARLY.search(r.get("product", ""))) or r.get("status") == "conditional"
        if early:
            pub = dt.date.fromisoformat(r["listed_on"])
            if n.get("stated_period_years"):
                yrs, src = n["stated_period_years"], n.get("stated_period_source", "the guidance")
                label = f"stated period {yrs} years ({src})"
            else:
                yrs, label = 3, "PMG48 default of 3 years from publication (HE-072); the guidance may state its own"
            end = add_years(pub, int(yrs))
            days = (end - as_of).days
            state = f"{days} days remaining" if days >= 0 else f"passed {-days} days ago"
            print(f"- Evidence window: {label}; counted from publication, {fmt(pub)}, to {fmt(end)}; as of {fmt(as_of)}, {state}. A window is a fact to check, not a lapse.")
        if a.share and asked:
            col = [x for x in n.get("collected", []) if x in asked]
            print(f"- Person's formula, collected / asked: {len(col)} / {len(asked)} = {len(col) / len(asked):.0%} (the person's score, not the body's)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
