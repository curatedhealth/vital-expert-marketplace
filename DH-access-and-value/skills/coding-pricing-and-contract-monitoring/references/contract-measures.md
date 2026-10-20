# Contract performance measures

Interpretive reference for tasks A2 and B1. Defines what is computed from the person's data and which sourced rules give it meaning. Rows cited from `coding-pricing-sources.md` and `outcomes-contracting-sources.md` (by topic). Read on 19 October 2026; not owner-reviewed.

## The measures

| Measure | Formula | Data needed (the person's) | What gives it meaning |
|---|---|---|---|
| Denial rate | denied / submitted | Claims submitted and denied per period | US billing conditions (US11 to US15); OIG finding on incomplete RPM components (MO4) as a risk signal only |
| Paid rate | paid / submitted | Claims paid | Same |
| Unresolved claims | submitted - paid - denied | All three counts | Pending, appealed or not yet adjudicated |
| Realized unit price | paid amount / claims paid | Paid amount | Compare with the agreed amount; for Medicare, with the national amount before geographic adjustment (US8, US9) |
| Realization | realized / agreed | Agreed amount from the contract | Below 1 means less was paid than agreed per unit |
| Volume against tiers | units so far in the contract year vs tier thresholds | Units dispensed or billed | Contract tiers; German statutory floors from 1 January 2027 (DE3) |
| Outcome component at stake | outcome share x payer portion x agreed amount x units paid | Outcome share from the contract; payer portion 1 unless the outcome share applies to part of the amount | German minimum 20 percent (DE2); ACCESS withhold 50 percent of the Medicare portion, which is 80 percent of the allowed amount, so payer portion 0.8 (BH initial $72 of $180) (US32; outcomes file, "ACCESS: Medicare portion and payment basis") |
| Outcome component earned | at stake x attainment | Attainment under the contract's definition | ACCESS: full payment at 50 percent attainment, proportional below, reduction capped at 50 percent (outcomes file, "ACCESS: attainment threshold and formula") |

`scripts/contract_performance.py` computes all of these from a CSV.

## Sourced rules that shape the measures

| Market | Rule | Row |
|---|---|---|
| Germany | Outcome-linked share at least 20 percent from 1 January 2026 | DE2 |
| Germany | Volume discount from 1 January 2027: at least 2 percent above 3,000 units a year, at least 30 percent above 100,000 | DE3 |
| Germany | Group maximum falls to 75 percent (permanent) or 60 percent (trial) above 10,000 redeemed codes; manufacturer must notify at 2,001 and 10,001 | DE15, DE16 |
| Germany | How the volume discount and the maximum reductions interact is not sourced | Coding file Changes and conflicts 8 |
| Germany | Framework leaves outcome measures and attainment method to the parties | Outcomes file, "Framework agreement: how outcome components are defined" |
| US ACCESS | Monthly payments capped at 50 percent; rest reconciled after 12 months; outcome attainment threshold 50 percent; substitute spend threshold 90 percent | US32, US33 |
| US ACCESS | Patient counts as a success only if all required measures are reported and met; lost to follow-up stays in the denominator | Outcomes file, "ACCESS: all-or-nothing per patient" |
| US ACCESS | Claims are zero-paid by MACs; CMS pays, less 2 percent sequestration | US35 |
| US Medicare | G0552 contractor priced; MAC rates reported inconsistent | US19 |

## Rules for using the measures

- Every count, price and attainment figure is the person's. The model does not estimate missing ones.
- Attainment of an outcome component is a contract measure, not clinical evidence.
- Statutory floors are facts about the law, not the person's contract terms; show both when they differ.
- Do not extrapolate a quarter to a year or forecast tier crossings.
