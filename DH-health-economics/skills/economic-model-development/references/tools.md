# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `analytics_risk-tornado`). Counted calls draw on the library key's monthly allowance; a call that returns an error says "Nothing was counted".

Behavior below was observed in live calls on 19 October 2026 with illustrative numbers. Saved outputs: `examples/live/analytics_calls_2026-10-19.json`, `examples/live/verify_calls_2026-10-19.json`, `examples/live/catalogue_and_experts_2026-10-19.json`. Every analytics tool computes only on numbers the person supplies; every result is a hypothesis.

## analytics.budget-impact-model

- Arguments: `eligible_population`, `current_mix` (`name`, `share`, `annual_cost_per_patient`; shares sum to 1), `new_treatment_annual_cost_per_patient`, `uptake_curve` (schema: list of objects).
- Returned HTTP 422 ("Nothing was counted") on three shapes: `uptake_curve` as `[{year, uptake}]` with a one-item mix; `[{year, share}]` with a two-item mix; `[{value}]`. Earlier builds saw 422 on other shapes (register N5).
- Use: try once with the person's inputs. On 422, run the same arithmetic with `analytics.scenario-modeler` (below) or `scripts/he_model.py`, and say the calculator rejected the payload.
- The catalogue job `budget-impact` is listed `available` while its only tool returns 422 (register C12).

## analytics.scenario-modeler

- Exposed and working on 19 October 2026 (earlier builds recorded it as not exposed, register C12).
- Arguments: `parameters` (name to number, or to a list with one value per period), `formula` (arithmetic over the names and `t`), `periods`, `aggregate` (`sum`, `cumulative` or `none`).
- `t` starts at 0. A list parameter is read per period.
- Live: `population * uptake * (device_cost - offset)` with population 10000, uptake [0.05, 0.1, 0.15], device_cost 250, offset 120 returned 65,000, 130,000 and 195,000 (cumulative 390,000), the same as `scripts/he_model.py` on the illustrative model.
- Pitfall: `^` is rejected with HTTP 400; use `**` for powers. `cost / (1 + r) ** t` with cost 1000 and r 0.035 returned 1000, 966.183575 and 933.5107 (sum 2,899.694275), so year index 0 is undiscounted.
- Pitfall: `aggregate: "none"` still returns `cumulative_value` per period and `aggregate_value: null`.
- It has no arms: for a cost-utility model, write one formula for the incremental net monetary benefit, or use `scripts/he_model.py`.

## analytics.risk-tornado

- Exposed and working on 19 October 2026. Same `parameters`, `formula`, `periods` as the scenario modeler, plus `aggregate` (`sum` or `cumulative`; `none` rejected), `variation_pct` (default 0.2) and optional `parameter_ranges` (name to [low, high]).
- Pitfall 1: list parameters are skipped (`skipped_parameters: ["uptake"]`); uptake curves never appear in the tornado. Give a scalar multiplier parameter if the person wants uptake varied.
- Pitfall 2: parameters without a range get plus or minus 20 percent by default. On a utility level that is not a plausible range (0.72 became 0.576 to 0.864). Pass the person's ranges for every parameter; if they have none, say the default was applied and is not theirs.
- Pitfall 3 (do not tornado a ratio): with the ICER formula `(cost_new - cost_old) / (qaly_new - qaly_old)`, qaly_old at its default high (0.864) made the incremental QALY negative and the output -2,016, which the tool ranked as the smallest swing with no flag. Run the tornado on net monetary benefit at the person's threshold, `wtp * d_qaly - d_cost`, which returned base 150, d_qaly 0.01 to 0.03 giving -50 to 350, d_cost 150 to 400 giving 250 to 0; `scripts/sensitivity_summary.py` reproduced these numbers and adds switching values and quadrant flags.

## analytics.vba-price-anchor

- Arguments: `comparator_cost_per_patient`, `incremental_qalys`, `wtp_thresholds` as a plain list of numbers (objects return 422 although the schema says objects, register N5).
- Live: 600, 0.02, [20000, 30000] returned 1,000 and 1,200 per patient, with fixed defaults `non_drug_cost_offset_per_patient: 0` and `units_per_patient: 1` that no argument can set.
- Pitfall: the response cites "NICE (2022). NICE health technology evaluations: the manual", the manual's former title (now PMG36, HE-033), and Neumann 2014 on a $50,000 threshold. The tool's citation is not a source for any threshold: thresholds are the person's (`reference-cases.md` shows what each body states).
- Use only when the person asks for a value-based price ceiling. A ceiling is not a price; price positions belong to dh-commercial (pricing-and-value-proposition) and payer prices to dh-market-access (coding-pricing-and-payer-contracting).

## verify.qualify_source, verify.check_claim, verify.build_record

- For a published input (an effect size, a utility, a unit cost from a paper): `qualify_source` with the DOI, then `check_claim` with the claim, the verbatim passage (`text`, `locator`) and the full returned source object (register C18).
- Live: CHEERS 2022 DOI rated "gold". A method rule in the passage's own words ("Report the discount rate(s) and reason chosen") came back "partial", rationale "the passage does not state the figure": the tool expects a number. A claim stating the opposite of its passage came back "unsupported", not "contradicted" (register N3). Read every passage yourself; accept an input only when the passage states it in the same direction.
- Pitfall: `qualify_source` on the NICE PMG48 methods page returned "inadmissible, no provenance" (register C1). Cite NICE rules from `reference-cases.md` with their row ids; do not send them to Verify.
- Pitfall: the `check_claim` citation returns `doi: null` and `year: null` although `qualify_source` holds both (register C18). Cite from the `qualify_source` result.
- `build_record` needs a named human in `cleared_by`; it refuses a model or tool name.

## Catalogue jobs

- `budget-impact` and `price-anchor` are `available`; `start_job` returns the method steps and tool inputs and runs nothing. `value-dossier` is `design_partners` and cannot be started.
- `find_job {query: "economic model cost-effectiveness"}` returned no job: there is no catalogue job for a cost-utility model or for model validation. Formula rows say "none" for those tasks.

## Not used here

`watch_*` tools. Literature searching: the review method lives in dh-clinical-validation (`literature-and-real-world-evidence-review`).
