# Output format: company profile

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with a tool (`python3 scripts/profile_table.py --count ANSWER.md`, which drops the calls list and source columns), not by estimate. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, the "Full version on request" line. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

1. **Answer:** who the reference resolved to (and on what basis), what the records hold (authorizations, registered studies, filings), status as read (or "[GAP]: not read") and the largest gap with its reason. Two or three sentences.
2. **Products and authorizations:** table Product · Record · Pathway in words · Decision date · Source (URL and retrieval date). From `scripts/profile_table.py`. At most six rows.
3. **Studies and filings:** one line on registered studies as linked (brand or indication only); a filings table Form · Filed · Amount as stated · What the form does not show (rows DL-002, DL-006, DL-015, DL-018 (inference) for Form D).
4. **Safety, recalls and status:** safety events and recall flags quoted from the saved `compare_portfolio` result with its retrieval date (`none_found`: "none found in the loaded enforcement source; not proof of none"), or "not read `[GAP]`"; status as read from a filing or register, or "Status: [GAP]: not read" with the filings to open (`references/company-status.md`); what a Form 15 or Form 25 does not mean, where one applies. Never 0, "none" or "US company" for a missing field.
5. **What the library does not hold for this company:** each source not loaded that touches the person's markets, with its reason.
6. **Direct reads to do:** at most three (breach portal and archive, Companies House, EDGAR full-text for 8-K items), each with its row.
7. **Your material (only if supplied):** facts with the document name the person gave; never merged with the record table.
8. **Gaps and stops:** contradictions the script printed; device status beyond the record goes to `dh-regulatory-and-quality` regulatory-pathway-and-classification.
9. **Full version:** one line offering it, before the record block.
10. **Calls made** (before the record block; not counted in the word cap): each call with its arguments and retrieval date.
11. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Company profile draft for OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Resolution and identifiers
### Products and authorizations
| Product | Record | Pathway in words | Product code | Regulation | Decision date | Source and retrieval date |
|---|---|---|---|---|---|---|
### Registered studies as linked
### Filings stored and what each form shows
| Form | Filed | Amount as stated | What the form does not show | Rows |
|---|---|---|---|---|
### Safety events and recall flags (saved compare_portfolio)
### Company status (filings and registers read, or [GAP]: not read)
### Perimeter: sources loaded and not loaded
### Direct reads to do
### Your material
### Contradictions inside the response
### Gaps
### Calls made (before the record block)
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
