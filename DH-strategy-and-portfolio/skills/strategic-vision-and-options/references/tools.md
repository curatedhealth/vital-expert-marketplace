# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `analytics_risk-tornado`). Counted calls draw on the library key's monthly allowance; a call that returns an error says "Nothing was counted".

**How this file was built.** The connector was disconnected during this build (20 October 2026), so no call was made. Every behavior below comes from live outputs saved on 19 October 2026 by earlier builds, copied into `examples/live/` (file named on each entry, read 20 October 2026), and from those builds' `tools.md` files. Where a tool has no saved output, the step is marked **needs a live check**. Most of this skill runs on the sourced references and the person's own numbers; the library is used for public-record facts on named candidates and for arithmetic on the person's scores and inputs.

## analytics.mcda (counted; B1, on the person's scores only)

- Arguments: `alternatives` (each `id` and `scores`, criterion to a number on 0 to 4) and `criteria_weights` (the person's weights, summing to 1).
- Saved: `mcda_partner_options.json` (illustrative inputs typed for the measurement, 19 October 2026): method "EVIDEM Multi-Criteria Decision Analysis (weighted-sum, 0-4 scale)"; values 77.5, 63.75, 62.5 with contributions. `scripts/options_check.py rank --input examples/live/mcda_partner_options.json` reproduces all three values and prints "analytics.mcda values match this arithmetic".
- Pitfalls (register C17): every criterion is read as higher-is-better (`negative_criteria: []` cannot be set); name criteria so higher is better ("capital need avoided", not "capital need"). No robustness view and no tie flag: `options_check.py rank` prints the swap points. A missing score returned HTTP 400 in a sibling build and nothing was counted: drop an unscored option and list it as not ranked.
- Never call it with proposed scores. The rank is arithmetic on the person's scores, never the choice (SP-080).

## analytics.rice (counted; B1, only if the person scores options with RICE)

- Arguments: `initiatives`, each `id`, `reach`, `impact` (0.25, 0.5, 1, 2 or 3), `confidence`, `effort`.
- Saved: `rice_percent_confidence.json` (19 October 2026): confidence must be a whole percent (80, not 0.8); given 0.8 a sibling build saw scores 100 times too small. Check each `score` equals reach x impact x (confidence / 100) / effort. The method cites a vendor article (Intercom 2016): a calculator the person chooses, not a sourced rule.

## analytics.scenario-modeler (counted; B1, on the person's inputs)

- Saved: `analytics_calls_2026-10-19.json` (illustrative inputs). Arguments `parameters` (name to number, or a list with one value per period), `formula`, `periods`, `aggregate` (`sum`, `cumulative` or `none`). `population * uptake * (device_cost - offset)` with 10000, [0.05, 0.1, 0.15], 250, 120 returned 65,000, 130,000 and 195,000 (cumulative 390,000).
- Pitfalls: `^` is rejected with HTTP 400 (use `**`); `t` starts at 0, so period 0 is undiscounted; `aggregate: "none"` still returns cumulative values.
- Use only to run the person's own option arithmetic (for example the person's cost and benefit inputs for build versus license, after their own optimism-bias adjustment, SP-096). Every output is a hypothesis on the person's numbers.

## analytics.risk-tornado (counted; B1, on the person's inputs and ranges)

- Saved: `analytics_calls_2026-10-19.json`. Same arguments plus `variation_pct` (default 0.2) and `parameter_ranges` (name to [low, high]).
- Pitfalls: list parameters are skipped (`skipped_parameters: ["uptake"]`); parameters without a range get plus or minus 20 percent, which is not the person's range; on a ratio formula an input made the denominator negative and the tool ranked the sign flip as the smallest swing with no flag. `scripts/options_check.py tornado` prints flags R1 (default range), R2 (skipped), R3 (sign change) and R4 (ratio formula).
- Pass the person's range for every parameter; if they have none, say the default was applied and is not theirs.

## diligence-dh.build_company_profile (counted; A1, for a named build, partner, license or acquisition candidate)

