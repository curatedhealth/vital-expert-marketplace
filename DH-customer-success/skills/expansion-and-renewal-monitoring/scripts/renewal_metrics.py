#!/usr/bin/env python3
"""Renewal and expansion figures from the person's own account file, on definitions the person states.

No source defines customer health, renewal rate, churn, net revenue retention or expansion
for digital health (research file CUSTOMER_SUCCESS_IMPLEMENTATION.md, "Not sourced"). This
script therefore sets no definition of its own. It reads the person's definitions from a
JSON file, refuses to run when one it needs is missing, and prints the formula it used
beside every figure. Nothing is sent anywhere.

Subcommands

  horizon     Accounts whose renewal date falls inside the person's horizon.
              Needs in the definitions: as_of, horizon_days. Optional: not_ready_if
              (a list of {"field": ..., "op": ..., "value": ...} rules the person adopted).
  cohort      Renewal cohort: renewed, lost, open, excluded; account-count rate and,
              if the person names value fields, value retention with and without expansion.
              Needs: period_start, period_end, status_field, renewed_values, lost_values,
              open_values, open_in_denominator. Optional: exclude (field -> list of values),
              value_before_field, value_after_field, loss_reason_field, currency.
  expansion   Offers matched to signed expansions. Needs: offer_field, offer_outcome_field,
              signed_values, refused_values, offer_open_values, offer_open_in_denominator.
              Optional: refusal_reason_field, offer_made_values (default ["yes"]),
              offer_period_start, offer_period_end, offer_date_field (default offer_date).

Account file: CSV, one row per account and renewal event. Column names are the person's;
the definitions file names them. Always present: account_id, contract_id, renewal_date
(YYYY-MM-DD). Dates in ISO form.

Usage:
  python3 renewal_metrics.py horizon   ACCOUNTS.csv DEFINITIONS.json
  python3 renewal_metrics.py cohort    ACCOUNTS.csv DEFINITIONS.json
  python3 renewal_metrics.py expansion ACCOUNTS.csv DEFINITIONS.json
"""
import csv
import json
import sys
from collections import Counter, defaultdict
from datetime import date, timedelta

OPS = {
    "eq": lambda a, b: a == str(b),
    "ne": lambda a, b: a != str(b),
    "gt": lambda a, b: _num(a) is not None and _num(a) > float(b),
    "lt": lambda a, b: _num(a) is not None and _num(a) < float(b),
    "in": lambda a, b: a in [str(x) for x in b],
}


def _num(s):
    try:
        return float(str(s).replace(",", "").strip())
    except (TypeError, ValueError):
        return None


def d(s):
    s = (s or "").strip()
    return date.fromisoformat(s) if s else None


def full(dt):
    return f"{dt.day} {dt.strftime('%B')} {dt.year}" if dt else "no date"


