#!/usr/bin/env python3
"""Complaint log analysis: recurrence after CAPA closure, ageing, and reporting timeliness.

Inputs (the person's own records; nothing here goes to the library)
  complaints.csv  one row per complaint and jurisdiction assessed. Columns:
      complaint_id, received_date, awareness_date, product, version, complaint_code,
      jurisdiction (EU, GB or US; blank if no reportability assessment),
      event_type (a clock id below, or blank), reportability_decision
      (reportable, not_reportable, undecided, or blank), decision_date, submitted_date, closed_date
  capas.csv       optional. One row per CAPA. Columns:
      capa_id, complaint_code, closed_date, window_days (the person's effectiveness window), owner
  rules.json      optional. The person's own thresholds, for example
      {"ageing_days": 30, "ageing_owner": "Complaint unit lead"}
      No threshold is assumed when none is given.

Dates are YYYY-MM-DD. Blank means not recorded.

Clock ids and limits (references/vigilance-clocks.md; rows VG4 to VG6, VG12, VG17, VG18, VG22, VG28, R9):
  eu-serious-incident 15, eu-death-or-unanticipated 10, eu-public-health-threat 2 (calendar days, awareness = day 0)
  gb-serious-incident 15, gb-death-or-unanticipated 10, gb-public-health-threat 2 (GB counting [GAP]; calendar days applied as proposed)
  us-mdr-30 30 calendar days; us-mdr-5 5 work days, Monday to Friday except Federal holidays (803.3; R9).
      For us-mdr-5 rows, awareness_date must be the date a manager or supervisor with regulatory, scientific or
      technical oversight became aware that remedial action is needed (803.3; VG19), which may be later than
      first receipt. Do not treat a us-mdr-5 date as passed unless that date is the one recorded.
  Federal holidays are always excluded from work-day counts: by default from scripts/us_federal_holidays.txt
  (OPM list for 2026 and 2027, R14), or from --holidays (one YYYY-MM-DD per line; text after # is ignored).
  If a work-day window runs outside the file's years, or the file is missing, the output warns that the due
  date may be later.
  us-806-correction 10 working days from initiation: put the initiation date in awareness_date for that row.

Output: four sections in Markdown (or --json). The script counts and dates; it never says a CAPA
is effective, never sets a threshold and never decides reportability.

Usage: python3 complaint_trends.py complaints.csv [--capas capas.csv] [--rules rules.json]
                                    [--as-of YYYY-MM-DD] [--holidays file] [--json]
"""
import argparse
import csv
import datetime as dt
import json
import os
import sys
from collections import Counter, defaultdict

DEFAULT_HOLIDAYS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "us_federal_holidays.txt")

CLOCKS = {
    "eu-serious-incident": ("calendar", 15), "eu-death-or-unanticipated": ("calendar", 10),
    "eu-public-health-threat": ("calendar", 2), "gb-serious-incident": ("calendar", 15),
    "gb-death-or-unanticipated": ("calendar", 10), "gb-public-health-threat": ("calendar", 2),
    "us-mdr-30": ("calendar", 30), "us-mdr-5": ("workday", 5), "us-806-correction": ("workday", 10),
}


def d(s):
    s = (s or "").strip()
    return dt.date.fromisoformat(s) if s else None


def load_holidays(path):
    out = {}
    with open(path) as fh:
        for line in fh:
            body, _, label = line.partition("#")
            if body.strip():
                out[d(body)] = label.strip() or "Federal holiday"
    return out


def due_date(event, anchor, holidays):
    """Return (due date, holidays skipped in the window)."""
    mode, n = CLOCKS[event]
    if mode == "calendar":
        return anchor + dt.timedelta(days=n), []
    x, c, skipped = anchor, 0, []
    while c < n:
        x += dt.timedelta(days=1)
        if x.weekday() >= 5:
            continue
        if x in holidays:
            skipped.append(x)
            continue
        c += 1
    return x, skipped


def read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        return [{k.strip(): (v or "").strip() for k, v in row.items()} for row in csv.DictReader(fh)]


