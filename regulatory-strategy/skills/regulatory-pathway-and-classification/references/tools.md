# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them (for example `regulatory-dh_search_devices`). Counted calls draw on the library key's monthly allowance; free calls do not. Jurisdiction codes: US, EU, UK, CH, or all.

Behavior below was observed in live calls on 19 October 2026. Saved outputs: `examples/live/insomnia_cbt_calls_2026-10-19.json`.

## What the library holds (regulatory-dh.list_jurisdictions, free)

- US: 1,226 authorizations (FDA 510(k), De Novo, PMA for the digital health product-code perimeter), dated; last load 19 October 2026.
- EU: 3,142 EUDAMED devices carrying a medical device software EMDN code. The decision date is empty on all 3,142, so no EU timing can be read from the library.
- UK: no device registrations (MHRA PARD has no API) `[GAP]`; MHRA safety alerts only.
- CH: nothing loaded (swissdamed is web-only) `[GAP]`.
- Also TW (32) and CA (227; `is_software` is null, so a software-only search excludes them). Japan, China, Australia, Korea, Brazil, Singapore and others are closed, each with a stated reason.

Call it first when the person names a jurisdiction, so a gap is worded correctly.

## regulatory-dh.classify_product (counted)

- Arguments: `name` plus `intended_purpose`, or `reference` (K, DEN or P number, Basic UDI-DI).
- With a reference: returns the FDA product code, its label and regulation number, labeled "from record" (K191716 returned QVO, "Computerized Behavioral Therapy Device For Insomnia", 882.5801).
- With a description only: returns no classification ("FDA product code, EMDN and GMDN are not inferred from the text") and up to three VITAL taxonomy segments with a similarity score (0.276 for "Digital Therapeutic (DTx)" on a CBT-I description). These are text matches to VITAL's own taxonomy, not a regulatory class.
- How to use it in A1: it is an input, not a decision. Use it to confirm the stored class of a named comparable or of the person's own cleared device. Never present a taxonomy match as a class.
- GMDN is not stored.

## regulatory-dh.search_devices (counted)

- Required `query` (product or manufacturer, 3+ characters). Optional `jurisdiction`, `limit` 1 to 25, `software_only` ("true" default).
- Returns per device: manufacturer, jurisdiction, pathway, `risk_class`, status, `decision_date`, `submission_date`, `product_code` (FDA code or EMDN), `regulation_number`, `predicate_references`, source URL, retrieval date.
- It is a name search, not a search by indication or intended use. To find comparables for a new product, search known competitor or manufacturer names, then widen through the product code with `find_predicates` and `get_pathway_precedents`.
- EU rows carry the EUDAMED search page as `source_url`, not the device page; cite the Basic UDI-DI with it.

## regulatory-dh.get_authorization (counted)

- Required `reference`: K, DEN or P number, Basic UDI-DI, or SRN plus trade name.
- Returns all stored fields. Pitfall: `status` is FDA's raw decision code for some rows ("DENG" for a granted De Novo, DEN160018); quote it and say what the source calls it, without translating beyond the record.

## regulatory-dh.find_predicates (counted)

- `reference` (K or DEN number): the predicate chain as named in FDA 510(k) summaries, up to five levels, each node with decision date, summary PDF URL and `predicate_basis`. K191716 named DEN160018; a De Novo node says it names no predicate.
- `product_code` instead: recent decisions in that code with their stated predicates (QVO returned K233577 and K191716).
- Predicates come from the summary PDFs; openFDA has no predicate field. A node whose summary was not read is `[GAP]`.
- Pitfall: a chain can cross product codes (K191716 in QVO names DEN160018 in PWE). Report each node's own code.
- Pitfall: a chain can end at a node the library does not hold. On 19 October 2026 the QRX chain from `find_predicates(product_code="QRX")` stopped at K201476 with no record, and `get_authorization("DEN170043")` returned "no stored authorization"; FDA's AI-enabled device list holds that De Novo (row `06/12/2018,DEN170043,DreaMed Advisor Pro,"DreaMed Diabetes, Ltd.",Clinical Chemistry,QCC`, research_reg2/raw/ailist.csv line 1506, columns: Date of Final Decision, Submission Number, Device, Company, Panel (Lead), Primary Product Code). Saved in `examples/live/predicate_chain_qrx_2026-10-19.json`. Say the chain is truncated, mark the founding De Novo `[GAP]` unless a row holds it, and point the owner to FDA's De Novo database (RP US-66). Do not state which De Novo founded a regulation unless a row says so.

