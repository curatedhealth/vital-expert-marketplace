# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `analytics_mcda`). Counted calls draw on the library key's monthly allowance; a call that returns an error says "Nothing was counted". Do not call `watch_*` tools.

The connector was disconnected while this skill was built (20 October 2026). Every behavior below comes from live outputs saved by earlier builds on 19 and 20 October 2026, copied unchanged into `examples/live/` and cited by file. A step with no saved output is marked **needs a live check**. Every analytics tool computes only on numbers the person supplies; every result is arithmetic on those numbers, not a decision.

## analytics.mcda (B1)

- Arguments: `{alternatives: [{id, scores: {criterion: 0 to 4}}], criteria_weights: {criterion: weight}}`.
- Returns `method: "EVIDEM Multi-Criteria Decision Analysis (weighted-sum, 0-4 scale)"`, per item `value_estimate` (0 to 100) and `contributions`, `weights_used`, `negative_criteria: []` (`examples/live/mcda_partner_options.json`, 19 October 2026). The value is 25 x sum of weight x score: `scripts/portfolio_rank.py mcda` recomputed 77.5, 63.75 and 62.5 exactly (`examples/live/portfolio_rank_runs_output.md`).
- The citation returned with one saved call names Goetghebeur et al. 2008 (EVIDEM) and Marsh, IJzerman et al. 2016 (ISPOR MCDA) (`examples/live/analytics_mcda_segments_illustrative.json`). Cite the ISPOR rows from `prioritization-methods.md` (SP-074 to SP-081, [PAPER] [WF]), not the tool's citation.
- Pitfalls (register C17): every criterion is treated as higher-is-better and the input has no field to mark one as lower-is-better, so phrase each criterion so 4 is best (for example "capacity fit", not "capacity used"); no robustness view (use `scripts/portfolio_rank.py swap`); ties are not flagged; a missing score returned HTTP 400, nothing counted; two identical calls returned 503 before one succeeded (`mcda_partner_options.json`, `other_attempts`). On 503, retry once, then compute by hand from the same formula and say the calculator was not used. Drop an item with a missing score and list it as not ranked.
- Never call it with proposed scores.

## analytics.rice (B1, when the person's rule is RICE)

- Arguments: `{initiatives: [{id, reach, impact, confidence, effort}]}`. Returns `score` = reach x impact x (confidence / 100) / effort, with `confidence` echoed as a fraction (`examples/live/rice_confidence_percent.json`: 900 x 1.5 x 0.8 / 2 = 540).
- Pitfall (register N5): confidence is read as a percent. Sent as a fraction (0.8), it was divided by 100 again and echoed as 0.008, shrinking every score a hundredfold without an error (`examples/live/rice_confidence_fraction.json`). Send percent. `scripts/portfolio_rank.py rice` flags this.
- Pitfall: an impact of 1.5 was accepted, so the tool does not validate the impact scale; the scale is the person's. `name` comes back null; use `id`.
- The tool cites McClure 2016 (Intercom), a vendor note, not a sourced row.

## analytics.scenario-modeler (B1 sensitivity)

- Arguments: `parameters` (name to number, or to a list with one value per period), `formula` (arithmetic over the names and `t`), `periods`, `aggregate` (`sum`, `cumulative` or `none`) (`examples/live/analytics_calls_2026-10-19.json`, measured by the economic-model build).
- Live: `population * uptake * (device_cost - offset)` with list `uptake` returned 65,000, 130,000 and 195,000; `t` starts at 0. Powers need `**`; `^` returned HTTP 400. `aggregate: "none"` still returns cumulative values.
- Use in this skill: recompute the person's own weighted sum or their own risk-adjusted figure under scenarios they name (for example their probability of success at two values), with every parameter labeled theirs. Never enter a market size, price, valuation, return or benchmark probability the person did not give. A portfolio formula has not been run live: **needs a live check**.

## analytics.risk-tornado (B1 sensitivity)