def recurrence(complaints, capas):
    out = []
    for c in capas:
        closed = d(c.get("closed_date"))
        code = c.get("complaint_code", "")
        win = c.get("window_days", "")
        win_n = int(win) if win.isdigit() else None
        if not closed:
            out.append({"capa_id": c["capa_id"], "complaint_code": code, "closed_date": None,
                        "status": "CAPA not closed; no recurrence check", "after_closure": [], "owner": c.get("owner") or "owner not named"})
            continue
        seen = set()
        after = []
        for r in complaints:
            rd = d(r.get("received_date"))
            if r.get("complaint_code") != code or not rd or rd <= closed or r["complaint_id"] in seen:
                continue
            if win_n is not None and (rd - closed).days > win_n:
                continue
            seen.add(r["complaint_id"])
            after.append({"complaint_id": r["complaint_id"], "received": rd.isoformat(),
                          "days_after_closure": (rd - closed).days, "version": r.get("version") or "[GAP]"})
        window_txt = ("within the %d-day window you set" % win_n) if win_n is not None else "no window set: all later complaints counted"
        out.append({"capa_id": c["capa_id"], "complaint_code": code, "closed_date": closed.isoformat(),
                    "window": window_txt, "recurrences": len(after), "after_closure": after,
                    "owner": c.get("owner") or "owner not named"})
    return out


def ageing(complaints, as_of, rules):
    seen, rows = set(), []
    limit = rules.get("ageing_days")
    for r in complaints:
        if r["complaint_id"] in seen:
            continue
        seen.add(r["complaint_id"])
        if d(r.get("closed_date")):
            continue
        rd = d(r.get("received_date"))
        days = (as_of - rd).days if rd else None
        flag = ""
        if limit is not None and days is not None:
            flag = "over your %d-day limit" % limit if days > limit else "within your limit"
        rows.append({"complaint_id": r["complaint_id"], "received": rd.isoformat() if rd else "[GAP]",
                     "days_open": days, "complaint_code": r.get("complaint_code"), "flag": flag or "no limit set"})
    rows.sort(key=lambda x: -(x["days_open"] or 0))
    return rows


def timeliness(complaints, as_of, holidays, hol_years):
    rows = []
    for r in complaints:
        ev = r.get("event_type", "")
        if not ev:
            continue
        aw = d(r.get("awareness_date"))
        row = {"complaint_id": r["complaint_id"], "jurisdiction": r.get("jurisdiction") or "[GAP]", "event_type": ev,
               "awareness": aw.isoformat() if aw else "[GAP]", "decision": r.get("reportability_decision") or "[GAP]"}
        if ev not in CLOCKS:
            row.update(due=None, status="unknown event type: %s" % ev)
            rows.append(row)
            continue
        if not aw:
            row.update(due=None, status="no awareness date recorded: clock cannot be computed")
            rows.append(row)
            continue
        due, skipped = due_date(ev, aw, holidays)
        if CLOCKS[ev][0] == "workday":
            row["holidays_excluded"] = ["%s %s" % (h.isoformat(), holidays[h]) for h in skipped]
            row["holiday_coverage_warning"] = any(y not in hol_years for y in range(aw.year, due.year + 1))
        sub, dec_date = d(r.get("submitted_date")), d(r.get("decision_date"))
        decision = (r.get("reportability_decision") or "").lower()
        if sub:
            status = "submitted on time" if sub <= due else "submitted %d days after the due date" % (sub - due).days
        elif decision == "reportable":
            status = "decided reportable, not submitted; due date passed" if as_of > due else "decided reportable, not yet submitted; due date not passed"
        elif decision == "not_reportable":
            status = "decided not reportable"
            if dec_date and dec_date > due:
                status += " on %s, after the due date for this event type; record that the date was missed" % dec_date.isoformat()
            elif not dec_date:
                status += "; decision date not recorded [GAP]"
        else:
            status = "undecided; due date passed" if as_of > due else "undecided; due date not passed"
        if ev == "us-mdr-5":
            status += " (counted from the awareness_date given; valid only if it is the management awareness date, 803.3)"
        if row.get("holidays_excluded"):
            status += "; holidays excluded: " + ", ".join(row["holidays_excluded"])
        if row.get("holiday_coverage_warning"):
            status += "; WARNING: window outside the holiday file's years, due date may be later"
        row.update(due=due.isoformat(), submitted=sub.isoformat() if sub else None, status=status)
        rows.append(row)
    return rows


