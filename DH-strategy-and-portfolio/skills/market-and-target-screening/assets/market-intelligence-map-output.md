# Output format: market intelligence map (ecosystem map)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words (`scripts/screen_helpers.py wordcount <answer.md>`, or by hand). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

1. **Answer:** one or two sentences: the market as scoped (product type, indication if given, jurisdictions), how many lanes hold records, and the one coverage limit that most changes the picture. If a market size was asked: "No source in this skill gives a market size; none is supplied."
2. **Ecosystem map:** Lane · Entry (record as stated) · Source (named in plain words, then the row id or the library tool) · Date. Lanes in order: Buyers, Payers, Peers, Rules. At most four rows per lane in short mode. Buyers the person named carry "from your material"; a lane with nothing is one row "[GAP]: <class>". Payers, DE always carries the DE34 counts row ("BfArM DiGA page, as of 9 September 2026"; whole directory, not the indication); never cut it for length, cut rules rows first. Payers, US puts US7 (G0552 to G0554 payable only for devices classified under 21 CFR 882.5801; Federal Register, 9 December 2024) beside each peer's stored regulation number, as a fact, not a qualification call. Peers give the holder as stored and, where `named-company-status.md` has it, the current FDA listing holder and the company's status from its filings.
3. **Coverage:** one line per lane on what its source cannot see (`market-intelligence-rules.md` section 3, column 4).
4. **Gaps that matter:** at most three, classed per `gap-rules.md`, plus, for peers no row in `named-company-status.md` covers, the status line: "Status: [GAP]: not read for [companies]. The store does not show whether a company was acquired, deregistered, delisted or is in bankruptcy or insolvency; filings to open per company on request (A2)." If the question concerns a device product, one line routing device status to `dh-regulatory-and-quality` regulatory-pathway-and-classification.
5. **Decisions for the person:** which lanes matter, which segment labels to use, which actors to add, and who clears the record (asked directly if not named); nothing chosen for them.
6. **Full version:** one line offering it, before the record block.
7. **Calls made** (before the record block; not counted in the word cap): tool and arguments, one line each.
8. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Market intelligence map draft. Records only; no market size, share or segment choice." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Scope
Product type or segment · Indication (or "not given") · Jurisdictions · Actors from the person's material.
### Perimeters
| Store | Loaded (records) | Not loaded or partial, and why | As of |
|---|---|---|---|
### Buyers
| Buyer (person's words) | Role (user, buyer, payer as typed) | Record check, if any | Source | Date |
|---|---|---|---|---|
### Payers
| Scheme | Listings in store | Posture | What it does not show | Source | Date |
|---|---|---|---|---|---|
### Peers
| Company | Products (as stored) | Authorizations (wording per DL-126 to DL-128) | Studies | Safety records | Evidence maturity (rubric v1) | Source | Retrieved |
|---|---|---|---|---|---|---|---|
### Rules
| Instrument | Date | What it covers (row's words) | Rows | Who decides if it applies |
|---|---|---|---|---|
### Grouping (only if asked)
| Product | WHO classification (second edition) axis and category, "proposed" | Record it rests on | Rows |
|---|---|---|---|
### Company status and current holders
One line per peer covered by `named-company-status.md` (filing, date, what it does not mean; current FDA listing holder apart from the applicant at clearance); one line "Status: [GAP]: not read" for the rest, per `screening-rules.md` section 5.
### Gaps
| Lane | Fact | Class | Next step |
|---|---|---|---|
### Routes
Quality of this map over time: `pipeline-and-market-monitoring` A3 (this pack). Payer coverage: `dh-access-and-value` coverage-pathway-and-access-strategy. Device status: `dh-regulatory-and-quality` regulatory-pathway-and-classification. Positioning: `dh-go-to-market` market-segmentation-and-gtm-strategy.
### Calls made (before the record block)
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
