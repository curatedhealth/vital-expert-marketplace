#!/usr/bin/env python3
"""Decision table for HTA and reimbursement monitoring (DH-03.01.3.2, task A2).

Usage:
  decision_tracker.py FILE [FILE ...] [--as-of YYYY-MM-DD] [--own OWN.json] [--official]

FILE   saved library output with a "results" list (find_scheme_precedents,
       get_reimbursement_status or search_listings), as in examples/live/.
--own  the person's own submission events, a JSON list such as
       [{"body": "BfArM", "event": "bfarm_complete", "date": "2026-08-01"}].
       Events and the clock each starts (rows in references/hta-submissions-sources.md):
         bfarm_complete          decision due 3 months later, extendable by 3 (DE21)
         bfarm_incomplete_notice completion due within 3 months, else refusal (DE22)
         bfarm_decision_notified objection due within 1 month (DE24); re-application not before 12 months if refused (DE23)
         pecan_complete          CNEDiMTS opinion within 60 days (FR14)
         pecan_missing_items     items due within 30 days, else deemed abandoned (FR14)
         pecan_decision          file LPPR within 6 months or LATM within 9 months (FR14)
         latm_complete           CNEDiMTS opinion within 90 days; 70 if under PECAN (FR17)
         has_draft_opinion       10 days to comment or request a hearing (FR19)
         nice_early_use_published evidence period: key uncertainties resolvable within 3 years (UK7)
--official  print the official outcome figures with their rows and how to read them.

The script lays out facts and flags. It never infers a decision, and its counts are
counts of library rows, not a complete register.
"""
import argparse
import json
from collections import Counter, defaultdict
from datetime import date, timedelta
import calendar

CLOCKS = {
    "bfarm_complete": [("months", 3, "BfArM decision due (extendable by up to 3 more months)", "DE21")],
    "bfarm_incomplete_notice": [("months", 3, "Completion due at the latest (BfArM sets the period, up to 3 months), else refusal", "DE22")],
    "bfarm_decision_notified": [("months", 1, "Objection (Widerspruch) window closes", "DE24"),
                                ("months", 12, "Earliest re-application if refused or withdrawn (new evidence only)", "DE23")],
    "pecan_complete": [("days", 60, "CNEDiMTS PECAN opinion due", "FR14")],
    "pecan_missing_items": [("days", 30, "Missing items due, else request deemed abandoned", "FR14")],
    "pecan_decision": [("months", 6, "LPPR filing due", "FR14"), ("months", 9, "LATM filing due", "FR14"),
                       ("months", 12, "PECAN year ends (non-renewable)", "FR12")],
    "latm_complete": [("days", 90, "CNEDiMTS LATM opinion due (70 days if under PECAN)", "FR17")],
    "has_draft_opinion": [("days", 10, "Comments or hearing request due", "FR19")],
    "nice_early_use_published": [("months", 36, "End of the fixed evidence period for key uncertainties", "UK7")],
}

OFFICIAL = [
    ("BfArM, as of 9 September 2026", "254 applications since 27 May 2020: 196 trial, 58 permanent", "DE33"),
    ("BfArM, as of 9 September 2026", "Outcomes: 62 listed, 29 refused, 131 withdrawn, 14 in review, 18 delisted (7 at the manufacturer's request)", "DE34"),
    ("GKV-Spitzenverband, to 31 December 2025", "Of 60 trial listings: 34 permanent, 16 removed, 10 still on trial; trials averaged 20 months", "DE-1, DE-6"),
    ("CNEDiMTS 2025", "Reimbursement recommended for 214 products (91 percent); progress recognized for 41 (19 percent)", "FR21"),
    ("CNEDiMTS 2025", "LATM: 10 opinions on 8 dossiers, 8 favorable, 2 unfavorable", "FR22"),
    ("CNEDiMTS 2025", "PECAN: 5 requests, 1 favorable, 4 unfavorable", "FR23"),
    ("CNEDiMTS 2025", "69 percent of LPP and intra-GHS requests (204 of 297) suspended at least once for incompleteness; 51 percent (153 of 297) for administrative reasons only", "FR24"),
]
READING = [
    "Withdrawals (131) far exceed refusals (29); a refusal-only rate understates failed applications (conflict note 9).",
    "BfArM outcome categories describe current state and can overlap (a delisted DiGA was once listed); do not sum them to 254.",
    "BfArM does not name applicants or refused products (DE32). Actual review days are not published.",
    "These figures are context for the person's judgment, never their odds or targets.",
]


