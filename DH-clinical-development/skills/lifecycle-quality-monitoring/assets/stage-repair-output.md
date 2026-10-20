# Output format: stage repair review against the person's rules

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with a tool (the answer without the calls list, piped to `wc -w`), not by estimate. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, the "Full version on request" line. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** rules met, missed and not measurable (the person's rules, counted); the decision the person needs to make.
2. **Misses:** table Rule (person's words) · Fact and source · Missing item · Owner (named, or "owner not named") · Block (as decided, or "your call") · Reread date (or "not set") · Responding work.
3. **Not measurable:** one line each with what is missing.
4. **Re-check at the reread date:** the rules touching open items.
5. **Record (last line of the answer body):** "Stage repair review draft for OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
6. **Calls made (after the record line):** list.

## Full mode

### Answer
### Rules as confirmed by the person
| # | Rule (person's words) | Owner | Read by |
|---|---|---|---|
### Check
| # | Result | Fact | Source | Rows |
|---|---|---|---|---|
### Misses, owners, blocks, reread dates and responding work
### Proposed rules (only if asked; not applied)
### Gaps
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
### Calls made (after the record line)
