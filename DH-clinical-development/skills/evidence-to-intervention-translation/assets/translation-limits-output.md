# Output format: translation limits (draft for the person and the owners they name)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** the limits found, how many are "shown not to help", "not studied" and "stated in an indication", and the one decision the person needs to make.
2. **Limits:** table Limit · Kind · Passage that sets it (quoted, locator) · Behavior that stays off (proposed until confirmed) · Who may reopen (the person's words, or owner not named) · Evidence that would reopen it · Rows (each [PAPER] row with its own paper's DOI in the same cell).
3. **Expansion under consideration (if any):** the EtD criteria (TM110 and TM111, DOI 10.1186/s12961-018-0320-2; the equity question is TM111) with facts held or [GAP]; judgment left to the person.
4. **What reopening touches:** one line each, only those triggered (PL59, PL75, PL95, PC-US-23); applicability is for the owner the person names for regulatory status, or owner not named.
5. **Record:** "Translation limits draft. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. This is the last line of the answer body.
6. **Calls made:** list. Follows the record line.

## Full mode

### Answer
### Edges found
| Product element (claim, rule, feature) | Source covers | Product would cover | Kind | Passage | Rows |
|---|---|---|---|---|---|
### Limits
| Limit | Behavior that stays off | Linked rule or claim | Who may reopen | Evidence that would reopen it | Rows |
|---|---|---|---|---|---|
### Evidence-to-decision criteria for the expansion under consideration
| Criterion | Question (TM111) | Facts held | Judgment (the person's) | Rows |
|---|---|---|---|---|
### Precedents (named products, from their records and decision summaries)
### Gaps
### Decisions for the person and the owners they name
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
### Calls made
