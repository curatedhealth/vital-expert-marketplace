#!/usr/bin/env python3
"""Outcome attainment and a customer health view from the person's own account file,
against targets the person sets. Nothing is sent anywhere; no target is ever invented.

Files
  ACCOUNTS.csv  one row per account, period and measure (aggregates only, no patient rows):
      account_id, period_end (YYYY-MM-DD), measure, numerator, denominator,
      denominator_basis (eligible, enrolled, invited, activated, ... as the person states it),
      value (optional; computed as numerator / denominator when blank),
      source_type (product_log, customer_report, prom_aggregate, survey, ...)
  TARGETS.json  the person's measures, targets and health rule:
      {"set_by": "...", "set_on": "YYYY-MM-DD", "version": "...",
       "measures": {"<measure>": {"label": "...", "kind": "uptake|use|prom_aggregate|service|economic|...",
                                   "direction": "higher|lower", "target": 0.5,
                                   "denominator_basis": "eligible" (optional, the basis the person requires)}},
       "accounts": {"<account_id>": {"<measure>": {"target": 0.4}}}   (optional per-account overrides),
       "health_rule": {"type": "all" | "min_met" | "none", "measures": [...], "min_met": 2} (optional),
       "adopted_rules": ["day_one_open_blocks"] (optional; only rules the person adopted)}
  META.csv (optional)  account_id, go_live, support_ended, day_one_open (yes/no)
  NOTES.csv            note_id, account_id, sent_on, author, measure, period_end, stated_value, claim

Subcommands
  attain      per account and measure: value, target, met / missed / not measured, gap to target.
  health      per account: measures met under the person's health rule; no rule, no status.
  thresholds  per measure: accounts meeting the target per period, targets no account met,
              measures with no data in the latest period, and (with --previous) target changes
              between versions and the accounts each change turns to met.
  notes       matches each value note to a signal row: supported, value differs, or no signal row.

Labels printed on every run: uptake, use and customer-reported outcome aggregates are not clinical
evidence; an outcome aggregate from an uncontrolled customer cohort is not evidence of effect.

Usage: python3 account_health.py SUBCOMMAND ACCOUNTS.csv --targets TARGETS.json [options]
"""
import argparse
import csv
import json
import sys
from collections import defaultdict
from datetime import date

LABEL = ("Label: these are uptake, use and customer-reported figures. They are not clinical evidence; "
         "an outcome aggregate from a customer cohort without a comparator is not evidence of effect.")


def d(s):
    s = (s or "").strip()
    return date.fromisoformat(s) if s else None


def read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        return [{k.strip(): (v or "").strip() for k, v in r.items()} for r in csv.DictReader(fh)]


def num(s):
    s = (s or "").strip()
    if not s:
        return None
    return float(s)


def load_accounts(path):
    out = []
    for r in read_csv(path):
        v = num(r.get("value"))
        n, den = num(r.get("numerator")), num(r.get("denominator"))
        computed = False
        if v is None and n is not None and den:
            v, computed = n / den, True
        r["_value"], r["_computed"], r["_n"], r["_den"] = v, computed, n, den
        out.append(r)
    return out


def fmt(v):
    if v is None:
        return "n/a"
    if float(v).is_integer() and abs(v) >= 10:
        return f"{int(v):,}"
    return f"{v:.3f}".rstrip("0").rstrip(".") if abs(v) < 10 else f"{v:,.1f}"


def target_for(t, account, measure):
    base = dict(t.get("measures", {}).get(measure, {}))
    base.update(t.get("accounts", {}).get(account, {}).get(measure, {}))
    return base


def judge(value, spec):
    """Return status and gap. Status only when the person set a target."""
    if "target" not in spec or spec.get("target") is None:
        return "no target set", None
    if value is None:
        return "not measured [GAP]", None
    tgt = float(spec["target"])
    direction = spec.get("direction", "higher")
    if direction == "lower":
        return ("met" if value <= tgt else "missed"), value - tgt
    return ("met" if value >= tgt else "missed"), value - tgt


def latest_period(rows):
    ps = sorted({r["period_end"] for r in rows if r.get("period_end")})
    return ps[-1] if ps else None


