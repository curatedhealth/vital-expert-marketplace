# Output format: stage gate record

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with a tool (the answer without the calls list, piped to `wc -w`), not by estimate. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, the "Full version on request" line. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** of the person's N criteria, how many are present, missing and not measurable; the decision as the person stated it, with date and decider; the missing item that blocks most.
2. **Criteria:** table # · Criterion (person's words) · Present, missing or not measurable · Work product reference or fact · Rows (DOI beside any TM or PL110 to PL120 row in the same cell).
3. **Decision as stated:** decision, date, decider, attendees, all in the person's words; if go with a missing item, both facts side by side and the person's stated reason.
4. **Open items:** item · owner (named, or "owner not named") · blocks · reread date (or "reread date not set").
5. **Gaps and stops.**
6. **Record (last line of the answer body):** "Gate record draft for OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
7. **Calls made (after the record line):** list (usually none).

## Full mode

### Answer
### Criteria as confirmed by the person
### Check
| # | Criterion | Result | Work product and version | Fact | Rows |
|---|---|---|---|---|---|
### Decision, date, decider and attendees (as stated)
### Open items, owners, blocks and reread dates
### Proposed criteria (only if asked; not applied)
### Gaps
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
### Calls made (after the record line)
