# Output format: V&V completeness and compliance read

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/delivery_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 70, trace 140, build under test 60, plans 60, limits 40, record 50.

1. **Answer** (two or three sentences): candidate build and read date; hazards with no case, hazards with only unit-level cases, cases on another build, failed or unrun cases, plans missing or naming another product. No "complete" verdict unless your own rule defines it.
2. **Trace gaps:** Hazard · Cases · Flag in words · Source (row).
3. **Cases not on the candidate build:** Case · Build · Waiver (yours) · repeat or waive is yours.
4. **Plans:** missing, draft, template or naming another product.
5. **Limits:** class definitions not in the sources; the script reads records, not documents.
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "V&V completeness read draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Header (product, candidate build, read date, your rule verbatim)
### Trace from hazard to case
| Hazard | Item | Class (yours) | Cases | Levels | Flags |
|---|---|---|---|---|---|
### Case records
| Case | Hazards | Spec | Expected | Build | Result | Waiver | Flags |
|---|---|---|---|---|---|---|---|
### Class versus hazard (facts for you; nothing reclassified)
### Plan completeness
| Plan | Document | Version | Status | Product named | Flags |
|---|---|---|---|---|---|
### Rules behind the read (source name and date, row)
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
V&V completeness read draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
