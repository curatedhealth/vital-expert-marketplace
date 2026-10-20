# Output format: market intelligence quality check

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words (`scripts/monitor_helpers.py wordcount <answer.md>`, or by hand). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

1. **Answer:** two sentences: on the person's rule, the count in elements as the helper prints it ("Failed elements: N"), then the entries (pass, fail, not measurable); never only entries. Which lanes or jurisdictions have no record; whether any rule entry has moved. No verdict on the market.
2. **Your rule:** numbered elements in the person's words (or "proposed: source, date, segment covered", not applied until confirmed), maximum age (or "not given: ages shown, not judged"), lanes and jurisdictions that matter, blocking element (or "not given").
3. **Failed and not measurable:** Lane · Entry · Element · Result · Owner (yours) · Recheck date (yours).
4. **Coverage:** one line per lane: entries, gaps, missing jurisdictions, and the gap class (not loaded, not asked, lookup missed). For a lane that passes on count, one line on what it holds (for example a rules lane with no device or DiGA rule, routed to `dh-regulatory-and-quality` regulatory-pathway-and-classification); a whole-directory figure (DE33, DE34) is said not to be indication-specific.
4b. **What a board reader cannot open:** entries whose source is only a row id or tool name, with the readable source (name and URL) from the `mi-check` notes; whether that is an element is the person's call.
4c. **Peers:** holder as stored; current FDA listing holder and filed status where `named-company-status.md` covers them (from the `mi-check` notes); "Status: [GAP]: not read" for the rest.
5. **Moved rules:** instrument, old wording in the map, dated fact now, rows.
6. **Decision for the person:** the one call they need to make (for example who owns the empty lane).
7. **Full version:** one line offering it, before the record block.
8. **Calls made** (before the record block; not counted in the word cap): tool and arguments, one line each, and the `mi-check` command line if run.
9. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Market intelligence check draft on your rule. No market size; nothing scored." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Your rule
| No. | Element, in your words | Proposed? | Blocks release? |
|---|---|---|---|
### Entries
| Lane | Jurisdiction | Entry | Source | Date | Age | Result per element |
|---|---|---|---|---|---|---|
### Coverage
| Lane | Entries | Gaps | Jurisdictions with no entry | Gap class | Next step |
|---|---|---|---|---|---|
### Perimeter now versus the map's date
| Store or scheme | In the map | Now | Source and date |
|---|---|---|---|
### Moved rules
| Instrument | In the map | Dated fact now | Rows |
|---|---|---|---|
### Peer status and current holders
One line per peer: holder as stored; current FDA listing holder and status from filings where `named-company-status.md` covers it, with source and date; otherwise "Status: [GAP]: not read" with the filings to open.
### Readable sources
| Entry | Source in the map | Readable source (name, URL) | Rows |
|---|---|---|---|
### Failed elements: owner and recheck
| Element | Entry | Owner (yours) | Recheck date or stop (yours) |
|---|---|---|---|
### Calls made (before the record block)
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
