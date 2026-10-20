# Tools: calls this skill uses, as measured by earlier builds

Connector: VITAL Digital Health Library (`mcp.vital.expert`), diligence suite `diligence-dh`. Names below are the library's; your assistant may prefix them (for example `diligence-dh_build_company_profile`). Counted calls draw on the library key's monthly allowance; free calls do not.

**How this file was built.** The connector was disconnected during this build (20 October 2026); no call was made. Every behavior below comes from live outputs saved on 19 October 2026 by the dh-go-to-market builds, read on 20 October 2026, and copied into `examples/live/` with the file named for each. Where no saved output exists, the step is marked **needs a live check** and is described from the saved catalogue or tool text only.

## diligence-dh.build_company_profile (counted)

- **Saved call:** `{company: "Akili Interactive Labs, Inc."}` (`examples/live/build_company_profile_akili_2026-10-19.json`, from channel-and-partner-design, read 20 October 2026). Also `{company: "Big Health, Inc."}` inside the partnership-screen job run (`examples/live/job_partnership_screen_2026-10-19.json`, from channel-and-partner-design, read 20 October 2026).
- **Argument:** `company`: exact legal name, brand, FDA submission number, LEI, EUDAMED SRN or SEC filer number. Matching is exact; a near spelling comes back only as a proposal (old skill text).
- **Returned (Akili):** resolution "resolved", basis "normalized_legal_name"; identifiers EUDAMED SRN US-MF-000048993 and SEC CIK 0001741200; three products under product code QFT, regulation 882.5803 (EndeavorRx De Novo DEN200026, 15 June 2020; EndeavorRx 510(k) K231337, 13 December 2023; EndeavorOTC 510(k) K233496, 14 June 2024) with FDA URLs; 10 registered studies, 3 linked by brand and 6 by indication only; two Form D rows (9 June 2021, USD 110,000,007; 23 May 2018, USD 55,000,010); evidence maturity 100 (90 of 90), reimbursement and jurisdiction breadth excluded; retrieved 19 October 2026.
- **Returned (Big Health):** Daylight K233872 (SCP, 30 August 2024) and Sleepio K233577 (QVO, 5 August 2024); 4 studies, none linked by brand; evidence maturity 56 (50 of 90); gaps listed: LEI, EUDAMED SRN, SEC CIK, UK company number, Swiss register number, EU, UK, CH and DE authorization or listing, reimbursement, private funding rounds.
- **Pitfalls:**
  - The De Novo `status` is FDA's raw code "DENG" (register C3). Write "De Novo, granted".
  - `funding` says "[GAP]", "no funding source licensed or integrated", while `funding_and_filings` in the same response lists two Form D amounts (register C2). Read the Form D rows by `public-record-rules.md` section 1; private rounds stay `[GAP]`.
  - `reimbursement` says "no reimbursement source loaded" (register C2). Reimbursement is not this skill's subject: route to `dh-access-and-value` coverage-pathway-and-access-strategy.
  - Company level, not product level: a brand or FDA number resolves to the maker, so every product, study and recall of that maker comes with it. Say which products the row covers.
  - Run `scripts/profile_table.py` on the saved output; never paste the raw response.

## diligence-dh.get_evidence_maturity (counted)

- **Saved calls:** `{company: "K191716"}` and `{company: "somnio"}` (`examples/live/evidence_maturity_K191716_somnio_2026-10-19.json`, from market-segmentation-and-gtm-strategy, read 20 October 2026).
- **Returned:** K191716 resolved to Pear Therapeutics, Inc. (by FDA submission number), score 67 (60 of 90), rubric v1 (7 October 2026), the formula, each component's rule and inputs, reimbursement and jurisdiction breadth not assessable, interpretation limits. somnio resolved to mementor DE GmbH (by exact brand name), score 33 (30 of 90): regulatory status 20 (3 authorizations, no De Novo), clinical evidence 0 (no product-linked studies), product breadth 10; risk flags "cleared product(s) with no registered study naming the brand in the loaded sources" and "2 filing names normalize to this company and are combined; the combination is a proposal until a person validates it".
- **Pitfalls:**
  - The limits say "US sources only", yet somnio's three authorizations earn regulatory points and its maker is German (register P2 evidence, cm notes). Name the register behind each authorization; `scripts/profile_table.py` flags the mismatch.
  - Clinical evidence counts studies in the loaded registry (clinicaltrials: 128 records on 19 October 2026). Published trials outside it do not count: "no registered study linked in the loaded sources", never "no evidence".
  - An FDA number resolves to the company, not the one product.
  - The combined filing names are a proposal: repeat the flag.
  - The score is the library's convention (`evidence-frameworks.md` section 2), never a framework level.

## diligence-dh.compare_portfolio (counted; owned by funding-and-portfolio-comparison)

- Used here when the person wants the same company read beside a peer, and as the only saved source of safety events and recall flags: Pear Therapeutics, Inc. `risk_flags` "fda_recall: Class II on 2021-06-07" for reSET and reSET-O (`safety_events` 2); Big Health and Akili `safety_events: none_found`. Cite these in A1, A2 and B1 whenever recalls or safety bear on the question, with the retrieval date (19 October 2026). `none_found` means the loaded enforcement source was searched and holds no row: "none found in the loaded enforcement source, retrieved 19 October 2026; not proof of none". The saved flag text is truncated ("...") in the saved file; quote it as saved. `build_company_profile` carries no safety or recall field: never print "0" or "none" from its silence. Saved: `examples/live/compare_portfolio_dtx_2026-10-19.json` (Pear 67, Big Health 56, Akili 100; GAIA AG, Deutschland 78 with EU 31 authorizations; HelloBetter unresolved, every metric not assessable). "A cell the sources cannot fill is not assessable, never zero." For a portfolio view, route to `funding-and-portfolio-comparison` (this pack).