def code_counts(complaints):
    seen, cnt = set(), Counter()
    for r in complaints:
        if r["complaint_id"] in seen:
            continue
        seen.add(r["complaint_id"])
        rd = d(r.get("received_date"))
        cnt[(r.get("complaint_code") or "[GAP]", rd.strftime("%Y-%m") if rd else "[GAP]")] += 1
    table = defaultdict(dict)
    for (code, month), n in cnt.items():
        table[code][month] = n
    return {k: dict(sorted(v.items())) for k, v in sorted(table.items())}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("complaints")
    p.add_argument("--capas")
    p.add_argument("--rules")
    p.add_argument("--as-of", default=dt.date.today().isoformat())
    p.add_argument("--holidays")
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)

    complaints = read_csv(a.complaints)
    capas = read_csv(a.capas) if a.capas else []
    rules = json.load(open(a.rules)) if a.rules else {}
    hol_path = a.holidays or DEFAULT_HOLIDAYS
    holidays, hol_note = {}, None
    if os.path.exists(hol_path):
        holidays = load_holidays(hol_path)
        hol_note = ("excluded (file given: %s)" % a.holidays) if a.holidays else (
            "excluded (OPM Federal holiday list for %s, R14)" % " and ".join(str(y) for y in sorted({h.year for h in holidays})))
    elif a.holidays:
        p.error("holiday file not found: %s" % a.holidays)
    else:
        hol_note = None
        print("WARNING: default holiday file %s not found; Federal holidays are NOT excluded from work-day counts "
              "(803.3 requires it). Pass --holidays." % DEFAULT_HOLIDAYS, file=sys.stderr)
    hol_years = {h.year for h in holidays}
    as_of = d(a.as_of)

    res = {"as_of": as_of.isoformat(), "complaints": len({r["complaint_id"] for r in complaints}),
           "recurrence_after_capa_closure": recurrence(complaints, capas),
           "open_complaint_ageing": ageing(complaints, as_of, rules),
           "reporting_timeliness": timeliness(complaints, as_of, holidays, hol_years),
           "counts_by_code_and_month": code_counts(complaints),
           "holidays_excluded": hol_note or "not excluded: holiday file missing"}
    if a.json:
        json.dump(res, sys.stdout, indent=2)
        print()
        return 0

    print("# Complaint log analysis as of %s (%d complaints)\n" % (res["as_of"], res["complaints"]))
    print("## 1. Recurrence after CAPA closure\n")
    if not capas:
        print("No CAPA file given [GAP].\n")
    else:
        print("| CAPA | Complaint code | Closed | Window | Recurrences | Complaint ids (days after closure, version) | Owner |")
        print("|---|---|---|---|---|---|---|")
        for r in res["recurrence_after_capa_closure"]:
            ids = "; ".join("%s (%d, %s)" % (x["complaint_id"], x["days_after_closure"], x["version"]) for x in r["after_closure"]) or "none"
            print("| %s | %s | %s | %s | %s | %s | %s |" % (r["capa_id"], r["complaint_code"], r["closed_date"] or "open",
                  r.get("window", r.get("status")), r.get("recurrences", "n/a"), ids, r["owner"]))
        print("\nA recurrence is a later complaint with the same code. Whether it is the same cause, and whether the CAPA was effective, is your decision.\n")
    print("## 2. Open complaint ageing\n")
    if rules.get("ageing_days") is None:
        print("No ageing limit set by you; days open shown without a verdict.\n")
    print("| Complaint | Received | Days open | Code | Against your limit |")
    print("|---|---|---|---|---|")
    for r in res["open_complaint_ageing"]:
        print("| %s | %s | %s | %s | %s |" % (r["complaint_id"], r["received"], r["days_open"], r["complaint_code"], r["flag"]))
    print("\n## 3. Reporting timeliness against the clocks\n")
    print("| Complaint | Jurisdiction | Event type | Awareness | Due by | Decision | Status |")
    print("|---|---|---|---|---|---|---|")
    for r in res["reporting_timeliness"]:
        print("| %s | %s | %s | %s | %s | %s | %s |" % (r["complaint_id"], r["jurisdiction"], r["event_type"], r["awareness"],
              r.get("due") or "n/a", r["decision"], r["status"]))
    print("\nClocks: EU and GB calendar days from awareness (day 0); US 30 calendar days or 5 work days; 806 counts from initiation. "
          "Federal holidays %s. GB day counting is not in the sourced rules [GAP]." % (hol_note or "NOT excluded (holiday file missing): work-day due dates may be later"))
    if any(r["event_type"] == "us-mdr-5" for r in res["reporting_timeliness"]):
        print("US 5-day rows count from management awareness that remedial action is needed (803.3, VG19), which may be later than first receipt.")
    print("\n## 4. Complaints by code and month\n")
    months = sorted({m for v in res["counts_by_code_and_month"].values() for m in v})
    print("| Code | " + " | ".join(months) + " |")
    print("|---|" + "---|" * len(months))
    for code, v in res["counts_by_code_and_month"].items():
        print("| %s | " % code + " | ".join(str(v.get(m, "")) for m in months) + " |")
    print("\nCounts only. Whether a rise is statistically significant is decided by the method in your PMS plan (MDR Art. 88, VG9).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
