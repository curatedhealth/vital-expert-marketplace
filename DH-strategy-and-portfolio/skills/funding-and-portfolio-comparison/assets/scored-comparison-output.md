# Output format: scored comparison and decision record

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/portfolio_table.py words ANSWER.md` (it leaves out the calls list and table source columns), not by estimate. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, the "Full version on request" line. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

Build lines 1 to 3 from `scripts/portfolio_table.py swap` output and the `analytics.mcda` response.

1. **Answer:** the computed order, the nearest swap point, and the decision if the person stated one. Then: "The order is your scores and weights, computed; it is not a recommendation to invest, pass or price."
2. **Order with its basis:** table Order · Company · Value · each criterion's score (the person's) · weights in the header. Ties named.
3. **How solid:** at most four swap points, "A stays above B unless WEIGHT moves above or below X", and any pair where one scores at least as high on every criterion ("holds at any weights").
4. **Not ranked:** each company with the missing score named.
5. **Pass rules (if given):** meets, does not meet, or cannot tell from the record, per company, against the rule as the person wrote it.
6. **Decision:** as stated, decider and date as given, or "decision not given". A declined invest, pass or valuation question: the facts-only record, labeled "draft for the owner", no recommendation. **Owner:** as the person named, in their words, or "Owner not named: who clears this?"
6b. **Status:** per company, as the record states (form, item, date, URL, read date, and what it does not mean: a Form 15 or 25 is not dissolution, DL-144, DL-149), or "`[GAP]`: not read" with the filings to open (8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15; register). Never from press or memory (`references/company-status.md`).
7. **Stops:** deal or data rule questions listed with rows and routed to the owner the person names for legal or compliance questions (or owner not named).
8. **Full version:** one line offering it, before the record block.
9. **Calls made** (before the record block; not counted in the word cap): list.
10. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Scored comparison record draft for OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Inputs (the person's): criteria, direction, weights, scores
### Computed order and check against the tool
### Swap points
### Not ranked
### Pass rules
### Decision, decider, date (as given)
### Status per company (references/company-status.md)
### Open questions and stops
### Sources and retrieval dates (A2 table)
### Calls made (before the record block)
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