## diligence-dh.retrieve_guidance (counted)

- **Saved call:** `{query: "anti-kickback safe harbor", limit: 5}` (`examples/live/other_calls_2026-10-19.json`, read 20 October 2026): no passage, "[GAP]", "no passage retrieved in this namespace"; upstream tool `regulatory-dh.retrieve_guidance`. The regulatory guidance store behaves the same for most queries (register C6).
- **Needs a live check:** no diligence query (for example "Form D", "evidence standards framework", "HIPAA breach notification") has been run. Until one is, the rules in this skill come from `references/` only. If you call it, quote any passage with its `source_url` and retrieval date; a passage with `source_url` "[GAP]" is not a source.

## diligence-dh.list_sources (free)

- **Needs a live check:** no saved output. The old skill text says it returns "every source with credential state, last load, and row counts. A source not loaded states the reason. This call is free."
- **Nearest saved evidence:** `commercial-dh.list_commercial_dh_sources` returns the diligence census sources (`examples/live/list_commercial_dh_sources_2026-10-19.json`, read 20 October 2026). Loaded: openFDA 1,224; openFDA enforcement 892; clinicaltrials 128; EUDAMED software 3,141; SEC EDGAR 175; NIH RePORTER 18; EU TED 41; GLEIF 7; MHRA alerts 10; openFDA MAUDE 107; 510(k) summaries 915. Not loaded, with reasons: Companies House ("API key not yet provisioned"), Zefix ("credentials not available"), DiGA directory ("access under section 21 DiGAV not yet granted"), NICE ("commercial licence deferred until the Market Access product"), funding ("no funding source licensed or integrated"). Regulatory jurisdictions: US 1,226, EU 3,142, UK 0, CH 0, TW 32, CA 227.
- **Pitfall:** the census says the DiGA directory is not loaded while `diga_verzeichnis` (82 records) is listed as loaded in other responses (register C11 evidence). Report both lines; for German listed status route to `dh-access-and-value` coverage-pathway-and-access-strategy.
- **Use:** call it once at the start of A1 to state the perimeter. A source not loaded makes every related field `[GAP]` with that reason.

## Company status (no library tool)

- No diligence-dh tool returns whether a company still exists, filed for bankruptcy, was delisted, deregistered or acquired. A recent row in a profile is not proof the company is active. Use the status step in `company-status.md`.
- SEC pages refuse automated requests without a declared User-Agent contact (DL-153 [WF]). Ask which contact the person's organization uses; never send the person's email address or name and never invent a contact. Without one, list the filings to open and write "Status: [GAP]: not read".
- The EDGAR submissions API needs no key and gives current and former names, exchanges and tickers (DL-150 to DL-152 [WF]).

## Catalogue jobs

- `company-dossier` (Diligence suite, status available on 19 October 2026): tools `diligence-dh.build_company_profile`, `diligence-dh.generate_report`, `diligence-dh.get_funding_signals`, plus the seven `verify.*` tools (`examples/live/list_jobs_2026-10-19.json`, read 20 October 2026). In this pack, `generate_report` belongs to `investment-memo-and-decision-record` and `get_funding_signals` to `funding-and-portfolio-comparison`; this skill uses the profile step. `start_job` returns method steps and runs nothing (`examples/live/start_job_runs_2026-10-19.json`, from gtm-positioning-monitoring); the task steps remain the method. **Needs a live check:** `start_job {job_id: "company-dossier"}` has not been run.
- `evidence-maturity`: named by the old skill ("Catalogue job `evidence-maturity`", tool `diligence-dh.get_evidence_maturity`). **Needs a live check:** no saved job card or `start_job` output.

## verify.qualify_source, verify.check_claim, verify.build_record

- Register pages and regulator documents are rated "inadmissible, no provenance" (register C1; OIG AO 26-15 in `examples/live/other_calls_2026-10-19.json`). The rows in `references/` carry URL, quote and read date; cite them directly.
- For a published paper: `qualify_source {doi}` then `check_claim` with the claim, the passage `{text, locator}` and the full qualify_source object. Accept a claim only when the passage says the same thing in the same direction (register N3); "unverifiable" is not support.
- `verify.build_record` refuses a record without a human `cleared_by.name` (`examples/live/verify_build_record_refusal_2026-10-19.json`, from market-segmentation-and-gtm-strategy). Call it only with the name of the person who clears the output.

## Not used here

- `diligence-dh.get_funding_signals`: `funding-and-portfolio-comparison` (this pack).
- `diligence-dh.generate_report`: `investment-memo-and-decision-record` (this pack). The catalogue job `investment-memo` is never started.
- `diligence-dh.screen_market`, `search_companies`: `market-and-target-screening` (this pack).
- `diligence-dh.get_deltas`: `pipeline-and-market-monitoring` (this pack). `watch_companies` and every `watch_*` tool: never called.
