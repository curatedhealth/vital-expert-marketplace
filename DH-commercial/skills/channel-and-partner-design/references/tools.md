# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `diligence-dh_build_company_profile`). Counted calls draw on the library key's monthly allowance; free calls do not.

This competency is mostly method: its rules sit in `references/`. The library adds a public view of a named partner, a peer screen, two ranking calculators for what the person scored, and the record. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`.

## commercial-dh.list_commercial_dh_sources (free)

- No arguments. Returns the Diligence sources (with record counts and load dates), the Regulatory jurisdictions and the Market Access schemes in one response.
- Observed: SEC EDGAR 175 filings, NIH RePORTER 18, EU TED 41, openFDA 1,224 clearances; Companies House, Zefix, the DiGA directory feed for Diligence, NICE and private funding rounds not loaded.
- Use it once before A1 Step 4 to know what a partner view can and cannot show. A source not loaded makes every related field `[GAP]`.

## diligence-dh.search_companies (counted)

- Arguments: `query` and/or `segment` (dtx, samd-diagnostic, cdss, rpm, digital-health), `country`, `has_authorization`, `limit`.
- Pitfall: `segment: "rpm"` returned 0 companies. The same day the peer screen reported `segments_loaded: ["dtx"]`. Only the dtx segment holds companies; other segment values return nothing. Search by name instead.

## diligence-dh.build_company_profile (counted)

- Argument: `company` (legal name, brand, FDA number, LEI, EUDAMED SRN or SEC filer number; exact match; near spellings come back as proposals).
- Returns identifiers by scheme, products with authorizations, linked studies with the link basis, safety events, filings, an evidence maturity score with its formula, and gaps.
- Observed (`Akili Interactive Labs, Inc.`): identifiers EUDAMED SRN, FDA applicant name and SEC CIK; EndeavorRx and EndeavorOTC under product code QFT, regulation 882.5803; 10 studies, 3 naming the brand and 6 linked by sponsor and indication only (weaker link); evidence maturity 100 on 90 of 90 assessable points, with reimbursement and jurisdiction breadth excluded.
- Pitfalls: the De Novo status is the raw code "DENG". `funding` says `[GAP]` "no funding source licensed or integrated" while `funding_and_filings` in the same response lists two Form D amounts: read Form D as an offering the company stated, and private rounds as `[GAP]`. `reimbursement` says "no reimbursement source loaded" even though the Market Access suite holds the US DMHT codes; reimbursement is Market Access's subject anyway.
- Use: describe a named partner only by what its record states (authorizations, studies, filings). The evidence maturity score is the library's stated convention, not a judgment of the partner; never turn it into a partner score.

## diligence-dh.get_funding_signals (counted)

- Argument: `company`. Returns SEC filings made by the company, NIH grants and EU TED awards, each with URL and retrieval date; private rounds are `[GAP]`.
- Observed (`Pear Therapeutics, Inc.`): 46 SEC filings (25 Form 8-K) dated 9 February 2016 to 10 April 2023; 6 NIH grants.
- Pitfalls: filing rows carry no Form 8-K item number and `counterparty` is null on every row, so an Item 1.01 material definitive agreement (CP-US-79) cannot be told apart from other 8-K events without opening the filing at its URL. `sum_of_stated_amounts` adds Form D amounts and other types together; quote amounts by type only. The latest filing date is not a statement about the company's current status: say "latest filing in the store" and nothing more.
- Use: for A2 disclosure (is a party a reporting company that files 8-Ks) and as a public signal on a partner. Open the filing URL to read what an 8-K covers.

## commercial-dh.screen_commercial_peers (counted)

- Arguments: `segment` (Diligence segment or company name), optional `name`, `limit` 1 to 25.
- Returns the Diligence market screen (ranked by evidence maturity score, then name; "no other weighting") and, per peer, a device and listing lookup.
- Observed (`segment: "dtx", limit: 8`): 18 matches in the dtx segment of 2,205 companies in the store; eight returned (Akili, AppliedVR, Click, Luminopia, Swing, Cognifisense, NightWare, Pear). The response was very large because the full coverage block repeats for every peer.
- Pitfall: the per-peer device and listing lookups pass the legal company name ("Akili Interactive Labs, Inc.") and found nothing for any of the eight, while the screen itself shows Akili with 3 authorizations. Trust the `screen_market` block; treat the per-peer "no stored device" lines as a search miss, not absence. For a peer's authorizations, call `build_company_profile`.
- Use: "who else sells in this segment" as context for channel choice. The ranking is the library's convention, not a channel recommendation.

## analytics.mcda (counted)

- Arguments: `alternatives` (each `id` and `scores`, a map of criterion to number on 0 to 4) and `criteria_weights` (should sum to 1).
- Method returned: "EVIDEM Multi-Criteria Decision Analysis (weighted-sum, 0-4 scale)". Each value is the sum of weight times score divided by 4, times 100; `contributions` break it down.
- Observed: three partner options, four criteria, weights 0.35, 0.25, 0.20, 0.20: values 77.5, 63.75 and 62.5.
- Pitfalls: every criterion is treated as higher-is-better (`negative_criteria` is empty and cannot be set); name criteria so higher is better ("compliance fit", not "compliance risk"). A missing score returned a bare HTTP 400 with no message; check inputs before calling (`scripts/rank_check.py`). No robustness view: compute swap points with the script. Two calls failed with HTTP 503 and "Nothing was counted"; a retry after a pause worked. The response carries an unrelated note about price figures.

## analytics.rice (counted)

- Argument: `initiatives`, each with `id`, `reach`, `impact`, `confidence`, `effort`.
- Method returned: "RICE Prioritization (Reach x Impact x Confidence / Effort)", citing McClure (2016), Intercom.
- Pitfalls:
  - **Confidence is read as a percent.** Sending 0.8 came back as 0.008 and scores 100 times too small (Reseller onboarding kit: 2 instead of 200). Send confidence as 0 to 100 (80 means 80 percent). The order was the same in the observed call, but the scores were wrong.
  - Impact 1.5 was accepted although the description allows only 0.25, 0.5, 1, 2 or 3. Check impact values before calling.
- Observed with percent confidence: 540, 200, 150 and 133.33 for four initiatives.

## diligence-dh.retrieve_guidance (counted)

- `query: "anti-kickback safe harbor"` returned no passage ("no passage retrieved in this namespace"). The guidance store holds nothing on fraud and abuse, partner contracting or channel rules. The sourced references in this skill replace it.

## verify.qualify_source (counted)

- `url` of OIG advisory opinion 26-15 returned tier "inadmissible", "no provenance", publisher and date null. Regulator documents are not admitted as sources yet, so Verify cannot check a CP row. The rows already carry URL, verbatim quote and read date; cite them directly.

## agent-pack.list_experts and agent-pack.download_agent

- `list_experts {query: "partnership"}` returned three experts in Digital Commercial: Digital Partnerships Director (`digital-partnerships-director`, the worker for this skill), Partnerships Manager, Digital Health, and the Digital Health Access & Reimbursement Lead.
- `download_agent {expert: "digital-partnerships-director"}` returned 108,025 characters. Its stop rules are the source of `references/governance.md`. Offer it only when the person wants the role on their own assistant.

## verify.build_record (counted)

- Needs `clearances` with a human `cleared_by.name`; it refuses a missing or tool or model name. Call it only when an output leaves the conversation and the person names who clears it.


## Catalogue jobs (list_jobs, get_job, find_job, start_job)

Measured 19 October 2026 (`examples/live/list_jobs_commercial.json`). `list_jobs` returned 13 Commercial jobs, all `available`. `start_job` takes only `job_id`; it returns the method steps, the tool names and the inputs of the non-Verify tools, and "does not run the buyer's model". The assistant then makes the calls itself. Every job closes with the seven `verify.*` tools; `verify.build_record` still needs a named human. Prices in the job list are hypotheses, not charges.

Connector finding (all three new jobs): the jobs list `analytics.segmentation`, `analytics.scenario-modeler` and `analytics.risk-tornado`, and `start_job` describes their inputs, but the connector exposes only four analytics tools (`mcda`, `rice`, `budget-impact-model`, `vba-price-anchor`). A search for those names returned none of them. When a job reaches one of these steps the output shows `[GAP] ...: tool not exposed`; nothing is computed in its place.

### partnership-screen (task B1), live run with illustrative scores

- Steps returned: company profile, then peer screen; MCDA on the buyer's scores for those companies; segmentation when the buyer gives numeric features; show weights and scores; do not store; close with Verify.
- Calls made: `diligence-dh.build_company_profile {company: "Big Health, Inc."}`; `commercial-dh.screen_commercial_peers {segment: "dtx", limit: 5}`; `analytics.mcda` on three companies with ILLUSTRATIVE scores (Big Health 70, Akili 62.5, Click 60 on weights 0.5, 0.3, 0.2); `analytics.mcda` with one option missing a score. Saved: `examples/live/job_partnership_screen.json`.
- What came back: the profile resolved (Daylight K233872 and Sleepio K233577 with dates and FDA URLs; four studies, none linked by brand; reimbursement and funding `[GAP]`). The peer screen returned five of 18 dtx companies ordered by evidence maturity score only; its device and listing lookups by company name matched nothing for any peer.
- Pitfalls: (1) the job says a missing score leaves that option blank, but MCDA refuses the whole call with HTTP 400: drop the unscored option before the call and list it as not ranked; (2) the named company is not part of the peer list; (3) `analytics.segmentation` is not exposed; (4) `name` is null on MCDA rows.
- What it leaves as a gap: every score and weight (the person's), segmentation, and any fact the registers do not hold (funding, reimbursement, non-US authorizations).

## Not used here

- `commercial-dh.get_pricing_corridor`, `analytics.vba-price-anchor`: pricing belongs to Commercial 3.x and Market Access.
- `watch_*` tools.
