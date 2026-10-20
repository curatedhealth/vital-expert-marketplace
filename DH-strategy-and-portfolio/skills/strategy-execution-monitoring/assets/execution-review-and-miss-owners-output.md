# Output format: execution review and miss owners

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/execution_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 60, rules 50, failed elements 140, limits 60, decisions 50, record 50.

1. **Answer** (two sentences): counts of units whose rule is met, failed and not measurable; the failed elements by name; how many have an owner and a recheck date; the flag that most limits the review. No overall verdict.
2. **Your rules:** one line per rule type, verbatim; units without a rule listed.
3. **Failed elements:** Unit · Element · Fact behind it · Owner (yours, or owner not named) · Recheck date (yours, "not given", or "stopped").
4. **Limits:** not measurable, not comparable, tests without a prior rule, partner company status line (quoted from filings by name and date where a row covers the company, or `[GAP]`: not read), one line each.
5. **For you to decide:** each with its facts; kill or continue is yours. Where you call a test failed or successful, the logged result and its direction against the comparator, verbatim from the log ("31% vs 24%"), beside the flag that no rule was written before the start.
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Execution review draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Your pass rules (verbatim, numbered)
### Results against your rules
| Unit | Your rule | Result | Met, failed, not measurable | Flags |
|---|---|---|---|---|
### Failed elements, owners and recheck dates
| Unit | Element | Fact behind it | Owner | Recheck date or stopped | Follow-up (your words) |
|---|---|---|---|---|---|
### Not measurable or not comparable
### Partner facts behind failed units (status quoted from filings, source name and date, row after)
### Logged results of tests you called failed or successful (verbatim from the log, with direction against the comparator)
### For you to decide
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Execution review draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
