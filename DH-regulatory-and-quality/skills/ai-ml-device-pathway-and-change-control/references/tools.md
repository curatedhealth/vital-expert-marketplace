# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`), Regulatory suite. Names are the library's (`regulatory-dh.search_devices`); your assistant may prefix them. All behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`. Counted calls draw on the library key's monthly allowance; `list_jurisdictions` is free.

## regulatory-dh.list_jurisdictions (free)

- Arguments: none.
- Returned on 19 October 2026: US 1,226 authorizations, 892 safety events, loaded 19 October 2026 (openFDA); EU 3,142 authorizations from EUDAMED software codes, decision date empty on all 3,142; UK 0 authorizations (MHRA PARD not loaded), 10 safety alerts; CH nothing loaded; TW 32; CA 227 (is_software null on all, so a software-only search excludes them). JP, CN, AU, KR and others closed with a reason.
- Use it first. It is the denominator for every gap: an EU device with no decision date, or a UK device with no row, says nothing about the market.

## regulatory-dh.search_devices (counted)

- Required: `query` (product or manufacturer name, 3+ characters). Optional: `jurisdiction` (US, EU, UK, CH, all), `limit` 1 to 25, `software_only` ("true" default).
- Returns per row: `product`, `manufacturer`, `jurisdiction`, `pathway` (FDA_510K, FDA_DE_NOVO, FDA_PMA, CE_MARK), `risk_class`, `status`, `decision_date`, `submission_date`, `product_code`, `regulation_number`, `predicate_references`, `source_url`, `retrieved_at`, `identifiers`.
- Observed: "Aidoc" returned ten US 510(k) rows (QAS, QFM, QIH codes), newest decision 14 May 2026. "Brainomix" returned five US rows and no EU row. "Briefcase" with `jurisdiction` EU returned two EUDAMED rows, class IIa, "On the EU market".
- Pitfalls:
  - It is a name search. "stroke" in the EU matched product names ("Stroke VCAR", "ABC Stroke Risk Score Calculator"), not intended uses.
  - No field says whether a device uses AI, carries a PCCP, or is on FDA's AI-enabled device list. Never infer AI or PCCP status from a row. Check the FDA list or the decision summary.
  - EU rows have no decision date and their `source_url` is EUDAMED's generic search screen, not the device page. Quote the Basic UDI-DI so the person can find it.
  - The same product appears under different spellings and manufacturer strings across jurisdictions ("BriefCase-Triage" and "Aidoc Medical , Ltd." in the US; "Briefcase-Triage" and "Aidoc Medical Ltd." in the EU). Match on identifiers, not names.

## regulatory-dh.get_authorization (counted)

- Required: `reference` (K, DEN or P number; Basic UDI-DI; or "SRN trade name").
- Observed for K261317: the same fields as `search_devices`, nothing more. No intended use text, no summary text, no PCCP field.

## regulatory-dh.find_predicates (counted)

- Arguments: `reference` (K or DEN number) or `product_code`.
- Observed for K261317: a chain five levels deep to DEN170073 (ContaCT, Viz.Al, Inc., granted 13 February 2018), each node with decision date, source URL and `summary_url` (the FDA summary PDF), `predicate_basis` "named in the FDA 510(k) summary".
- Pitfall: the `depth` field is by first discovery, so a device reached by two paths shows one depth. Read the edges, not the depth, when the chain branches.

## regulatory-dh.get_pathway_precedents (counted)

- Arguments: `product_code` or `emdn_code`; optional `jurisdiction`.
- Observed for QAS (US): 88 decisions (87 510(k), 1 De Novo), by year 2018 to 2026, median 104 calendar days from submission to decision (min 18, max 449, n 88), one De Novo grant (DEN170073), last decision 16 September 2026.
- Pitfalls: the days are between the stored submission and decision dates, in calendar days; they are not MDUFA "FDA days" and not total project time. A product code's count is not an AI count: the code is a device type.

## regulatory-dh.get_market_status (counted)

- Arguments: `name` or `reference`.
- Observed for "BriefCase-Triage": ten rows; nine identical US rows (one per 510(k)) each saying US true, EU false, and one EU row ("Briefcase-Triage", "Aidoc Medical Ltd.") saying US false, EU true. UK and CH always `[GAP]`.
- Pitfall: rows are not merged across jurisdictions, so each row contradicts the other. Do not quote a "false". Read each jurisdiction from the row that holds it, and say the matrix does not link them.

## regulatory-dh.classify_product (counted)

- Arguments: `name`, `intended_purpose`, or `reference`.
- Observed for a new stroke CT triage description: no stored record; "FDA product code, EMDN and GMDN are not inferred from the text"; two VITAL taxonomy matches at similarity 0.23 and 0.208. The live segment label contains a dash; the saved copy shows it with a colon.
- Use it only for a product already on file. For a new product, it confirms there is nothing to read; the class arguments come from `ai-ml-routes.md`.

## regulatory-dh.generate_report (counted)

- Arguments: `reference` or `product_code`; `template` memo, identity, regulatory, precedents, safety.
- Observed for K261317 with template "regulatory": identity, authorization, predicate chain, product-code precedents, all with sources. Its `market_status` block was taken from the EU row and reads "US: false" for the US device it describes. Do not pass that block through; restate market status from `search_devices` rows.

## regulatory-dh.retrieve_guidance (counted)

- Required: `query`. Optional: `namespace`, `limit`.
- Observed: "predetermined change control plan artificial intelligence" and "AI Act high-risk medical device" returned nothing. "PCCP" returned five passages that read as Health Canada guidance (they say "medical device licence amendment application"), each with `source_url` `[GAP]` and no retrieval date.
- Rule: a passage without a source URL cannot support a claim. Do not quote these passages. Use `references/` instead, and call this tool at most once per run.

## verify.qualify_source and verify.build_record (counted)

- `verify.qualify_source` with the FDA PCCP guidance URL (`https://www.fda.gov/media/166704/download`) returned tier "inadmissible", "no provenance", although it names FDA as publisher. Regulator guidance therefore cannot be checked through Verify today; do not spend calls on `check_claim` for rules from FDA, EU or MHRA texts. The rows in `references/` carry their own URL, quote and read date.
- `verify.build_record` needs a named human in `cleared_by`; it refuses a model or tool name.

## Not called

`watch_register` (out of scope for this skill), `get_register_deltas` and `get_deltas` (used by the readiness monitoring skill), `compare_authorizations`, `get_market_status` beyond the test above.
