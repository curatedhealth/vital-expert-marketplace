# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them (for example `commercial-dh_map_money_flow`). Counted calls draw on the library key's monthly allowance; free calls do not.

Behavior below was observed in live calls on 19 October 2026. Trimmed outputs: `examples/live/`.

## commercial-dh.list_commercial_dh_sources (free)

- No arguments. Returns three blocks: the census sources, the regulatory jurisdictions and the Market Access schemes.
- Use it to say what the library holds before any gap is written. On 19 October 2026: DE_DIGA 82 listings (loaded 15 October 2026), US_CMS_RPM 4, US_CMS_DMHT 3, FR_PECAN 2, FR_LATM 2, FR_LPPR 0.
- Pitfall: in the same response the census block lists the source "diga" (DiGA directory BfArM) as `not_loaded` ("access under section 21 DiGAV not yet granted") while the Market Access block holds 82 DE_DIGA listings from `diga_verzeichnis`. The listings are a public mirror; the BfArM feed and history are what is missing. Say so if the person asks where German prices come from.

## commercial-dh.map_money_flow (counted)

- `reference` (required) plus caller-supplied `user`, `buyer`, `payer`, `note`. An unnamed role comes back `[GAP]`.
- Returns the three roles as given, `conflated` (true when two roles are the same string), and the product's market matrix from `market-access-dh.get_market_matrix` (listed or `[GAP]` per scheme, with status, date and source URL).
- Pitfall: the sankey exhibit links the roles in argument order (user to buyer to payer) with no amounts and no direction of payment. It does not show who pays whom. Draw the money flow from the person's description, not from the exhibit.
- It adds no fact the caller did not give, apart from the listing block. Unlisted schemes are `[GAP]`, never "not reimbursed".

## market-access-dh.find_scheme_precedents (counted)

- Required `scheme`. Optional `indication`, `product_category`, `limit` 1 to 25.
- Use it for comparators. For DE_DIGA search by ICD-10-GM code or German term: `{scheme: "DE_DIGA", indication: "F51"}` returned somnovia (236 EUR), HelloBetter Schlafen (241.25 EUR) and somnio (224.99 EUR), each with listing date, source URL and retrieval date 15 October 2026. English terms can miss rows.
- Pitfall: `price` carries no unit, prescription period or manufacturer-versus-negotiated flag.

## commercial-dh.get_pricing_corridor (counted)

- Required `reference`. Fans out to Market Access tools; the somnio response was 69,786 characters.
- Defect (register N4, confirmed again): `prices` held somnio's own price twice (224.99 EUR; once from `search_listings` with a source URL, once from `compare_schemes` with `source_url: null`) and ten prices (490 to 795 EUR) from `find_scheme_precedents` rows of other DiGA in any indication, without product names. None of the three insomnia comparators was among them.
- Use: only the row whose `source_url` matches the named product, as its registered price. Build comparators with `find_scheme_precedents` and an indication. `scripts/comparator_prices.py` does the separation on saved output.

## analytics.vba-price-anchor (counted)

- `comparator_cost_per_patient`, `incremental_qalys`, `wtp_thresholds` (plain list of numbers; objects return HTTP 422 although the schema says objects, register N5).
- Returns per threshold `value_based_budget_per_patient` and `price_per_unit_ceiling`, plus defaults `non_drug_cost_offset_per_patient: 0` and `units_per_patient: 1`, which the arguments cannot set. Live: 800, 0.03, [20000, 30000] returned 1,400 and 1,700.
- Every input is the person's, including the threshold. The output is a hypothesis.

## analytics.budget-impact-model (counted when it answers)

- Returned HTTP 422 on 19 October 2026 with `uptake_curve` as `[{year, uptake}]` ("Nothing was counted"). Earlier builds saw 422 on four other shapes (register N5). Run the arithmetic in the conversation instead (see `price-evidence.md`).

## verify.qualify_source and verify.check_claim (counted)