- Argument: `company` (exact legal name, brand, FDA number or SEC number).
- Saved: `partner_profile_akili.json` (`{company: "Akili Interactive Labs, Inc."}`, retrieved 19 October 2026 18:59 UTC): EUDAMED SRN US-MF-000048993, SEC CIK 0001741200; EndeavorRx DEN200026 (15 June 2020, `status` "DENG"), K231337 (13 December 2023); EndeavorOTC K233496 (14 June 2024); product code QFT; studies 10 (3 by brand, 6 by indication only); two Form D rows (9 June 2021 USD 110,000,007; 23 May 2018 USD 55,000,010); evidence maturity 100, rubric v1 (7 October 2026), reimbursement and jurisdiction breadth excluded.
- Pitfalls: "DENG" is FDA's raw De Novo code (register C3), write "De Novo granted"; `funding` says `[GAP]` beside two Form D rows (register C2); `reimbursement` says no source loaded (register C2). No company status field: run the status step. The profile's CIK 0001741200 carries only the two Form D rows; the listed parent whose 8-Ks, Form 25 and Form 15 show the acquisition is Akili, Inc., CIK 1850266 (SP-148 [WF]): say which entity each fact belongs to. `scripts/options_check.py facts` turns the file into the A1 table and prints the status as read for Akili, Pear, Big Health and Aidoc.

## diligence-dh.compare_portfolio (counted; A1, only when the person names 2 to 12 candidates)

- Saved: `compare_portfolio_dtx_2026-10-19.json`: Somryst resolved to Pear Therapeutics, Inc. (67, two Class II recall flags dated 7 June 2021); Big Health, Inc. 56; Akili 100; deprexis to GAIA AG 78 (combined filing names "a proposal until a person validates it"); HelloBetter unresolved. "A cell the sources cannot fill is not assessable, never zero." Despite the tool name, this compares companies, not the person's product portfolio.

## diligence-dh.get_funding_signals (counted; A1, only when the candidate files with the SEC)

- Saved: `funding_signals_pear.json` (`{company: "Pear Therapeutics, Inc."}`): 46 SEC filings 9 February 2016 to 10 April 2023; 8-K rows carry no item number; `sum_of_stated_amounts` is never money raised. Used for the 8-K rows to open in the company status step.

## Company status and listing holders (research pass, not the library)

- The library has no status tool. The research pass of 20 October 2026 read the primary records for four companies in saved outputs and holds them as rows in `strategy-and-portfolio-research.md` section 8: Akili's EDGAR record, 8-Ks of 30 April, 29 May and 2 July 2024, Form 25-NSE of 2 July 2024 and Form 15-12G of 12 July 2024 (SP-148 to SP-154, [WF]); Pear's EDGAR record, 8-Ks of 7 and 10 April 2023 and Form 25-NSE of 2 May 2023 (SP-155 to SP-161, [WF]); Big Health and Aidoc not found as SEC filers (SP-162, [WF]) but active in FDA registration and listing (SP-163, SP-164); current FDA listing holders for Somryst, EndeavorRx, reSET and reSET-O (SP-165 to SP-169, from openFDA, dataset updated 5 October 2026). Each row carries its URL, so a reader can open it.
- SEC pages were read through WebFetch with no declared contact; a live EDGAR read by the person's assistant needs the contact their organization uses (DL-153 [WF]). The EDGAR company browser is closed to automated tools; the submissions record (data.sec.gov) and the Archives index were used.
- Not read: Virtual Therapeutics Corporation's status; the court sale orders for Pear's products; the Akili Form 25 body; FDA De Novo decision summaries (pivotal study and endpoint). Each stays `[GAP]`.

## verify.build_record (counted)

- Saved: `verify_build_record_refusal.json`: `{cleared_by: {name: "Claude"}}` returned "build_record refuses a record without a human cleared_by.name". Call it only when the output leaves the conversation and the person names who clears it.

## verify.qualify_source and verify.check_claim (needs a live check for this skill's sources)

- Regulator pages have been rated "inadmissible, no provenance" in sibling builds (register C1). SP and DL rows already carry URL, verbatim quote and read date: cite them directly. For a [PAPER] row, accept a claim only with a passage read in the same direction (register N3); `check_claim` needs the full `qualify_source` object (register C18).

## Catalogue jobs

- `list_jobs_2026-10-19.json` (19 October 2026) lists no job for strategy, vision, option appraisal or experiment design. `partner-prioritization` runs `analytics.mcda` and `analytics.rice` but is scoped to partners and indications; call the calculators directly. Every task's formula row says "Catalogue job: none".

## Not used here

- `diligence-dh.watch_companies` and every `watch_*` tool: never called.
- `literature.*`: the review method is `dh-clinical-development` literature-and-real-world-evidence-review.
- `regulatory-dh.*`: device status and pathways are `dh-regulatory-and-quality` regulatory-pathway-and-classification.
