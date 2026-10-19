#!/usr/bin/env python3
"""Review clocks for an FDA submission, and calendar-day spans for comparables.

Mode 1, the person's own submission (events they supply):
  python3 review_clock.py events --file events.csv --pathway 510k|denovo|pma [--as-of YYYY-MM-DD]
  events.csv columns: date,event   with event one of
    received   (submission received; FDA clock starts; for an eSTAR that passes screening, the receipt date)
    hold       (Additional Information or Major Deficiency letter issued; FDA clock stops)
    response   (complete response received; FDA clock restarts)
    decision   (MDUFA decision)
  Counting follows the MDUFA V commitment letter as read in references (S-25, S-26): FDA days
  run while the submission is under review at FDA and stop on a hold letter. Day counting
  conventions inside FDA (same-day events) are not sourced; the script counts calendar-day
  differences and says so.

Mode 2, comparables from saved library output (get_authorization / search_devices rows):
  python3 review_clock.py comparables --file authorizations.json
  Prints the calendar days between the stored submission_date and decision_date per record.
  These are calendar days between the dates FDA's record states, including time on hold; they
  are not FDA days and cannot be set against a FDA-day goal.

The goals and actual-performance figures printed are copied from the reference rows, each with
its row id. The script never predicts a date.
"""
import argparse, csv, json, sys
from datetime import date

GOALS = {  # FDA-day decision goals, MDUFA V (RP US-46 to RP US-48, RP US-60)
    "510k": ("90 FDA days for 95% of 510(k)s", 90, "RP US-46"),
    "denovo": ("150 FDA days; 70% goal, shown as 80% for FY 2026 and 90% for FY 2027", 150, "RP US-47, RP US-60"),
    "pma": ("180 FDA days for 90% (no advisory committee)", 180, "RP US-48"),
}
ESCALATION = {  # S-27, S-32
    "510k": (100, "written feedback on all outstanding issues if no decision by 100 FDA days (S-27)"),
    "denovo": (180, "on request, discussion of all outstanding issues after 180 FDA days (S-32)"),
}
ACTUAL = {  # receipt cohorts FY 2023, FY 2024, FY 2025 (FY 2026 still open)
    "510k": "within 90 FDA days 99.32%, 98.81%, 97.94%; average total days 141.46, 143.64, 141.24; average review cycles 1.67, 1.69, 1.69 (RP US-57, RP US-58, S-41)",
    "denovo": "within 150 FDA days 93.98%, 98.61%, 92.00%; average FDA days 130.60, 121.26, 132.16; average industry days 139.47, 126.25, 145.96; average total days 270.07, 247.51, 278.12 (RP US-60, RP US-61, S-45)",
    "pma": "180-day goal met 98.55%, 96.88%, 97.26% (RP US-63)",
}


def d(s):
    return date.fromisoformat(s.strip())


def run_events(path, pathway, as_of):
    rows = sorted(({"date": d(r["date"]), "event": r["event"].strip().lower()} for r in csv.DictReader(open(path))), key=lambda r: r["date"])
    if not rows or rows[0]["event"] != "received":
        sys.exit("the first event must be 'received'")
    fda = industry = 0
    running, mark, holds = True, rows[0]["date"], 0
    end = None
    for r in rows[1:]:
        span = (r["date"] - mark).days
        if r["event"] == "hold":
            if not running:
                sys.exit("hold while already on hold at %s" % r["date"])
            fda += span; running = False; holds += 1
        elif r["event"] == "response":
            if running:
                sys.exit("response while the FDA clock is running at %s" % r["date"])
            industry += span; running = True
        elif r["event"] == "decision":
            if not running:
                sys.exit("decision recorded while on hold at %s" % r["date"])
            fda += span; end = r["date"]
        else:
            sys.exit("unknown event %r" % r["event"])
        mark = r["date"]
        if end:
            break
    if end is None:
        stop = d(as_of) if as_of else date.today()
        span = (stop - mark).days
        if running:
            fda += span
        else:
            industry += span
        end_label = "as of %s (no decision yet; clock %s)" % (stop.isoformat(), "running at FDA" if running else "on hold with the sponsor")
        end = stop
    else:
        end_label = "decision on %s" % end.isoformat()
    total = (end - rows[0]["date"]).days
    goal_text, goal_days, goal_row = GOALS[pathway]
    out = ["Pathway: %s" % pathway, "Received: %s; %s" % (rows[0]["date"].isoformat(), end_label),
           "FDA days: %d   Sponsor (hold) days: %d   Total calendar days: %d   Hold letters: %d" % (fda, industry, total, holds),
           "MDUFA V decision goal: %s [%s]. FDA days used against it: %d of %d." % (goal_text, goal_row, fda, goal_days)]
    if pathway in ESCALATION:
        n, txt = ESCALATION[pathway]
        out.append("Escalation point: %s. Reached: %s." % (txt, "yes" if fda >= n else "no"))
    out.append("Actual performance for context, not a forecast: " + ACTUAL[pathway])
    out.append("Basis: calendar-day differences between the dates supplied; FDA's own same-day counting rules are not sourced here.")
    return "\n".join(out)


def run_comparables(path):
    data = json.load(open(path, encoding="utf-8"))
    recs = data.get("results", data if isinstance(data, list) else [])
    lines = ["| Reference | Device | Pathway | Submission date (record) | Decision date (record) | Calendar days | Source |", "|---|---|---|---|---|---|---|"]
    for r in recs:
        sd, dd = r.get("submission_date"), r.get("decision_date")
        days = (d(dd) - d(sd)).days if sd and dd else "[GAP] date not stored"
        lines.append("| %s | %s | %s | %s | %s | %s | %s |" % (r.get("reference") or (r.get("identifiers", {}).get("FDA_SUBMISSION") or ["?"])[0], r.get("product"), r.get("pathway"), sd or "[GAP]", dd or "[GAP]", days, r.get("source_url", "")))
    lines.append("")
    lines.append("Calendar days between the dates the FDA record states, including any time on hold with the sponsor. Not FDA days; do not compare with a FDA-day goal. The record does not show earlier submissions for the same device.")
    return "\n".join(lines)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="mode", required=True)
    e = sub.add_parser("events"); e.add_argument("--file", required=True); e.add_argument("--pathway", choices=list(GOALS), required=True); e.add_argument("--as-of")
    c = sub.add_parser("comparables"); c.add_argument("--file", required=True)
    a = ap.parse_args()
    print(run_events(a.file, a.pathway, a.as_of) if a.mode == "events" else run_comparables(a.file))
