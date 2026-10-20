#!/usr/bin/env python3
"""Reporting clock: the latest permitted report date for a complaint or event, per jurisdiction.

Every rule below carries the research row it came from (references/quality-systems-sources.md
and references/primary-text-additions.md). The script computes dates; it never decides whether
an event is reportable. That decision belongs to the person's reporting owner.

Event types
  EU  (MDR Article 87, calendar days, awareness day = day 0, MDCG 2023-3 Rev.2; rows VG4 to VG8, VG12)
    eu-serious-incident        15 days
    eu-death-or-unanticipated  10 days (death or unanticipated serious deterioration)
    eu-public-health-threat     2 days (serious public health threat)
    eu-fsca                     before the field safety corrective action is undertaken (no day count)
  GB  (UK MDR 2002 regulation 44ZH as inserted by SI 2024/1368, in force 16 June 2025; rows VG26 to VG28)
    gb-serious-incident        15 days
    gb-death-or-unanticipated  10 days
    gb-public-health-threat     2 days
    GB day counting and the GB awareness definition are not in the sourced rows [GAP]. The script
    applies the MDCG calendar-day convention as a proposed reading and says so.
  US
    us-mdr-30                  30 calendar days after the day of awareness (21 CFR 803.50; VG17)
    us-mdr-5                    5 work days after the day of awareness (21 CFR 803.53; VG18);
                                work day = Monday to Friday except Federal holidays (803.3; R9)
                                anchor is the date a manager or supervisor with regulatory, scientific or technical oversight became aware that remedial action is needed (803.3; VG19), which may be later than first receipt; rerun with that date.
    us-806-correction          10 working days from initiating the correction or removal (21 CFR 806.10; VG22);
                                anchor is the initiation date, not the awareness date. Part 806 does not define
                                "working day" in the rows read [GAP]; the 803.3 work-day rule is applied as a
                                proposed reading.

Federal holidays are always excluded from work-day counts (803.3: "Work day means Monday through Friday,
except Federal holidays."; R9). By default the script reads scripts/us_federal_holidays.txt, the OPM list for
2026 and 2027 (R14). Pass --holidays to use another file (one YYYY-MM-DD per line; text after # is ignored).
If a work-day window runs outside the years the file covers, or the file is missing, the script prints a
warning: the due date shown may then be earlier than the true one. The output names each holiday excluded.

Usage
  python3 reporting_clock.py --date 2026-10-12 --event eu-serious-incident gb-serious-incident us-mdr-30
  python3 reporting_clock.py --date 2026-10-12 --event all-for-incident [--reportability-date 2026-10-16]
  python3 reporting_clock.py --date 2026-10-14 --event us-806-correction --holidays us_holidays.txt
  add --as-of 2026-10-19 to show days remaining; add --json for machine-readable output
"""
import argparse
import datetime as dt
import json
import os
import sys

DEFAULT_HOLIDAYS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "us_federal_holidays.txt")

RULES = {
    "eu-serious-incident": ("EU", "calendar", 15, "awareness",
        "MDR Art. 87(3): immediately once a causal relationship is established or reasonably possible, and not later than 15 days after awareness (VG4)"),
    "eu-death-or-unanticipated": ("EU", "calendar", 10, "awareness",
        "MDR Art. 87(5): death or unanticipated serious deterioration, immediately and not later than 10 days after awareness (VG6)"),
    "eu-public-health-threat": ("EU", "calendar", 2, "awareness",
        "MDR Art. 87(4): serious public health threat, immediately and not later than 2 days after awareness (VG5)"),
    "eu-fsca": ("EU", "none", None, "planned FSCA start",
        "MDR Art. 87(8): report the FSCA in advance of it being undertaken, except in urgency (VG8)"),
    "gb-serious-incident": ("GB", "calendar-proposed", 15, "awareness",
        "UK MDR 2002 reg. 44ZH: not later than 15 days after awareness (VG28)"),
    "gb-death-or-unanticipated": ("GB", "calendar-proposed", 10, "awareness",
        "UK MDR 2002 reg. 44ZH: death or unanticipated serious deterioration, not later than 10 days (VG28)"),
    "gb-public-health-threat": ("GB", "calendar-proposed", 2, "awareness",
        "UK MDR 2002 reg. 44ZH: serious public health threat, not later than 2 days (VG28)"),
    "us-mdr-30": ("US", "calendar", 30, "awareness",
        "21 CFR 803.50(a): no later than 30 calendar days after the day of awareness (VG17)"),
    "us-mdr-5": ("US", "workday", 5, "management awareness that remedial action is needed (803.3; may be later than first receipt)",
        "21 CFR 803.53: no later than 5 work days after the day of awareness, for events needing remedial action or on FDA's written request (VG18, R9)"),
    "us-806-correction": ("US", "workday-proposed", 10, "initiation of the correction or removal",
        "21 CFR 806.10(b): within 10 working days of initiating the correction or removal (VG22)"),
}

