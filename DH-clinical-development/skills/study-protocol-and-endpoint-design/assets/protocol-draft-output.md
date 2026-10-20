# Output format: protocol draft by SPIRIT 2025 item

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with a tool (the answer without the calls list, piped to `wc -w`), not by estimate. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, the "Full version on request" line. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build lines 1 and 2 with `scripts/spirit_tally.py --filled "..." --not-relevant "..."`, which reads the 53 SP- ids and prints counts that sum to 53 and every open id once by section.

1. **Answer:** items filled or partly filled, stated not relevant, open (counts over the 34 items and their sub-items, which sum to 53), and the open item that blocks the most, with what it blocks. Two sentences.
2. **Status by id:** one line "Filled or partly: ids (what is missing, in two or three words, only where partly)." One line "Not relevant: ids." One line "Open, by section:" as the script prints it, ids only. Every open id appears once, including 1b and 2; do not repeat them elsewhere.
3. **Open items that block, by dependency:** at most five rows, item · what is missing · who supplies it (named, or "owner not named"). Other open items stay in line 2 only.
4. **Digital additions triggered:** one line each, item and row, at most six (for example "Item 13: visit modality fixed in the protocol, CV67"). Where an app collects outcome or safety data, always include item 17: DHT safety monitoring plan (CV62), and item 13: visit records with type, location, date and originator (CV69).
5. **Registration and results duties, one line each:** ICMJE at or before first consent, with a data sharing plan (CV132; SP-6, CV135). If an applicable clinical trial: 21 days, results within one year (CV141, CV145); applicability to the owner the person names for regulatory status, or owner not named (CV142). Diversity action plan (PE-34, PE-36, PE-41). New in 2025 and open: item 11, item 29 (CV116, SPIRIT 2025 DOI 10.1136/bmj-2024-081477); centralized monitoring where visits are remote (CV71).
6. **Gaps and stops:** device status `[GAP]` if not stated, pointing to `dh-regulatory-and-quality` regulatory-pathway-and-classification.
7. **Calls made:** list (often none).
8. **Record:** "Protocol draft for OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Item table
| Item | Topic | Status (filled, not relevant, open) | Content or [GAP] | Came from | Digital addition and rows |
|---|---|---|---|---|---|
### Drafted text
Per filled item, in SPIRIT order, protocol register. Numbers only from the person.
### Open items by dependency
### Stops for the accountable owner
### Gaps
### Calls made
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
