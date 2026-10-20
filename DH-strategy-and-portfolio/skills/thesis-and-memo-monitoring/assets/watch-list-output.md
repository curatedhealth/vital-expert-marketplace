# Output format: thesis watch list

Short mode: 450 words maximum, counted without the calls list and the Source, Source of now and Rows columns. Before handing over, count the words with `python3 scripts/thesis_check.py --words ANSWER.md` (counts the body above the calls list and leaves out Source, Source of now and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

Budget in words: answer 60, watch list 200, not measurable 40, clocks 40, missing 50, record 45.

1. **Answer** (two sentences): how many of the person's assumptions a public signal can carry, which cannot (T3), and what the person still has to give.
2. **Watch list:** # · Assumption (your words) · Signal and call · What it cannot show · Value at memo · Trigger (your words). Owner and reread date columns only where the person gave them; otherwise one line under the table.
3. **Not measurable from the record:** the assumptions, and that the person's own data (labeled non-public) would be needed.
4. **When a change can appear:** the filing clocks that bear on the signals and the change log's start date, one line.
5. **Missing:** triggers, owners ("owner not named"), reread dates ("not given"), as questions.
6. **Full version:** one line offering it, before the record block.
7. **Calls made** (before the record block; not counted in the word cap): each call with its arguments.
8. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Thesis watch list draft. No watch set. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Watch list
| # | Assumption (your words) | Company | Signal | Call | What it cannot show | Value at memo (date) | Trigger (your words) | Rule (machine form, if yours) | Owner | Reread date | Rows or file |
|---|---|---|---|---|---|---|---|---|---|---|---|
### Not measurable from the record (T3)
### Filing clocks and the change log
| Signal | When a record can appear | Row |
|---|---|---|
### Proposed (only if asked; not applied until you confirm)
### Missing inputs
### Record
Thesis watch list draft. No watch set. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
