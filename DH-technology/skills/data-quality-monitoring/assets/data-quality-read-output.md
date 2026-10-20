# Output format: data quality read

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/dq_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build lines 2 and 3 from `scripts/dq_check.py run` and `compare` output; do not recount by hand. Budget in words: answer 70, results 150, changes 80, limits 60, record 50.

1. **Answer** (two sentences): as of the read date and for the version read, counts of checks that pass, fail, have no limit or were not run against your limits; failed checks by name with counts; leak features; the largest change from the previous version as a fact.
2. **Results:** Check · Category · Failing (count of denominator) · Your limit · Result; uniqueness and relational failures first.
3. **Changes from the previous version:** rows; fields whose missing share or summary moved, old against new; "a fact about the data, not a drift verdict".
4. **Limits of this read:** V1 or V2; checks with no limit; verification only (no external reference, DA-94); counts are not evidence of reliability or validity (DA-139, CMS, context).
5. **Calls made**, then one line offering the full version.
6. **Record (the very last line, nothing after it):** "Data quality read draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Version, read date and rules (written for version, on date)
### Results against your limits (script output)
| Check | Kahn category | Field | Rows checked | Failing | Share | Your limit | Result |
|---|---|---|---|---|---|---|---|
### Features with rows dated after the index time
### Comparison with the previous version (script output)
| Field | Missing share old | Missing share new | Old summary | New summary |
|---|---|---|---|---|
### What the read does not show
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Data quality read draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
