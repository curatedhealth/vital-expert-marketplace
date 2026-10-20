# Output format: funding signals read

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/portfolio_table.py words ANSWER.md` (it leaves out the calls list and table source columns), not by estimate. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, the "Full version on request" line. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

Build lines 1 and 2 from `scripts/portfolio_table.py funding` output; do not recount by hand.

1. **Answer:** the filing types and counts in the store, their date range, and what the record cannot show that the person asked about (valuation, investors, private rounds). Two sentences.
2. **Filings by type:** table Type · Count · What it shows · What it does not show · Rows. At most six types; the rest in full mode.
3. **Amounts on record:** only per filing row, with type, date, reference and "amount as stored". No sum across types. If none: "No amount stated in the rows read."
4. **Grants and awards:** source, count, date range; "public funding for a stated project, not equity".
5. **The person's figures (if any):** each labeled "the person's figure, source as named". Confidential material: "from the person (confidential)", kept apart.
6. **Status:** per company, as the record states (form, item, date, URL, read date, and what it does not mean: a Form 15 or 25 is not dissolution, DL-144, DL-149), or "`[GAP]`: not read" with the filings to open (8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15; register). Never from press or memory (`references/company-status.md`).
7. **Gaps:** private rounds `[GAP]`; sources not loaded; 8-K items not stated; for a period before 12 October 2026 the library change log does not apply (give the dated filings instead of "no change"); anything needing a live check. **Owner:** as the person named, in their words, or "Owner not named: who clears this?"
8. **Full version:** one line offering it, before the record block.
9. **Calls made** (before the record block; not counted in the word cap): list, with retrieval dates.
10. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Funding signals read draft for OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Company and identifiers (as resolved, SEC CIKs)
### Filings by type
| Type | Count | Date range | What it shows | What it does not show | Rows |
|---|---|---|---|---|---|
### Filing rows read
| Type | Date | Amount as stored | Item (if opened) | Reference and URL | Retrieved |
|---|---|---|---|---|---|
### Grants and awards
### The person's figures (labeled)
### Status (references/company-status.md)
### Gaps and owner
### Calls made (before the record block)
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
