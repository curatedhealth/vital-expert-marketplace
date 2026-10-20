#!/usr/bin/env python3
"""Track patient insights from capture to decision on the person's own files.

Nothing is sent anywhere. Every rule that turns a number into a verdict is the person's;
the script counts, checks consistency and lists what is missing.

Files (CSV, header row, UTF-8). Column names are fixed; extra columns are ignored.

  captures.csv   One row per thing a participant said or did, in their words.
                 capture_id, session_id, captured (YYYY-MM-DD), participant_ref (a code
                 such as P03, never a name), participant_type (patient, carer, staff,
                 clinician, other), kind (request or observation), insight_id, words
  insights.csv   One row per insight (a point the team tracks to a decision).
                 insight_id, summary, status (open, accepted, deferred, refused),
                 decision_date, reason, owner (as the person names them), decision_due
                 (optional, the person's date), linked_change (change id, for accepted),
                 version (product version that shows it), safety_constraint (yes, no, blank)
  changes.csv    One row per design change in a release.
                 change_id, description, credited_to_codesign (yes or no), insight_ids
                 (semicolon list), in_backlog_before (optional YYYY-MM-DD: the date the
                 change was already planned), shipped_version, shipped_date (optional)
  sessions.csv   One row per session.
                 session_id, date, planned_types (semicolon list, for example
                 "patient;carer"), attended (semicolon list of type:count, for example
                 "patient:4;carer:1;staff:1")

Subcommands
  check   FILE [FILE ...]           Column check and a scan for identifiers (emails, phone
                                    numbers, long ID numbers, dates of birth, name or address
                                    columns). Run it before anything else.
  tally   CAPTURES [--repeat N]     Per insight: distinct participants, sessions, types,
                                    requests vs observations. --repeat is the person's rule
                                    for a "repeated point"; the register's starting rule is
                                    "more than one participant" (N = 2), used only if the
                                    person adopts it.
  status  INSIGHTS CAPTURES --as-of YYYY-MM-DD
                                    Status counts, open insights with age since first
                                    capture, past the person's own decision_due, decided
                                    without reason or owner, accepted without a linked
                                    change or version, safety-constraint flags.
  trace   CHANGES INSIGHTS CAPTURES Changes credited to co-design with no insight link, links
                                    to unknown insights, insights with no capture, changes
                                    planned before the first capture of every linked insight,
                                    accepted insights with no shipped change.
  fit     SESSIONS [CAPTURES]       Planned participant types vs attended, staff present,
                                    and captures from staff counted apart from patients.

Usage: python3 insight_tracker.py SUBCOMMAND FILES [options]
"""
import argparse
import csv
import re
import statistics
import sys
from collections import defaultdict
from datetime import date

COLS = {
    "captures": ["capture_id", "session_id", "captured", "participant_ref", "participant_type",
                 "kind", "insight_id", "words"],
    "insights": ["insight_id", "summary", "status", "decision_date", "reason", "owner",
                 "decision_due", "linked_change", "version", "safety_constraint"],
    "changes": ["change_id", "description", "credited_to_codesign", "insight_ids",
                "in_backlog_before", "shipped_version", "shipped_date"],
    "sessions": ["session_id", "date", "planned_types", "attended"],
}
STATUSES = {"open", "accepted", "deferred", "refused"}
PATIENT_SIDE = {"patient", "carer"}

