# Output format: evidence movement read

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with a tool (`python3 scripts/maturity_diff.py --count ANSWER.md`, which drops the calls list and source columns), not by estimate. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, the "Full version on request" line. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

1. **Answer:** per company, score then and now with dates, and whether any difference is an INPUT change (and its record) or only METHOD, COVERAGE or RESOLUTION. Two or three sentences.
2. **Differences:** table Company · Date to date · Score (points) then and now · Change · Class · Record behind it (or "record not yet read"). From `scripts/maturity_diff.py`. At most eight rows.
3. **Flags and status:** resolution and recall flags from either run, verbatim, classed RESOLUTION until the person validates them (as the script prints); each company's status as read from a filing or register, or "Status: [GAP]: not read" with the filings to open; a Form 15 or Form 25 is not dissolution.
4. **Perimeter:** coverage changes as printed, labeled "not evidence".
5. **Change log (only if used):** "no change recorded" or events, with the log's limits (log started 12 October 2026; event dates, not load dates).
6. **Measures (only if A1 exists):** triggered, not triggered or not measurable, one line each.
7. **Gaps and stops:** inputs not compared, reference mismatches, trimmed outputs.
8. **Full version:** one line offering it, before the record block.
9. **Calls made** (before the record block; not counted in the word cap): each call with arguments and retrieval date, and the script command.
10. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Evidence movement read draft for OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Runs compared
| Company | Reference | Earlier run (date, file) | Later run (date, file) |
|---|---|---|---|
### Differences by class
| Company | Change | Class | Record behind it | Rows |
|---|---|---|---|---|
### Flags carried forward and company status
### Source coverage
### Change log and its limits
### Measures applied
### Gaps
### Calls made (before the record block)
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
