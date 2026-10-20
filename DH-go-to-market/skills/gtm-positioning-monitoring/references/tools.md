# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them. Counted calls draw on the library key's monthly allowance; free calls do not. Behavior below was observed in live calls on 19 October 2026 (trimmed outputs in `examples/live/`). The library twice returned "could not answer this call (503). Nothing was counted"; a retry a minute later worked.

Artifact checks (A1) run on the person's own copies and need no connector. The person's artifacts, lines and claim lists never go into a library call.

## commercial-dh.list_commercial_dh_sources (free)

- No arguments. Census sources, regulatory jurisdictions and Market Access schemes, with counts, last load dates and what is not loaded.
- Use it in A2 as the dated perimeter and to compare scheme counts and clock rules with an earlier saved run. On 19 October 2026: DE_DIGA 82 listings (15 October 2026); US_CMS_DMHT 3 and US_CMS_RPM 4 codes; UK and CH device authorizations 0; no funding source.
- Pitfall: the census lists the DiGA directory as not loaded while the DE_DIGA scheme holds 82 listings from a directory mirror.

## commercial-dh.get_deltas (counted)

- Required `reference` (product code, manufacturer or company name); optional `since` (YYYY-MM-DD). Copies events from regulatory, diligence and Market Access delta tools.
- `{reference: "Pear Therapeutics, Inc.", since: "2026-01-01"}` returned no events; the Market Access feed returned "market_access_dh.get_deltas is not on that server".
- Pitfall: the wrapper drops the diligence change-log block (when the log began, last sweep, limits). Without it "no events" cannot be read. For companies, call `diligence-dh.get_deltas` directly.

## diligence-dh.get_deltas (counted)

- Required `companies` (1 to 12 names) and `since`. Returns per company "no change recorded" or the changes, plus the log: first entry 12 October 2026, last sweep 19 October 2026, and limits ("the since filter uses event dates ... not observed_at"; "no change recorded is a statement about in-window event-dated log rows up to last_sweep_at").
- `{companies: ["Big Health, Inc.", "Akili Interactive Labs, Inc."], since: "2025-01-01"}`: no change recorded for both. Changes dated before the log began may be missing; say so.

## commercial-dh.screen_commercial_peers (counted)

- `segment` (taxonomy: on 19 October 2026 only `dtx` loaded), optional `name`, `limit` 1 to 25. Ranked by evidence maturity score; covers only the companies the store holds.
- For monitoring, rerun with the same arguments as the saved earlier run and compare with `scripts/positioning_check.py peers-diff`. Runs with different arguments are not comparable (the script warns).
- Pitfalls: per-peer device lookups use company names and missed 9 of 10 companies; `name` takes one of the `limit` slots; the `limit: 10` response was 62,474 characters.

## diligence-dh.compare_portfolio (counted)

- Required `companies`, 2 to 12 references (legal name, brand, FDA number, LEI, EUDAMED or SEC number). Returns per company: resolution basis, authorizations by jurisdiction, studies by link tier, safety events, funding signal counts (SEC EDGAR, NIH RePORTER, EU TED), evidence maturity with components, risk flags, and a comparison table. "A cell the sources cannot fill is not assessable, never zero."
- Live, 19 October 2026: `["Somryst", "Big Health", "Akili Interactive Labs, Inc."]` gave Pear Therapeutics, Inc. 67 (60 of 90), Big Health, Inc. 56 (50 of 90), Akili 100 (90 of 90); `["deprexis", "HelloBetter"]` gave GAIA AG, Deutschland 78 (70 of 90, EU 31 authorizations) and HelloBetter unresolved (`examples/live/compare_portfolio_dtx_2026-10-19.json`).
- Pitfalls:
  - Company level, not product level: a brand resolves to its maker, so "Somryst" carries Pear's reSET and reSET-O recall flags. Say which products the row covers.
  - Exact matching: "HelloBetter" returned every cell `not_assessable`. Use the maker or brand exactly as a listing or the screen states it; otherwise write "lookup missed".
  - `reimbursement_listings` is `not_assessable` ("no reimbursement source is loaded") for every company, although the same response lists `diga_verzeichnis` (82 records) as loaded. Take listed status from `market-access-dh.find_scheme_precedents`.
  - Combined filing names ("GAIA AG" and "GAIA AG, Deutschland") are flagged "a proposal until a person validates it". Repeat the flag.