- Same `parameters`, `formula`, `periods`, plus `aggregate` (`sum` or `cumulative`), `variation_pct` (default 0.2) and `parameter_ranges` (name to [low, high]) (`analytics_calls_2026-10-19.json`).
- Pitfall 1: list parameters are skipped (`skipped_parameters: ["uptake"]`).
- Pitfall 2: parameters without a range are moved plus or minus 20 percent by default. A weight of 0.30 becomes 0.24 to 0.36 and the weights no longer sum to 1. Pass the person's ranges for every parameter; if they have none, say the default was applied and is not theirs.
- Pitfall 3: a ratio can flip sign at a default bound and the tool ranks it without a flag (ICER run returned -2,016). Do not tornado a ratio; run it on a linear form.
- Use in this skill: the person's weighted-sum formula for one item, `25 * (w_need * s_need + w_evidence * s_evidence + ...)`, with ranges on the scores or weights the person is unsure of. Not run live for a portfolio formula: **needs a live check**.

## regulatory-dh.search_devices (A1, public authorization of a named product)

- Arguments: `{query, jurisdiction}`. Live: `{query: "Big Health", jurisdiction: "US"}` returned Daylight (K233872, 510(k), decision 30 August 2024, product code SCP) and Sleepio® (K233577, 510(k), decision 5 August 2024, product code QVO), both regulation 882.5801, predicate K191716, with `source_url` and `retrieved_at` (`examples/live/search_devices_BigHealth_US.json`, 19 October 2026). Coverage line: "US: 1226 authorizations loaded".
- The FDA registration and listing record names the same two products "SleepioRx" (K233577) and "DaylightRx Treatment" (K233872) under establishment BIG HEALTH INC (SP-163); match on the submission number, not the name.
- Pitfall (register C7): name search is exact; "Sleepio" without "®" returned nothing in another build, while the submission number worked. Search by submission number where the person has one.
- Use only for a product the person names (a candidate, a comparator, or their own product's public record). Never put the person's confidential program names into a library call.

## commercial-dh.generate_report, identity block (A1, a named candidate)

- Live: `{reference: "Somryst", template: "commercial", ...}` resolved to Pear Therapeutics, Inc. and listed reSet DEN160018 (14 September 2017), reSET-O K173681 (10 December 2018) and Somryst K191716 (23 March 2020, QVO, 882.5801); `latest_8K` 10 April 2023; `sec_edgar_filings` 46; reimbursement "[GAP] no reimbursement source loaded" (`examples/live/generate_report_somryst_commercial.json`, 19 October 2026; first attempt 503, not counted).
- Pitfall (register C2): the same response says "authorization [GAP]" while its identity block holds K191716. Use the identity block and say so.
- Its `latest_8K` (10 April 2023) is the latest 8-K the library stored, not the latest filing: Pear's EDGAR record ends with a Form 25-NSE of 2 May 2023 (SP-155, [WF]).
- It gives no company status and no current listing holder: add the status line and the listing holder from `licensing-and-deal-flags.md` sections 3 and 4 (for Somryst: Pear 8-K, 7 April 2023, chapter 11, SP-156; listed today by Nox Medical, SP-167).

## verify.build_record (B2)

- Needs a named human in `cleared_by.name`; a model name was refused: "build_record refuses a record without a human cleared_by.name" (`examples/live/verify_build_record_refusal.json`, 19 October 2026). Call it only when the record leaves the conversation and the person has named who clears it.

## verify.qualify_source and verify.check_claim (only if a published figure is checked)

- Sequence for a [PAPER] row (for example SP-082): `qualify_source` with the DOI, then `check_claim` with the claim, the verbatim passage (`text`, `locator`) and the full returned source object (register C18). A reversed claim returned "unsupported", not "contradicted" (register N3; `examples/live/connector_calls_2026-10-20.json`). Accept a figure only with a passage read in the same direction. Not run for SP rows: **needs a live check**.

## Catalogue jobs and experts

- No catalogue job covers product portfolio prioritization or governance decisions. `list_jobs` on 20 October 2026: "22 jobs in four suites; none covers integration, handoffs, dependencies or joint decisions" (`connector_calls_2026-10-20.json`). The commercial job `partner-prioritization` runs the same two tools (`analytics.mcda`, `analytics.rice`) but is scoped to partners (`examples/live/list_jobs_2026-10-19.json`); it is not used here. Formula rows say "none".
- `agent-pack.list_experts {query: "chief-digital-health-officer"}` returned the bound worker's description (`connector_calls_2026-10-20.json`).

## Not used here

`watch_*` tools; `diligence-dh.compare_portfolio` and `get_funding_signals` (investment portfolio work: `funding-and-portfolio-comparison`, this pack); `analytics.budget-impact-model` (HTTP 422 on every saved shape, register N5; economic models route to `dh-access-and-value` economic-model-development).
