#!/usr/bin/env python3
"""Implementation outcomes from the person's own site file (and optional milestone file).

Nothing is sent anywhere. No threshold, target or score is set by this script; every
verdict comes from a rule the person states, outside the script.

SITES file (CSV, one row per site approached), columns:
  site                  site name or code (no patient or staff names)
  status                approached | agreed | live | paused | withdrawn
  go_live_planned       go-live date agreed with the site at baseline (YYYY-MM-DD, blank if none)
  go_live_actual        date the site met its go-live bar (blank if not yet)
  eligible_patients     people eligible for the service at the site (valid denominator)
  active_patients       eligible people who used the service in the period
  providers_expected    providers trained in or expected to deliver the service
  providers_delivering  providers who delivered it in the period
  expected_usage        usage agreed at commissioning, per active patient per period (optional)
  observed_usage        observed usage in the same unit (optional)

MILESTONES file (CSV, optional), columns:
  site, milestone, core (yes/no), baseline_due (date in the plan the site agreed),
  due (current due date, may differ if re-baselined), done (date completed, blank if open)

Definitions used (row ids in references/customer-success-research.md):
  Adoption, setting level  = sites agreed, live or paused / sites approached (CS28)
  Penetration, patients    = active_patients / eligible_patients (CS39, first formula;
                             denominator is the eligible population, not volunteers, CS27)
  Penetration, providers   = providers_delivering / providers_expected (CS39, second formula)
  Usage against profile    = observed_usage / expected_usage (NICE ESF standard 16, CS61)
  Fidelity to plan         = milestones done on or before their baseline due date /
                             milestones whose baseline due date is on or before the as-of date
                             (fidelity to planned courses of action and timeliness, CS9)
  Core fidelity            = the same, core milestones only (core components, CS4, CS48)
  Slippage (days)          = done - baseline_due, or as_of - baseline_due for an open milestone
                             past its baseline date; go-live slippage likewise on go_live_planned
  Re-baselined             = milestones whose current due differs from baseline_due (shown, never
                             used to hide slippage)

Usage: python3 implementation_outcomes.py SITES.csv --as-of YYYY-MM-DD [--milestones FILE.csv]
"""
import argparse
import csv
import statistics
import sys
from datetime import date

AGREED = {"agreed", "live", "paused"}


def d(s):
    s = (s or "").strip()
    return date.fromisoformat(s) if s else None


def n(s):
    s = (s or "").strip()
    if not s:
        return None
    return float(s)