## diligence-dh.get_evidence_maturity (counted)

- Required `company` (exact name, brand or FDA number). Returns the score, the formula ("score = round(100 x points earned / assessable maximum); a component whose source is not loaded is excluded from the maximum, not counted as zero"), rubric v1 (7 October 2026), each component's rule and inputs, excluded components (reimbursement, jurisdiction breadth) and interpretation limits ("a stated convention for comparing documented evidence, not a predictive model or a valuation").
- Live, 19 October 2026: `K191716` resolved to Pear Therapeutics, Inc., 67; `somnio` resolved to mementor DE GmbH, 33 (clinical evidence 0 of 40, flag "cleared product(s) with no registered study naming the brand in the loaded sources") (`examples/live/evidence_maturity_K191716_somnio.json`).
- Use: context about a peer's published evidence. Never a judgment of the person's product, a segment score, or a prediction. Do not run it on the person's own product to rate it; if they ask, show the inputs and the excluded components and leave the reading to them.
- Pitfalls:
  - The limits say "US sources only; absence of EU, UK or Swiss data lowers nothing", yet EU authorizations earn regulatory points (somnio: 3 authorizations, 20 points; deprexis: EU 31). Name the register behind each authorization.
  - Clinical evidence counts registered studies in the loaded trial registry only. A DiGA maker with published trials can score 0 here; say "no registered study linked in the loaded sources", never "no evidence".
  - An FDA number resolves to the company, not the single product.

## market-access-dh.find_scheme_precedents (counted, listed status only)

- `{scheme: "DE_DIGA", indication: "F51", limit: 10}` returned three permanent insomnia DiGA with listing dates. Rerun to see a new listing in the person's indication; the directory copy is a mirror first loaded 15 October 2026.

## market-access-dh.get_status_history (counted, listed status only)

- `{reference: <product>, scheme: "DE_DIGA"}` returns the stored status changes. HelloBetter Schlafen: a BfArM notice entry, permanent from 17 December 2024, BfArM notice 18 of 2 January 2025. somnio and somnovia: only the first-load snapshot, with the gap "transition history not published in loaded sources" (`examples/live/get_status_history_DE_DIGA_F51.json`, 19 October 2026).
- Pitfall: the first entry's `changed_on` is the listing date and carries the current status label; it is not a status change. Do not say the library has no DiGA history: it holds BfArM notices where loaded.

## verify.build_record (counted)

- Needs a named human in `cleared_by.name`; a model name is refused ("build_record refuses a record without a human cleared_by.name").

## agent-pack.list_experts (free)

- `function: digital-commercial` lists the worker `digital-marketing-manager` and the department head `digital-marketing-manager-dh`, who "maps every proposed claim to a graded source ... and flags off-label and listing-as-proof mistakes".

## Catalogue jobs (start_job)

- `start_job {job_id}` takes only the job id. On 19 October 2026 it returned the job's method steps, tool names and input fields, and ran nothing ("This call does not run the buyer's model. Close with the Verify tools named above."). It cannot be pointed at a product. The direct calls in each task remain the method (`examples/live/start_job_runs.json`).
- `competitor-landscape`: steps "Call commercial-dh.generate_report for the category", then `diligence-dh.compare_portfolio`, then Verify; "Do not call regulatory-dh.compare_authorizations. That job is activation pending." Pitfall: `generate_report` requires a product or company `reference`, so "for the category" cannot be run as written; run it for one named product (Somryst, `examples/live/generate_report_somryst_commercial.json`) and run `compare_portfolio` on the peers.
- `screen-commercial-peers`: one call, `screen_commercial_peers`, and "Keep a feed that did not answer as a gap."

## Not used here

- `watch_product` and other watch tools: never called. Monitoring uses dated reruns saved by the person.
- `commercial-dh.audit_claims`: the claims audit (DH-02.01.3.2) owns claim checks; this skill routes flagged claims there.
- `verify.check_claim` on marketing copy: it decides on word overlap (register N3); not used to judge a line.