def rows(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        return [{k.strip(): (v or "").strip() for k, v in r.items()} for r in csv.DictReader(fh)]


def need(defs, keys, sub):
    missing = [k for k in keys if k not in defs or defs[k] in (None, "", [])]
    if missing:
        print(f"Cannot run '{sub}': these definitions are yours to state and are missing: "
              + ", ".join(missing) + ".")
        print("Nothing was computed. Add them to the definitions file and run again.")
        sys.exit(2)


def pct(n, base):
    return f"{100 * n / base:.1f} percent" if base else "not computable (denominator 0)"


def money(x, cur):
    return f"{x:,.0f} {cur}".strip()


def header(defs, sub):
    print(f"Renewal metrics, '{sub}', on the definitions you stated (evidence class O, owner-stated).")
    if defs.get("definitions_owner"):
        print(f"Definitions owner as you named them: {defs['definitions_owner']}")
    else:
        print("Definitions owner: owner not named.")


def horizon(data, defs):
    need(defs, ["as_of", "horizon_days"], "horizon")
    header(defs, "horizon")
    as_of = d(defs["as_of"])
    end = as_of + timedelta(days=int(defs["horizon_days"]))
    rules = defs.get("not_ready_if", [])
    print(f"Window: renewal date after {full(as_of)} and on or before {full(end)} "
          f"({defs['horizon_days']} days, your horizon).")
    inside = sorted([r for r in data if r.get("renewal_date") and as_of < d(r["renewal_date"]) <= end],
                    key=lambda r: r["renewal_date"])
    past = [r for r in data if r.get("renewal_date") and d(r["renewal_date"]) <= as_of
            and r.get(defs.get("status_field", "status"), "") in defs.get("open_values", [])]
    print(f"Accounts in the window: {len(inside)} of {len(data)}")
    if rules:
        print("Readiness rule you adopted: not ready if any of "
              + "; ".join(f"{x['field']} {x['op']} {x['value']}" for x in rules))
    else:
        print("No readiness rule stated: readiness column left blank.")
    print("| Account | Contract | Renewal date | Days to renewal | Readiness (your rule) | Rule hit |")
    print("|---|---|---|---|---|---|")
    for r in inside:
        hits = [f"{x['field']} {x['op']} {x['value']}" for x in rules
                if OPS[x["op"]](r.get(x["field"], ""), x["value"])]
        ready = "" if not rules else ("not ready" if hits else "ready")
        days = (d(r["renewal_date"]) - as_of).days
        print(f"| {r['account_id']} | {r['contract_id']} | {full(d(r['renewal_date']))} | {days} | {ready} | "
              f"{'; '.join(hits)} |")
    if past:
        print("Renewal date already passed and status still open (check the record): "
              + ", ".join(f"{r['account_id']} ({r['contract_id']}, {full(d(r['renewal_date']))})" for r in past))


def in_period(r, defs, field="renewal_date"):
    ps, pe = d(defs.get("period_start")), d(defs.get("period_end"))
    v = d(r.get(field))
    if v is None:
        return False
    return (ps is None or v >= ps) and (pe is None or v <= pe)


def excluded(r, defs):
    for f, vals in (defs.get("exclude") or {}).items():
        if r.get(f, "") in [str(v) for v in vals]:
            return f"{f} = {r.get(f)}"
    return None


def cohort(data, defs):
    need(defs, ["period_start", "period_end", "status_field", "renewed_values", "lost_values",
                "open_values", "open_in_denominator"], "cohort")
    header(defs, "cohort")
    sf = defs["status_field"]
    cur = defs.get("currency", "")
    print(f"Cohort: accounts with a renewal date from {full(d(defs['period_start']))} to "
          f"{full(d(defs['period_end']))} (your period).")
    cohort_rows = [r for r in data if in_period(r, defs)]
    exc = [(r, excluded(r, defs)) for r in cohort_rows if excluded(r, defs)]
    kept = [r for r in cohort_rows if not excluded(r, defs)]
    ren = [r for r in kept if r.get(sf) in defs["renewed_values"]]
    lost = [r for r in kept if r.get(sf) in defs["lost_values"]]
    opn = [r for r in kept if r.get(sf) in defs["open_values"]]
    unk = [r for r in kept if r not in ren and r not in lost and r not in opn]
    print(f"In period: {len(cohort_rows)}; excluded by your rule: {len(exc)}; counted: {len(kept)}")
    for r, why in exc:
        print(f"  excluded {r['account_id']} ({r['contract_id']}): {why}")
    print(f"Renewed ({sf} in {defs['renewed_values']}): {len(ren)} | Lost ({defs['lost_values']}): {len(lost)} | "
          f"Open ({defs['open_values']}): {len(opn)} | Status not in your lists: {len(unk)}")
    if unk:
        print("  Not classified, your status lists do not cover them (kept out of every figure, check the record): "
              + ", ".join(f"{r['account_id']} ({r.get(sf) or 'blank'})" for r in unk))
    den = len(ren) + len(lost) + (len(opn) if defs["open_in_denominator"] else 0)
    den_txt = "renewed + lost" + (" + open" if defs["open_in_denominator"] else "")
    print()
    print("| Figure | Formula used (your definitions) | Value |")
    print("|---|---|---|")
    print(f"| Account renewal rate | renewed / ({den_txt}) = {len(ren)} / {den} | {pct(len(ren), den)} |")
    if not defs["open_in_denominator"] and opn:
        print(f"| Note | open accounts are outside the denominator by your definition: {len(opn)} | |")
    vb, va = defs.get("value_before_field"), defs.get("value_after_field")
    if vb and va:
        base = [r for r in ren + lost + (opn if defs["open_in_denominator"] else [])]
        missing = [r["account_id"] for r in base if _num(r.get(vb)) is None
                   or (r in ren and _num(r.get(va)) is None)]
        if missing:
            print(f"| Value figures | not computed: value missing for {', '.join(missing)} | [GAP] |")
        else:
            start = sum(_num(r[vb]) for r in base)
            lost_v = sum(_num(r[vb]) for r in lost)
            contr = sum(max(0.0, _num(r[vb]) - _num(r[va])) for r in ren)
            expn = sum(max(0.0, _num(r[va]) - _num(r[vb])) for r in ren)
            open_v = sum(_num(r[vb]) for r in opn) if defs["open_in_denominator"] else 0.0
            print(f"| Starting value of the counted cohort | sum of {vb} over {den_txt} | {money(start, cur)} |")
            print(f"| Value lost | sum of {vb} over lost | {money(lost_v, cur)} |")
            print(f"| Contraction | sum over renewed of max(0, {vb} - {va}) | {money(contr, cur)} |")
            print(f"| Expansion | sum over renewed of max(0, {va} - {vb}) | {money(expn, cur)} |")
            if defs["open_in_denominator"]:
                print(f"| Open value (counted as not retained until signed) | sum of {vb} over open | {money(open_v, cur)} |")
            gross = start - lost_v - contr - open_v
            net = gross + expn
            print(f"| Value retained without expansion | (start - lost - contraction"
                  f"{' - open' if defs['open_in_denominator'] else ''}) / start = {money(gross, cur)} / {money(start, cur)} "
                  f"| {pct(gross, start)} |")
            print(f"| Value retained with expansion | (start - lost - contraction"
                  f"{' - open' if defs['open_in_denominator'] else ''} + expansion) / start = {money(net, cur)} / "
                  f"{money(start, cur)} | {pct(net, start)} |")
    print()
    rf = defs.get("loss_reason_field")
    if lost:
        print("Lost accounts with contract ids" + (f" and the reason recorded in '{rf}':" if rf else ":"))
        for r in lost:
            print(f"  {r['account_id']} | {r['contract_id']} | {full(d(r['renewal_date']))}"
                  + (f" | {r.get(rf) or 'no reason recorded [GAP]'}" if rf else ""))
        if rf:
            c = Counter((r.get(rf) or "no reason recorded") for r in lost)
            print("Losses by recorded reason (kept separate, never merged): "
                  + "; ".join(f"{k}: {v}" for k, v in c.most_common()))
    if opn:
        print("Open accounts (still in the cohort" + (", counted in the denominator" if defs["open_in_denominator"]
                                                      else ", outside the denominator by your definition") + "):")
        for r in opn:
            print(f"  {r['account_id']} | {r['contract_id']} | {full(d(r['renewal_date']))}")
    print("Renewed accounts with contract ids: " + ", ".join(f"{r['account_id']} ({r['contract_id']})" for r in ren))


def expansion(data, defs):
    need(defs, ["offer_field", "offer_outcome_field", "signed_values", "refused_values", "offer_open_values",
                "offer_open_in_denominator"], "expansion")
    header(defs, "expansion")
    of, oo = defs["offer_field"], defs["offer_outcome_field"]
    yes = [str(v) for v in defs.get("offer_made_values", ["yes"])]
    offers = [r for r in data if r.get(of, "") in yes]
    if defs.get("offer_period_start") or defs.get("offer_period_end"):
        win = {"period_start": defs.get("offer_period_start"), "period_end": defs.get("offer_period_end")}
        offers = [r for r in offers if in_period(r, win, defs.get("offer_date_field", "offer_date"))]
        print(f"Offers dated from {full(d(win['period_start']))} to {full(d(win['period_end']))} (your offer period).")
    else:
        print("No offer period stated: every offer in the file is counted.")
    signed = [r for r in offers if r.get(oo) in defs["signed_values"]]
    refused = [r for r in offers if r.get(oo) in defs["refused_values"]]
    opn = [r for r in offers if r.get(oo) in defs["offer_open_values"]]
    other = [r for r in offers if r not in signed and r not in refused and r not in opn]
    den = len(signed) + len(refused) + (len(opn) if defs["offer_open_in_denominator"] else 0)
    den_txt = "signed + refused" + (" + open" if defs["offer_open_in_denominator"] else "")
    print(f"Offers made ({of} in {yes}): {len(offers)}")
    print("| Figure | Formula used (your definitions) | Value |")
    print("|---|---|---|")
    print(f"| Offers signed | count of {oo} in {defs['signed_values']} | {len(signed)} |")
    print(f"| Offers refused | count of {oo} in {defs['refused_values']} | {len(refused)} |")
    print(f"| Offers open | count of {oo} in {defs['offer_open_values']} | {len(opn)} |")
    print(f"| Offer acceptance | signed / ({den_txt}) = {len(signed)} / {den} | {pct(len(signed), den)} |")
    if other:
        print("Outcome not in your lists (not counted as signed; a meeting or verbal yes is not a signature unless "
              "your definition says so): " + ", ".join(f"{r['account_id']} ({r.get(oo) or 'blank'})" for r in other))
    rf = defs.get("refusal_reason_field")
    if refused:
        print("Refused offers" + (f" with the reason recorded in '{rf}':" if rf else ":"))
        for r in refused:
            print(f"  {r['account_id']} | {r['contract_id']}" + (f" | {r.get(rf) or 'no reason recorded [GAP]'}" if rf else ""))
    if signed:
        print("Signed: " + ", ".join(f"{r['account_id']} ({r['contract_id']})" for r in signed))


def main():
    if len(sys.argv) != 4 or sys.argv[1] not in ("horizon", "cohort", "expansion"):
        print(__doc__)
        sys.exit(1)
    sub, acc, dfn = sys.argv[1:]
    data = rows(acc)
    defs = json.load(open(dfn, encoding="utf-8"))
    {"horizon": horizon, "cohort": cohort, "expansion": expansion}[sub](data, defs)
    print()
    print("Figures computed on your data and your definitions. They are not benchmarks and set no target. "
          "AI-assisted draft.")


if __name__ == "__main__":
    main()
