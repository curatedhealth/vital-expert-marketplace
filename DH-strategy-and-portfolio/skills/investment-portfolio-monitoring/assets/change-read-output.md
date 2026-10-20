# Output format: change read

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/portfolio_watch.py words ANSWER.md` (it leaves out the calls list and table source columns), not by estimate. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, the "Full version on request" line. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

Build lines 1 and 2 from `scripts/portfolio_watch.py` output; do not recount by hand.

1. **Answer:** as of the read date, what changed for which holdings, the window the log covers (first entry, last sweep), and the flag that most limits the read. Two sentences. Where a window starts before the log began (12 October 2026), say so here: that span is not "no change".
2. **Holdings table:** as the script prints it (holding, window asked, library answer, covered by the log, owner, reread date, flags).
3. **Changes as returned:** type, event date, source, retrieval date; 8-K item only once the filing is opened. If none: "No change recorded in the library's log from FIRST ENTRY to LAST SWEEP."
4. **Against the earlier run (if any):** field changes from `diff`, at most five; score changes routed to `evidence-maturity-monitoring` (this pack).
4b. **Before the log began (each W1 holding):** the holding's dated primary filings and authorization records for the uncovered span: saved `get_funding_signals` output first ("filings in the store up to DATE, the latest filing in the store, not a statement about the company today"), then the EDGAR filing list per CIK and FDA or DiGA records for the person to open. Never "no change" for that span.
4c. **Status:** per company, as the record states (form, item, date, URL, read date, and what it does not mean: a Form 15 or 25 is not dissolution, DL-144, DL-149), or "`[GAP]`: not read" with the filings to open (8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15; register). Never from press or memory (`references/company-status.md`).
5. **Outside the library:** signals the person reads directly (UK filings, HHS breach portal, private rounds).
6. **Gaps.** **Owner:** as the person named, in their words, or "Owner not named: who clears this?"
7. **Full version:** one line offering it, before the record block.
8. **Calls made** (before the record block; not counted in the word cap): list, with retrieval dates.
9. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Portfolio change read draft for OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Holdings table (script output)
### Limits as returned
### Changes as returned
| Holding | Change | Event date | Source | Retrieved | Rows |
|---|---|---|---|---|---|
### Before the log began (W1 holdings)
### Status per holding (references/company-status.md)
### Diff against the earlier run (script output)
### Outside the library
### Gaps
### Calls made (before the record block)
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
