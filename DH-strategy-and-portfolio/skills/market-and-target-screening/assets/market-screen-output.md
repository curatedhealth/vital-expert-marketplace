# Output format: market screen (long list)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words (`scripts/screen_helpers.py wordcount <answer.md>`, or by hand). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

1. **Answer:** one or two sentences: how many companies the store matched for the segment and jurisdiction, how many are shown, and the one coverage limit that most changes the picture.
2. **Long list:** Company · Country · Products (as stored) · Authorizations · Studies · Safety records · Evidence maturity (N, rubric v1) · Retrieved. At most ten rows; the rest in full mode.
3. **Coverage:** one line: the screen's own statement ("covers only the companies the store holds, not the market") and the sources not loaded with their reasons.
4. **Gaps that matter:** at most three, classed per `gap-rules.md`, plus one status line for the whole list: "Status: [GAP]: not read. The store does not show whether a company was acquired, deregistered, delisted or is in bankruptcy or insolvency; filings to open per company on request (A2)."
5. **Decisions for the person:** the criteria and pass rules B1 needs, if they want a short list.
6. **Full version:** one line offering it, before the record block.
7. **Calls made** (before the record block; not counted in the word cap): tool and arguments, one line each.
8. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Market screen draft. Order is the library's sort, not a ranking. No market size." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Perimeter
| Source | Loaded (records) | Not loaded and why | As of |
|---|---|---|---|
### Long list
| Company | Country | Jurisdictions | Products | Authorizations | Studies | Safety records | Evidence maturity (points, rubric v1) | Retrieved |
|---|---|---|---|---|---|---|---|---|
Order: the library's sort (evidence maturity score, then company name). Not a ranking of targets.
### Named companies added
| Company | Lookup used | Result | Gap class |
|---|---|---|---|
### Evidence maturity: how to read it
One paragraph from `screening-rules.md` section 3, with [PAPER] rows and DOIs (Rows cell: "DL-117, DOI 10.2196/37677").
### Company status
One line for the list: the store does not show whether a company was acquired, deregistered, delisted or is in bankruptcy or insolvency (`screening-rules.md` section 5). "Status: [GAP]: not read", with the filings to open per company on request (A2).
### Gaps
| Fact | Class | Next step |
|---|---|---|
### Calls made (before the record block)
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
