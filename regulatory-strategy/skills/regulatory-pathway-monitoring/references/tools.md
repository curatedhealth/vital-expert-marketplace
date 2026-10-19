# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them. Counted calls draw on the library key's monthly allowance; free calls do not. Jurisdiction codes: US, EU, UK, CH, or all.

Behavior below was observed in live calls on 19 October 2026. Saved outputs: `examples/live/monitoring_calls_2026-10-19.json`.

## regulatory-dh.list_jurisdictions (free)

- What is loaded, per jurisdiction, with counts and last load date. On 19 October 2026: US 1,226 authorizations and 892 safety events (openFDA, enforcement, PMA); EU 3,142 authorizations with the decision date empty on all, and 0 safety events; UK 0 registrations and 10 MHRA alerts (last load 14 October 2026); CH nothing loaded; TW 32; CA 227. Germany's DiGA history feed is closed (token absent).
- Call it first in every monitoring run: it is the denominator for every gap and tells you whether the copy is fresh.

## regulatory-dh.get_register_deltas and regulatory-dh.get_deltas (counted)

- Same tool under two names (the response of `get_deltas` names itself `get_register_deltas`). Call one, not both.
- Required `since` (YYYY-MM-DD) and one scope: `product_code`, `manufacturer` or `emdn_code`; optional `jurisdiction`.
- The change log only exists for a scope with a registered watch. Without one it returns no rows and the gap "no watch is registered for this scope; the change log has not started" (QVO since 1 January 2026; V92 since 1 October 2026). That is a statement about the log, never "no change in the market".
- Watches are created with `regulatory-dh.watch_register`, which this skill describes but does not call; the person decides whether to set one, and their administrator owns watch scoping. Until a watch exists, A1 detects change by comparing a saved earlier snapshot with a fresh read (Step 3 of A1).

## regulatory-dh.watch_register (described only)

- Arguments: one of `product_code`, `manufacturer`, `emdn_code`; optional `jurisdiction`. Returns a snapshot hash; changes appear after the library's next enrichment sweep.
- Not called by this skill. If the person wants future changes, tell them it exists and that the change log starts only once it is set. The Market Access suite's equivalent watch is not separated by customer key (register item N2); whether the regulatory watch is separated was not tested.

## regulatory-dh.get_market_status (counted)

- `name` or `reference`. Authorized true or false per US and EU; UK and CH always `[GAP]` today.
- Pitfalls: the name "Sleepio" missed the stored "Sleepio®" (the reference K233577 worked); "somnio" returned two rows for one product, one EU true and one EU false. Use the reference; quote conflicts.

## regulatory-dh.get_authorization and regulatory-dh.search_devices (counted)

- Use them to take the snapshot for a comparison: status, decision date, class, code, retrieval date.
- EU rows store no decision date and link the EUDAMED search page, not the device page; cite the Basic UDI-DI.

## regulatory-dh.search_safety_events (counted)

- At least one of `manufacturer`, `product`, `product_code` is required; a jurisdiction-only call returns "give manufacturer, product or product_code". Optional `jurisdiction`, `since`, `limit` 1 to 25.
- Returns recalls (US: enforcement records whose product text mentions software terms), MAUDE report counts per product code per year, and MHRA alerts.
- Pitfalls:
  - A `product_code` search returned recalls for products in another code from the same manufacturer (QVO returned two reSET recalls of 7 June 2021; reSET's authorization is in code PWE). Check every row's product.
  - MAUDE counts are per product code, not per product: a search for the product "Somryst" and a search for the manufacturer "Big Health" both returned the QVO count (1 report, 2023), which cannot be attributed to either.
  - Recall `source_url` is the openFDA endpoint, not the recall record, and no recall number is stored. Cite the event date, firm and title, and point to FDA's recall database for the record.
  - `severity` "Class II" is the recall classification, not the device class.
- Swissmedic actions are not loaded; EU vigilance is not available.

## regulatory-dh.compare_authorizations (counted)

- `safety_event_count` reads "not assessable" for K191716 and K233577 and 2 for DEN160018. "Not assessable" is not zero.

## regulatory-dh.generate_report (counted)

- With `product_code` it chose one device without saying why and returned `safety_events: []` for the code. Use it only for one named device; for monitoring use the individual tools.

## verify.build_record (counted)

- Needs a named human in `cleared_by`. Use it only when an output leaves the conversation.

## Not used here

- `verify.check_claim` on register facts: register pages are rated "no provenance" (register item C1).
- The person's own submission dates, hold days, complaint data and vigilance cases never go into a library call.
