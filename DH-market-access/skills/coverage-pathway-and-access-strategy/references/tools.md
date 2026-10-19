# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them. Counted calls draw on the monthly allowance of the library key; free calls do not. Schemes accepted everywhere a `scheme` argument appears: DE_DIGA, FR_PECAN, FR_LPPR, FR_LATM, BE_MHEALTH, UK_NICE_EVA, UK_NICE_HTG, UK_NICE_NHAP, US_CMS_RPM, US_CMS_DMHT, AU_MSAC, CH_BAG, ES_REDETS, FI_DIGIHTA, IE_HSE_CGM, SE_TLV.

## market-access-dh.list_schemes (free)

- Arguments: none.
- Returns per scheme: `code`, `country`, `authority`, `pathway_kind`, `clock_rule`, `source_url`, `notes`, `listing_count`, `last_load`, `posture`, `posture_reason`.
- Use it first. It is the denominator for every gap.

## market-access-dh.search_listings (counted)

- Required: `query` (product, manufacturer, scheme id or decision reference, 2+ characters).
- Optional: `country` (ISO code), `scheme`, `status` (provisional, permanent, conditional, delisted, withdrawn, covered, unknown), `limit` 1 to 25.
- Returns per row: `product`, `manufacturer`, `scheme`, `status`, `status_raw`, `scheme_identifier`, `decision_reference`, `listed_on`, `ends_on`, `price`, `currency`, `indications`, `source_url`, `retrieved_at`, `source_license`, `evidence_passage`.
- Pitfall: a name match is not identity. Confirm manufacturer and identifier.

- Language: indications are stored in the register's own language. For DE_DIGA search in German or by ICD-10-GM code ("Insomnie", "F51"); an English term ("insomnia") can return nothing. Try the ICD code first for any scheme that stores one.
- Known quirks (library as of 19 October 2026): a scheme code as `query` (for example "US_CMS_RPM") returns nothing, so list a scheme with `find_scheme_precedents` instead; the United Kingdom's `country` code is `UK` (the tool's own description says GB, which returns nothing); some code rows (CMS 99457, 99458) leave `price` empty while the amount sits in `evidence_passage`, so quote the passage and say so.

## market-access-dh.find_scheme_precedents (counted)

- Required: `scheme`. Optional: `indication` (text matched against stored indications), `product_category`, `limit` 1 to 25.
- Returns prior listings on that scheme. Use it to list a scheme's rows and to find comparable paid products.

## market-access-dh.get_market_matrix (counted)

- Arguments: `name` (product name) or `reference` (scheme identifier, decision reference, product identifier).
- Returns every scheme with listed or not, status, dates, identifiers, source URL. Unlisted schemes are `[GAP]`, never denied.

## market-access-dh.get_reimbursement_status (counted)

- Required: `reference` (product name, DiGA-ID, mHealth id, NICE guidance id or CMS code) and `scheme`.
- Returns the current status derived from stored history, with durability days and days to a stated end date when the source states one.

## market-access-dh.get_status_history (counted)

- Required: `reference`. Optional: `scheme`.
- Returns ordered changes with `status_raw`, `changed_on`, `note`, `source_url`.
- Pitfall: history may start at the library's first snapshot ("day zero"). Earlier transitions are `[GAP]`.

## market-access-dh.retrieve_guidance (counted)

- Required: `query`. Optional: `namespace` (`guidance` default, or `ontology-navigation`), `limit` 1 to 25.
- Returns passages with `source_url` and `retrieved_at`, or `[GAP]` when none is stored.
- Pitfall: matching is lexical. Passages without a source URL cannot support a claim. Passages are never status.

## market-access-dh.generate_report (counted)

- Required: `reference`. Optional: `template` (`memo` default, `identity`, `status`, `history`, `matrix`), `format` (`markdown` default, `json`).
- Returns a cite-bound brief and its markdown. Missing fields are the literal `[GAP]`.
- Pitfall: its gap lines do not distinguish an uncovered scheme from a covered scheme without the product. Reclassify with `references/gap-rules.md`.

## verify.verify_text and verify.check_claim (counted): not for register facts

- As of 19 October 2026 the Verify tools rate register pages (for example the BfArM DiGA directory) as inadmissible, "no provenance", so every register fact comes back "unverifiable". Do not spend counted calls on them for this task. Use them for literature or uploaded documents in other tasks.

## Verify on literature: the call sequence that works

Tested 19 October 2026: `verify.qualify_source` with a DOI returns a gold-tier literature source; `verify.check_claim` with the claim, the verbatim passage (text and locator) and that returned source object returns "supported" or another status with a citation. `verify.verify_text` with bare DOIs as `sources` returns "unverifiable" for every claim, so do not use it for literature until that is fixed.

## verify.build_record (counted)

- Required: `clearances` with a named human in `cleared_by`. Optional: `text`, `claims`, `findings`, `sources`.
- Refuses a model or tool name as the clearer.

