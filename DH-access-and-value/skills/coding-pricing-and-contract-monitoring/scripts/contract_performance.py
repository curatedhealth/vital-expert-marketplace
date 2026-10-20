#!/usr/bin/env python3
"""Contract performance: claims, price realization, volume tiers and outcome component,
computed from the person's own CSV and checked against the person's own rules.

Input CSV (one row per contract, route or code, and period; the person's data):
  market,period,payer,route,claims_submitted,claims_paid,claims_denied,paid_amount,
  agreed_unit_price,units_ytd,outcome_share,outcome_attainment[,payer_portion]
  - claims_*: counts. Blank means not measured.
  - paid_amount: total paid in the period, in the contract currency.
  - agreed_unit_price: the contract's agreed amount per unit (per claim, prescription or month).
  - units_ytd: units dispensed or billed so far in the contract year (for volume tiers).
  - outcome_share: share of the agreed amount that depends on outcomes, 0 to 1 (contract term).
  - payer_portion: optional; the share of the agreed amount that the payer pays and that the
    outcome share applies to, 0 to 1. Blank means 1. For ACCESS the agreed amount is the allowed
    amount and the withhold applies to the Medicare portion, 80 percent of it: payer_portion 0.8
    (outcomes file, "ACCESS: Medicare portion and payment basis"; BH initial $72 of $180).
  - outcome_attainment: share of the outcome component earned in the period, 0 to 1, as the
    person measured it under the contract's own definition.

Rules JSON (optional; the person's rules and owners, never set by the script):
  {"DE|GKV-SV|DiGA": {
     "max_denial_rate": {"value": 0.05, "owner": "Head of Revenue Cycle"},
     "min_realization": {"value": 0.98, "owner": "Head of Market Access"},
     "min_outcome_attainment": {"value": 0.8, "owner": "Medical Lead"},
     "volume_tiers": [{"above": 3000, "discount": 0.02}, {"above": 100000, "discount": 0.30}]}}
  Keys are market|payer|route, or market alone.

Output, per row:
  denial rate, paid rate, unresolved claims, realized unit price and realization against the
  agreed price, the volume tier reached and units to the next tier, outcome component at stake
  and earned, each rule pass / miss / no rule set / not measurable, and the stall point (first
  missed rule in the order: claims, price realization, outcome component).

If no tiers are given for a German DiGA row, the statutory minimum tiers from 1 January 2027
(at least 2 percent above 3,000 units a year, at least 30 percent above 100,000; section 134
SGB V, references/contract-measures.md) are shown for reference, labeled as statute, not as
the contract.

The script never sets a rule, never names an owner and never forecasts.

Usage: python3 contract_performance.py data.csv [--rules rules.json] [--json]
"""
import argparse
import csv
import json

STATUTORY_DE_TIERS = [{"above": 3000, "discount": 0.02}, {"above": 100000, "discount": 0.30}]
ORDER = ["max_denial_rate", "min_realization", "min_outcome_attainment"]
STAGE = {"max_denial_rate": "claims (coding and billing)",
         "min_realization": "price realization",
         "min_outcome_attainment": "outcome component"}


def num(v):
    v = (v or "").strip().replace(",", "")
    return None if v == "" else float(v)


def rules_for(rules, row):
    for key in (f"{row['market']}|{row['payer']}|{row['route']}", row["market"]):
        if key in rules:
            return rules[key]
    return {}


def check(rule, value, kind):
    if rule is None:
        return "no rule set"
    if value is None:
        return "not measurable [GAP]"
    if kind == "max":
        return "pass" if value <= rule["value"] else "miss"
    return "pass" if value >= rule["value"] else "miss"


