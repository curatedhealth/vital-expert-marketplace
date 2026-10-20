# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them. Counted calls draw on the library key's monthly allowance; free calls do not. Scheme codes: DE_DIGA, FR_PECAN, FR_LPPR, FR_LATM, BE_MHEALTH, UK_NICE_EVA, UK_NICE_HTG, UK_NICE_NHAP, US_CMS_RPM, US_CMS_DMHT, AU_MSAC, CH_BAG, ES_REDETS, FI_DIGIHTA, IE_HSE_CGM, SE_TLV.

Behavior below was observed in live calls on 19 October 2026.

## market-access-dh.list_schemes (free)

- No arguments. Returns per scheme: authority, pathway kind, clock rule, listing count, last load date, posture.
- Use it first: it says which markets the library can monitor at all, and how fresh each copy is.

## market-access-dh.get_reimbursement_status (counted)

- Required: `reference` (name or identifier), `scheme`.
- Returns the current status with `listed_on`, `ends_on`, price, source and retrieval date, plus `durability_days_in_current_status` and `days_to_stated_end`.
- Pitfall: `durability_days_in_current_status` counts from the stored `changed_on`. For DiGA loaded at the first snapshot, `changed_on` is the listing date, so for a DiGA that moved from trial to permanent it overstates how long it has been permanent. Do not quote it as "permanent since".

## market-access-dh.get_status_history (counted)

- Required: `reference`. Optional: `scheme`.
- Returns ordered changes (`status`, `status_raw`, `changed_on`, `note`, `source_url`).
- What it can show today: for **deleted** DiGA, two rows (the last status before deletion with its listing date, then the deletion date). For **listed** DiGA, one row only: the current status dated at the listing date, with the note "transition history not published in loaded sources". The date a trial DiGA became permanent is therefore not in the library. Say `[GAP]` for it.
- Comparing two of your own runs over time is the reliable way to see a change; keep the earlier output.

## market-access-dh.search_listings (counted)

- Required: `query` (2+ characters: product, manufacturer, identifier). Optional: `country`, `scheme`, `status` (provisional, permanent, conditional, delisted, withdrawn, covered, unknown), `limit` 1 to 25.
- The status filter needs a real query; you cannot list "all provisional DiGA" with it. To list a scheme's rows, use `find_scheme_precedents`.
- Search in the register's language or by ICD code for DiGA ("Insomnie", "F51"). The United Kingdom is `UK`.

## market-access-dh.find_scheme_precedents (counted)

- Required: `scheme`. Optional: `indication`, `product_category`, `limit` 1 to 25 (most recent listings first).
- Use it for cohort views (all recent trial listings, deletions in an indication) and for comparables: how similar products progressed.
- Deleted DiGA rows carry the listing and deletion dates inside `evidence_passage` ("Aufgenommen am … Gestrichen am …"); `scripts/coverage_clocks.py` reads them.
- Pitfalls seen: `ends_on` is empty for trial listings; `manufacturer_country` can say DE for manufacturers the same row names as Swiss or Italian; one row's status says permanent while its stored passage says provisional. Quote the passage and say "check the register" where they disagree.

## market-access-dh.get_market_matrix (counted)

- `name` or `reference`. Every scheme with listed or not, status and dates. Use it for a multi-market snapshot; classify gaps with `gap-rules.md`.

## market-access-dh.watch_scheme (counted)

- Optional `scheme`, `product`. Registers a watch and returns a snapshot hash and timestamp.
- Changes appear only after the library's next refresh, not instantly. Watches are not yet separated by customer key (the tool says so); do not put confidential product names in a watch until that is fixed.
- Call it only when the person asks to be told about future changes. Record the hash in the output so the next run can compare.

## Not used here

- `verify.verify_text` and `verify.check_claim` on register facts: they rate register pages "no provenance", so register facts come back unverifiable. Register facts are cited to the register page instead.
- The buyer's own uptake data never goes into a library call.

## verify.build_record (counted)

- Needs a named human in `cleared_by`. Use it only when an output leaves the conversation.
