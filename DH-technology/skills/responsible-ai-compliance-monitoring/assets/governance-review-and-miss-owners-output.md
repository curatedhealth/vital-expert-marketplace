# Output format: governance review and miss owners

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/evidence_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 60, rule 30, failed items 170, duties 50, decisions 50, record 45.

1. **Answer** (two sentences): whether your rule is met; the failed items by name; how many have an owner, a release-waits call and a present-by date; the count of items that would have to become present (computed). No release call.
2. **Your rule:** verbatim, with the date written. None: "pass rule not given [GAP]".
3. **Failed items:** Item · Why · Owner (yours, or owner not named) · Release waits (yours, or not given) · Present by (yours, or not given; earlier than the read date stated as a fact).
4. **Duties beside the decision** (for your legal owner): one line each, with source and row.
5. **For you to decide:** each with its facts; release is yours.
6. **Calls made** (script command), then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Governance review draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Your pass rule (verbatim, date written)
### Results against your rule
| Item | Requirement | Status | Fails your rule | Source and rows |
|---|---|---|---|---|
### Failed items, owners, release waits and dates
| Item | Why | Owner | Release waits | Present by | Duty beside it (for your legal owner) |
|---|---|---|---|---|---|
### Not yet applicable (with dates)
### For you to decide
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Governance review draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
