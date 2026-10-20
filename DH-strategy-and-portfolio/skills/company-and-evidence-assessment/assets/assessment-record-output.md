# Output format: company and evidence assessment record

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with a tool (`python3 scripts/profile_table.py --count ANSWER.md`, which drops the calls list and source columns), not by estimate. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, the "Full version on request" line. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

1. **Answer:** of the person's N criteria, how many are met, not met and not measurable; the decision as the person stated it (or "decision not given"); the open item that blocks most. Two sentences. No recommendation.
2. **Criteria read:** table Criterion (person's words) · Met, not met or not measurable · Fact · Source (record and retrieval date, or "your material"). At most eight rows.
3. **Safety and status carried in:** safety events and recall flags from the saved `compare_portfolio` result (or not read `[GAP]`); status as read, or "Status: [GAP]: not read" with the filings to open. One or two lines.
4. **Data and privacy facts to request (only where the target handles health data):** at most four, each with its row, "for the owner you name for compliance, or owner not named".
5. **Decision as stated:** decision, date and decider in the person's words; where the decision sits beside an unmet criterion, both facts side by side with the person's stated reason.
6. **Open items:** item · What would settle it · Owner (as named, or owner not named) · Reread date (as given, or not given).
7. **Gaps and stops:** no valuation, price, multiple, return or market size is given (none is sourced); transaction rules go to `investment-memo-and-decision-record` (this pack).
8. **Full version:** one line offering it, before the record block.
9. **Calls made** (before the record block; not counted in the word cap): list (often none).
10. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Assessment record draft for OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Criteria as stated
### Criteria read against the records
| # | Criterion | Status | Fact | Source | Rows |
|---|---|---|---|---|---|
### Safety events, recall flags and company status
### Facts from your material (kept apart)
### Data and privacy requests (for the owner the person names for compliance, or owner not named)
### Decision as stated
### Open items, owners and reread dates
### Gaps
### Calls made (before the record block)
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
