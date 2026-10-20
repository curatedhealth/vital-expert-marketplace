# Output format: integration review and miss owners

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/integration_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 60, rules 50, failures 150, limits 50, decisions 60, record 50.

1. **Answer** (two sentences): counts of units met, failed and not measurable against your rules; failures by name; how many have an owner and a release or a named acceptance; the flag that most limits the review. No overall verdict.
2. **Your rules:** one line per rule type, verbatim; units without a rule listed.
3. **Failures:** Unit · Failure · System to change (yours) · Owner (yours, or owner not named) · Release, or accepted by (yours, or "not given").
4. **Blocking:** the map error class and the workflow step you named as blocking, with the change and owner (yours, or "not named").
5. **For you to decide:** open assignments, unnamed acceptances, recheck dates not given, whether a profile that failed every sample holds go-live.
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Integration review draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Your rules (verbatim, numbered)
### Nonconformance assignments
| Failure class | Profile | System to change | Owner | Release or patch | Accepted by and reason |
|---|---|---|---|---|---|
### Failed cells
| Cell | Scope requested | HTTP status or OperationOutcome | App or EHR configuration | Owner | Status |
|---|---|---|---|---|---|
### Map error classes by version and the blocking class
### The step that must change before the next release (change and owner)
### Not measurable (no rule, no data)
### For you to decide
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Integration review draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
