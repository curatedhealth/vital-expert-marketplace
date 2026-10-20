# Output format: data quality review and feature repair

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/dq_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build line 3 from `scripts/dq_check.py review` output. Budget in words: answer 60, limits 40, failed checks 160, order 40, decisions 60, record 50.

1. **Answer** (two sentences): failed checks on which version; how many have an owner, a repair, a new version and a recheck date; the gap that most limits the review. No fit-for-training verdict.
2. **Your limits:** one line per limit type, verbatim, with version and date written; checks without a limit listed.
3. **Failed checks:** Check · Field · Failing · Owner (yours, or owner not named) · Repair (yours, or "not given") · New version · Recheck date (yours, or "not given"); R4 and R6 as facts.
4. **Repair order:** by dependency, from the failing checks.
5. **For you to decide:** which version is used for training (not the failed one, old task); a new test set if a model was already evaluated (DA-73, EMA, context); limit changes and the date written.
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Data quality review draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Your limits (verbatim, numbered, with version and date written)
### Failed checks, owners, repairs and versions (script output)
| Check | Field | Failing | Owner | Repair | New version | Recheck date | Flags |
|---|---|---|---|---|---|---|---|
### Checks without a limit (reported, not marked)
### Repair log rows that do not match a failed check
### Repair order by dependency
### For you to decide
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Data quality review draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
