# Output format: evidence measures

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with a tool (`python3 scripts/maturity_diff.py --count ANSWER.md`, which drops the calls list and source columns), not by estimate. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, the "Full version on request" line. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

1. **Answer:** the record events that count as evidence movement for the person's thesis, the changes that do not count, and the baseline level (confirmed, or "not confirmed"). Two sentences.
2. **Events that count:** table Event · Record that shows it · Rows · Person's or proposed. At most six rows. Every [PAPER] row carries its DOI beside it.
3. **Does not count:** one line each: METHOD, COVERAGE, RESOLUTION changes; an unconfirmed level; a new Form D (DL-117, DOI 10.2196/37677; DL-124, DOI 10.1371/journal.pone.0323390).
4. **Baseline:** framework, level, date, who confirmed it; what to check at each reread (CS56; DL-113, DOI 10.1038/s41746-023-00836-5).
5. **Save at each run (proposed):** full response, exact reference, retrieval date, perimeter, saved safety events and recall flags, company status as read (or "[GAP]: not read").
6. **Triggers:** in the person's words, owner as named (or owner not named), reread date as given (or not given).
7. **Gaps and stops:** a target pace or benchmark is not sourced `[GAP]`.
8. **Full version:** one line offering it, before the record block.
9. **Calls made** (before the record block; not counted in the word cap): usually none.
10. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Evidence measures draft for OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Thesis as stated
### Events that count
| Event | Record that shows it | Clock or rule | Rows | Person's or proposed |
|---|---|---|---|---|
### What does not count
### Framework baseline and what to check at each reread
### Fields to save at each run
### Triggers, owners and reread dates
### Gaps
### Calls made (before the record block)
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
