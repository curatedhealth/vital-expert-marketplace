# Output format: conformance gaps and go-live scope

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/fhir_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 70, gaps 140, hold 60, adoption 40, decisions 60, record 50.

1. **Answer** (two sentences): checks run and misses by profile; how many you flagged as blocking go-live; unmatched codes held; the item that most limits the record. No ready, certified or compliant verdict.
2. **Gap record:** Payload · Resource · Element path · Result · Blocks go-live (yours, or "not given").
3. **Not checked:** resource types with no sheet entry.
4. **Hold list:** count by source system; steward and promotion rule (yours, or "steward not named").
5. **Adoption definition:** who, which action, which period (yours, or "not given").
6. **For you to decide:** each open blocking flag, each acceptance with the person who accepted it, go-live scope.
7. **Calls made**, then one line offering the full version.
8. **Record (the very last line, nothing after it):** "Gap record draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Guide, version and check sheet (as you gave them)
### Gap record
| Payload | Resource | Element path | Sheet rule | Result | Blocks go-live (yours) | Accepted by (yours) |
|---|---|---|---|---|---|---|
### Not checked (no sheet entry)
### Unmatched code hold
| Source system | Count | In production map? | Steward (yours) | Promotion rule (yours) |
|---|---|---|---|---|
### Adoption definition (yours)
### Gaps
### For you to decide
### Calls made
### One line offering anything not shown
### Record (the very last line)
Gap record draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
