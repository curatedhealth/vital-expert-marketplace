# Worked run: A1 Reporting and reference-case check, then A2 Validity and input monitoring (illustrative inputs, live connector)

Run on 19 October 2026. SleepWell is fictional; the methods summary, the model inputs and the "observed" values are ILLUSTRATIVE, typed for the test. The connector calls and the script runs are real.

Files: `examples/inputs/sleepwell_model_description_illustrative.md` (the methods summary checked); `examples/inputs/dcbti_model_illustrative.json` (the model); `examples/inputs/sleepwell_observed_illustrative.json` (the model plus observed-value scenarios); outputs `examples/cheers_check_output_sleepwell.md` and `examples/monitoring_output_sleepwell.md`; connector outputs in `examples/live/`.

## The request (illustrative)

"Here's the methods summary of our SleepWell model for a NICE HealthTech topic expected to launch in 2027. Is it ready? Also, our first-year real-world data show GP savings of 70 GBP a year, not 120, and a utility gain of 0.012, not 0.02. Does the model still hold at 20,000 GBP per QALY? Our HTA lead Maya Lin clears anything external."

## Calls and runs

1. `scripts/cheers_check.py examples/inputs/sleepwell_model_description_illustrative.md --body NICE`.
2. `verify.qualify_source {doi: "10.1177/23814683211061097"}`: gold. `verify.check_claim` on the item 10 rule: "partial" ("the passage does not state the figure"); on a claim opposite to HE-005's passage: "unsupported", not "contradicted" (register N3). Both read by hand; the HE rows stand.
3. `verify.qualify_source {url: NICE PMG48 methods page}`: "inadmissible, no provenance" (register C1); NICE rules cited by row instead.
4. `scripts/he_model.py examples/inputs/dcbti_model_illustrative.json`: recomputation of the base case.
5. `analytics.scenario-modeler` with `population * uptake * (device_cost - offset)`: 65,000, 130,000, 195,000, matching the script's budget impact.
6. `scripts/sensitivity_summary.py examples/inputs/sleepwell_observed_illustrative.json`: observed values as scenarios.

## The answer (short mode, as the skill would hand it over)

**Answer.** In this methods summary, four findings would stop a NICE reviewer: utilities valued with the Dolan 1997 3L tariff for a topic launching after 27 August 2026, where PMG51 requires the UK 5L value set and no 3L utilities in sensitivity analyses (HE-058, HE-061, HE-062); productivity gains in the base case, which NICE excludes from the reference case (HE-038); "cost-effective ... proves its value" at a single 20,000 GBP threshold, where NICE uses no precise maximum and its two manuals state different ranges (HE-049, HE-050, HE-051, HE-074); and costs stated as "the NHS" rather than NHS and PSS (HE-037). On your observed values, the result moves from the dominant quadrant to north-east: ICER 2,283 GBP per QALY, net monetary benefit 364.93 GBP at your 20,000 threshold (base case 784.55). Whether that is acceptable is NICE's call.

**CHEERS items not found in this summary:** 4 (analysis plan), 19 (distributional effects), 21 and 25 (engagement), 28 (conflicts of interest). Items 1 to 3, 5 to 7, 11 to 14, 18, 22, 23 and 26: wording not sourced here `[GAP]`. No score is given (HE-005, DOI 10.1177/23814683211061097).

**Validity evidence.** Face validity: two sleep physicians reviewed structure and inputs (claimed; no record shown). Verification: the base case recomputes (dCost -97.96, dQALY 0.0343). Cross, external, predictive: none shown `[GAP]`; your observed data start external validity.

**Observed versus assumed.** GP saving 120 assumed, 70 observed: dCost turns positive (47.02), ICER 1,370. Utility gain 0.02 assumed, 0.012 observed: still dominant, net benefit 509.92. Both: ICER 2,283. Source, period and population of the observed values: not stated `[GAP]`.

**Also noted.** The sensitivity analysis used plus or minus 20 percent on every input, and a 1.5% discount scenario that NICE allows only if all three HE-048 criteria hold.

**Stop and record.** The review stops for Maya Lin; draft for the owner. Clears it: Maya Lin. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Notes

- Every number above appears in the script outputs or saved connector outputs for this run.
- The threshold of 20,000 GBP is the person's; it is one of the two written NICE ranges, shown as context, not as a verdict.
