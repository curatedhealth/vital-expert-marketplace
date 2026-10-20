# Output format: record completeness check

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/drift_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build lines 2 and 3 from `scripts/drift_check.py records` output; do not recount by hand. Budget in words: answer 60, rule 50, table 200, open watches 60, record 45.

1. **Answer** (two sentences): counts against your rule (or "pass rule not given"), the production models that fail and on which elements, open fired watches.
2. **Your pass rule:** elements, date written; or the old tasks' elements labeled "proposed", not used to score.
3. **Records (script output):** Model · Version · In production · Flags · Against your rule.
4. **Open fired watches:** model · fired on · action the watch specifies · watch owner on your register; none closed.
5. **Calls made**, then one line offering the full version.
6. **Record (the very last line, nothing after it):** "Record check draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Your pass rule (verbatim, with date)
### Records against your rule (script output)
| Model | Version | In production | Flags | Against your rule |
|---|---|---|---|---|
### Flag meanings and rows
| Flag | Meaning | Rows |
|---|---|---|
| V1 | No intended use or decision named | old DH-01.04.3.1.1; DA-10 |
| V2 | Test set independence none or not given | DA-39 to DA-41 (draft) |
| V3 | No metric named before the run, or named after it | old DH-01.04.3.1.3; DA-13 |
| V4 | No subgroup result | DA-38, DA-43 (draft) |
| P1, P2 | No run id; no approver | old DH-01.04.2.2.1 |
| W1 to W4 | No watch; no threshold; fired with no action; fired with action | old DH-01.04.2.2.2 and .3 |
### Open fired watches
### Populations not validated
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Record check draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
