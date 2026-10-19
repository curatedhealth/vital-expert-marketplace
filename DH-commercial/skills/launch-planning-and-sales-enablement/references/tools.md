# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `commercial-dh_get_launch_sequence`). Counted calls draw on the key's monthly allowance; free calls do not. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`.

The commercial suite reads three upstream suites (Regulatory DH, Diligence census, Market Access DH) and quotes their rows. It holds no data of its own.

## commercial-dh.list_commercial_dh_sources (free)

- No arguments. Returns the census sources, the regulatory jurisdictions and the market access schemes, each with load date and posture.
- Use it first in A1 to say what the library can see. Observed: no UK device registrations (MHRA alerts only), no Swiss records, EU decision dates empty on 3,142 of 3,142, DE_DIGA 82 listings loaded 15 October 2026 but "not the history feed".
- Pitfall: the census row `diga` says "not loaded, access under section 21 DiGAV not yet granted" while Market Access holds the 82 directory listings. Read the Market Access row for DiGA facts.

## commercial-dh.get_launch_sequence (counted)

- Required `reference`. Optional `peers` (up to 10 names), `limit`, `route_hypothesis` (Swiss: `self_pay`, `vvg_supplementary`, `okp_compulsory`; omitted means `[GAP]`).
- Returns events: `field` (decision_date, listed_on, changed_on), `value`, `upstream_tool`, `source_url`, `retrieved_at`, `product`.
- Observed pitfalls:
  - Peers that do not match a stored name are dropped silently: `{reference: "deprexis", peers: ["HelloBetter Depression","selfapy","Somryst"]}` returned deprexis only, with no line per missing peer. Use exact stored names; get them from `market-access-dh.find_scheme_precedents` first. Write each missing peer as "not found in the library `[GAP]`" yourself.
  - A brand name does not reach the regulatory record: `{reference: "Somryst"}` returned no event for Somryst; `{reference: "K191716"}` returned the FDA decision date 23 March 2020. Pass the FDA submission number for US products.
  - A short name merges different products: peer "HelloBetter" returned six listings with different DiGA-IDs (00965, 01304, 01376, 01497, 01513, 01772) all labeled "HelloBetter". Separate them by the DiGA-ID in `source_url` and say which product each is.
  - `changed_on` equals `listed_on` for most DiGA (only a day-zero snapshot is stored). A second `changed_on` (for example Selfapy 11 April 2022, Novego 9 October 2023, HelloBetter 17 July 2023, each pointing to a BfArM media file) carries no status value: report the date and source, and say "status after the change not stated `[GAP]`".
  - The route is only the caller's hypothesis; the response says a stored listing does not set it.

## commercial-dh.get_launch_readiness (counted, large)

- Required `reference`. Optional `intended_use`, `user`, `buyer`, `payer`, `note`, `claims` (up to 20), `segment`, `name`, `route_hypothesis`.
- Returns seven criteria (`roles`, `note`, `authorization`, `claims`, `route`, `peers`, `price`), each met, attested or `[GAP]`, with `met_count`, plus embedded money flow, claims audit, pricing corridor and peer screen.
- Observed: the deprexis call returned 102,610 characters (more than many assistants can read in one turn). Ask the person before calling; read only `criteria`, `met_count` and the claims labels.
- Observed pitfalls: `claims` is "met" once claims are labeled, whatever the labels; `peers` is "met" with `peer_count 0` (the screen rejected the segment "deprexis": use one of cdss, digital-health, dtx, rpm, samd-diagnostic); `price` is "met" from the public register price; `authorization` is `[GAP]` for deprexis although the same response's regulatory block holds an EU_MDR CE_MARK Class I record (Basic UDI-DI 42606706365P). Report `met_count` as the connector's count, never as readiness.
- Price rows inside it are register amounts and include other products' prices (register item N4). Price figures from commercial tools are hypotheses for this skill; payer prices are Market Access's subject.

## commercial-dh.generate_commercial_brief (counted, large)

- Alias of `generate_report` with template `memo`. Same arguments as readiness plus `format` and `limit`.
- Observed for deprexis (segment `dtx`, limit 5): 72,154 characters; the body is mostly raw JSON in code blocks (1,845 lines), the Identity section lists 31 GAIA AG products, the Peers section says "peer_count 10" and names none, the Pricing corridor section is empty, and the gap list says "DE authorization or listing: DiGA directory: access not granted" beside a DE_DIGA permanent row.
- Use it only when the person wants the connector's full dossier as an attachment. Never paste it as the answer; build the answer from `assets/launch-sequence-output.md`.

## commercial-dh.audit_claims (counted)

- Required `reference`. Optional `claims` (up to 20), `intended_use`.
- Labels each claim `matches_record`, `exceeds_record` or `no_authorization_on_file` against the intended purpose stored on the regulatory record.
- Observed: the library stores no intended purpose text. For K191716 (Somryst, 510(k), product code QVO, "Computerized Behavioral Therapy Device For Insomnia") all four claims were `exceeds_record`, including the on-label one ("delivers cognitive behavioral therapy for chronic insomnia to adults 22 and older") and the coverage claim ("covered by Medicare"). For deprexis by name all claims were `no_authorization_on_file`, although an EU record exists. The labels therefore do not separate on-label from off-label claims today.
- Use: record the label in the claim table as the connector's label, then flag each claim with `references/claim-rules.md` against the labeling text the person supplies. Never treat `exceeds_record` or `matches_record` as a finding.
- It also returns an evidence maturity block. Observed: risk flags for reSET and reSET-O recalls attached to a Somryst query (company-level, not product-level). Do not cite them as the product's safety record.

