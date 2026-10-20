# Output format: signal scan and triage

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/horizon_helpers.py words ANSWER.md` (counts the whole answer except the calls list, and leaves out the Source, Rows and Retrieved columns); without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 70, signal table 200, leads 50, coverage and gaps 60, record 50. Every fact names its source in plain words with its date, then the row id ("FDA 510(k) K261317, decided 14 May 2026"; "Pear 8-K, filed 7 April 2023 (SP-156) [WF]"); never a row id alone.

1. **Answer** (two or three sentences): how many signals in the window and scope, the two or three that bear most on the person's scope, every maker the saved or live records show under each product code in scope, the leads not yet confirmed, and the coverage limit that most changes the picture. No trend unless asked; then "proposed reading".
2. **Signals:** Id · Type · Event date · Record (identifier) · Does not show · Source (name and date, row).
3. **Makers on record under the product code** (if a product code is in scope): every maker the records read show, with decisions in and before the window; how many decisions in the window's years are not yet tied to a maker; the public record that lists all of them (FDA's 510(k) database, searchable by product code, DL-131); ask for maker names to search.
4. **Leads, not signals:** each with the record that would confirm it and "record not read `[GAP]`".
5. **Logs and coverage:** the change-log line as returned (never "no change"); what the library does not load.
6. **Company status** (each named company): the status already read (`references/company-status.md` section 6) cited by filing or register name and date, or "Status: [GAP]: not read" with the filings to open. A product's current FDA listing holder is stated apart from the company that was authorized.
7. **Calls made**, then one line offering the full version.
8. **Record (the very last line):** "Signal log draft. Signals are records; trends are yours. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Scope, window and filters (yours, or proposed)
### Perimeter
| Source | Loaded | Not loaded or limited | Last load |
|---|---|---|---|
### Signal log
| Id | Type | Event date | Record and identifier | What it does not show | Source | Retrieved |
|---|---|---|---|---|---|---|
### Decisions per device type by year (if a product code is in scope)
| Year | Decisions | Change on year before | Of which tied to a maker in the records read |
|---|---|---|---|
Counts of decisions for a device type; the last year is partial. Whether this is a trend is your reading.
### Makers on record under the product code (`scripts/horizon_helpers.py makers`)
| Maker (as stored) | Decisions under the code (identifier, date) | In window | Source |
|---|---|---|---|
Only makers in the records read; the full list is in FDA's 510(k) database by product code (DL-131).
### Dated rule and program changes in the window
| Change | Instrument and date | Status as read | Rows |
|---|---|---|---|
### Leads, not signals
| Lead (as brought) | Record that would confirm it | Looked up | Status |
|---|---|---|---|
### Filtered out and proposed noise
| Item | Filter or reason | Yours or proposed |
|---|---|---|
### Proposed readings (only if asked)
| Reading | Signals for | Signals against | Status |
|---|---|---|---|
Proposed readings; whether any is a trend is your call.
### Company status (named companies)
| Company | Status (filing or register, date, row) | What it does not mean | Current FDA listing holder of its product, if different |
|---|---|---|---|
### Gaps
| Fact | Class | Next step |
|---|---|---|
### Calls made
### Record (the very last line)
Signal log draft. Signals are records; trends are yours. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