ID_PATTERNS = [
    ("email address", re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")),
    ("phone number", re.compile(r"(?<!\d)(?:\+?\d[\d ()-]{8,}\d)(?!\d)")),
    ("long ID number", re.compile(r"(?<!\d)\d{9,}(?!\d)")),
    ("US SSN pattern", re.compile(r"(?<!\d)\d{3}-\d{2}-\d{4}(?!\d)")),
    ("date of birth wording", re.compile(r"\b(?:born on|date of birth|DOB)\b", re.I)),
]
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ID_COLUMNS = re.compile(r"^(?:name|full_?name|first_?name|last_?name|surname|patient_?name|"
                        r"dob|date_?of_?birth|address|postcode|zip|mrn|nhs_?number|ssn|email|phone)$",
                        re.I)


def d(s):
    s = (s or "").strip()
    return date.fromisoformat(s) if s else None


def read(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        rdr = csv.DictReader(fh)
        header = [h.strip() for h in (rdr.fieldnames or [])]
        rows = [{(k or "").strip(): (v or "").strip() for k, v in r.items()} for r in rdr]
    return header, rows


def kind_of(header):
    for k, cols in COLS.items():
        if cols[0] in header and all(c in header for c in cols[:3]):
            return k
    return None


def split(s):
    return [x.strip() for x in (s or "").split(";") if x.strip()]


def cmd_check(files):
    problems = 0
    for path in files:
        header, rows = read(path)
        k = kind_of(header)
        print(f"== {path}: {len(rows)} rows, recognized as {k or 'unknown'}")
        if k:
            missing = [c for c in COLS[k] if c not in header]
            if missing:
                print("  missing columns:", ", ".join(missing))
                problems += 1
        for h in header:
            if ID_COLUMNS.match(h):
                print(f"  IDENTIFIER COLUMN: '{h}'. Remove it; use a participant code.")
                problems += 1
        for i, r in enumerate(rows, start=2):
            for col, val in r.items():
                if not val or ISO_DATE.match(val):
                    continue
                for label, pat in ID_PATTERNS:
                    m = pat.search(val)
                    if m and (label != "phone number" or len(re.sub(r"\D", "", m.group())) >= 10):
                        print(f"  line {i}, column {col}: possible {label}. Check and remove.")
                        problems += 1
        if k == "insights":
            for i, r in enumerate(rows, start=2):
                if r.get("status") and r["status"].lower() not in STATUSES:
                    print(f"  line {i}: status '{r['status']}' is not one of {sorted(STATUSES)}")
                    problems += 1
        if k == "captures":
            for i, r in enumerate(rows, start=2):
                if r.get("kind") and r["kind"].lower() not in {"request", "observation"}:
                    print(f"  line {i}: kind '{r['kind']}' is not request or observation")
                    problems += 1
    print(f"Problems found: {problems}")
    return problems


def group_captures(rows):
    g = defaultdict(list)
    for r in rows:
        g[r.get("insight_id") or "(no insight)"].append(r)
    return g


def cmd_tally(path, repeat):
    _, rows = read(path)
    g = group_captures(rows)
    print(f"Captures: {len(rows)}; insights referenced: {len([k for k in g if k != '(no insight)'])}")
    print("insight_id | patient-side participants | staff or clinician captures | sessions | "
          "requests | observations | repeated (rule)")
    for iid in sorted(g):
        rs = g[iid]
        pts = {r["participant_ref"] for r in rs if r.get("participant_type", "").lower() in PATIENT_SIDE}
        staff = sum(1 for r in rs if r.get("participant_type", "").lower() not in PATIENT_SIDE)
        sess = {r["session_id"] for r in rs}
        req = sum(1 for r in rs if r.get("kind", "").lower() == "request")
        obs = sum(1 for r in rs if r.get("kind", "").lower() == "observation")
        rep = "no rule set" if repeat is None else ("yes" if len(pts) >= repeat else "no")
        print(f"{iid} | {len(pts)} | {staff} | {len(sess)} | {req} | {obs} | {rep}")
    if "(no insight)" in g:
        print(f"Captures not yet linked to an insight: {len(g['(no insight)'])}")
    print("Patient-side counts patients and carers only; staff captures are listed apart.")


def cmd_status(ipath, cpath, as_of):
    _, ins = read(ipath)
    _, caps = read(cpath)
    first = {}
    for r in caps:
        c = d(r.get("captured"))
        if c and r.get("insight_id"):
            first[r["insight_id"]] = min(first.get(r["insight_id"], c), c)
    counts = defaultdict(int)
    for r in ins:
        counts[(r.get("status") or "blank").lower()] += 1
    print(f"As of {as_of.isoformat()}. Insights: {len(ins)}")
    print("Status counts: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    ages = []
    print("\nOpen insights (age in days since first capture):")
    for r in ins:
        if (r.get("status") or "").lower() == "open":
            f = first.get(r["insight_id"])
            age = (as_of - f).days if f else None
            if age is not None:
                ages.append(age)
            due = d(r.get("decision_due"))
            past = " | past the decision_due you set" if due and due < as_of else ""
            owner = r.get("owner") or "owner not named"
            print(f"  {r['insight_id']} | {age if age is not None else 'no capture date'} | "
                  f"owner: {owner} | due: {r.get('decision_due') or 'none set'}{past}")
    if ages:
        print(f"  median age {statistics.median(ages)}; oldest {max(ages)}")
    print("\nChecks:")
    n = 0
    for r in ins:
        st = (r.get("status") or "").lower()
        iid = r["insight_id"]
        if st in {"accepted", "deferred", "refused"}:
            if not r.get("reason"):
                print(f"  {iid}: {st} with no reason recorded"); n += 1
            if not r.get("owner"):
                print(f"  {iid}: {st} with no owner recorded"); n += 1
            if not r.get("decision_date"):
                print(f"  {iid}: {st} with no decision date"); n += 1
        if st == "accepted":
            if not r.get("linked_change"):
                print(f"  {iid}: accepted with no linked change"); n += 1
            if not r.get("version"):
                print(f"  {iid}: accepted with no product version named"); n += 1
        if (r.get("safety_constraint") or "").lower() == "yes" and st == "accepted":
            print(f"  {iid}: accepted and marked as touching a safety constraint: "
                  "stops for the accountable owner"); n += 1
        if iid not in first:
            print(f"  {iid}: no capture row links to this insight"); n += 1
    print(f"  {n} item(s)")


def cmd_trace(chpath, ipath, cpath):
    _, chs = read(chpath)
    _, ins = read(ipath)
    _, caps = read(cpath)
    known = {r["insight_id"]: r for r in ins}
    first = {}
    for r in caps:
        c = d(r.get("captured"))
        if c and r.get("insight_id"):
            first[r["insight_id"]] = min(first.get(r["insight_id"], c), c)
    credited = [r for r in chs if (r.get("credited_to_codesign") or "").lower() == "yes"]
    traced, untraced, planned_before, unknown = [], [], [], []
    for r in credited:
        ids = split(r.get("insight_ids"))
        if not ids:
            untraced.append(r["change_id"]); continue
        bad = [i for i in ids if i not in known]
        if bad:
            unknown.append((r["change_id"], bad))
        good = [i for i in ids if i in known and i in first]
        if not good:
            untraced.append(r["change_id"]); continue
        bb = d(r.get("in_backlog_before"))
        if bb and all(bb < first[i] for i in good):
            planned_before.append((r["change_id"], bb, min(first[i] for i in good)))
        else:
            traced.append(r["change_id"])
    print(f"Changes: {len(chs)}; credited to co-design: {len(credited)}")
    print(f"Traced to a capture: {len(traced)} {traced}")
    print(f"Credited but no capture link (not from this research): {len(untraced)} {untraced}")
    for cid, bb, fc in planned_before:
        print(f"Planned before capture: {cid} in backlog {bb.isoformat()}, first linked capture "
              f"{fc.isoformat()} (do not credit co-design for the idea; the capture may still "
              "support it)")
    for cid, bad in unknown:
        print(f"Unknown insight ids on {cid}: {bad}")
    linked = set()
    for r in chs:
        linked.update(split(r.get("insight_ids")))
    open_accepted = [r["insight_id"] for r in ins
                     if (r.get("status") or "").lower() == "accepted" and r["insight_id"] not in linked]
    print(f"Accepted insights with no change in this file: {len(open_accepted)} {open_accepted}")
    if credited:
        print(f"Trace coverage: {len(traced)} of {len(credited)} credited changes")


def parse_attended(s):
    out = {}
    for part in split(s):
        if ":" in part:
            t, n = part.split(":", 1)
            try:
                out[t.strip().lower()] = int(n)
            except ValueError:
                out[t.strip().lower()] = None
        else:
            out[part.lower()] = None
    return out


def cmd_fit(spath, cpath=None):
    _, ss = read(spath)
    print("session | date | planned | attended | planned types missing | staff or clinicians present")
    for r in ss:
        planned = [p.lower() for p in split(r.get("planned_types"))]
        att = parse_attended(r.get("attended"))
        missing = [p for p in planned if not att.get(p)]
        staff = {k: v for k, v in att.items() if k not in PATIENT_SIDE}
        print(f"{r['session_id']} | {r.get('date')} | {';'.join(planned)} | {r.get('attended')} | "
              f"{', '.join(missing) or 'none'} | {staff or 'none'}")
    if cpath:
        _, caps = read(cpath)
        by = defaultdict(lambda: defaultdict(int))
        for c in caps:
            by[c["session_id"]][(c.get("participant_type") or "blank").lower()] += 1
        print("\nCaptures by participant type per session (staff words are not patient co-design):")
        for sid in sorted(by):
            print(f"  {sid}: " + ", ".join(f"{k} {v}" for k, v in sorted(by[sid].items())))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("check"); p.add_argument("files", nargs="+")
    p = sub.add_parser("tally"); p.add_argument("captures"); p.add_argument("--repeat", type=int)
    p = sub.add_parser("status"); p.add_argument("insights"); p.add_argument("captures")
    p.add_argument("--as-of", required=True)
    p = sub.add_parser("trace"); p.add_argument("changes"); p.add_argument("insights"); p.add_argument("captures")
    p = sub.add_parser("fit"); p.add_argument("sessions"); p.add_argument("captures", nargs="?")
    a = ap.parse_args()
    if a.cmd == "check":
        sys.exit(1 if cmd_check(a.files) else 0)
    if a.cmd == "tally":
        cmd_tally(a.captures, a.repeat)
    elif a.cmd == "status":
        cmd_status(a.insights, a.captures, date.fromisoformat(a.as_of))
    elif a.cmd == "trace":
        cmd_trace(a.changes, a.insights, a.captures)
    elif a.cmd == "fit":
        cmd_fit(a.sessions, a.captures)


if __name__ == "__main__":
    main()
