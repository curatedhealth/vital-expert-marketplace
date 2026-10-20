# Output format: investment portfolio comparison table

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/portfolio_table.py words ANSWER.md` (it leaves out the calls list and table source columns), not by estimate. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, the "Full version on request" line. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

Build lines 1 to 3 from `scripts/portfolio_table.py compare` output; do not retype values by hand.

1. **Answer:** what the records show across the set and the main gap, including any status read (or that status was not read), in two sentences. No order of merit.
2. **Comparison table:** Company as resolved (query) · Authorizations · Studies (by brand / indication only / unlinked) · Safety events · Funding signal counts · Evidence maturity (score, points, rubric v1) · Source and retrieval date. Unresolved names appear as "lookup missed".
3. **Notes the person must see:** at most six: company level (which products a row covers), combined filing names ("a proposal until a person validates it"), fields and sub-fields absent ("field absent", never 0), `none_found` versus `not_assessable`, sources not loaded, the CIKs the store holds ("other registrants and form types are not shown"). Authorizations are not incorporation: never "US company".
3b. **Status:** per company, as the record states (form, item, date, URL, read date, and what it does not mean: a Form 15 or 25 is not dissolution, DL-144, DL-149), or "`[GAP]`: not read" with the filings to open (8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15; register). Never from press or memory (`references/company-status.md`).
4. **What the score is:** one line: "The library's stated convention for documented evidence (rubric v1, 7 October 2026), not a valuation, a prediction or a rank."
5. **The person's columns (if any):** figures the person supplied, labeled "from the person"; confidential material labeled and kept apart.
6. **Next step for the person:** score the companies for B1, or route (pack and skill). **Owner:** as the person named, in their words, or "Owner not named: who clears this?"
7. **Full version:** one line offering it, before the record block.
8. **Calls made** (before the record block; not counted in the word cap): list, with retrieval dates.
9. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Portfolio comparison draft for OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Comparison table (script output)
### Evidence maturity components per company
| Company | Regulatory status | Clinical evidence | Active development | Product breadth | Excluded | Rows |
|---|---|---|---|---|---|---|
### Notes per company
### What the frameworks count and leave out (DL rows with DOIs beside each row id)
### The person's columns (labeled)
### Status per company (references/company-status.md)
### Gaps and owner
### Calls made (before the record block)
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