def attain_table(rows, t, period):
    """Return list of dicts for one period across every account x target measure."""
    accounts = sorted({r["account_id"] for r in rows})
    idx = {(r["account_id"], r["period_end"], r["measure"]): r for r in rows}
    measures = list(t.get("measures", {}).keys())
    out = []
    for a in accounts:
        for m in measures:
            spec = target_for(t, a, m)
            r = idx.get((a, period, m))
            v = r["_value"] if r else None
            status, gap = judge(v, spec)
            flags = []
            if r:
                need = spec.get("denominator_basis")
                have = r.get("denominator_basis", "")
                if need and have and need.lower() != have.lower():
                    flags.append(f"denominator is '{have}', your target needs '{need}' (CS27)")
                    if status in ("met", "missed"):
                        status = f"not comparable (would read {status})"
                if need and not have:
                    flags.append("denominator basis not stated")
                if r["_computed"]:
                    flags.append("value computed from numerator/denominator")
                if r.get("source_type"):
                    flags.append(f"source: {r['source_type']}")
            out.append({"account": a, "measure": m, "kind": spec.get("kind", "not stated"),
                        "value": v, "target": spec.get("target"), "direction": spec.get("direction", "higher"),
                        "status": status, "gap": gap, "n": r["_den"] if r else None, "flags": flags})
    return out


def cmd_attain(args):
    t = json.load(open(args.targets))
    rows = load_accounts(args.file)
    period = args.period or latest_period(rows)
    tab = attain_table(rows, t, period)
    print(f"Outcome attainment, period ending {period}. Targets: set by {t.get('set_by', 'not stated')}, "
          f"version {t.get('version', 'not stated')}, set on {t.get('set_on', 'not stated')}.")
    print("| Account | Measure | Kind | Value | Your target | Status | Gap to target | Denominator | Notes |")
    print("|---|---|---|---|---|---|---|---|---|")
    for x in tab:
        tgt = "none" if x["target"] is None else (("at most " if x["direction"] == "lower" else "at least ") + fmt(float(x["target"])))
        print(f"| {x['account']} | {x['measure']} | {x['kind']} | {fmt(x['value'])} | {tgt} | {x['status']} | "
              f"{fmt(x['gap'])} | {fmt(x['n'])} | {'; '.join(x['flags'])} |")
    met = sum(x["status"] == "met" for x in tab)
    miss = sum(x["status"] == "missed" for x in tab)
    nm = sum(x["status"].startswith("not measured") for x in tab)
    print(f"\nCells: {len(tab)}; met {met}; missed {miss}; not measured {nm}.")
    print(LABEL)


def cmd_health(args):
    t = json.load(open(args.targets))
    rows = load_accounts(args.file)
    period = args.period or latest_period(rows)
    tab = attain_table(rows, t, period)
    meta = {r["account_id"]: r for r in read_csv(args.meta)} if args.meta else {}
    as_of = d(args.as_of) if args.as_of else None
    rule = t.get("health_rule") or {"type": "none"}
    rtype = rule.get("type", "none")
    rmeasures = rule.get("measures") or list(t.get("measures", {}).keys())
    adopted = set(t.get("adopted_rules", []))
    by_acc = defaultdict(list)
    for x in tab:
        by_acc[x["account"]].append(x)
    print(f"Health view, period ending {period}. Rule: {rtype}"
          + (f" (measures: {', '.join(rmeasures)}" + (f"; at least {rule.get('min_met')} met" if rtype == 'min_met' else "") + ")" if rtype != "none" else " (no rule set: counts only, no status)")
          + (f". Adopted rules: {', '.join(sorted(adopted))}" if adopted else ""))
    print("| Account | Met | Missed | Not measured or not comparable | Health under your rule | Day-one workflow open | Months since support ended |")
    print("|---|---|---|---|---|---|---|")
    for a in sorted(by_acc):
        xs = [x for x in by_acc[a] if x["measure"] in rmeasures]
        met = [x["measure"] for x in xs if x["status"] == "met"]
        missed = [x["measure"] for x in xs if x["status"] == "missed"]
        nm = [x["measure"] for x in xs if x["status"].startswith(("not measured", "not comparable"))]
        if rtype == "all":
            status = "meets your rule" if len(met) == len(xs) else "misses your rule"
            if nm and not missed:
                status = "not decidable: " + ", ".join(nm) + " not measured or not comparable"
        elif rtype == "min_met":
            k = int(rule.get("min_met", len(xs)))
            status = "meets your rule" if len(met) >= k else ("misses your rule" if len(met) + len(nm) < k else f"not decidable: {len(nm)} not measured")
        else:
            status = "no rule set"
        m = meta.get(a, {})
        day1 = m.get("day_one_open", "") or "not stated"
        if "day_one_open_blocks" in adopted and day1.lower() in ("yes", "y", "true") and status == "meets your rule":
            status = "not marked healthy: day-one workflow open (rule you adopted)"
        months = "not stated"
        if m.get("support_ended") and as_of:
            se = d(m["support_ended"])
            mo = (as_of.year - se.year) * 12 + as_of.month - se.month - (1 if as_of.day < se.day else 0)
            months = f"{mo}" + (" (6 or more: maintenance window reached, CS26, CS30)" if mo >= 6 else " (under 6)")
        print(f"| {a} | {len(met)} | {len(missed)} {('(' + ', '.join(missed) + ')') if missed else ''} | {len(nm)} | {status} | {day1} | {months} |")
    print("\nNo score, color or average across measures is computed. " + LABEL)


