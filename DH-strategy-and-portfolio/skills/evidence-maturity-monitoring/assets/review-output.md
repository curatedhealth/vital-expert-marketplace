# Output format: evidence review

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with a tool (`python3 scripts/maturity_diff.py --count ANSWER.md`, which drops the calls list and source columns), not by estimate. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, the "Full version on request" line. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

1. **Answer:** of the person's N measures, how many triggered, did not trigger or are not measurable; the level as confirmed (and any newly proposed level, labeled). Two sentences. No buy, hold or sell.
2. **Measures checked:** table Measure (person's words) · Status · Class and record · Owner (as named, or owner not named).
3. **Company status:** each company's status carried from A2: read from a filing or register, or "Status: [GAP]: not read" with the filings to open.
4. **Triggers:** for each, the record, the action as the person decided it (or "decision not given"), and the reread date (as given, or not given).
5. **Level:** confirmed baseline; "proposed level X under FRAMEWORK, for you to confirm" only where an INPUT change bears on it, with the framework's limits and rows (DOI beside each [PAPER] row).
6. **Routes:** where each follow-up goes (pack and skill).
7. **Gaps and stops:** no value statement, no rating, no benchmark.
8. **Full version:** one line offering it, before the record block.
9. **Calls made** (before the record block; not counted in the word cap): list (often none).
10. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Evidence review draft for OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Measures and owners as stated
### Measures checked against the movement read
| # | Measure | Status | Class | Record and retrieval date | Owner |
|---|---|---|---|---|---|
### Triggers: record, decision, reread date
### Company status (filings and registers read, or [GAP]: not read)
### Framework level: confirmed and proposed
### Follow-up routes
### Gaps
### Calls made (before the record block)
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