## market-access-dh.find_scheme_precedents (counted)

- Required `scheme`. Optional `indication`, `product_category`, `limit` 1 to 25.
- Use it to get exact stored peer names before `get_launch_sequence`. For DiGA search by ICD code or German term: `{scheme: "DE_DIGA", indication: "F32"}` returned seven depression DiGA (most recent listing first), each with DiGA-ID, status, `listed_on`, price and source URL.
- `ends_on` is empty on every DiGA row; trial end dates are `[GAP]`.

## regulatory-dh.get_authorization (counted)

- Required `reference`: a K, DEN or P number, a Basic UDI-DI, or "<SRN> <trade name>".
- Use it to read a US comparable's classification regulation before citing DMHT or wellness rows. Observed 19 October 2026: `{reference: "K191716"}` returned Somryst, 510(k), product code QVO, `regulation_number` 882.5801, predicate DEN160018, source openFDA, retrieved 13 October 2026 (`examples/live/get_authorization_K191716.json`).

## literature.* and verify.* (counted), for A2 evidence

- To support a claim with a publication: `verify.qualify_source` with the DOI, then `verify.check_claim` with the claim, a quoted passage `{text, locator}` and the source. Accept "supported" only when the passage reads in the same direction as the claim (register N3: `check_claim` has returned "supported" on word overlap). `verify.verify_text` with bare DOIs returns "unverifiable" (register C18).
- Register pages and regulator guidance are rated "no provenance" by Verify (register C1): cite them to their URL instead of sending them to Verify.

## analytics.rice (counted), for B1 only on the person's scores

- `initiatives`: each with `id`, `reach`, `impact` (0.25, 0.5, 1, 2 or 3), `confidence`, `effort`. Every number is the person's.
- Observed (illustrative numbers, `examples/live/rice_runs.json`): `confidence` is read as a percent and divided by 100 without warning. Passing 0.8 gave 0.008 and scores 100 times too small; passing 80 gave the expected scores (120 x 1 x 0.5 / 1 = 60). Pass confidence as a percent and check one score by hand. `name` comes back null; the response carries an unrelated note about price figures.

## analytics.mcda (counted), for B1 only on the person's scores

- Not called in this build. Earlier builds measured it (register C17): scores 0 to 4, weights summing to 1, every criterion treated as higher-is-better, no robustness view, ties not flagged. Phrase criteria so that higher is better and work out where weights would flip the order by hand.

## verify.build_record (counted)

- Needs a named human in `cleared_by`; refuses a missing name or a tool or model name. Use it only when an output leaves the conversation.


## Catalogue jobs (list_jobs, get_job, find_job, start_job)

Measured 19 October 2026 (`examples/live/list_jobs_commercial.json`). `list_jobs` returned 13 Commercial jobs, all `available`. `start_job` takes only `job_id`; it returns the method steps, the tool names and the inputs of the non-Verify tools, and "does not run the buyer's model". The assistant then makes the calls itself. Every job closes with the seven `verify.*` tools; `verify.build_record` still needs a named human. Prices in the job list are hypotheses, not charges.

Connector finding (all three new jobs): the jobs list `analytics.segmentation`, `analytics.scenario-modeler` and `analytics.risk-tornado`, and `start_job` describes their inputs, but the connector exposes only four analytics tools (`mcda`, `rice`, `budget-impact-model`, `vba-price-anchor`). A search for those names returned none of them. When a job reaches one of these steps the output shows `[GAP] ...: tool not exposed`; nothing is computed in its place.

### sales-leave-behind (task B1), live run on K191716

- Steps returned: brief, price corridor and, if asked, literature first; then the buyer's claims, roles and note; `audit_claims` on the claims; keep the product name on each corridor row; do not store; close with Verify.
- Calls made: `generate_commercial_brief {reference: "K191716", format: "json", limit: 3, segment: "dtx", user, buyer, payer (placeholder), claims: [the one approved claim], note}`; `get_pricing_corridor {reference: "K191716"}`; `audit_claims {reference: "K191716", claims: [same]}`; and a DiGA check `audit_claims {reference: "somnio", claims: [1]}`. Saved: `examples/live/job_sales_leave_behind_K191716.json`.
- What came back: brief JSON of 379,126 characters; readiness `met_count` 5 of 7 (route and price `[GAP]`); peers: ten dtx companies including Pear Therapeutics itself; corridor `[GAP]` (no Market Access row for K191716); the on-label claim labeled `exceeds_record` (no intended purpose stored).
- Pitfalls: (1) the job says "each price row names its product", but corridor rows have no product field (register N4); (2) the job says a DiGA listing is printed beside `no_authorization_on_file`, but the somnio response has no `listing_on_file` field; (3) a placeholder payer string is counted as "attested" in readiness, so omit an unnamed role; (4) `start_job` lists route values `us_commercial`, `de_diga`, `fr_reimbursement`, `uk_nice`, but the brief's tool schema accepts only the three Swiss values.
- What it leaves as a gap: the leave-behind text itself. The job is research; the leave-behind is built in B1 from approved claim ids only.

## Not called here

- `commercial-dh.watch_product`: not called (watches are not separated per customer key; register N2). Launch monitoring belongs to the sibling skill.
- Prices from `get_pricing_corridor` and analytics price tools: not used. Price positioning is Commercial 3.1; payer prices are Market Access.
