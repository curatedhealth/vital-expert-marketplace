# Output format: screen and rule movement

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words (`scripts/monitor_helpers.py wordcount <answer.md>`, or by hand). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

1. **Answer:** whether the screen, the perimeter or the rules moved since DATE, in one or two sentences.
2. **Screen:** "Same arguments: yes or no." Then Company · Change · Earlier · Later (or "runs not comparable").
3. **Perimeter:** sources newly loaded or dropped, labeled "new coverage, not a market change".
4. **Rules after DATE:** Date · Change · Instrument · Rows · Status. "For the owner you name for legal questions; not applied to any deal here."
5. **Hypotheses for review:** at most three, each tied to one of the person's triggers.
6. **Full version:** one line offering it, before the record block.
7. **Calls made** (before the record block; not counted in the word cap): tool and arguments, one line each.
8. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Movement read draft." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Perimeter then and now
| Source | Earlier | Now | Note |
|---|---|---|---|
### Screen rerun
Arguments earlier · Arguments now · Same: yes or no · total_matches earlier and now
| Company | Change | Earlier | Later |
|---|---|---|---|
### Evidence maturity movement
| Company | Input that changed | Earlier | Later | Rubric |
|---|---|---|---|---|
### Rule and register changes after DATE
| Date | Change | Instrument | Rows | Status |
|---|---|---|---|---|
### Hypotheses for review
### Gaps
### Calls made (before the record block)
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
