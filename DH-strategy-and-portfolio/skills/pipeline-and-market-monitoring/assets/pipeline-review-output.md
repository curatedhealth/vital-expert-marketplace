# Output format: pipeline review

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words (`scripts/monitor_helpers.py wordcount <answer.md>`, or by hand). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

1. **Answer:** how many pipeline entries meet one of the person's triggers, and which. Two sentences. No recommendation.
2. **Triggers (yours):** numbered, in the person's words.
3. **Entries that need a look:** Company · Status (primary record, or `[GAP]`: not read) · Trigger met (change, event date, source) · Owner (yours) · Routed work (pack and skill) · Reread date (yours).
4. **No trigger met:** names, with the log caveat where the read was "no change recorded".
5. **Not measurable:** names and reason (`gap-rules.md`).
6. **Decision for the person:** the one call they need to make.
7. **Full version:** one line offering it, before the record block.
8. **Calls made** (before the record block; not counted in the word cap): tool and arguments, one line each.
9. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Pipeline review draft on your triggers. Not investment advice." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Triggers (yours)
| No. | Trigger, in your words | Record type it reads | Source loaded? |
|---|---|---|---|
### Entries
| Company | Stage (yours) | Status (primary record, or [GAP]: not read) | Trigger | Result (met, not met, not measurable) | Fact, date, source | Owner (yours) | Reread date (yours) |
|---|---|---|---|---|---|---|---|
### Routed work
| Company | Work | Route (pack and skill) |
|---|---|---|
### Rerun at the reread date
### Gaps
### Calls made (before the record block)
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
