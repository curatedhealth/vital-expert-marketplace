# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them. Counted calls draw on the library key's monthly allowance; a call that returns an error says "Nothing was counted". Do not call `watch_*` tools.

The connector was disconnected while this skill was built (20 October 2026). Every behavior below comes from live outputs saved by earlier builds on 19 and 20 October 2026, copied unchanged into `examples/live/` and cited by file. A step with no saved output is marked **needs a live check**. Most of this skill runs on the person's own records with `scripts/forum_check.py`; the library adds recomputation, a named counterparty's public record and changes, and the record.

## analytics.mcda (A2, recomputing a recorded rank)

- Arguments: `{alternatives: [{id, scores}], criteria_weights}`. Returns `value_estimate` (0 to 100) and `contributions` per item, method "EVIDEM Multi-Criteria Decision Analysis (weighted-sum, 0-4 scale)" (`examples/live/mcda_partner_options.json`, 19 October 2026). The value is 25 x sum of weight x score; `scripts/forum_check.py drift` uses the same formula, and the sibling skill's script reproduced the tool's 77.5, 63.75 and 62.5 exactly.
- Use: recompute the forum's rank from the scores and weights in the person's own record, so the recorded rank can be checked. Without code execution, call the tool with exactly those numbers.
- Pitfalls (register C17): every criterion higher-is-better; no robustness view; ties not flagged; a missing score returned HTTP 400; two identical calls returned 503 before one succeeded. On 503, retry once, then compute by hand and say so.

## analytics.rice (A2, when the forum's rule was RICE)

- Score = reach x impact x (confidence / 100) / effort. Confidence must be sent as a percent; a fraction is divided by 100 again and every score shrinks a hundredfold without an error (register N5; `examples/live/rice_confidence_percent.json`, `rice_confidence_fraction.json`). If a recorded RICE rank looks a hundredfold small, check the scale before reading drift.

## analytics.scenario-modeler and analytics.risk-tornado (A2, only if the person asks how firm a past rank was)

- Measured by the economic-model build (`examples/live/analytics_calls_2026-10-19.json`): `parameters`, `formula`, `periods`, `aggregate`; powers need `**`; the tornado skips list parameters and moves unranged parameters plus or minus 20 percent, which moves weights off a sum of 1; a ratio can flip sign without a flag. Pass the person's ranges. A portfolio formula has not been run live: **needs a live check**.

## diligence-dh.get_deltas (A2, changes for a named licensor or partner)

- Live: `{companies: ["Big Health, Inc.", "Akili Interactive Labs, Inc."], since: "2025-01-01"}` returned "no change recorded" for both, with `log.first_entry_at` 12 October 2026, `last_sweep_at` 19 October 2026, and limits: the since filter uses event dates; "the change log began on the first_entry_at date; older clearances loaded before the log existed may have no entries"; "no change recorded is a statement about in-window event-dated log rows up to last_sweep_at" (`examples/live/diligence_get_deltas_BigHealth_Akili.json`, 19 October 2026).
- Use: only for a licensor or partner the person names. When the period starts before 12 October 2026, say the log cannot show earlier changes and offer the company's dated primary filings and authorization records instead; never report "no change" for that period. It gives no company status (`licensing-and-deal-flags.md` section 3). The saved call named "Akili Interactive Labs, Inc."; the EDGAR registrant is Akili, Inc. (CIK 1850266), and Akili Interactive Labs, Inc. is its wholly owned subsidiary, not a former name (SP-148, [WF]). Akili's own filings show the merger agreement of 29 May 2024 and the change in control on 2 July 2024 (SP-150, SP-151), both before the log began, so the saved "no change recorded" says nothing about them.

## regulatory-dh.search_devices and commercial-dh.generate_report identity block (A2, a named product's public record)

- `search_devices {query: "Big Health", jurisdiction: "US"}` returned Daylight K233872 (510(k), 30 August 2024) and Sleepio® K233577 (510(k), 5 August 2024) with source URLs (`examples/live/search_devices_BigHealth_US.json`). Name search is exact (register C7); use the submission number.
- `generate_report {reference: "Somryst", template: "commercial", ...}` identity block: Somryst K191716, 510(k), 23 March 2020, Pear Therapeutics, Inc.; latest 8-K stored 10 April 2023 (`examples/live/generate_report_somryst_commercial.json`); the same response says "authorization [GAP]" while its identity block holds K191716 (register C2). The stored "latest 8-K" is not the latest filing: Pear's EDGAR record ends with a Form 25-NSE of 2 May 2023 (SP-155, [WF]); Nox Medical lists Somryst today (SP-167). Add both from `licensing-and-deal-flags.md` sections 3 and 4.

## verify.build_record (B1)

- Needs a named human in `cleared_by.name`; a model name was refused (`examples/live/verify_build_record_refusal.json`, 19 October 2026).

## Catalogue jobs and experts

- No catalogue job covers governance review or decision quality: `list_jobs` on 20 October 2026 returned "22 jobs in four suites; none covers integration, handoffs, dependencies or joint decisions" (`examples/live/connector_calls_2026-10-20.json`); the commercial job list holds no review job (`examples/live/list_jobs_2026-10-19.json`). Formula rows say "none".
- `agent-pack.list_experts {query: "chief-digital-health-officer"}` returned the bound worker's description (`connector_calls_2026-10-20.json`).

## Not used here

`watch_*` tools (watches are not separated by customer key, register N2); investment portfolio tools (`diligence-dh.compare_portfolio`, `get_funding_signals`: `investment-portfolio-monitoring`, this pack).