def analyze_row(row, rules):
    r = rules_for(rules, row)
    sub, paid, den = num(row.get("claims_submitted")), num(row.get("claims_paid")), num(row.get("claims_denied"))
    amount, agreed = num(row.get("paid_amount")), num(row.get("agreed_unit_price"))
    units, share, att = num(row.get("units_ytd")), num(row.get("outcome_share")), num(row.get("outcome_attainment"))
    out = {k: row.get(k) for k in ("market", "period", "payer", "route")}
    out["denial_rate"] = round(den / sub, 4) if sub and den is not None else None
    out["paid_rate"] = round(paid / sub, 4) if sub and paid is not None else None
    out["unresolved_claims"] = (sub - paid - den) if None not in (sub, paid, den) else None
    out["realized_unit_price"] = round(amount / paid, 2) if paid and amount is not None else None
    out["realization"] = (round(out["realized_unit_price"] / agreed, 4)
                          if out["realized_unit_price"] is not None and agreed else None)
    tiers = r.get("volume_tiers")
    tier_source = "your contract"
    if not tiers and row.get("market") == "DE":
        tiers, tier_source = STATUTORY_DE_TIERS, "statutory minimum from 1 January 2027 (not your contract)"
    if tiers and units is not None:
        reached = [t for t in tiers if units > t["above"]]
        nxt = [t for t in tiers if units <= t["above"]]
        out["volume_tier"] = {
            "source": tier_source,
            "units_ytd": units,
            "reached": reached[-1] if reached else None,
            "next": nxt[0] if nxt else None,
            "units_to_next": (nxt[0]["above"] - units + 1) if nxt else None,
        }
    else:
        out["volume_tier"] = None
    portion = num(row.get("payer_portion"))
    portion = 1.0 if portion is None else portion
    if None not in (share, agreed, paid):
        at_stake = share * portion * agreed * paid
        out["outcome_component_at_stake"] = round(at_stake, 2)
        out["outcome_component_earned"] = round(at_stake * att, 2) if att is not None else None
    else:
        out["outcome_component_at_stake"] = out["outcome_component_earned"] = None
    out["outcome_attainment"] = att
    values = {"max_denial_rate": out["denial_rate"], "min_realization": out["realization"],
              "min_outcome_attainment": att}
    checks, stall = {}, None
    for key in ORDER:
        rule = r.get(key)
        verdict = check(rule, values[key], "max" if key.startswith("max") else "min")
        checks[key] = {"value": values[key], "rule": rule["value"] if rule else None,
                       "owner": rule.get("owner", "owner not named") if rule else None, "verdict": verdict}
        if verdict == "miss" and stall is None:
            stall = STAGE[key]
    out["checks"] = checks
    out["stall_point"] = stall
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--rules")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    rules = json.load(open(a.rules, encoding="utf-8")) if a.rules else {}
    with open(a.csv, newline="", encoding="utf-8") as fh:
        rows = [analyze_row(r, rules) for r in csv.DictReader(fh)]
    if a.json:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return
    print("Contract performance on your data, against your rules. No forecast; verdicts only where you set a rule.\n")
    for o in rows:
        print(f"{o['market']} | {o['payer']} | {o['route']} | {o['period']}")
        print(f"  claims: denial rate {o['denial_rate']}, paid rate {o['paid_rate']}, unresolved {o['unresolved_claims']}")
        print(f"  price: realized per unit {o['realized_unit_price']}, realization vs agreed {o['realization']}")
        vt = o["volume_tier"]
        if vt:
            reached = f"{vt['reached']['discount']:.0%} above {vt['reached']['above']:,}" if vt["reached"] else "none"
            nxt = (f"{vt['next']['discount']:.0%} above {vt['next']['above']:,}, {vt['units_to_next']:,.0f} units away"
                   if vt["next"] else "none")
            print(f"  volume ({vt['source']}): {vt['units_ytd']:,.0f} units; tier reached {reached}; next {nxt}")
        print(f"  outcome component: at stake {o['outcome_component_at_stake']}, earned {o['outcome_component_earned']}, "
              f"attainment {o['outcome_attainment']}")
        for k, c in o["checks"].items():
            print(f"  rule {k}: value {c['value']} vs {c['rule']} -> {c['verdict']}"
                  + (f" (owner: {c['owner']})" if c["owner"] else ""))
        print(f"  stall point: {o['stall_point'] or 'none against the rules set'}\n")


if __name__ == "__main__":
    main()