## regulatory-dh.get_pathway_precedents (counted)

- `product_code` (FDA) or `emdn_code` (EU), optional `jurisdiction`.
- Returns decision counts by pathway and year, De Novo grants, and calendar days from submission to decision where both dates are stored (QVO: 2 decisions, both 510(k), 271 and 272 days; PWE: one De Novo and one 510(k), 374 and 486 days).
- These are calendar days including time with the sponsor. They are not FDA days and cannot be compared with MDUFA goals; compare them with the average total days in `pathway-facts.md` instead, and say n.
- Pitfall: counts are per code, so a code's founding De Novo can sit under a different code (QVO shows no De Novo; its chain starts at DEN160018 in PWE).
- EU: V92 returned 1,256 CE_MARK decisions, every one "date not stored", and time to decision `[GAP]`. An EMDN code is broad; the count is not a set of comparables.

## regulatory-dh.compare_authorizations (counted)

- `references` 2 to 12, optional `jurisdiction`. Table of class, pathway, decision date, predicate, safety-event count.
- Pitfall: `safety_event_count` reads "not assessable" for K191716 and K233577 and 2 for DEN160018. "Not assessable" is not zero; check `search_safety_events` and the pathway monitoring skill before saying anything about safety.

## regulatory-dh.get_market_status (counted)

- `name` or `reference`. Where a product is authorized (US, EU, UK, CH); UK and CH are always `[GAP]` today.
- Pitfalls: a name search can miss a stored product with a trademark sign ("Sleepio" returned nothing; reference K233577 returned "Sleepio®"). Prefer the reference. A name can return two rows for one product from different joins ("somnio" returned one row with EU true and one with EU false, the second carrying the DiGA manufacturer string); quote both and check EUDAMED.
- Reimbursement fields come from the Market Access suite and are out of scope here.

## regulatory-dh.retrieve_guidance (counted)

- Returned no passage for a Rule 11 question. The rules in this skill come from `references/`, not from this tool. Call it only to check whether a passage has since been loaded, and cite its URL and date if one comes back.

## regulatory-dh.generate_report (counted)

- `reference` or `product_code`, `template` (memo, identity, regulatory, precedents, safety).
- With a product code it picked one device (Sleepio®) without saying why. Use the individual tools in A2 instead; use the report only for one named device.

## analytics.mcda (counted)

- `alternatives` (each `id` and `scores`, a map of criterion to a 0 to 4 number) and `criteria_weights` (sum to 1).
- Returns a value estimate (weighted sum scaled to 100) and each criterion's contribution; method "EVIDEM Multi-Criteria Decision Analysis (weighted-sum, 0-4 scale)" with its citations.
- No robustness view and no tie flag: two options returned 57.5 each in the test. `scripts/mcda_swap_points.py` recomputes the values and gives the swap weights.
- Only the person's scores go in. The test scores in the saved output were entered by the build agent to measure the tool and are not anyone's judgment.

## verify.build_record (counted)

- Needs a named human in `cleared_by`. Use it only when an output leaves the conversation.

## Not used here

- `regulatory-dh.watch_register`: monitoring belongs to the pathway monitoring skill; it is only described there.
- `verify.check_claim` on register facts: Verify rates register pages "no provenance" (register item C1). Cite the register page and retrieval date instead.
