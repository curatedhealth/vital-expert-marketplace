# Output format: change read since the memo

Short mode: 450 words maximum, counted without the calls list and the Source, Source of now and Rows columns. Before handing over, count the words with `python3 scripts/thesis_check.py --words ANSWER.md` (counts the body above the calls list and leaves out Source, Source of now and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

Budget in words: answer 60, status 60, record changes and log 90, rule changes 120, hypotheses 50, record 45.

1. **Answer** (two sentences): whether anything in the record or the rules moved since the memo date that touches the thesis, with the log caveat where the record is quiet.
2. **Company status** (always): quoted from the filing or register read with its date, including the rows in `references/named-company-status.md` (source name and date, what each form does not mean, and a product's current FDA listing holder apart from the applicant), or "Company status [GAP]: not read" with the latest 8-K (date, URL) and the items to open.
3. **Record and filings:** changes by event date with source; or "no change recorded; log began DATE, last sweep DATE; about the log, not the company". Where the memo predates the log (T5), the dated filings and authorizations for that period instead of "no change".
4. **Rule changes since the memo:** Change · Instrument and date · Status · Row. Only regimes the memo flagged.
5. **Hypotheses for review:** one line per change.
6. **Full version:** one line offering it, before the record block.
7. **Calls made** (before the record block; not counted in the word cap): each call with its arguments; the connector note and the perimeter go here.
8. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Change read draft. Companies described by their record only. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Perimeter now
### Company status
| Filing or register | Date | URL | Status as read, quoted (or `[GAP]`: not read) | What it does not mean | Rows |
|---|---|---|---|---|---|
### Record changes since DATE
| Company | Change | Type | Event date | Source URL | Retrieved |
|---|---|---|---|---|---|
### Change log
| First entry | Last sweep | Since used | T5 |
|---|---|---|---|
### Filings and authorizations by date (compared with the memo's run)
| Company | Type | Earlier count or latest date | Now | New rows |
|---|---|---|---|---|
### Evidence maturity (library convention)
| Company | Rubric at memo | Rubric now | Score at memo | Score now | Component that moved | Comparable |
|---|---|---|---|---|---|---|
### Rule changes since DATE
| Date | Change | Instrument | Status | Row |
|---|---|---|---|---|
### Scheduled, not yet reached
### Hypotheses for review
### Gaps
### Calls made (before the record block)
### Record
Change read draft. Companies described by their record only. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
