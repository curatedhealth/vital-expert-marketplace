# Output format: memo fact base

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/memo_facts.py words ANSWER.md` (counts the body above the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

Build from `scripts/memo_facts.py facts` output; do not retype figures. Budget in words: answer 60, status 60, authorizations table 80, filings 70, evidence 40, gaps 80, record 45.

1. **Answer** (two sentences): what the record shows about COMPANY as of the retrieval date and the largest gap. No valuation, no recommendation.
2. **Company status** (always): for a company in `references/named-company-status.md`, the filings as read on 20 October 2026, each with its source name and date and what it does not mean (for Pear: Pear 8-K, 7 April 2023, chapter 11, SP-156; Pear 8-K, 10 April 2023, Nasdaq delisting notice, SP-160; Form 25-NSE, 2 May 2023, not dissolution, SP-155, DL-144), and each product's current FDA listing holder apart from the applicant. Otherwise "Company status `[GAP]`: not read" with the latest 8-K, Form 25 or Form 15 rows by date with accession and URL, the items to open (1.03, 2.01, 3.01, 5.01), and one line on what Form 25 or 15 does not mean (DL-144, DL-149 (inference)).
3. **Authorizations:** Product · Reference · Pathway in words · Decision date · Source. Only products the question touches.
4. **Filings:** counts by type and date range in one line; Form D rows by date and stored amount; "Form D shows no valuation or investor names (DL-016; DL-018 (inference))". Private rounds `[GAP]`.
5. **Evidence and safety:** evidence maturity (score, rubric, one limit verbatim) and safety events as stated, one line each.
6. **Gaps:** one line each, by reason.
7. **Full version:** one line offering it, before the record block.
8. **Calls made** (before the record block; not counted in the word cap): each call with its arguments; the connector note goes here.
9. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Memo fact base draft. Public record only. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Perimeter (what the library loads and does not load, with dates)
### Identity
| Identifier | Value | Source | Retrieved |
|---|---|---|---|
### Company status
| Filing or register | Date | Accession or number | URL | Status as read, quoted (or `[GAP]`: not read) | What it does not mean | Rows |
|---|---|---|---|---|---|---|
### Products and authorizations
| Product | Register | Reference | Pathway in words | Product code | Regulation | Decision date | Source URL | Retrieved |
|---|---|---|---|---|---|---|---|---|
### Registered studies
| Link tier | Count | Source | Retrieved |
|---|---|---|---|
### Safety events
| Date | Event as stated | Products | Source | Retrieved |
|---|---|---|---|---|
### Filings and funding signals
| Source | Type | Count | Date range | Retrieved |
|---|---|---|---|---|
| Form D date | Stored amount | What it does not show | Rows |
|---|---|---|---|
### Evidence
| Framework or convention | Result | Its limits | Rows (DOI for [PAPER]) | Retrieved |
|---|---|---|---|---|
### Gaps
| Fact | Reason | Next step |
|---|---|---|
### Calls made (before the record block)
### Record
Memo fact base draft. Public record only. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
