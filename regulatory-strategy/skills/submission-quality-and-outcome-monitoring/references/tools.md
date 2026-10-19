# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them. `list_jurisdictions` is free; the others are counted. Behavior observed in live calls on 19 October 2026; trimmed outputs in `examples/live/`.

## regulatory-dh.list_jurisdictions (free)

- US 1,226 authorizations (FDA 510(k), De Novo and PMA decisions in the digital health product-code perimeter; last load 19 October 2026). EU 3,142 EUDAMED software devices with the decision date empty on all 3,142. UK: no authorizations (MHRA PARD not loaded), 10 safety alerts. CH: nothing loaded. JP, CN, AU, KR and others closed.
- Call it once to say what the library can show. EU time to certificate cannot come from the library.

## regulatory-dh.get_pathway_precedents (counted)

- `product_code` (FDA) or `emdn_code` (EU); `jurisdiction` US, EU, UK, CH or all.
- Returns decision counts by pathway and year, De Novo grants, and `time_to_decision`: median, minimum and maximum calendar days between stored `submission_date` and `decision_date`.
- Measured: QFT 4 decisions (1 De Novo, 3 510(k)), median 205, min 60, max 228 days. QVO 2 510(k)s, median 271. PWE 1 De Novo and 1 510(k), median 430 (374 and 486). EMDN Z12019092 (EU): 2 CE_MARK rows, "date not stored", time to decision `[GAP]`.
- Pitfalls: the median mixes pathways in one code; it is calendar days, not FDA days; with two to four decisions it is not a distribution. Split per record with `get_authorization` and `scripts/review_clock.py comparables`.

## regulatory-dh.get_authorization (counted)

- Required `reference`: K, DEN or P number, Basic UDI-DI, or "<SRN> <trade name>".
- Returns every stored field with source URL and retrieval date: pathway, class, `status`, `submission_date`, `decision_date`, product code, regulation number, predicates.
- Measured: K233577 (Sleepio, 510(k), received 7 November 2023, decided 5 August 2024, predicate K191716); DEN160018 (reSet, De Novo, 16 May 2016 to 14 September 2017); DEN200026 (EndeavorRx, De Novo, 16 April 2020 to 15 June 2020).
- Pitfalls: De Novo `status` is the raw code "DENG" (granted), not plain words. The dates are the ones FDA's record states; the record does not link earlier submissions for the same device, so a short span (60 days for DEN200026) is not the device's whole regulatory history. Describe only what the record states.

## regulatory-dh.search_devices (counted)

- Required `query` (product or manufacturer, 3+ characters); `jurisdiction`; `limit`. Measured: "Somryst" in US returned K191716 with product code QVO, predicate DEN160018, dates and source.
- Use it to find the reference for a comparable the person names.

## regulatory-dh.find_predicates (counted)

- `reference` or `product_code`. With QVO it listed the recent decisions in the code with stated predicates (K233577 names K191716; K191716 names DEN160018). Use it to list comparables in a product code the person names; never to choose a predicate.

## regulatory-dh.generate_report (counted)

- Measured with `reference=K191716, template=regulatory`: identity, pathway, predicate chain, prior decisions in the code, gaps.
- Pitfall: `market_status.authorized.EU` was `false` though the EUDAMED copy holds no decision dates. Say "not found in the library's EUDAMED copy".

## verify.build_record (counted)

- Needs a named human in `cleared_by`. Only when an output leaves the conversation.

## Not used here

- `verify.verify_text` and `verify.check_claim` on register facts: register pages rate "no provenance" (register C1). Cite register facts to the register page.
- `check_claim` for literature is used only in the sibling skill, and only with a results passage (register N3).
- `retrieve_guidance`: on 19 October 2026 it returned no device-submission passages for eSTAR, the software guidance, Annex II or clinical evaluation (see the sibling skill's tools file); the completeness check uses `content-maps.md`.
- Watch tools: described only. A person who wants to follow a product code can re-run `get_pathway_precedents` and compare with the saved output.
- The person's own dossier text and agency letters never go into a library call.