def cmd_thresholds(args):
    t = json.load(open(args.targets))
    rows = load_accounts(args.file)
    periods = sorted({r["period_end"] for r in rows})
    latest = periods[-1] if periods else None
    measures = list(t.get("measures", {}).keys())
    print(f"Threshold review. Targets version {t.get('version', 'not stated')} set by {t.get('set_by', 'not stated')} on {t.get('set_on', 'not stated')}. Periods in file: {', '.join(periods)}.")
    print("| Measure | Your target | " + " | ".join(f"Met at {p}" for p in periods) + " | Flag |")
    print("|---|---|" + "---|" * len(periods) + "---|")
    ever_met = {}
    for m in measures:
        cells, flags, any_met = [], [], False
        for p in periods:
            tab = [x for x in attain_table(rows, t, p) if x["measure"] == m]
            measured = [x for x in tab if not x["status"].startswith("not measured")]
            met = sum(x["status"] == "met" for x in tab)
            any_met = any_met or met > 0
            cells.append(f"{met} of {len(measured)} measured")
        latest_rows = [r for r in rows if r["measure"] == m and r["period_end"] == latest and r["_value"] is not None]
        if not any_met:
            flags.append("no account has met this target in any period")
        if not latest_rows:
            flags.append(f"no data in the latest period ({latest}): is it still stored?")
        else:
            have = {r["account_id"] for r in latest_rows}
            missing = sorted({r["account_id"] for r in rows} - have)
            if missing:
                flags.append(f"no data at {latest} for {', '.join(missing)}")
        nc = [x["account"] for x in attain_table(rows, t, latest) if x["measure"] == m and x["status"].startswith("not comparable")]
        if nc:
            flags.append(f"denominator basis differs from your target for {', '.join(nc)}")
        spec = t["measures"][m]
        tgt = ("at most " if spec.get("direction") == "lower" else "at least ") + fmt(float(spec["target"])) if spec.get("target") is not None else "none"
        print(f"| {m} | {tgt} | " + " | ".join(cells) + f" | {'; '.join(flags) or 'none'} |")
        ever_met[m] = any_met
    ov = t.get("accounts", {})
    if ov:
        print("\nAccount-specific targets in this version: " + "; ".join(
            f"{a}: " + ", ".join(f"{m} {v.get('target')}" for m, v in ms.items()) for a, ms in sorted(ov.items())))
    extra = sorted({r["measure"] for r in rows} - set(measures))
    if extra:
        print(f"\nMeasures in the account file with no target: {', '.join(extra)}.")
    if args.previous:
        old = json.load(open(args.previous))
        print(f"\nTarget changes from version {old.get('version', 'not stated')} to {t.get('version', 'not stated')} (latest period {latest}):")
        print("| Measure | Old target | New target | Change | Accounts met under old | Accounts met under new | Accounts turned to met by the change |")
        print("|---|---|---|---|---|---|---|")
        for m in sorted(set(measures) | set(old.get("measures", {}))):
            o = old.get("measures", {}).get(m, {})
            n = t.get("measures", {}).get(m, {})
            if o.get("target") == n.get("target") and o.get("direction") == n.get("direction"):
                continue
            old_tab = {x["account"]: x for x in attain_table(rows, old, latest) if x["measure"] == m}
            new_tab = {x["account"]: x for x in attain_table(rows, t, latest) if x["measure"] == m}
            om = {a for a, x in old_tab.items() if x["status"] == "met"}
            nm = {a for a, x in new_tab.items() if x["status"] == "met"}
            if o.get("target") is None:
                ch = "added"
            elif n.get("target") is None:
                ch = "removed"
            else:
                direction = n.get("direction", "higher")
                easier = (float(n["target"]) < float(o["target"])) if direction == "higher" else (float(n["target"]) > float(o["target"]))
                ch = "eased (easier to meet)" if easier else "tightened (harder to meet)"
            print(f"| {m} | {o.get('target', 'none')} | {n.get('target', 'none')} | {ch} | {len(om)} | {len(nm)} | {', '.join(sorted(nm - om)) or 'none'} |")
        oo, no = old.get("accounts", {}), t.get("accounts", {})
        for a in sorted(set(oo) | set(no)):
            for m in sorted(set(oo.get(a, {})) | set(no.get(a, {}))):
                ot, nt = oo.get(a, {}).get(m, {}).get("target"), no.get(a, {}).get(m, {}).get("target")
                if ot != nt:
                    print(f"Account-specific target for {a}, {m}: {ot if ot is not None else 'none'} in the previous version, {nt if nt is not None else 'none'} now.")
        print("A target eased after the results were seen, turning accounts to met, is a finding for the person's review; the script does not judge whether the change was justified.")


