# Output format: company change read

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words (`scripts/monitor_helpers.py wordcount <answer.md>`, or by hand). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

1. **Answer:** whether the library's log records any change since DATE for the named companies, in one or two sentences.
2. **Changes:** Company · What changed (as the record names it) · Event date · Source · Retrieved.
3. **No change recorded:** names, with the log caveat (log began DATE; last sweep DATE; event-dated rows only; "about the log, not the company"). If the period starts before the log began, say so and offer the dated filings and authorization records for it; never "no change" for that part.
4. **Status:** one line per company from a primary filing or register entry (form or item, date, source, read date, and what it does not mean), or "Status: [GAP]: not read. Filings to open: ...". Never from press, memory or a quiet log.
5. **What the library cannot see:** one line from the perimeter, with where to check.
6. **Hypotheses for review:** at most three, each tied to one of the person's triggers.
7. **Full version:** one line offering it, before the record block.
8. **Calls made** (before the record block; not counted in the word cap): tool and arguments, one line each.
9. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Change read draft. No watch set." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Perimeter at this read
| Source | Loaded (records) | Not loaded and why |
|---|---|---|
### Changes
| Company | Change | Event date | Source URL | Retrieved | Read as (row) |
|---|---|---|---|---|---|
### No change recorded
| Company | Since | Log first entry | Last sweep | Caveat | Dated filings and authorizations offered for the window before the log |
|---|---|---|---|---|---|
### Company status
| Company | Status as the record states it (form or item, date) | Source and read date | Does not mean (row) |
|---|---|---|---|
### What the library cannot see
| Source | Why | Where to check |
|---|---|---|
### Hypotheses for review
### Gaps
### Calls made (before the record block)
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