GROUPS = {
    "all-for-incident": ["eu-serious-incident", "eu-death-or-unanticipated", "eu-public-health-threat",
                         "gb-serious-incident", "gb-death-or-unanticipated", "gb-public-health-threat",
                         "us-mdr-30", "us-mdr-5"],
}

NOTES = {
    "calendar": None,
    "calendar-proposed": "GB counting convention and awareness definition not in the sourced rows [GAP]; MDCG calendar-day convention applied as a proposed reading",
    "workday": "Federal holidays {h}",
    "workday-proposed": "Part 806 does not define 'working day' in the rows read [GAP]; 803.3 work-day rule applied as a proposed reading. Federal holidays {h}",
    "none": "No day count in the sourced row",
}


def parse_date(s):
    return dt.date.fromisoformat(s)


def load_holidays(path):
    """Return (dates {date: label}, years covered). Text after # is a label or comment."""
    dates = {}
    with open(path) as fh:
        for line in fh:
            body, _, label = line.partition("#")
            body = body.strip()
            if body:
                dates[parse_date(body)] = label.strip() or "Federal holiday"
    return dates, {d.year for d in dates}


def add_workdays(start, n, holidays):
    d, counted, skipped = start, 0, []
    while counted < n:
        d += dt.timedelta(days=1)
        if d.weekday() >= 5:
            continue
        if d in holidays:
            skipped.append(d)
            continue
        counted += 1
    return d, skipped


