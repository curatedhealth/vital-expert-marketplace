#!/usr/bin/env python3
"""Access funnel: stage-to-stage conversion per market, against the person's pass rules.

Inputs
  counts.csv   one row per market and period, one column per funnel stage, in order.
               Example header: market,period,prescribed_or_approved,code_redeemed,active_week_4,repeat_prescription
               Counts are the buyer's own data. Blank means not measured.
  rules.json   optional. The pass rules the person set, in their words and numbers:
               {"DE": {"code_redeemed": {"min_rate": 0.80, "owner": "Head of Patient Services",
                        "rule": "At least 8 in 10 prescriptions become an activated code"}}}
               min_rate is the minimum conversion from the previous stage.

Output
  A table per market and period: each stage, its count, conversion from the previous stage,
  the person's rule, pass or miss, and the owner they named. The first missed stage is
  marked as the stall point. Official reference rates (references/uptake-measures.md) are
  shown beside the rate for context only; they are national averages, not targets.

The script never sets a rule and never names an owner. A stage without a rule is "no rule set".

Usage: python3 access_funnel.py counts.csv [--rules rules.json] [--json]
"""
import argparse
import csv
import json
import sys

# National reference rates, for context only (Germany, GKV-Spitzenverband report of
# 1 April 2026, period to 31 December 2025). See references/uptake-measures.md.
REFERENCE = {
    ("DE", "code_redeemed"): (0.82, "DE national: 82% of DiGA prescribed or approved were activated, 18% of codes never redeemed (GKV report of 1 April 2026, period to 31 December 2025)"),
    ("DE", "repeat_prescription"): (0.17, "DE national: 17% of people who activated a DiGA received a repeat prescription (GKV report of 1 April 2026); base is activations, so compare with care"),
}

ID_COLUMNS = ("market", "period")


def load_rules(path):
    if not path:
        return {}
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def to_int(value):
    value = (value or "").strip().replace(",", "")
    if value == "":
        return None
    return int(float(value))


def analyse(counts_path, rules):
    with open(counts_path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        stages = [c for c in reader.fieldnames if c not in ID_COLUMNS]
        rows = list(reader)
    report = []
    for row in rows:
        market = row.get("market", "").strip()
        period = row.get("period", "").strip()
        market_rules = rules.get(market, {})
        lines = []
        stall = None
        previous = None
        for stage in stages:
            count = to_int(row.get(stage))
            rate = None
            if previous not in (None, 0) and count is not None:
                rate = count / previous
            rule = market_rules.get(stage)
            verdict = "no rule set"
            if rule and "min_rate" in rule:
                if rate is None:
                    verdict = "not measurable [GAP]"
                elif rate >= rule["min_rate"]:
                    verdict = "pass"
                else:
                    verdict = "miss"
                    if stall is None:
                        stall = stage
            ref = REFERENCE.get((market, stage))
            lines.append({
                "stage": stage,
                "count": count,
                "rate_from_previous": None if rate is None else round(rate, 3),
                "rule": rule.get("rule") if rule else None,
                "min_rate": rule.get("min_rate") if rule else None,
                "verdict": verdict,
                "owner": rule.get("owner") if rule else None,
                "reference": ref[1] if ref else None,
            })
            previous = count if count is not None else None
        report.append({"market": market, "period": period, "stall_point": stall, "stages": lines})
    return report


def pct(x):
    return "" if x is None else f"{x * 100:.0f}%"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("counts")
    ap.add_argument("--rules")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    report = analyse(args.counts, load_rules(args.rules))
    if args.json:
        json.dump(report, sys.stdout, ensure_ascii=False, indent=2)
        print()
        return
    for block in report:
        print(f"\n### {block['market']} · {block['period']}")
        print(f"Stall point: {block['stall_point'] or 'none against the rules set'}\n")
        print("| Stage | Count | From previous | Your rule | Result | Owner | National reference (context) |")
        print("|---|---|---|---|---|---|---|")
        for s in block["stages"]:
            print(f"| {s['stage']} | {'' if s['count'] is None else s['count']} | {pct(s['rate_from_previous'])} | "
                  f"{s['rule'] or ''} | {s['verdict']} | {s['owner'] or ''} | {s['reference'] or ''} |")


if __name__ == "__main__":
    main()
