# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them. Counted calls draw on the library key's monthly allowance; free calls do not.

**How this file was built.** The connector was disconnected during this build (20 October 2026), so no call was made for this skill. Every behavior below comes from live outputs saved on 19 October 2026 by earlier builds, read on 20 October 2026, and copied unchanged into `examples/live/` (origins in `examples/live/SOURCES.md`). A step marked **needs a live check** rests on a description, not on a saved output. Counted calls in this build: 0.

## diligence-dh.get_funding_signals, counted: task A1

- **Saved call:** `{company: "Pear Therapeutics, Inc."}` (`examples/live/funding_signals_pear.json`, first saved in `channel-and-partner-design`, 19 October 2026).
- **What came back:** two SEC CIKs (0001615898, 0001835567); `total_public_signals` 52; SEC EDGAR 46 filings by type (8-K 25, 10-Q 6, D 4, S-4/A 3, 10-K 2, S-1 2, 8-K/A 1, S-4 1, D/A 1, S-1/A 1), dated 9 February 2016 to 10 April 2023, each row with type, date, amount, counterparty, reference and SEC URL; NIH RePORTER 6 grants (20 June 2017 to 21 September 2020); EU TED `none_found`; `private_rounds` "[GAP]".
- **Pitfalls:**
  - No 8-K item number on any row, and `counterparty` null on every row: an Item 1.01 agreement (DL-020) or Item 2.01 acquisition (DL-022) cannot be told from other 8-K events without opening the filing URL.
  - `sum_of_stated_amounts` (USD 366,766,832 for Pear) adds amounts across filing types; the tool's own caveat says "a Form D amount sold and an award amount are different things, so read by type". Never quote the sum. Quote amounts per filing row, by type.
  - The latest filing date (10 April 2023 for Pear) is the latest filing in the store, not a statement about the company today. Never infer status, solvency or intent from it.
  - Two CIKs for one company: say both and that the library combined them.
  - The store holds the CIKs it lists and selected form types only: the Pear store shows no Form 25 or Form 15. Status comes from the status step (`references/company-status.md`), never from the filing gap.
- **Needs a live check:** behavior for a company with no SEC CIK (for example a German DiGA maker); whether EU TED rows carry amounts.

## diligence-dh.build_company_profile, counted: A1, only when the person wants the filing rows inside a full company view

- **Saved call:** `{company: "Akili Interactive Labs, Inc."}` (`examples/live/partner_profile_akili.json`, 19 October 2026). `funding_and_filings` listed SEC EDGAR 2 filings, both Form D: 9 June 2021, amount 110,000,007 USD, and 23 May 2018, amount 55,000,010 USD. Identifiers as returned: SEC CIK 0001741200 only; any other Akili registrant is not in this record.
- **Pitfalls:** the same response says `funding: "[GAP]"`, "no funding source licensed or integrated" (register C2). The tool does not say which Form D Item 13 field (total offering amount or amount sold, DL-015) the amount is; write "amount as stored, Item 13 field not stated". The full company view belongs to `company-and-evidence-assessment` (this pack); do not call both skills' tools for the same company.

## diligence-dh.compare_portfolio, counted: task A2

- **Arguments:** `companies`, 2 to 12 references (legal name, brand, FDA number, LEI, EUDAMED or SEC number). The old skill's boundary: "Compare 2 to 12 companies the buyer names. A company the store does not hold is a gap."
- **Saved calls** (`examples/live/compare_portfolio_dtx_2026-10-19.json`, 19 October 2026): `["Somryst", "Big Health", "Akili Interactive Labs, Inc."]` gave Pear Therapeutics, Inc. 67 (60 of 90), Big Health, Inc. 56 (50 of 90), Akili 100 (90 of 90); `["deprexis", "HelloBetter"]` gave GAIA AG, Deutschland 78 (70 of 90, EU 31 authorizations) and HelloBetter unresolved.
- **Reading guide as returned:** "value null with status not_assessable means the input is missing; none_found means the source was searched and holds no row for the company. Neither is a zero."
- **Pitfalls:**
  - Company level: "Somryst" resolved to Pear and carries the reSET and reSET-O recall flags of 7 June 2021.
  - Exact matching: "HelloBetter" came back unresolved with every metric `not_assessable`. Write "lookup missed" and ask for the maker's legal name or a register number.
  - `funding_signal_counts` is missing from the Big Health and GAIA AG rows (field absent, neither `none_found` nor `not_assessable`). A missing field is not zero; run `get_funding_signals` for that company if the person needs it. Pear's counts (SEC 46, NIH 6) match its `get_funding_signals` output (`scripts/portfolio_table.py crosscheck`).
  - `reimbursement_listings` is `not_assessable` for every company although the response lists `diga_verzeichnis` (82 records) as loaded (register C11). Reimbursement belongs to `dh-access-and-value` coverage-pathway-and-access-strategy.
  - Combined filing names are "a proposal until a person validates it". Repeat the flag.
  - Not loaded on 19 October 2026: Companies House, the BfArM DiGA directory feed, NICE, any funding source, Zefix.
