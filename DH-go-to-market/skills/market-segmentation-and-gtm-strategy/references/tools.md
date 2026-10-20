# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them. Counted calls draw on the library key's monthly allowance; free calls do not. Behavior below was observed in live calls on 19 October 2026 (trimmed outputs in `examples/live/`). The library twice returned "could not answer this call (503). Nothing was counted"; a retry a minute later worked.

## commercial-dh.list_commercial_dh_sources (free)

- No arguments. Returns three feed lists: the diligence census sources (record counts, last load, what is not loaded and why), the regulatory jurisdictions (authorization counts), and the Market Access schemes (kind, clock rule, listing count, posture).
- Use it first in A1: it is the perimeter. On 19 October 2026: no UK company register, no Swiss register, no funding source, no NICE license; UK and CH device authorizations 0; FR_LPPR, UK_NICE_NHAP, AU_MSAC, CH_BAG, ES_REDETS, FI_DIGIHTA, SE_TLV hold no listings.
- Pitfall: the census says the DiGA directory is "not loaded" while the Market Access scheme DE_DIGA holds 82 listings from a directory mirror. For German peers and routes, use `market-access-dh.find_scheme_precedents` on DE_DIGA.

## commercial-dh.screen_commercial_peers (counted)

- Arguments: `segment` (a diligence taxonomy segment: `dtx`, `samd-diagnostic`, `cdss`, `rpm`, `digital-health`, or a company name), optional `name` (a product to include), `limit` 1 to 25.
- Runs `diligence-dh.screen_market`, then `regulatory-dh.search_devices` and `market-access-dh.search_listings` for each peer name.
- Ranking is evidence maturity score, then company name; "this screen covers only the companies the store holds, not the market". On 19 October 2026 the store loaded only the `dtx` segment and jurisdictions CA, EU, TW, US; `segment: dtx` gave 18 matches, all ten returned were US companies.
- Pitfalls:
  - Peer lookups use the company's legal name, so `search_devices` found nothing for 9 of 10 companies although the screen counts their authorizations (for example "Akili Interactive Labs, Inc.", 3 authorizations, no device row). Read products from `screen_market.results[].products` and, if needed, look up a product by name.
  - `search_listings` found nothing for any of the ten, and the coverage line says `market_access_dh.search_listings: [GAP]` even though the tool answered. Code-based US routes (DMHT, RPM) list codes, not products, so a product never matches them.
  - `name` takes one of the `limit` slots: `limit: 3, name: "Somryst"` returned Somryst plus the top two companies.
  - The response for `limit: 10` was 62,474 characters. Use `scripts/gtm_helpers.py peers` on the saved output.
  - The exhibit can show raw FDA codes ("DENG" for a granted De Novo).
  - Name-based peer lookups miss 882.5801 devices: the screen lists Daylight and Sleepio as Big Health products, but its device lookup by the legal name returned no row (`examples/peer_table_dtx_2026-10-19.md`). For a US DMHT segment, also call `regulatory-dh.search_devices` with `{query: <short maker name>, jurisdiction: "US"}` for each known maker ("Big Health" returned Sleepio K233577, QVO, 882.5801, and Daylight K233872, SCP; `examples/live/search_devices_BigHealth_US.json`). Report regulation number and product code; where the miss remains, say 'lookup missed' and name the product code to search.

## diligence-dh.screen_market (counted)

- Arguments: `segment`, `jurisdiction` (US, EU, UK, CH), `min_evidence_maturity`, `limit`.
- `segment: dtx, jurisdiction: EU` returned one company (Novasight, Israel). German DiGA makers are not in this screen. An empty or short screen is a coverage limit, not an empty market.

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

## diligence-dh.build_company_profile (counted, used only where a company view is needed)

- `company`: exact legal name, brand, FDA number, LEI, EUDAMED or SEC number. Returns identifiers, products with authorizations, studies, recalls, filings, evidence maturity with its formula, and gaps per source. `generate_report` with `template: commercial` embeds this profile, so do not call both for the same company.

## commercial-dh.generate_report (counted)

