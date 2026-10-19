# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them (for example `regulatory-dh_get_market_status`). Counted calls draw on the library key's monthly allowance; free calls do not.

Behavior below was observed in live calls on 19 October 2026. Saved outputs are in `examples/live/`.

## regulatory-dh.list_jurisdictions (free)

- No arguments. Returns per jurisdiction: stored authorizations, safety events, last load date, sources; plus a `closed` list.
- Observed: US 1,226 authorizations (last load 19 October 2026); EU 3,142 (no decision dates); UK 0 authorizations (MHRA alerts only); CH 0; TW 32; CA 227 (not searchable by product). Closed: JP, AU, BR, SG, CN, KR and others.
- Call it first in every monitoring run: it says which regions the library can monitor at all and how fresh each copy is.

## regulatory-dh.get_market_status (counted)

- `name` or `reference`. Returns `authorized` per US, EU, UK, CH; reimbursement `[GAP]` in this release.
- Pitfalls seen: one row per stored record, each saying `false` for jurisdictions that record is not in (Brainomix 360 e-ASPECTS: two rows US true / EU false, one row US false / EU true; the exhibit shows EU false). No source URL, no retrieval date, no CA or TW column.
- How to use it: merge rows (any true wins); restate `false` as "no record in the library's copy"; take identifiers, classes and dates from `search_devices`.

## regulatory-dh.search_devices (counted)

- Required: `query`. Optional: `jurisdiction` (US, EU, UK, CH, all), `limit` 1 to 25, `software_only`.
- Use `limit` 25: results are capped and US records come first. EU records carry no decision date and a generic EUDAMED search URL; cite the Basic UDI-DI. A product may show MDD-era and MDR records with different classes; report each by identifier.

## regulatory-dh.get_register_deltas and get_deltas (counted)

- Required: `since` (YYYY-MM-DD). Scope: one of `product_code` (FDA), `manufacturer`, `emdn_code`; optional `jurisdiction`. `get_deltas` is the same tool under a shared name.
- Observed: every call returned no rows with "no watch is registered for this scope; the change log has not started" (manufacturer Brainomix since 1 January 2026; product code QAS since 1 July 2026; EMDN Z11030592 since 1 September 2026). The same day, `search_devices` showed US decisions inside those windows (Brainomix K260406, 12 June 2026). The log records only what a watch has seen since it was registered.
- Rule: an empty log is "no change recorded; the log has not started for this scope", never "nothing changed". To see change without a watch, compare two of your own dated `search_devices` runs, or filter US records by `decision_date` (EU records have none).
- The log covers register events (authorizations, safety events, status), not guidance or law. Guidance and law changes come from `references/change-sources.md`.

## regulatory-dh.retrieve_guidance (counted)

- Required: `query`. Lexical match on stored chunks, not a semantic search.
- Observed: multi-word questions returned nothing; single keywords returned passages ("MDSAP": MDCG 2020-14, August 2020; "EUDAMED": MDCG 2019-15 rev1, MDCG 2022-12, MDCG 2021-13 rev.1). Most passages have `source_url` `[GAP]`; every `retrieved_at` is null; "software" returned unrelated research papers.
- It does not say whether a document is current, draft or superseded. MDCG 2019-15 rev1 predates Regulation (EU) 2024/1860 and describes EUDAMED registration in the future tense.
- Rule: use it only to find a document name; check status and date in `change-sources.md` or on the regulator's page; never cite a passage without a source URL.

## Not called

- `watch_register`: described only, not called by this skill. If the person wants future register changes logged, tell them a watch starts the log from the day it is registered and that the change log is empty before that; registering one is the person's choice in their own connector setup.

## verify.build_record (counted)

- Needs a named human in `cleared_by`. Use it only when an output leaves the conversation.
