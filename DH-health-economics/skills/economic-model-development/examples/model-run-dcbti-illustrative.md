# Worked run: A2 Model inputs and runs, then B1 Results and sensitivity (illustrative inputs, live connector)

Run on 19 October 2026 against the live VITAL Digital Health Library. The product, SleepWell, is fictional and every number is ILLUSTRATIVE, typed for the test. The connector calls and the script runs are real. Saved outputs: `examples/live/analytics_calls_2026-10-19.json`; input file `examples/inputs/dcbti_model_illustrative.json`.

## The request (illustrative)

"We're preparing for a NICE HealthTech conversation on SleepWell, our digital CBT for insomnia app for adults in England. Usual care costs 600 GBP per patient per year. SleepWell adds 250 GBP in year one and saves 120 GBP a year in GP visits. It adds 0.02 QALYs in year one and we assume half of that each later year. Three-year horizon. Run budget impact for 10,000 eligible adults with 5, 10 and 15 percent uptake, and the cost-utility. Show it at 20,000 and 30,000 GBP per QALY. Our HTA lead, Maya Lin, will clear it."

## Calls made

1. `analytics.budget-impact-model {eligible_population: 10000, current_mix: [{name: "Usual care", share: 1, annual_cost_per_patient: 600}], new_treatment_annual_cost_per_patient: 850, uptake_curve: [{year: 1, uptake: 0.05}, {year: 2, uptake: 0.1}, {year: 3, uptake: 0.15}]}`: HTTP 422, nothing counted (register N5).
2. `analytics.scenario-modeler {parameters: {population: 10000, uptake: [0.05, 0.1, 0.15], device_cost: 250, offset: 120}, formula: "population * uptake * (device_cost - offset)", periods: 3, aggregate: "none"}`: 65,000; 130,000; 195,000 (cumulative 390,000).
3. `scripts/he_model.py examples/inputs/dcbti_model_illustrative.json`: same budget impact; cost-utility below.
4. `scripts/sensitivity_summary.py examples/inputs/dcbti_model_illustrative.json`: one-way and scenarios below.
5. Cross-check of the tornado: `analytics.risk-tornado {parameters: {wtp: 20000, d_qaly: 0.02, d_cost: 250}, formula: "wtp * d_qaly - d_cost", periods: 1, aggregate: "sum", parameter_ranges: {wtp: [20000, 20000], d_qaly: [0.01, 0.03], d_cost: [150, 400]}}` returned base 150, d_qaly -50 to 350, d_cost 250 to 0. `scripts/sensitivity_summary.py examples/inputs/crosscheck_tornado_illustrative.json` returned the same numbers, with switching values 0.0125 (d_qaly) and 400 (d_cost).
6. Not done: the ICER tornado. A live `analytics.risk-tornado` on `(cost_new - cost_old) / (qaly_new - qaly_old)` returned -2,016 when the default range pushed qaly_old above qaly_new, ranked as the smallest swing. That is why B1 works on net benefit.

## The answer (short mode, as the skill would hand it over)

**Answer.** On your inputs, SleepWell costs 97.96 GBP less per patient over three years than usual care (discounted at 3.5%) and adds 0.0343 discounted QALYs: the dominant quadrant, so no ICER ratio is reported. Net monetary benefit is 784.55 GBP at your 20,000 threshold and 1,127.84 GBP at 30,000. For 10,000 eligible adults, the net budget impact is 65,000, 130,000 and 195,000 GBP in years 1 to 3. These are hypotheses on your inputs; whether they are acceptable is NICE's call.

**Key inputs (all yours, ILLUSTRATIVE, none checked against a source yet).**

| Input | Value | Source kind |
|---|---|---|
| Usual care cost per year | 600 GBP | Person's figure `[GAP]` source |
| SleepWell cost, year 1 | 250 GBP | Person's figure |
| GP visit saving per year | 120 GBP | Person's assumption `[GAP]` source |
| QALY gain year 1, then halving | 0.02, 0.5 | Person's assumption; value set not stated `[GAP]` |

**Drivers (one-way, at 20,000).** The utility gain moves net benefit most (441.26 to 1,127.84 GBP for 0.01 to 0.03), then waning (647.51 to 1,046.12), the GP saving (610.57 to 958.53; at the low end of your 60 to 180 range the result moves from the dominant to the north-east quadrant) and the year-1 cost (884.55 to 634.55). No input crosses zero net benefit within your ranges. Usual care cost and baseline utility: no range given.

**Scenarios.** Offsets not realized: ICER 7,282 GBP per QALY, north-east. One-year horizon: ICER 6,500. No discounting: still dominant.

**Reference case.** NICE discounts at 3.5% (HE-047) on NHS and PSS costs (HE-037); utilities for a new HealthTech topic come from the UK 5L value set (HE-058, HE-059, HE-062). NICE thresholds: PMG48 states 20,000 to 30,000 GBP (HE-074) and PMG36 states 25,000 to 35,000 GBP (HE-050, HE-051); an open conflict, shown both ways.

**Not shown.** Probabilistic sensitivity analysis `[GAP]`. The budget impact calculator rejected the payload (HTTP 422); the same arithmetic ran on the scenario modeler and the script, which agree.

**Stop and record.** Results for NICE stop for Maya Lin; draft for the owner. Clears it: Maya Lin. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Notes on the run

- The quadrant change on the GP saving is reported as the script reports it (a change within the range), not as a solved point: the script solves switching values for net benefit, not for the quadrant boundary.
- Every number above appears in the script output or the saved connector output for this run.
