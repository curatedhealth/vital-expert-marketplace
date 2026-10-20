#!/usr/bin/env python3
"""Governance effectiveness indicators from the person's own QMS data, plus FDA 483 context.

Subcommands (each reads a CSV; nothing is sent anywhere):

  capa      CAPA ageing and closure.
            Columns: id, opened (YYYY-MM-DD), closed (blank if open), due (optional),
            effectiveness_verified (yes/no/blank, optional), process (optional).
            Options: --as-of YYYY-MM-DD (required), --bins 30,90,180 (optional display bins
            the person chooses; none by default).
  findings  Audit finding closure and repeats.
            Columns: id, audit_date, source (internal, notified body, MDSAP, FDA ...),
            process, grade (optional), due (optional), closed (blank if open),
            repeat_of (optional id of an earlier finding).
            Options: --as-of YYYY-MM-DD (required).
            A repeat is counted as MDSAP defines it: a nonconformity identified in audits
            within the previous 3 years (research row QS47), using repeat_of links the
            person supplies.
  mr        Management review coverage and action closure.
            Columns: date, inputs_covered (semicolon list), actions_raised, actions_closed.
            Options: --required "complaints;capa;audits" (the person's own input list).
  fda483    FDA FY 2025 Form 483 device citations grouped by CFR section (context only;
            pre-QMSR numbering). Columns as published: Reference Number, Frequency, ...

No subcommand sets a threshold or a target. Overdue means past the person's own due date.

Usage: python3 qms_indicators.py SUBCOMMAND FILE [options]
"""
import argparse
import csv
import re
import statistics
import sys
from collections import Counter, defaultdict
from datetime import date


def d(s):
    s = (s or "").strip()
    return date.fromisoformat(s) if s else None


