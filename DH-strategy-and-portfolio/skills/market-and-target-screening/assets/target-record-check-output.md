# Output format: target record check

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words (`scripts/screen_helpers.py wordcount <answer.md>`, or by hand). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

1. **Answer:** whether the store holds the company and under which name, and which of the statements the registers cannot carry. Two sentences.
2. **Status:** one line from a primary filing or register entry (form or item, date, source, read date, and what it does not mean), or "Status: [GAP]: not read. Filings to open: ...". Never from press or memory.
3. **Statements checked:** Statement (as given, and where from) · Register · Can show (row) · Cannot show (row) · On record (fact, date, source) · Statement status.
4. **Next checks:** at most three registers to search at the authority, with the identifier to use.
5. **Gaps and stops:** device status or pathway questions routed to `dh-regulatory-and-quality` regulatory-pathway-and-classification.
6. **Full version:** one line offering it, before the record block.
7. **Calls made** (before the record block; not counted in the word cap): tool and arguments, one line each.
8. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Record check draft. Facts from your material are labeled." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Identity in the store
| Name used | Resolved as | Products | Authorizations | Studies | Evidence maturity (points, rubric v1) | Retrieved |
|---|---|---|---|---|---|---|
### Statements checked
| Statement | Source of statement (public, the company, your material) | Register | Can show (row) | Cannot show (row) | On record | Statement status |
|---|---|---|---|---|---|---|
### Company status
| Record | Identifier | Read? | What it states (form or item, date, source, read date) | What it does not mean (row) |
|---|---|---|---|---|
### Registers not loaded in the store
| Register | Why not loaded | Where to check | Identifier |
|---|---|---|---|
### Gaps
| Fact | Class | Next step |
|---|---|---|
### Calls made (before the record block)
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
