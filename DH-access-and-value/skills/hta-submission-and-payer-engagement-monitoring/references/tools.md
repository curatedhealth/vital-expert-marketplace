# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them. Behavior observed in live calls on 19 October 2026; saved outputs are in `examples/live/`.

## market-access-dh.list_schemes (free)

- No arguments. Use once per run. On 19 October 2026: DE_DIGA 82 (partial, `ends_on` empty on all 82), FR_PECAN 2, FR_LATM 2, FR_LPPR 0, UK_NICE_EVA 15, UK_NICE_HTG 2, UK_NICE_NHAP 0, US_CMS_DMHT 3, US_CMS_RPM 4.
- The tool description still says LATM is empty; it holds 2 rows (register C7).

## market-access-dh.find_scheme_precedents (counted)

- Required `scheme`; optional `indication`, `product_category`, `limit` 1 to 25.
- DE_DIGA: use ICD-10-GM codes or German terms (`F51` gave 3 permanent insomnia DiGA; `F32` gave 7 depression DiGA, 1 provisional). The deleted depression DiGA MindDoc auf Rezept did not appear: deleted rows can carry empty indications (register C9).
- Rows carry status, dates, price and source, but not the study, the claimed effects or struck effects (`DE-24`), and no deletion reason (register C11). Read those on the directory page.
- `manufacturer_country` can be wrong (edupression.com: "SOFY GmbH, Österreich", country DE; proposed item N1).
- FR_PECAN: Continuum+ Connect has `ends_on` 22 September 2025 and still shows "provisional". The PECAN year has ended; the stored status is stale. Flag, never infer the outcome.
- UK_NICE_EVA: 15 rows are guidance documents (manufacturer "National Institute for Health and Care Excellence"), not products; HTE8/HTG675 and HTE9/HTG676 are the same guidance stored twice. Count 13 distinct guidance documents.
- UK_NICE_HTG: HTG778, titled "early-use assessment", is stored as `permanent` / "recommended". Early use is conditional (`UK6`). Report the title and "check the guidance".

## market-access-dh.get_reimbursement_status (counted)

- `reference`, `scheme`. Adds `durability_days_in_current_status` and `days_to_stated_end`.
- For Continuum+ Connect: `days_to_stated_end` -392 and `durability_days_in_current_status` 756 while the status is still provisional. A negative `days_to_stated_end` is a stale-status flag, not a duration.
- History starts at the library's first snapshot for many rows ("day-zero snapshot 2026-10-15"); earlier transitions are `[GAP]` (register C11).

## market-access-dh.search_listings and get_status_history (counted)

- `search_listings` needs `query` of 2+ characters; the `status` filter alone cannot list a scheme by status (register C7). `country` for the United Kingdom is `UK`.
- `get_status_history` as in the coverage monitoring skill: `changed_on` for a listed DiGA is the listing date, not the date of a status change.

## What the library does not hold for this competency

- No BfArM application, refusal or withdrawal records (BfArM does not publish them, `DE32`), and no BfArM aggregate statistics.
- No CNEDiMTS opinions (favorable or unfavorable), no HAS activity-report figures, and no FR_LPPR rows.
- No NICE re-evaluation outcomes, and no product names inside NICE guidance rows.
These come from `references/decision-sources.md` and the person's own documents. Filed as a data proposal in the build notes.

## verify.qualify_source then verify.check_claim (counted), for claims in a draft

- `qualify_source` with `doi` first (10.1155/da/2171041: tier gold, current).
- `check_claim` decides on word overlap. From a passage stating only the study question it returned "supported" for a design claim, an efficacy claim and that claim's negation. Accept "checked" only when the passage is the results or conclusion sentence and you have read that it states the finding in the same direction. The returned citation drops identifiers; build citations from `literature.get_record`.
- Do not send register facts to Verify (register C1); do not use `verify_text` with bare DOIs (register C18).

## verify.build_record (counted)

- Needs a named human in `cleared_by`. Only when an output leaves the conversation.

## Not used here

- `watch_scheme`: watches are not separated by customer key (proposed item N2). Use the coverage monitoring skill only if the person asks for a watch.
