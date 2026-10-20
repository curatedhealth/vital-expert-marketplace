#!/usr/bin/env python3
"""Program and partnership indicators from the person's own logs. Nothing is sent anywhere.

Subcommands (each reads one CSV):

  activities  Result per activity against the person's result definition.
              Columns: activity, period_start, period_end, result_definition, record_source
              (blank if no record), reached, result_count (blank if no record),
              claims_used (semicolon list, optional), allowed_claims (semicolon list, optional),
              target (optional, the person's own number).
              An activity with no record is "unscored (no record)", never zero.
              A claim used that is not on the activity's allowed list is listed.
  attrition   Dropout and nonusage attrition (Eysenbach, research rows PE-101 to PE-103).
              Columns: participant, start (YYYY-MM-DD), last_active (YYYY-MM-DD),
              followup_done (yes/no, optional).
              Options: --as-of YYYY-MM-DD (required), --step DAYS (default 7, the curve's
              interval, a display choice only).
              Prints the share still active at each step, the usage half-life (first step
              at which half or fewer remain active) and dropout attrition from followup_done.
              "Active" means last_active on or after start + step; it is a reading of the
              person's own definition of activity, stated in the output.
  support     Value of support per patient per calendar year against a cap figure the
              caller passes. Columns: patient (pseudonymous id), date, item, retail_value_usd,
              cash_equivalent (yes/no), recommended_by_hcp (yes/no/blank).
              Options: --year YYYY (required), --cap NUMBER (required; for 2026 the OIG figure
              is 623, research row CP-US-27; the script does not know any year's figure).
              Lists patients above the cap figure and items marked cash or cash equivalent or
              without a recorded recommendation. These are elements for the compliance owner,
              never a finding that support is or is not protected.
  partners    Agreement and disclosure completeness per partner.
              Columns: partner, support_type, amount (blank if non-financial),
              agreement_signed (YYYY-MM-DD or blank), first_support (YYYY-MM-DD),
              purpose_stated (yes/no), disclosed (yes/no), disclosure_year (optional).
              Flags support given before a signed agreement or with no agreement, agreements
              without a stated purpose, and support not disclosed. Code rules behind each
              flag are [INDUSTRY] rows PE-71, PE-75, PE-76, PE-80, PE-82.

No subcommand sets a threshold or a target. Targets and pass rules are the person's.

Usage: python3 engagement_monitor.py SUBCOMMAND FILE [options]
"""
import argparse
import csv
from collections import defaultdict
from datetime import date, timedelta


def d(s):
    s = (s or "").strip()
    return date.fromisoformat(s) if s else None