- Required `reference`. `template`: memo, identity, regulatory, reimbursement, commercial. Optional `segment`, `limit`, `buyer`, `user`, `payer`, `claims`, `intended_use`, `route_hypothesis` (Swiss only).
- `template: commercial` for Somryst returned sections Identity, Peers, Money flow, Claims audit, Launch sequence, Readiness checklist, Gaps, References. The first line states it is not a regulatory opinion.
- Pitfalls:
  - Identity is a raw JSON block inside the markdown; restate it as a table, never paste it.
  - Peers shows only a count ("peer_count 10"), no names; take names from `screen_commercial_peers`.
  - The readiness checklist marked authorization `[GAP]` (via `get_authorization`, which found nothing for "Somryst") while the same report's identity block holds 510(k) K191716 of 23 March 2020. Use the identity block and cite the FDA URL.
  - Reimbursement shows "no reimbursement source loaded" although US_CMS_DMHT conditions name 21 CFR 882.5801, Somryst's regulation number. The route exists for the segment; whether this product qualifies is Market Access's question.
  - Money flow echoes the three roles the caller gave; it adds no facts.
- Use it only when the person wants a shareable landscape memo for one named product; otherwise A1's table is the output.

## market-access-dh.find_scheme_precedents (counted)

- Required `scheme`; optional `indication`, `limit`. Use it here only for listed status: which peers are listed in a market's scheme for the indication. Search DiGA by ICD code ("F51" returned somnio, HelloBetter Schlafen, somnovia, all permanent). DMHT returns the three codes with their conditions (21 CFR 882.5801 and 882.5803).
- Prices in these rows are Market Access's subject and are hypotheses for this skill; do not put them in a segment table.
- Pitfall: `listed_on` is the first listing date, not the date the current status began. For each DiGA peer, call `market-access-dh.get_status_history {reference, scheme: "DE_DIGA"}` (counted) and report the status date where a BfArM notice records it (HelloBetter Schlafen: listed 18 December 2022, permanent from 17 December 2024, BfArM notice 18 of 2 January 2025). The first history entry's `changed_on` is the listing date and is labeled with the current status; it is not a status change. somnio and somnovia held only that first-load snapshot on 19 October 2026 (`examples/live/get_status_history_DE_DIGA_F51.json`).

## commercial-dh.get_deltas (counted)

- Not used in this skill's tasks; see the positioning monitoring skill.

## analytics.mcda (counted)

- `alternatives` (each `id` and `scores`, a map of criterion to 0 to 4), `criteria_weights` (sum to 1). Returns EVIDEM weighted-sum `value_estimate` (0 to 100) and contributions per criterion, with the method citation.
- Every criterion is treated as higher-is-better (`negative_criteria` is always empty and cannot be set). Phrase criteria so 4 is best (for example "room in the segment" rather than "competition").
- No robustness view and no tie flag. Use `scripts/gtm_helpers.py swap` for the weight at which adjacent segments swap.
- Ranks only what the person scored. Never call it with proposed scores.

## verify.build_record (counted)

- Needs a named human in `cleared_by.name`. `{cleared_by: {name: "Claude"}}` returned "build_record refuses a record without a human cleared_by.name". Call it only when an output leaves the conversation.

## agent-pack.list_experts (free) and download_agent

- `function: digital-commercial` lists nine experts, including `digital-marketing-manager` (this skill's worker), `digital-marketing-manager-dh` and `sales-leader-digital-health`. The buyer can download the worker with `agent-pack.download_agent`.

## Catalogue jobs (start_job)

- `start_job {job_id}` takes only the job id. On 19 October 2026 it returned the job's method steps, tool names and input fields, and ran nothing ("This call does not run the buyer's model. Close with the Verify tools named above."). It cannot be pointed at a product. The direct calls in each task remain the method (`examples/live/start_job_runs.json`).
- `competitor-landscape`: steps "Call commercial-dh.generate_report for the category", then `diligence-dh.compare_portfolio`, then Verify; "Do not call regulatory-dh.compare_authorizations. That job is activation pending." Pitfall: `generate_report` requires a product or company `reference`, so "for the category" cannot be run as written; run it for one named product (Somryst, `examples/live/generate_report_somryst_commercial.json`) and run `compare_portfolio` on the peers.
- `screen-commercial-peers`: one call, `screen_commercial_peers`, and "Keep a feed that did not answer as a gap."
- `partner-prioritization`: `analytics.mcda` on the buyer's alternatives, scores and weights (or `analytics.rice` for initiatives); "Show the weights and scores beside the rank." Same pitfalls as `analytics.mcda` above.

## Not used here

- `watch_product` and other watch tools: never called.
- `commercial-dh.audit_claims`: belongs to the claims audit (DH-02.01.3.2).
- `get_pricing_corridor`, `map_money_flow`: pricing (DH-02.01.3.1).