def cmd_notes(args):
    rows = load_accounts(args.file)
    notes = read_csv(args.notes)
    idx = {(r["account_id"], r["period_end"], r["measure"]): r for r in rows}
    tol = args.tol
    print(f"Value evidence check: {len(notes)} notes against the account file (tolerance {tol} on stated values, set by you).")
    print("| Note | Account | Sent on | Author | Measure | Period | Stated | In the account file | Status |")
    print("|---|---|---|---|---|---|---|---|---|")
    counts = defaultdict(int)
    for n in notes:
        key = (n.get("account_id", ""), n.get("period_end", ""), n.get("measure", ""))
        r = idx.get(key)
        stated = num(n.get("stated_value"))
        if not n.get("measure"):
            status = "unsupported: the note names no measure"
            have = "n/a"
        elif r is None or r["_value"] is None:
            status = "unsupported: no signal row for this account, measure and period"
            have = "none"
        else:
            have = fmt(r["_value"])
            if stated is None:
                status = "signal row exists; the note states no value to compare"
            elif abs(stated - r["_value"]) <= tol:
                status = "supported by the signal row"
            else:
                status = "value differs from the signal row"
        counts[status.split(":")[0]] += 1
        print(f"| {n.get('note_id')} | {n.get('account_id')} | {n.get('sent_on')} | {n.get('author') or 'not stated'} | {n.get('measure') or 'none'} | {n.get('period_end') or 'none'} | {fmt(stated)} | {have} | {status} |")
    print("\n" + "; ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
    print("A matched number is not a cleared claim: wording that states or implies clinical effect, cost saving or comparison stops for the person's owner. " + LABEL)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    for name in ("attain", "health", "thresholds", "notes"):
        s = sub.add_parser(name)
        s.add_argument("file", help="ACCOUNTS.csv")
        if name != "notes":
            s.add_argument("--targets", required=True)
        if name in ("attain", "health"):
            s.add_argument("--period", help="period_end to read (default: latest in the file)")
        if name == "health":
            s.add_argument("--meta", help="META.csv (optional)")
            s.add_argument("--as-of", help="YYYY-MM-DD, for months since support ended")
        if name == "thresholds":
            s.add_argument("--previous", help="previous TARGETS.json, to show changes")
        if name == "notes":
            s.add_argument("--notes", required=True)
            s.add_argument("--tol", type=float, default=0.0, help="tolerance you set for rounding (default 0)")
    a = p.parse_args()
    {"attain": cmd_attain, "health": cmd_health, "thresholds": cmd_thresholds, "notes": cmd_notes}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
