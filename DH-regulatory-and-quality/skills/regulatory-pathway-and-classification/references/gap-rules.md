# Gap rules

A gap is information, not an apology. The person needs to know why something is missing, because each reason leads to a different next step.

## Four kinds of result per device or jurisdiction

| Class | When | How to word it | Next step for the person |
|---|---|---|---|
| Found | The library holds a record. | State the stored fields, source page and retrieval date. | None. |
| Field missing | The record exists but a field is empty (decision date on every EU row, predicate where the summary was not read, safety count "not assessable"). | "Authorized in the EU (EUDAMED, retrieved 14 October 2026); the record stores no decision date `[GAP]`." | Check the register page for that field. |
| Loaded, device not found | The jurisdiction is loaded (US, EU, TW, CA) but no record matches. | "Not in the library's copy of the FDA register (1,226 authorizations, loaded 19 October 2026)." | Search the regulator's database directly before concluding; try the reference instead of the name. |
| Not loaded | The jurisdiction has no records in the library (UK registrations, CH, JP, CN, AU and others). | "The library holds no UK device registrations: MHRA PARD has no API." | The library cannot answer; check the regulator. |

## Rules and knowledge

- A rule not in a research row is `[GAP]` with the reason ("CDS criterion 2 text not quoted in the research pass"). Never fill it from memory.
- A rule whose source is superseded is flagged with both dates (CDS guidance of 2022 replaced on 6 and 29 January 2026; MDCG 2025-6 dates replaced by Regulation (EU) 2026/1744).
- A proposal is not law: GB indefinite CE recognition, the GB international reliance scheme and Swiss recognition of FDA approvals are proposals or drafts on 19 October 2026.

## Never

- Never turn absence from the library into "not authorized", "no predicate exists" or "no safety events".
- Never infer a class, pathway, product code or outcome for a device from its name or description. Describe a device only by what its record states.
- Never treat a VITAL taxonomy match from `classify_product` as a regulatory class.
