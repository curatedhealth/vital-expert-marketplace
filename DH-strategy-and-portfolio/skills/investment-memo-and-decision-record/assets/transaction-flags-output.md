# Output format: transaction and data flags

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/memo_facts.py words ANSWER.md` (counts the body above the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

Build the table from `scripts/memo_facts.py flags` output. Budget in words: answer 70, flags table 200, missing facts 60, owner decisions 50, record 50.

1. **Answer** (two sentences): which regimes the person's facts sit at or above a sourced figure in, which facts are missing. A share figure the person gives is shown beside the condition in the table only; the answer paragraph does not say it is under or over a threshold while competitor status or the market is "not given". Every conclusion is for the owner the person names for legal or compliance (or owner not named). Never "clear".
2. **Flags:** Regime · Your fact · Sourced figure or rule (instrument, date) · Rows · How your fact sits. Moved or pending rules (HSR form, EU 2026/1386, Swiss IPG) sit in this table only where they touch the deal. If the deal includes a license, add rows with Regime "Licensing (EU TTBER 2026/877)", "Licensing (DOJ/FTC 2017 guidelines)" and, for a registrant, "Licensing (SEC disclosure)": the person's share or term as they state it beside the condition, never "exempt" or "inside the safety zone". If the rights licensed include data, add a row "Health data (GDPR)": the person's fact (for example "training data licensed") beside DL-099 (data concerning health), DL-101 (inference) (Article 9(1) prohibition unless a 9(2) ground) and DL-105 (member-state add-ons); whether the data is health data is for the owner. Echo the technology pool fact, true or false, beside SP-140.
3. **Missing facts:** each "not given", with the question to ask.
4. **For the owner to decide:** the conclusions, each with its rows. Not answered here.
4a. **Memo line (draft for the owner):** one sentence the memo can carry, stating which conclusions are not established and which rows the owner must read, with no conclusion. For example: "Whether the license falls under Regulation (EU) 2026/877 or the DOJ/FTC safety zone is not established: competitor status, the relevant markets and the shares are for [owner] to fix (SP-136, SP-139, SP-144); the data rights need a GDPR Article 9 review (DL-099, DL-101 (inference))."
5. **Full version:** one line offering it, before the record block.
6. **Calls made** (before the record block; not counted in the word cap): each call with its arguments.
7. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Transaction and data flags draft for the owner. Not legal advice. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Your deal facts (verbatim, numbered; "not given" listed)
### US premerger notification
| Your fact | Figure | Instrument and date | Rows | How it sits |
|---|---|---|---|---|
### CFIUS
| Your fact | Rule | Rows | How it sits |
|---|---|---|---|
### DOJ bulk sensitive data
| Your fact | Threshold or rule | Rows | How it sits |
|---|---|---|---|
### EU and Swiss screening
| Your fact | Regime on your closing date | Rows | Note |
|---|---|---|---|
### Licensing (only if the deal includes a license; flagged for the owner the person names for legal or competition questions)
| Your fact (as you state it) | Rule or condition | Instrument and date | Rows | How your fact sits |
|---|---|---|---|---|
Rows to cover: 316/2014 expired 30 April 2026 (SP-134); 2026/877 from 1 May 2026 to 30 April 2038 (SP-135); 20% combined for competitors, 30% each for non-competitors, on any relevant market (SP-136); transition to 30 April 2027 for agreements in force on 30 April 2026 (SP-137); SPCs, hardcore research and development restriction, pools, 2026 Guidelines, data licensing (SP-138 to SP-142); DOJ/FTC principles, 20% safety zone, four-entity research and development test, outside the zone not presumed unlawful (SP-143 to SP-147); exhibits, redaction and 8-K Item 1.01 for a registrant (SP-130 to SP-133, DL-019 to DL-021). Whether the parties compete, the market definition and the shares are the owner's; the skill supplies none.
### Health data and breach records
| What to ask the target or check | Rows |
|---|---|
### Researcher's readings used (rows marked "(inference)")
### Not sourced (`[GAP]`)
### For the owner to decide
### Record
Transaction and data flags draft for the owner. Not legal advice. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
