# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them. Counted calls draw on the library key's monthly allowance; free calls do not.

**How this file was built.** The connector was disconnected during this build (20 October 2026), so no call was made. Every behavior below comes from live outputs saved on 19 October 2026 by earlier builds, copied into `examples/live/` (file named on each entry, read 20 October 2026), and from those builds' `tools.md` files. Where a tool has no saved output, it is described from the old skill text or the saved `list_jobs` only, and the step is marked **needs a live check**. The library twice returned "could not answer this call (503). Nothing was counted" on 19 October 2026; a retry worked.

## diligence-dh.list_sources (free) (needs a live check)

- No saved output. Old skill text: "Every source with credential state, last load, and row counts. A source not loaded states the reason. This call is free."
- Until checked, the perimeter comes from the `source_coverage` block that `compare_portfolio` and `get_evidence_maturity` return (`compare_portfolio_dtx_2026-10-19.json`): loaded `diga_verzeichnis` 82, `bfarm_diga_bekanntmachung` 17, `clinicaltrials` 128, `openfda` 1224, `eudamed_software` 3141, `sec_edgar` 175, `nih_reporter` 18; not loaded: `companies_house` ("API key not yet provisioned"), `diga` ("access under section 21 DiGAV not yet granted"), `nice` ("commercial licence deferred"), `funding` ("no funding source licensed"), `zefix` ("credentials not available").
- Use in A1 step 1: name what the library cannot see (no UK or Swiss company register, no private rounds).

## diligence-dh.build_company_profile (counted)

- Argument: `company` (exact legal name, brand, FDA number, LEI, EUDAMED SRN or SEC number; a near spelling comes back only as a labeled proposal).
- Saved: `partner_profile_akili.json` (`{company: "Akili Interactive Labs, Inc."}`, retrieved 19 October 2026 18:59 UTC). Returned identifiers (EUDAMED SRN US-MF-000048993, SEC CIK 0001741200); EndeavorRx DEN200026 (decision 15 June 2020, `status` "DENG"), EndeavorRx K231337 (13 December 2023), EndeavorOTC K233496 (14 June 2024), all product code QFT, regulation 882.5803, with FDA URLs; studies 10 (3 linked by brand, 6 by indication only); Form D rows 9 June 2021 USD 110,000,007 and 23 May 2018 USD 55,000,010; evidence maturity 100 (90 of 90), rubric v1, reimbursement and jurisdiction breadth excluded.
- Pitfalls:
  - `funding` says `[GAP]` "no funding source licensed or integrated" while `funding_and_filings` in the same response lists two Form D amounts (register C2). Report Form D amounts as amounts the filing states, by date; private rounds stay `[GAP]`.
  - `reimbursement` says "no reimbursement source loaded" although the Market Access scheme rows exist (register C2). Reimbursement is `dh-access-and-value` coverage-pathway-and-access-strategy's question.
  - `status` "DENG" is FDA's raw De Novo granted code (register C3); write "De Novo granted".
  - Company level, not product level.

## diligence-dh.get_funding_signals (counted)

- Argument: `company`. Returns SEC EDGAR filings by type, NIH RePORTER grants and EU TED awards, each with URL; private rounds `[GAP]`.
- Saved: `funding_signals_pear.json` (`{company: "Pear Therapeutics, Inc."}`, 19 October 2026). SEC CIKs 0001615898 and 0001835567; 52 public signals; SEC 46 (8-K 25, 10-Q 6, D 4, S-4/A 3, 10-K 2, S-1 2, 8-K/A 1, S-4 1, D/A 1, S-1/A 1), dated 9 February 2016 to 10 April 2023; NIH 6 (20 June 2017 to 21 September 2020); EU TED none found; `sum_of_stated_amounts` USD 366,766,832 with the caveat "adds the amounts the filings state; a Form D amount sold and an award amount are different things, so read by type".
- Pitfalls:
  - Never quote `sum_of_stated_amounts` as money raised; quote amounts by filing type and date.
  - No 8-K item number and `counterparty` null on every row (register P5): an Item 1.01 agreement (DL-020) cannot be found without opening the filing.
  - The latest filing date is not a status. Never infer why filings stopped, financial health or intent. The company status step (`memo-sources.md` section 8) lists the latest 8-K rows (only the newest row stores a URL in the saved copy) and marks status `[GAP]` until a filing is read. No Form 25 or Form 15 is among the stored types for Pear; whether the library loads those forms needs a live check.
  - Opening a filing at sec.gov by automated request needs a declared User-Agent contact (DL-153): ask which contact the person's organization uses; never the person's email address or name, never an invented one.
  - A Form D shows no valuation or investor names (DL-016, DL-018).

## diligence-dh.get_evidence_maturity (counted)

- Argument: `company` (exact name, brand or FDA number).
- Saved: `evidence_maturity_K191716_somnio.json`. `K191716` resolved to Pear Therapeutics, Inc., score 67 (60 of 90), rubric v1 (7 October 2026): regulatory status 30 of 30, clinical evidence 20 of 40, active development 0 of 10, product breadth 10 of 10; reimbursement and jurisdiction breadth not assessable; limits "a stated convention for comparing documented evidence, not a predictive model or a valuation" and "US sources only; absence of EU, UK or Swiss data lowers nothing and proves nothing". `somnio` resolved to mementor DE GmbH, 33 (clinical evidence 0).
- Use in a memo: the library's convention, with rubric version, components and limits, never as the evidence verdict. A framework-based assessment (NICE ESF tiers, Evidence DEFINED, V3) is `company-and-evidence-assessment` (this pack).
- Pitfalls: an FDA number resolves to the company, so the score covers every product of that company; EU authorizations earn points under a "US sources only" note; clinical evidence counts registered studies only, so a score of 0 means "no registered study linked in the loaded sources", never "no evidence".