def rows(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        return [{k.strip(): (v or "").strip() for k, v in r.items()} for r in csv.DictReader(fh)]


def ratio(a, b):
    if a is None or b is None:
        return "not measured [GAP]"
    if b == 0:
        return "denominator 0 [GAP]"
    return f"{a:g}/{b:g} = {100 * a / b:.1f} percent"


def fmt_days(x):
    return f"{x:+d} days"


def sites_report(data, as_of, warnings):
    print(f"## Sites (as of {as_of.isoformat()})")
    approached = len(data)
    agreed = sum(1 for r in data if r.get("status", "").lower() in AGREED)
    live = sum(1 for r in data if r.get("status", "").lower() == "live")
    print(f"Adoption, setting level (CS28): {agreed} of {approached} sites approached agreed, live or paused; {live} live")
    print()
    print("| Site | Status | Patient penetration (CS39) | Provider penetration (CS39) | Usage vs agreed profile (CS61) | Go-live slippage | Months since go-live |")
    print("|---|---|---|---|---|---|---|")
    tot = {"ap": 0.0, "ep": 0.0, "pd": 0.0, "pe": 0.0}
    pen_p, pen_v = [], []
    for r in data:
        site = r.get("site", "?")
        ep, ap = n(r.get("eligible_patients")), n(r.get("active_patients"))
        pe, pd = n(r.get("providers_expected")), n(r.get("providers_delivering"))
        eu, ou = n(r.get("expected_usage")), n(r.get("observed_usage"))
        if ep is not None and ap is not None:
            if ap > ep:
                warnings.append(f"{site}: active_patients ({ap:g}) exceeds eligible_patients ({ep:g}); check the denominator")
            tot["ap"] += ap; tot["ep"] += ep
            if ep:
                pen_p.append(ap / ep)
        if pe is not None and pd is not None:
            if pd > pe:
                warnings.append(f"{site}: providers_delivering ({pd:g}) exceeds providers_expected ({pe:g}); check the denominator")
            tot["pd"] += pd; tot["pe"] += pe
            if pe:
                pen_v.append(pd / pe)
        usage = "not measured [GAP]"
        if eu is not None and ou is not None:
            usage = f"{ou:g} vs {eu:g} = {100 * ou / eu:.0f} percent" if eu else "expected 0 [GAP]"
        planned, actual = d(r.get("go_live_planned")), d(r.get("go_live_actual"))
        if planned is None:
            slip = "no agreed date"
        elif actual:
            slip = fmt_days((actual - planned).days)
        elif as_of > planned:
            slip = f"not live, {fmt_days((as_of - planned).days)} past agreed date"
        else:
            slip = "not yet due"
        months = "not live"
        if actual:
            if actual > as_of:
                warnings.append(f"{site}: go_live_actual {actual} is after the as-of date")
            m = (as_of.year - actual.year) * 12 + (as_of.month - actual.month) - (1 if as_of.day < actual.day else 0)
            months = str(m)
        print(f"| {site} | {r.get('status', '')} | {ratio(ap, ep)} | {ratio(pd, pe)} | {usage} | {slip} | {months} |")
    print()
    if tot["ep"]:
        print(f"Pooled patient penetration: {tot['ap']:g}/{tot['ep']:g} = {100 * tot['ap'] / tot['ep']:.1f} percent; site range {100 * min(pen_p):.1f} to {100 * max(pen_p):.1f} percent")
    if tot["pe"]:
        print(f"Pooled provider penetration: {tot['pd']:g}/{tot['pe']:g} = {100 * tot['pd'] / tot['pe']:.1f} percent; site range {100 * min(pen_v):.1f} to {100 * max(pen_v):.1f} percent")
    print("Pooled figures are shown beside the per-site figures, never instead of them, and are not a score.")
    print()


def milestones_report(ms, as_of, warnings):
    print("## Milestones: fidelity to plan and slippage")
    by_site = {}
    for r in ms:
        by_site.setdefault(r.get("site", "?"), []).append(r)
    print("| Site | Due by as-of (baseline) | Done on time | Fidelity to plan (CS9) | Core fidelity (CS4, CS48) | Open past baseline | Re-baselined | Median slippage of late items |")
    print("|---|---|---|---|---|---|---|---|")
    late_rows = []
    for site, items in by_site.items():
        due = [r for r in items if d(r.get("baseline_due")) and d(r["baseline_due"]) <= as_of]
        on_time = [r for r in due if d(r.get("done")) and d(r["done"]) <= d(r["baseline_due"])]
        core_due = [r for r in due if r.get("core", "").lower() == "yes"]
        core_on = [r for r in on_time if r.get("core", "").lower() == "yes"]
        open_late = [r for r in due if not d(r.get("done"))]
        rebased = [r for r in items if r.get("due") and r.get("baseline_due") and r["due"] != r["baseline_due"]]
        slips = []
        for r in items:
            b, dn = d(r.get("baseline_due")), d(r.get("done"))
            if not b:
                warnings.append(f"{site} / {r.get('milestone')}: no baseline_due; not counted [GAP]")
                continue
            if dn and dn > b:
                s = (dn - b).days
            elif not dn and as_of > b:
                s = (as_of - b).days
            else:
                continue
            slips.append(s)
            late_rows.append((site, r.get("milestone", ""), r.get("core", ""), b, dn, s))
        fid = ratio(len(on_time), len(due)) if due else "none due yet"
        cfid = ratio(len(core_on), len(core_due)) if core_due else "no core item due"
        med = f"{statistics.median(slips):g} days" if slips else "none late"
        print(f"| {site} | {len(due)} | {len(on_time)} | {fid} | {cfid} | {len(open_late)} | {len(rebased)} | {med} |")
    print()
    if late_rows:
        print("Late milestones (slippage counted from the baseline date the site agreed):")
        print()
        print("| Site | Milestone | Core | Baseline due | Done | Days late |")
        print("|---|---|---|---|---|---|")
        for site, m, core, b, dn, s in sorted(late_rows, key=lambda x: -x[5]):
            print(f"| {site} | {m} | {core} | {b.isoformat()} | {dn.isoformat() if dn else 'open'} | {s} |")
        print()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sites")
    ap.add_argument("--as-of", required=True)
    ap.add_argument("--milestones")
    a = ap.parse_args()
    as_of = d(a.as_of)
    warnings = []
    sites_report(rows(a.sites), as_of, warnings)
    if a.milestones:
        milestones_report(rows(a.milestones), as_of, warnings)
    if warnings:
        print("## Data checks")
        for w in warnings:
            print(f"- {w}")
    print()
    print("No rule, threshold or target was applied. Verdicts need the person's own rules.")


if __name__ == "__main__":
    sys.exit(main())