def add_months(d, n):
    m = d.month - 1 + n
    y = d.year + m // 12
    m = m % 12 + 1
    return date(y, m, min(d.day, calendar.monthrange(y, m)[1]))


def load_rows(paths):
    rows = []
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            data = json.load(fh)
        for r in data.get("results", []):
            r = dict(r)
            r["_file"] = p.split("/")[-1]
            rows.append(r)
    return rows


def flags_for(r, as_of, seen_nice):
    flags = []
    status = r.get("status")
    ends = r.get("ends_on")
    if ends:
        days = (date.fromisoformat(ends) - as_of).days
        if days < 0 and status in ("provisional", "conditional"):
            flags.append("stated end %s passed %d days ago; status not updated; check the authority" % (ends, -days))
        elif days >= 0:
            flags.append("stated end %s, %d days ahead" % (ends, days))
    elif status == "provisional":
        flags.append("no end date stored")
    if "National Institute for Health and Care Excellence" in (r.get("manufacturer") or ""):
        flags.append("guidance row, not a product")
        key = (r.get("listed_on"), tuple(r.get("indications") or []))
        if key in seen_nice and seen_nice[key] != r.get("scheme_identifier"):
            flags.append("same guidance as %s (renumbered); count once" % seen_nice[key])
        else:
            seen_nice.setdefault(key, r.get("scheme_identifier"))
        if "early-use" in (r.get("product") or "").lower() and status == "permanent":
            flags.append("title says early use but status is permanent; early use is conditional (UK6); check the guidance")
    return flags


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*")
    ap.add_argument("--as-of", default=date.today().isoformat())
    ap.add_argument("--own")
    ap.add_argument("--official", action="store_true")
    a = ap.parse_args()
    as_of = date.fromisoformat(a.as_of)

    if a.own:
        with open(a.own, encoding="utf-8") as fh:
            events = json.load(fh)
        print("## Our submissions: clocks as of %s\n" % as_of.isoformat())
        print("| Body | Event | Date | Clock | Due | Days from as-of | Row |")
        print("|---|---|---|---|---|---|---|")
        for e in events:
            d = date.fromisoformat(e["date"])
            for unit, n, label, row in CLOCKS.get(e["event"], [("days", 0, "unknown event: no sourced clock [GAP]", "")]):
                due = add_months(d, n) if unit == "months" else d + timedelta(days=n)
                print("| %s | %s | %s | %s | %s | %d | %s |" % (e.get("body", ""), e["event"], d.isoformat(), label, due.isoformat(), (due - as_of).days, row))
        print("\nClocks are counted from the dates supplied. A clock that has passed is a fact to check with the body, not a decision.\n")

    if a.files:
        rows = load_rows(a.files)
        seen_nice = {}
        print("## Comparable decisions in the library, as of %s\n" % as_of.isoformat())
        print("| Product | Scheme | Status | status_raw | Listed | Flags | Source, retrieved |")
        print("|---|---|---|---|---|---|---|")
        by_scheme = defaultdict(Counter)
        distinct = set()
        for r in rows:
            fl = flags_for(r, as_of, seen_nice)
            ident = (r.get("scheme"), r.get("scheme_identifier"))
            if ident in distinct:
                continue
            distinct.add(ident)
            if not any("renumbered" in f for f in fl):
                by_scheme[r.get("scheme")][r.get("status")] += 1
            print("| %s | %s | %s | %s | %s | %s | %s, %s |" % (
                r.get("product"), r.get("scheme"), r.get("status"), r.get("status_raw"), r.get("listed_on"),
                "; ".join(fl) or "", r.get("source_url"), (r.get("retrieved_at") or "")[:10]))
        print("\nRow counts by scheme and status (library rows returned, renumbered guidance counted once; not a complete register):")
        for s, c in sorted(by_scheme.items()):
            print("- %s: %s" % (s, ", ".join("%s %d" % (k, v) for k, v in sorted(c.items()))))
        print()

    if a.official:
        print("## Official outcome figures (context, never targets)\n")
        print("| Body and period | Figure | Row |")
        print("|---|---|---|")
        for b, f, r in OFFICIAL:
            print("| %s | %s | %s |" % (b, f, r))
        print()
        for line in READING:
            print("- " + line)


if __name__ == "__main__":
    main()