- **Use:** run `python3 scripts/portfolio_table.py compare FILE.json` on the saved output; it prints the table and the notes the person must see.

## diligence-dh.get_evidence_maturity, counted: A2, only to show one company's rubric inputs

- Saved (`examples/live/evidence_maturity_K191716_somnio.json`): formula, rubric v1 (7 October 2026), each component's rule and inputs, excluded components, interpretation limits. `K191716` resolved to Pear (67); `somnio` to mementor DE GmbH (33, clinical evidence 0 of 40, flag "cleared product(s) with no registered study naming the brand in the loaded sources").
- Assigning an evidence level by a published framework belongs to `company-and-evidence-assessment` (this pack).

## analytics.mcda, counted: task B1, on the person's scores only

- **Saved call** (`examples/live/mcda_partner_options.json`, 19 October 2026, illustrative scores typed for the measurement): three options, four criteria, weights 0.35, 0.25, 0.20, 0.20; values 77.5, 63.75 and 62.5. Method "EVIDEM Multi-Criteria Decision Analysis (weighted-sum, 0-4 scale)".
- **Pitfalls:** every criterion is higher-is-better (`negative_criteria` cannot be set); a missing score returned a bare HTTP 400 (register C17); no robustness view and no tie flag (C17); `name` null on rows. Run `scripts/portfolio_table.py swap` on the input for the check, ties and swap points.
- Never call it with proposed scores, and never with library fields the person has not turned into scores themselves.

## Catalogue jobs

- `portfolio-comparison` is the job the old skill names ("Catalogue job `portfolio-comparison`", tool `diligence-dh.compare_portfolio`). Its `start_job` steps were not saved by any earlier build: **needs a live check**. Until then the direct calls in A2 are the method. On 19 October 2026 `start_job` for other jobs "does not run the buyer's model" and returned steps only (`examples/live/list_jobs_commercial.json` note and the commercial builds).
- `company-dossier` (Diligence) lists `diligence-dh.get_funding_signals` among its tools (`examples/live/list_jobs_commercial.json`, 19 October 2026). The job belongs to `company-and-evidence-assessment` (this pack); A1 makes the one call directly.
- Prices in the job list are hypotheses (USD 49 per job), not charges.

## diligence-dh.retrieve_guidance and list_diligence_sources

- `retrieve_guidance {query: "anti-kickback safe harbor"}` returned no passage, "no passage retrieved in this namespace" (`examples/live/other_calls.json`). Not used here: the filing rules come from `diligence-research.md`. A diligence query was not tried: **needs a live check**.
- The source perimeter is read from the `source_coverage_excerpt` block that `compare_portfolio` returns. `commercial-dh.list_commercial_dh_sources` (free) returned SEC EDGAR 175, NIH RePORTER 18, EU TED 41 and the not-loaded list (`examples/live/other_calls.json`).

## verify.build_record (counted)

- Needs a named human in `cleared_by.name`. `{cleared_by: {name: "Claude"}}` returned "build_record refuses a record without a human cleared_by.name" (`examples/live/verify_build_record_refusal.json`). Call it only when an output leaves the conversation and the person names who clears it.
- `verify.qualify_source` rates regulator and register pages "inadmissible, no provenance" (OIG AO 26-15, `examples/live/other_calls.json`; register C1). The DL rows carry URL, quote and read date; cite them directly.

## Direct SEC and register reads (status step)

- The library holds the CIKs and form types it lists only. A parent, successor or listed registrant (other CIK) and forms such as 15-12G, 25-NSE or SC 13D may be missing. When the log or the store does not cover the window or the status question, say so and name EDGAR company search as the person's direct read (`references/company-status.md`).
- The EDGAR submissions record gives current and former names, exchanges and tickers, needs no API key, and holds at least one year or 1,000 recent filings (DL-150 to DL-152, [WF]).
- If EDGAR is read directly, the User-Agent contact is one the person's organization gives and approves, never the user's email address, name or any account identifier; SEC caps automated access at 10 requests per second (DL-153, [WF]). With no contact given, send nothing and list the filings to open. Never invent a contact.
- Companies House and Zefix are not loaded in the library (19 October 2026); Companies House `company_status` is the person's direct read (DL-157 to DL-161). German insolvency notices: insolvenzbekanntmachungen.de (DL-165 to DL-167).

## Not used here

- `diligence-dh.watch_companies` and every `watch_*` tool: never called.
- `diligence-dh.get_deltas`: change reads belong to `investment-portfolio-monitoring` (this pack) and `pipeline-and-market-monitoring` (this pack).
- `diligence-dh.generate_report` and the `investment-memo` job: `investment-memo-and-decision-record` (this pack); the job is design partners only and is never started.