def rows(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        return [{k.strip(): (v or "").strip() for k, v in r.items()} for r in csv.DictReader(fh)]


def pct(n, base):
    return f"{100 * n / base:.0f} percent" if base else "n/a"


def capa(args):
    data = rows(args.file)
    as_of = d(args.as_of)
    open_ = [r for r in data if not r.get("closed")]
    closed = [r for r in data if r.get("closed")]
    ages = sorted((as_of - d(r["opened"])).days for r in open_)
    print(f"CAPA records: {len(data)}; open {len(open_)}; closed {len(closed)} (as of {as_of.isoformat()})")
    if ages:
        print(f"Open CAPA age in days: median {statistics.median(ages):g}, oldest {ages[-1]}, youngest {ages[0]}")
    if args.bins:
        edges = [int(x) for x in args.bins.split(",")]
        labels, lo = [], 0
        for e in edges:
            labels.append((lo, e))
            lo = e + 1
        print("| Age band (days, your bins) | Open CAPA |")
        print("|---|---|")
        for lo, hi in labels:
            print(f"| {lo} to {hi} | {sum(lo <= a <= hi for a in ages)} |")
        print(f"| over {edges[-1]} | {sum(a > edges[-1] for a in ages)} |")
    with_due = [r for r in open_ if r.get("due")]
    overdue = [r for r in with_due if d(r["due"]) < as_of]
    print(f"Open with a due date you set: {len(with_due)}; past that date: {len(overdue)}"
          + (" (" + ", ".join(r["id"] for r in overdue) + ")" if overdue else ""))
    if any("effectiveness_verified" in r for r in data):
        nv = [r for r in closed if r.get("effectiveness_verified", "").lower() not in ("yes", "y", "true")]
        print(f"Closed without a recorded effectiveness verification: {len(nv)} of {len(closed)}"
              + (" (" + ", ".join(r["id"] for r in nv) + ")" if nv else ""))
    if closed:
        days = sorted((d(r["closed"]) - d(r["opened"])).days for r in closed)
        print(f"Closed CAPA, days open: median {statistics.median(days):g}, longest {days[-1]}")
    if any(r.get("process") for r in open_):
        print("Open CAPA by process: " + ", ".join(f"{k} {v}" for k, v in Counter(r.get("process") or "not given" for r in open_).most_common()))


def findings(args):
    data = rows(args.file)
    as_of = d(args.as_of)
    by_id = {r["id"]: r for r in data}
    closed = [r for r in data if r.get("closed")]
    open_ = [r for r in data if not r.get("closed")]
    print(f"Audit findings: {len(data)}; closed {len(closed)} ({pct(len(closed), len(data))}); open {len(open_)} (as of {as_of.isoformat()})")
    overdue = [r for r in open_ if r.get("due") and d(r["due"]) < as_of]
    print(f"Open past the due date you set: {len(overdue)}" + (" (" + ", ".join(r["id"] for r in overdue) + ")" if overdue else ""))
    print("| Source | Findings | Closed | Open |")
    print("|---|---|---|---|")
    groups = defaultdict(list)
    for r in data:
        groups[r.get("source") or "not given"].append(r)
    for k, g in sorted(groups.items()):
        c = sum(1 for r in g if r.get("closed"))
        print(f"| {k} | {len(g)} | {c} | {len(g) - c} |")
    repeats = []
    for r in data:
        prior = by_id.get(r.get("repeat_of", ""))
        if prior and d(prior["audit_date"]) and d(r["audit_date"]):
            gap = (d(r["audit_date"]) - d(prior["audit_date"])).days
            if 0 <= gap <= 3 * 365 + 1:
                repeats.append((r["id"], prior["id"], r.get("process", "")))
    print(f"Repeat findings within 3 years (MDSAP definition, QS47, from your repeat_of links): {len(repeats)}")
    for rid, pid, proc in repeats:
        print(f"  {rid} repeats {pid} ({proc or 'process not given'})")
    if any(r.get("grade") for r in data):
        print("Grades as recorded: " + ", ".join(f"{k}: {v}" for k, v in sorted(Counter(r.get("grade") or "none" for r in data).items())))
    print("By process (open): " + ", ".join(f"{k} {v}" for k, v in Counter(r.get("process") or "not given" for r in open_).most_common()))


def mr(args):
    data = rows(args.file)
    required = [x.strip().lower() for x in (args.required or "").split(";") if x.strip()]
    print("| Review date | Inputs covered | Your required inputs missing | Actions raised | Actions closed |")
    print("|---|---|---|---|---|")
    for r in data:
        cov = [x.strip().lower() for x in r.get("inputs_covered", "").split(";") if x.strip()]
        missing = [x for x in required if x not in cov] if required else ["(no required list given)"]
        print(f"| {r.get('date')} | {len(cov)} | {', '.join(missing) or 'none'} | {r.get('actions_raised', '')} | {r.get('actions_closed', '')} |")
    raised = sum(int(r["actions_raised"]) for r in data if r.get("actions_raised", "").isdigit())
    closed = sum(int(r["actions_closed"]) for r in data if r.get("actions_closed", "").isdigit())
    print(f"Actions raised across reviews: {raised}; closed: {closed} ({pct(closed, raised)})")


def fda483(args):
    data = rows(args.file)
    total = 0
    groups = Counter()
    top_desc = {}
    for r in data:
        if r.get("Citation Program Area") and r["Citation Program Area"] != "Devices":
            continue
        ref = r.get("Reference Number", "")
        f = int(r.get("Frequency") or 0)
        total += f
        m = re.match(r"21 CFR (\d+)\.(\d+)", ref)
        key = f"21 CFR {m.group(1)}.{m.group(2)}" if m else (ref or "not given")
        groups[key] += f
        if f > top_desc.get(key, ("", -1))[1]:
            top_desc[key] = (r.get("Short Description", "").strip(), f)
    print(f"FY 2025 device 483 citations in the file: {total} across {len(data)} cite rows")
    print("Context only: FY 2025 ended 30 September 2025, before the QMSR took effect on 2 February 2026; sections are the retired QS regulation numbering. Not a complete list of observations (QS51).")
    print("| CFR section | Citations | Share of all device citations | Most cited short description in the section (as published) |")
    print("|---|---|---|---|")
    for k, v in groups.most_common(args.top):
        print(f"| {k} | {v} | {100 * v / total:.1f} percent | {top_desc.get(k, ('', 0))[0]} |")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("capa"); a.add_argument("file"); a.add_argument("--as-of", required=True); a.add_argument("--bins")
    b = sub.add_parser("findings"); b.add_argument("file"); b.add_argument("--as-of", required=True)
    c = sub.add_parser("mr"); c.add_argument("file"); c.add_argument("--required")
    e = sub.add_parser("fda483"); e.add_argument("file"); e.add_argument("--top", type=int, default=15)
    args = p.parse_args()
    {"capa": capa, "findings": findings, "mr": mr, "fda483": fda483}[args.cmd](args)


if __name__ == "__main__":
    main()