## diligence-dh.compare_portfolio (counted, when the memo compares the target with named peers)

- Required `companies`, 2 to 12. Saved: `compare_portfolio_dtx_2026-10-19.json`: Somryst resolved to Pear Therapeutics, Inc. 67, with two Class II recall flags dated 7 June 2021 (reSET, reSET-O); Big Health, Inc. 56; Akili 100; deprexis to GAIA AG, Deutschland 78 (EU 31 authorizations, combined filing names "a proposal until a person validates it"); HelloBetter unresolved.
- Pitfalls: exact names; `reimbursement_listings` always `not_assessable`; "A cell the sources cannot fill is not assessable, never zero." Portfolio work belongs to `funding-and-portfolio-comparison` (this pack).

## diligence-dh.generate_report (counted) (needs a live check)

- No saved output of the diligence version. Old skill text: "Cite-bound dossier from stored rows. template is memo, identity, regulatory, or evidence. Do not invent a filing." Catalogue job `company-dossier` lists it with `build_company_profile` and `get_funding_signals` (`list_jobs_commercial.json`).
- What the commercial version did, as a guide to what to check (`generate_report_somryst_commercial.json`, `commercial-dh.generate_report {reference: "Somryst", template: "commercial", ...}`): the Identity section was a raw JSON block of `build_company_profile` (Pear Therapeutics, Inc.; reSet DEN160018 14 September 2017; reSET-O K173681 10 December 2018; Somryst K191716 23 March 2020, QVO, 882.5801; two Class II recalls 7 June 2021; 46 SEC filings; latest 8-K 10 April 2023; evidence maturity 67); authorization was marked `[GAP]` although the identity block held K191716 (register C7); retrieval dates in References were `[GAP]` (register C1); the commercial memo template body was raw JSON across 1,845 lines (register P7).
- Rule until checked: in A1, prefer `build_company_profile` plus `get_funding_signals` (both measured). Call `generate_report {reference, template: "memo"}` only when the person wants the library's dossier; restate any JSON as tables, take authorizations from the identity block with the FDA URL, and record the behavior in the build notes.

## diligence-dh.retrieve_guidance (counted)

- Saved (`other_calls.json`): `{query: "anti-kickback safe harbor", limit: 5}` returned no passage, "[GAP] no passage retrieved in this namespace", upstream `regulatory-dh.retrieve_guidance` (register C6). Not used in this skill: the transaction and data rules come from `references/` only. **Needs a live check** for any HSR, CFIUS or HIPAA query before relying on it.

## analytics.mcda (counted, B1 only, on the person's scores)

- `alternatives` (each `id` and `scores`, criterion to 0 to 4) and `criteria_weights` (sum to 1). Saved: `mcda_partner_options.json` (illustrative inputs typed for the measurement): method "EVIDEM Multi-Criteria Decision Analysis (weighted-sum, 0-4 scale)"; values 77.5, 63.75, 62.5 with contributions.
- Pitfalls: every criterion is higher-is-better (`negative_criteria` cannot be set); a missing score returned HTTP 400 and nothing was counted (register C17): drop an unscored option and list it as not ranked; no robustness view or tie flag. Never call it with proposed scores, and never let the rank stand in for the person's decision.

## verify.build_record (counted)

- Needs a named human in `cleared_by.name`. Saved: `verify_build_record_refusal.json`: `{cleared_by: {name: "Claude"}}` returned "build_record refuses a record without a human cleared_by.name". Call it only when the output leaves the conversation and the person names who clears it.

## verify.qualify_source and verify.check_claim

- Regulator pages are rated "inadmissible", "no provenance" (OIG AO 26-15 in `other_calls.json`; register C1). The DL rows already carry URL, verbatim quote and read date: cite them directly. For a [PAPER] row, accept a claim only with a passage read in the same direction (register N3).

## agent-pack.list_experts and download_agent

- Not called in this build. Saved evidence from the evidence-group builds (ev-build-notes he1.md, 19 October 2026): `list_experts {query: "economic"}` returned `health-tech-investor` (Digital Health Leadership), "whose remit is investment diligence". Proposed in the build notes as the expert for this suite; not bound.

## Catalogue jobs

- `company-dossier` (Diligence): `build_company_profile`, `generate_report`, `get_funding_signals` (`list_jobs_commercial.json`). `start_job` takes only a job id, returns the steps and runs nothing (register C12). The direct calls in A1 are the method.
- `investment-memo`: design partners only. **Never started.** No library call drafts a memo for this skill.

## Not used here

- `diligence-dh.watch_companies` and every `watch_*` tool: never called.
- `diligence-dh.screen_market`, `search_companies`: `market-and-target-screening` (this pack).
- `diligence-dh.get_deltas`: `thesis-and-memo-monitoring` (this pack).
