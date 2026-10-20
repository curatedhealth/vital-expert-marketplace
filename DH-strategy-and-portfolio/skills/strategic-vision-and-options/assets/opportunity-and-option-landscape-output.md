# Output format: opportunity and option landscape

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/options_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build candidate lines from `scripts/options_check.py facts` output; do not retype figures. Budget in words: answer 60, opportunity 50, options 110, candidates 90, status 50, licensing 40, gaps 40, record 45.

1. **Answer** (two sentences): the opportunity in the person's words, the number of options on the longlist, what the record shows on named candidates, the largest gap. No preferred option.
2. **Opportunity:** one line in the person's words; proposed WHO axis and Oslo type; proposed TRL with the EU wording, or "TRL not proposed: state not given".
3. **Options:** Option · What must be true (your words) · Facts that bear on it · Source and rows (source name and date in plain words, row id after). Business as usual first; added options labeled "proposed".
4. **Candidates:** Company · Product · Reference · Pathway in words · Decision date · Source. Only candidates the question names.
5. **Company status** (one line per named company): for a company the research pass read, the status as the filings state it, each filing by name and date with its row ("Akili 8-K, 2 July 2024, Items 2.01 and 5.01 (SP-151 [WF])"), what each form does not mean (Form 25 concerns the listing only, DL-144; Form 15 is not dissolution, DL-149, inference), the product's current FDA listing holder beside the authorization holder, and the option the status blocks with what would unblock it. Otherwise "Company status `[GAP]`: not read" with the filings to open and the items (1.03, 2.01, 3.01, 5.01).
6. **For your legal owner** (only if an option is a license or collaboration): the rule, date and threshold, one line each, source in plain words then row; threshold and your figure side by side ("your figure: not given" if none), no leaning; data flags if health data is licensed (SP-142; DL-101, inference in part; DL-106); "conclusion for the owner you name, or owner not named".
7. **Gaps:** one line each, by reason.
8. **Calls made** (the connector note goes here), then one line offering the full version.
9. **Record (the very last line, nothing after it):** "Option landscape draft. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Opportunity (your words)
### Shared terms (proposed)
| Frame | Proposed reading | Its limit | Source and rows |
|---|---|---|---|
### Context for the markets you named
| Context | Fact | Source and rows |
|---|---|---|
### Proposed readiness level
| Proposed TRL | EU wording (verbatim) | Evidence you gave | Source and rows |
|---|---|---|---|
### Longlist
| Option | Origin (yours or proposed) | What must be true | Facts that bear on it | Source and rows |
|---|---|---|---|---|
### Named candidates
| Company | Product | Register | Reference | Pathway in words | Decision date | Source | Retrieved |
|---|---|---|---|---|---|---|---|
### Company status
| Company | Filing or register | Date | Accession or number | Status as read, quoted (or `[GAP]`: not read) | What it does not mean | Option it blocks | Source and rows |
|---|---|---|---|---|---|---|---|
### Authorization holder and current FDA listing holder
| Product | Authorized to (record, date) | Listed now by (FDA registration and listing, read date) | Source and rows |
|---|---|---|---|
### Licensing and disclosure facts for your legal owner
| Fact | Instrument and date | Source and rows |
|---|---|---|
### Gaps
| Fact | Reason | Next step |
|---|---|---|
### Calls made
### One line offering anything not shown
### Record (the very last line)
Option landscape draft. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
