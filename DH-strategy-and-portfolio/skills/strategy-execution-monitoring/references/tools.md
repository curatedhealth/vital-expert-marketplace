# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them. Counted calls draw on the library key's monthly allowance; a call that returns an error says "Nothing was counted".

**How this file was built.** The connector was disconnected during this build (20 October 2026), so no call was made. Every behavior below comes from live outputs saved on 19 October 2026 by earlier builds, copied into `examples/live/` (file named on each entry, read 20 October 2026), and from those builds' `tools.md` files. Where a tool has no saved output, the step is marked **needs a live check**. Most of this skill runs on the person's own benefits register, milestone log and experiment log through `scripts/execution_check.py`; the library is used for public-record changes on named partners and for arithmetic on the person's forecasts.

## diligence-dh.get_deltas (counted; A2 step 4, only for a partner, licensor or acquired company named in the strategy)

- Arguments: `companies` (exact legal names) and `since` (ISO date).
- Saved: `diligence_get_deltas_BigHealth_Akili.json` (`{companies: ["Big Health, Inc.", "Akili Interactive Labs, Inc."], since: "2025-01-01"}`, retrieved 19 October 2026): both "no change recorded", `change_count` 0; log `first_entry_at` 2026-10-12T23:34:07Z, `last_sweep_at` 2026-10-19T09:42:05Z; limits: the since filter uses event dates; "the change log began on the first_entry_at date; older clearances loaded before the log existed may have no entries"; "no change recorded is a statement about in-window event-dated log rows up to last_sweep_at".
- Pitfalls: a period that starts before 12 October 2026 cannot be read from the log: say so and offer the company's dated filings and authorization records for the period instead of "no change". `change_count` mixes authorization, study, safety event and filing changes. No status field.

## diligence-dh.build_company_profile (counted; A2 step 4, for the dated records of a named partner)

- Saved: `partner_profile_akili.json` (`{company: "Akili Interactive Labs, Inc."}`, retrieved 19 October 2026): EndeavorRx De Novo granted 15 June 2020 (DEN200026, raw `status` "DENG", register C3), 510(k) cleared 13 December 2023 (K231337); EndeavorOTC 510(k) cleared 14 June 2024 (K233496); two Form D rows (23 May 2018; 9 June 2021); SEC CIK 0001741200; no 8-K rows stored. Use the decision dates to answer "what changed in the period" when the log cannot. The profile's CIK carries only Form D rows; the listed parent whose filings show the acquisition is Akili, Inc., CIK 1850266 (SP-148 [WF]).

## Company status and listing holders (research pass, not the library)

- The library has no status tool. The research pass of 20 October 2026 holds primary-record rows for four companies in saved outputs (`strategy-and-portfolio-research.md` section 8): Akili 8-Ks of 29 May and 2 July 2024, Form 25-NSE of 2 July 2024 and Form 15-12G of 12 July 2024 (SP-148 to SP-154, [WF]); Pear 8-Ks of 7 and 10 April 2023 and Form 25-NSE of 2 May 2023 (SP-155 to SP-161, [WF]); Big Health and Aidoc not SEC filers (SP-162, [WF]) but active in FDA registration and listing (SP-163, SP-164); current FDA listing holders for Somryst, EndeavorRx, reSET and reSET-O (SP-165 to SP-169). Quote these by filing name and date (`execution-frameworks.md` section 5). Each row carries its URL.
- Not read: Virtual Therapeutics Corporation's status; Pear's court sale orders; the Akili Form 25 body. Each stays `[GAP]`.

## analytics.scenario-modeler (counted; A2, on the person's own forecast)

- Saved: `analytics_calls_2026-10-19.json` (illustrative inputs). `parameters`, `formula`, `periods`, `aggregate`. `population * uptake * (device_cost - offset)` with 10000, [0.05, 0.1, 0.15], 250, 120 returned 65,000, 130,000 and 195,000 (cumulative 390,000).
- Pitfalls: `^` rejected with HTTP 400 (use `**`); `t` starts at 0; `aggregate: "none"` still returns cumulative values.
- Use only to re-run the person's own benefit forecast with their actuals or their optimism-bias adjustment (SP-096); every output is a hypothesis on the person's numbers, never a target.

## analytics.risk-tornado (counted; A2, on the person's own forecast and ranges)

- Saved: `analytics_calls_2026-10-19.json`. Parameters without a range get plus or minus 20 percent (`variation_pct` 0.2), list parameters are skipped, and a ratio formula produced an unflagged sign flip. Pass the person's range for every parameter, or say the default was applied and is not theirs.

## verify.build_record (counted)

- Saved: `verify_build_record_refusal.json`: `{cleared_by: {name: "Claude"}}` returned "build_record refuses a record without a human cleared_by.name". Call it only when the output leaves the conversation and the person names who clears it.

## Catalogue jobs

- `list_jobs_2026-10-19.json` lists no job for strategy execution, benefits tracking or experiment monitoring. `product-watch` sets a `watch_product` watch and is not used (no `watch_*` calls). Every task's formula row says "Catalogue job: none".

## Not used here

- `diligence-dh.watch_companies`, `commercial-dh.watch_product` and every `watch_*` tool: never called. Monitoring is by dated reruns the person schedules.
- `analytics.mcda` and `analytics.rice`: choosing between options is `strategic-vision-and-options` (this pack); ranking products is `product-portfolio-prioritization` (this pack).