def compute(event, anchor, holidays, hol_source, hol_years):
    juris, mode, n, anchor_name, rule = RULES[event]
    skipped, uncovered = [], False
    if mode == "none":
        due = None
    elif mode.startswith("calendar"):
        due = anchor + dt.timedelta(days=n)  # day 0 = anchor, day 1 = next day (VG12)
    else:
        due, skipped = add_workdays(anchor, n, holidays)
        uncovered = any(y not in hol_years for y in range(anchor.year, due.year + 1))
    note = NOTES[mode]
    if note and "{h}" in note:
        if not hol_source:
            h = "NOT excluded (holiday file missing): the true due date may be later by the number of holidays in the window"
        else:
            h = "excluded (%s)" % hol_source
            h += ("; excluded in this window: %s" % ", ".join("%s %s" % (d.isoformat(), holidays[d]) for d in skipped)
                  if skipped else "; none fell in this window")
            if uncovered:
                h += ("; WARNING: the window runs outside the years the holiday file covers (%s), so holidays in "
                      "other years were not excluded and the true due date may be later" % ", ".join(str(y) for y in sorted(hol_years)))
        note = note.format(h=h)
    return {"event": event, "jurisdiction": juris, "anchor": anchor_name, "anchor_date": anchor.isoformat(),
            "count": n, "unit": mode, "due": due.isoformat() if due else None, "rule": rule, "note": note,
            "holidays_excluded": [d.isoformat() for d in skipped], "holiday_coverage_warning": uncovered}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--date", required=True, help="Anchor date YYYY-MM-DD: awareness date, or initiation date for us-806-correction")
    p.add_argument("--event", nargs="+", required=True, help="Event types, or all-for-incident")
    p.add_argument("--reportability-date", help="EU/GB: date the information arrived that made the incident reportable, if later than awareness")
    p.add_argument("--holidays", help="File of Federal holidays, one YYYY-MM-DD per line (default: scripts/us_federal_holidays.txt, OPM 2026 and 2027)")
    p.add_argument("--as-of", help="Show days remaining as of this date")
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)

    events = []
    for e in a.event:
        events.extend(GROUPS.get(e, [e]))
    unknown = [e for e in events if e not in RULES]
    if unknown:
        p.error("unknown event type(s): %s. Known: %s" % (", ".join(unknown), ", ".join(list(RULES) + list(GROUPS))))

    hol_path = a.holidays or DEFAULT_HOLIDAYS
    holidays, hol_years, hol_source = {}, set(), None
    if os.path.exists(hol_path):
        holidays, hol_years = load_holidays(hol_path)
        hol_source = ("file given: %s" % a.holidays) if a.holidays else "OPM Federal holiday list for %s, R14" % (
            " and ".join(str(y) for y in sorted(hol_years)))
    elif a.holidays:
        p.error("holiday file not found: %s" % a.holidays)
    else:
        print("WARNING: default holiday file %s not found; Federal holidays are NOT excluded from work-day counts "
              "(803.3 requires it). Pass --holidays." % DEFAULT_HOLIDAYS, file=sys.stderr)

    anchor = parse_date(a.date)
    rows = [compute(e, anchor, holidays, hol_source, hol_years) for e in events]

    if a.reportability_date:
        rd = parse_date(a.reportability_date)
        for r in rows:
            if r["jurisdiction"] in ("EU", "GB") and r["due"]:
                alt = compute(r["event"], rd, holidays, hol_source, hol_years)
                r["due_if_counted_from_reportability_date"] = alt["due"]
                r["reportability_note"] = ("MDCG 2023-3 Rev.2 asks the report to give both the incident awareness date and the "
                                           "reportability awareness date and explain the difference (VG13); which date starts the "
                                           "clock is not stated in the sourced rows [GAP]. The earlier due date is the safe reading; "
                                           "the reporting owner decides.")

    if a.as_of:
        asof = parse_date(a.as_of)
        for r in rows:
            if r["due"]:
                r["days_remaining"] = (parse_date(r["due"]) - asof).days

    if a.json:
        json.dump(rows, sys.stdout, indent=2)
        print()
        return 0

    print("Anchor date: %s. Latest permitted report dates (the rules also say 'immediately' where shown)." % anchor.isoformat())
    print()
    hdr = ["Event type", "Juris.", "Clock", "Counted from", "Due by"]
    if a.as_of:
        hdr.append("Days left as of %s" % a.as_of)
    print("| " + " | ".join(hdr) + " |")
    print("|" + "---|" * len(hdr))
    for r in rows:
        clock = "%s %s" % (r["count"], "calendar days" if r["unit"].startswith("calendar") else "work days") if r["count"] else "in advance"
        cells = [r["event"], r["jurisdiction"], clock, r["anchor"], r["due"] or "before the FSCA starts"]
        if a.as_of:
            dr = r.get("days_remaining")
            cells.append("" if dr is None else (str(dr) if dr >= 0 else "%d (date passed)" % dr))
        print("| " + " | ".join(cells) + " |")
    print()
    for r in rows:
        print("- %s: %s." % (r["event"], r["rule"]) + (" Note: %s." % r["note"] if r["note"] else ""))
        if "due_if_counted_from_reportability_date" in r:
            print("  If counted from the reportability date: %s. %s" % (r["due_if_counted_from_reportability_date"], r["reportability_note"]))
    if "us-806-correction" in events and len(events) > 1:
        print("- Warning: us-806-correction counts from the initiation of the correction or removal. This run used the same --date for every event; rerun it with the initiation date if that differs from the awareness date.")
    if "us-mdr-5" in events and len(events) > 1:
        print("- Warning: us-mdr-5 counts from management awareness that remedial action is needed (803.3), which may be later than the awareness date used for the other rows. Rerun it with that date before calling it passed.")
    if any(r.get("holiday_coverage_warning") for r in rows) or (not hol_source and any(r["unit"].startswith("workday") for r in rows)):
        print("- Warning: Federal holidays were not fully excluded for at least one work-day row (see its note). Supply a holiday file covering the window before relying on that date.")
    print()
    print("These dates are computed limits, not a reportability decision. The reporting owner decides whether and where to report.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