- Use for a literature or guidance passage behind a value message (task B1), never for register facts (register C1).
- Working sequence: `qualify_source` with the DOI, PMID or URL, then `check_claim` with the claim, the verbatim passage (`text`, `locator`) and the returned source object.
- `qualify_source {url: "https://www.fda.gov/media/102575/download"}` rated the FDA CFL guidance "silver" (first attempt returned HTTP 503).
- Pitfall (register N3): `check_claim` decides on word overlap. The claim in the passage's direction returned "supported" (69 percent overlap); its negation returned "partial" (58 percent), not "contradicted". Accept a "supported" only after you have read the passage yourself and it states the claim in the same direction.
- Pitfall (register C18): the returned citation has `title: null` and `year: null` although `qualify_source` returned the title. Cite from the `qualify_source` result.

## verify.build_record (counted)

- Needs a named human in `cleared_by`. `{cleared_by: {name: "Claude"}}` returned "build_record refuses a record without a human cleared_by.name". Use only when an output leaves the conversation.

## literature.search_literature (counted when it answers)

- Returned HTTP 503 twice on 19 October 2026. If the person needs a published source for a value message and the search fails, ask the person for the DOI or the document and qualify that.


## Catalogue jobs (list_jobs, get_job, find_job, start_job)

Measured 19 October 2026 (`examples/live/list_jobs_commercial.json`). `list_jobs` returned 13 Commercial jobs, all `available`. `start_job` takes only `job_id`; it returns the method steps, the tool names and the inputs of the non-Verify tools, and "does not run the buyer's model". The assistant then makes the calls itself. Every job closes with the seven `verify.*` tools; `verify.build_record` still needs a named human. Prices in the job list are hypotheses, not charges.

Connector finding (all three new jobs): the jobs list `analytics.segmentation`, `analytics.scenario-modeler` and `analytics.risk-tornado`, and `start_job` describes their inputs, but the connector exposes only four analytics tools (`mcda`, `rice`, `budget-impact-model`, `vba-price-anchor`). A search for those names returned none of them. When a job reaches one of these steps the output shows `[GAP] ...: tool not exposed`; nothing is computed in its place.

### health-system-value-brief (pricing A2 and B1; account growth A2), live run on somnio with illustrative numbers

- Steps returned: price corridor and, if asked, literature first; a collected number enters a calculator only if the seller adopts it; budget impact; price anchor; scenario and tornado when the seller gives a formula and a period count; print a gap if a calculator rejects the payload; do not store; close with Verify.
- Calls made: `get_pricing_corridor {reference: "somnio"}`; `literature.search_literature {query: "digital cognitive behavioral therapy for insomnia health care costs", limit: 3}`; `analytics.budget-impact-model` (population 2,000, two-option current mix, new cost 400, uptake [0.1, 0.2, 0.3], all ILLUSTRATIVE); `analytics.vba-price-anchor {comparator_cost_per_patient: 900, incremental_qalys: 0.02, wtp_thresholds: [50000, 100000]}` (ILLUSTRATIVE). Saved: `examples/live/job_health_system_value_brief_somnio.json`.
- What came back: corridor of 12 rows, one of them somnio's own price (224.99 EUR, DiGA 00508, with source URL), a duplicate without URL, and ten other DiGA prices with no product names (register N4); literature answered with three records, none carrying a cost figure, and labeled a published BJGP Open paper "preprint"; budget impact HTTP 422 (nothing counted; register N5); price anchor 1,900 and 2,900 (900 + 0.02 x threshold; defaults offset 0, units 1).
- Pitfalls: (1) scenario-modeler and risk-tornado are not exposed; (2) the budget impact calculator still rejects every payload shape tried; (3) corridor rows other than the product's own must be dropped before any number is offered for adoption.
- What it leaves as a gap: budget impact (calculator), scenario and sensitivity (tools not exposed), any number the seller has not typed or adopted.

## Not used here

- `watch_*` tools.
- `commercial-dh.audit_claims` for claims at large: the claims audit belongs to the sibling monitoring skill. In this skill it is called only in B1 Step 2b, on a case study's claims, for the authorization record; labels are the connector's, never findings (no intended purpose is stored).
