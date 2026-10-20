# Output format: watch rules and signals

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/portfolio_watch.py words ANSWER.md` (it leaves out the calls list and table source columns), not by estimate. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, the "Full version on request" line. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

1. **Answer:** the signals that exist for these holdings and the two most important things that do not count. Two sentences.
2. **Signals per holding type:** table Holding · Signal · Source (library or the person's direct read) · Clock · Can tell · Cannot tell · Rows. At most eight rows.
3. **The person's rules:** numbered, verbatim; any proposed rule labeled "proposed" with its row, never with an owner or date filled in.
4. **Does not count:** at most five lines, each with its row; rows that rest on an inference label it "(inference)" (for example DL-092 breaches under 500, DL-097 a vendor's breach under the client's name). A Form 15 or 25 is not dissolution (DL-144, DL-149).
4b. **Status signals for every holding:** 8-K Items 1.03, 2.01, 3.01, 5.01, Form 25, Form 15, Companies House status, German insolvency notices (`references/company-status.md`, DL-135 to DL-168), each with what it does not mean.
5. **Countable facts:** which script flag or count serves which rule. "A count is not a score."
6. **Gaps:** cadence, owners, thresholds not given; signals outside the library. **Owner:** as the person named, in their words, or "Owner not named: who clears this?"
7. **Full version:** one line offering it, before the record block.
8. **Calls made** (before the record block; not counted in the word cap): usually none.
9. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Watch rules draft for OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Holdings and their signal sets
| Holding | Type (SEC reporting, private US, UK, EU or Swiss) | Signals | Library or direct read | Rows |
|---|---|---|---|---|
### Rules (the person's, numbered; proposed ones labeled)
| No. | Rule | Signal | What counts | Owner | Reread | Rows |
|---|---|---|---|---|---|---|
### Does not count
### Countable facts and the rules they serve
### Gaps
### Calls made (before the record block)
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
