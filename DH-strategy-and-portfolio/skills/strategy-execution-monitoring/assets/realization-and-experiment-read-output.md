# Output format: realization and experiment read

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/execution_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build lines 1 to 4 from `scripts/execution_check.py` output; do not recount by hand. Budget in words: answer 60, benefits 100, milestones 80, tests 70, partner 70, record 45.

1. **Answer** (two sentences): as of the read date, counts of benefits met, not met and not measurable against your rules; milestones with failed elements; tests that cannot be read against a prior rule; the partner record line. No verdict on the strategy.
2. **Benefits:** Id · Baseline · Target · Actual (date) · Share of planned change · Your rule · Met · Flags.
3. **Milestones:** Id · Due · Completed · Elements failed · Objective it serves · Milestones that depend on it · Flags. Not-yet-due milestones say so.
4. **Option tests:** Id · Rule · Result as given · Flags; then "cannot be read against a rule written before the start: ...".
5. **Partner record** (only if named): changes in the log window with the log caveat, or the dated records for a period before 12 October 2026; **Company status**: quoted from the filings by name and date for a company the research pass read (what each form does not mean beside it), otherwise `[GAP]`: not read with the filings to open; current FDA listing holder beside the authorization holder; any mismatch between the partner's products on record and what you say it supplies; press claims labeled as yours and answered from the record.
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Realization read draft. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Benefits (script output)
### Milestones (script output)
### Option tests and experiments (script output)
### Named partners
| Company | What changed (type, date) | Log window and limits | Source | Retrieved |
|---|---|---|---|---|
### Company status
| Company | Filing or register | Date | Status as read, quoted (or `[GAP]`: not read) | What it does not mean | Source and rows |
|---|---|---|---|---|---|
### Forecast rerun on your inputs (if given)
| Parameter | Range (yours or default) | Output low to high | Flags |
|---|---|---|---|
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Realization read draft. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
