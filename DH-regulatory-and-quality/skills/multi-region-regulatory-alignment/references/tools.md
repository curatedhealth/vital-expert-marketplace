# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them (for example `regulatory-dh_search_devices`). Counted calls draw on the library key's monthly allowance; free calls do not.

Behavior below was observed in live calls on 19 October 2026. Saved outputs are in `examples/live/`.

## regulatory-dh.list_jurisdictions (free)

- No arguments. Returns per jurisdiction: stored authorizations, safety events, last load date, sources, scope; plus a `closed` list of jurisdictions the library cannot load and why.
- Observed: US 1,226 authorizations (openFDA, last load 19 October 2026); EU 3,142 (EUDAMED software, decision date empty on all 3,142); UK 0 authorizations (MHRA alerts only; MHRA PARD not loaded); CH 0 (swissdamed web-only); TW 32; CA 227 (MDALL name search). Closed: JP (PMDA forbids automated download), AU (TGA commercial use blocked), BR and SG (no software class), CN, KR and others.
- Use it first. It tells you which regions the library can answer at all. Australia, Brazil, Japan, Great Britain registration and Switzerland are "register not loaded" for the whole task.

## regulatory-dh.search_devices (counted)

- Required: `query` (product or manufacturer name, 3+ characters). Optional: `jurisdiction` (US, EU, UK, CH, all), `limit` 1 to 25, `software_only` ("true" default, or "false").
- Returns per record: product, manufacturer, jurisdiction, regime (US_FDA, EU_MDR, EU_MDD), pathway, risk class as the source states it, status, decision date, product code (FDA) or EMDN code (EU), predicates (FDA), identifiers (K or DEN number, Basic UDI-DI), source URL and retrieval date.
- Pitfalls seen:
  - EU rows have no decision date (empty on every stored EU record) and their `source_url` is the generic EUDAMED search page, not the record. Cite the Basic UDI-DI so the person can find it.
  - One product can have MDD-era and MDR records with different classes (Brainomix e-ASPECTS: EU_MDD Class IIa records and an EU_MDR Class IIb record, all "On the EU market"). Report each record by regime and identifier; never infer why the class differs.
  - Results are capped by `limit` and US records come first: "Brainomix" with `limit` 10 stopped at 7 US and 3 EU records; with `limit` 25 it returned 19, including the MDD-era EU records. Use `limit` 25 when building a map, and say so if the cap is reached.
  - Canada is listed by `list_jurisdictions` but is not in this tool's jurisdiction list and its coverage lines omit CA; the 227 CA rows cannot be reached here. Check MDALL directly.
  - A miss ("Viz.ai" returned nothing) is "register loaded, product not found", never "not authorized".

## regulatory-dh.compare_authorizations (counted)

- Required: `references`, 2 to 12 (K, DEN or P numbers, Basic UDI-DIs, or "SRN trade name"). Optional `jurisdiction`.
- Returns a side-by-side table: class, pathway, decision date, predicate, safety-event count. A field the source does not state is "not assessable".
- Use it to show the same software across regions in one table (for example K243294 and ++B720EASPECTSCEGK). The EU column will show "not assessable" for decision date and predicate; that is the store, not the product.

## regulatory-dh.get_market_status (counted)

- `name` or `reference`. Returns `authorized` per US, EU, UK, CH and a reimbursement field that is `[GAP]` in this release.
- Pitfalls seen (important):
  - It returns **one row per stored record**, and each row says `false` for every jurisdiction that record is not in. For Brainomix 360 e-ASPECTS it returned three rows: two with US true and EU false, one with US false and EU true. Its exhibit shows only the first (EU false).
  - `false` means "no record in the library's copy", never "not authorized". For Natural Cycles it returned six identical rows with EU false, and `search_devices` found no EU record; the library cannot say whether it is on the EU market.
  - It carries no source URL or retrieval date, and no CA or TW column.
- How to use it: merge the rows (any true wins), restate every false as a gap class, and take the record details from `search_devices`. `scripts/market_matrix.py` does this on saved output.

## regulatory-dh.retrieve_guidance (counted)

- Required: `query`. Optional: `limit` 1 to 25, `namespace` (guidance, ontology-navigation).
- It is a lexical match, not a semantic search. Multi-word questions returned nothing ("MDSAP audit report acceptance Health Canada TGA reliance"; "EUDAMED UDI device registration deadline ..."); a single keyword returned passages ("MDSAP": four chunks of MDCG 2020-14, August 2020; "EUDAMED": MDCG 2019-15 rev1, MDCG 2022-12, MDCG 2021-13 rev.1). "812.28" returned nothing.
- Most passages carry `source_url` `[GAP]` and every `retrieved_at` is null. "software" also returned unrelated research papers.
- Rule: use it only to find a document's name, then cite that document only if a row in `references/` sources it, or say `[GAP]`. Never cite a passage without a source URL. MDCG 2019-15 rev1 predates Regulation (EU) 2024/1860; do not use it for EUDAMED dates.

## analytics.mcda (counted)

- `alternatives` (each with `id` and `scores`, a map of criterion to a 0 to 4 number) and `criteria_weights` (summing to 1).
- Returns a value estimate per alternative and each criterion's contribution (EVIDEM weighted sum). No robustness view: work out swap points by hand (see B1).
- Only ever run on scores and weights the person gave. A test run on 19 October 2026 with test scores is saved in `examples/live/` and is not a recommendation.

## Not used here

- `watch_register`: described only. It is not called by this skill; monitoring belongs to DH-03.03.2.2.
- `verify.verify_text` and `verify.check_claim` on register records: register pages are rated "no provenance" (register item C1). Cite the register record instead.

## verify.build_record (counted)

- Needs a named human in `cleared_by`. Refuses a tool or model name. Use it only when an output leaves the conversation.