def rows(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        return [{k.strip(): (v or "").strip() for k, v in r.items()} for r in csv.DictReader(fh)]


def split(s):
    return [x.strip() for x in (s or "").split(";") if x.strip()]


def pct(n, base):
    return f"{100 * n / base:.0f} percent" if base else "n/a"


def activities(args):
    data = rows(args.file)
    print("| Activity | Period | Result definition | Record | Reached | Result | Share of reached | Your target | Off-list claims |")
    print("|---|---|---|---|---|---|---|---|---|")
    unscored = []
    for r in data:
        period = f"{r.get('period_start', '')} to {r.get('period_end', '')}"
        allowed = set(split(r.get("allowed_claims")))
        used = split(r.get("claims_used"))
        off = [c for c in used if allowed and c not in allowed] if allowed else (["no allowed list"] if used else [])
        if not r.get("record_source") or r.get("result_count", "") == "":
            unscored.append(r["activity"])
            res, share = "unscored (no record)", "n/a"
        else:
            n = int(r["result_count"])
            reached = int(r["reached"]) if r.get("reached") else 0
            res, share = str(n), pct(n, reached)
        print(f"| {r['activity']} | {period} | {r.get('result_definition', '')} | {r.get('record_source') or 'none'} | "
              f"{r.get('reached') or 'n/a'} | {res} | {share} | {r.get('target') or 'not set'} | {'; '.join(off) or 'none'} |")
    print()
    print(f"Activities: {len(data)}; unscored for lack of a record: {len(unscored)}" + (f" ({', '.join(unscored)})" if unscored else ""))
    print("Met or missed is judged only against the person's own target; no target, no verdict.")


def attrition(args):
    data = rows(args.file)
    as_of = d(args.as_of)
    step = args.step
    n = len(data)
    print(f"Participants: {n} (as of {as_of.isoformat()}); a participant counts as active at day t if last_active is on or after start + t days.")
    eligible_max = max((as_of - d(r["start"])).days for r in data) if data else 0
    print("| Day | Participants observable | Still active | Share active |")
    print("|---|---|---|---|")
    half = None
    t = 0
    while t <= eligible_max:
        obs = [r for r in data if (as_of - d(r["start"])).days >= t]
        act = [r for r in obs if (d(r["last_active"]) - d(r["start"])).days >= t]
        share = len(act) / len(obs) if obs else 0
        print(f"| {t} | {len(obs)} | {len(act)} | {pct(len(act), len(obs))} |")
        if half is None and t > 0 and obs and share <= 0.5:
            half = t
        t += step
    print()
    print("Usage half-life (first step with half or fewer still active): " + (f"day {half}" if half is not None else "not reached in the observed period"))
    fu = [r for r in data if r.get("followup_done", "") in ("yes", "no")]
    if fu:
        missed = sum(1 for r in fu if r["followup_done"] == "no")
        print(f"Dropout attrition (follow-up not done): {missed} of {len(fu)} ({pct(missed, len(fu))})")
    print("Nonusage attrition (stopped using) and dropout attrition (lost to follow-up) are reported separately (PE-102).")


def support(args):
    data = [r for r in rows(args.file) if d(r["date"]).year == args.year]
    per = defaultdict(float)
    for r in data:
        per[r["patient"]] += float(r["retail_value_usd"] or 0)
    over = sorted((p, v) for p, v in per.items() if v > args.cap)
    cash = [r for r in data if r.get("cash_equivalent", "").lower() == "yes"]
    norec = [r for r in data if r.get("recommended_by_hcp", "").lower() != "yes"]
    print(f"Calendar year {args.year}: {len(data)} support items to {len(per)} patients; total retail value ${sum(per.values()):,.2f}")
    print(f"Cap figure passed by the caller: ${args.cap:,.2f} per patient per calendar year")
    print(f"Patients above the cap figure: {len(over)}" + ("" if not over else " (" + ", ".join(f"{p} ${v:,.2f}" for p, v in over) + ")"))
    print(f"Items marked cash or cash equivalent: {len(cash)}" + ("" if not cash else " (" + ", ".join(f"{r['patient']} {r['item']}" for r in cash) + ")"))
    print(f"Items without a recorded recommendation by a licensed professional: {len(norec)}")
    print("These are elements for the compliance owner (CP-US-26 to CP-US-28). They are not a finding that support is or is not protected.")


def partners(args):
    data = rows(args.file)
    print("| Partner | Support | Amount | Agreement signed | First support | Flags |")
    print("|---|---|---|---|---|---|")
    flagged = 0
    for r in data:
        flags = []
        signed, first = d(r.get("agreement_signed")), d(r.get("first_support"))
        if not signed:
            flags.append("no signed agreement (PE-71, PE-80 [INDUSTRY])")
        elif first and first < signed:
            flags.append(f"support {(signed - first).days} days before the agreement (PE-71, PE-80 [INDUSTRY])")
        if r.get("purpose_stated", "").lower() != "yes":
            flags.append("purpose not stated in the agreement (PE-71 [INDUSTRY])")
        if r.get("disclosed", "").lower() != "yes":
            flags.append("not disclosed (PE-75, PE-82 [INDUSTRY])")
        flagged += bool(flags)
        print(f"| {r['partner']} | {r.get('support_type', '')} | {r.get('amount') or 'non-financial'} | {r.get('agreement_signed') or 'none'} | {r.get('first_support') or 'n/a'} | {'; '.join(flags) or 'none'} |")
    print()
    print(f"Partners: {len(data)}; with at least one flag: {flagged}. Codes marked [INDUSTRY] apply only if the company is bound by them.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("activities"); a.add_argument("file"); a.set_defaults(fn=activities)
    b = sub.add_parser("attrition"); b.add_argument("file"); b.add_argument("--as-of", required=True); b.add_argument("--step", type=int, default=7); b.set_defaults(fn=attrition)
    c = sub.add_parser("support"); c.add_argument("file"); c.add_argument("--year", type=int, required=True); c.add_argument("--cap", type=float, required=True); c.set_defaults(fn=support)
    e = sub.add_parser("partners"); e.add_argument("file"); e.set_defaults(fn=partners)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
