# Output format: call and selection hold-up read

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/foresight_check.py --words ANSWER.md` (counts the whole answer except the calls list, and leaves out the Source, Rows, Retrieved and Evidence columns); without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build counts from `scripts/foresight_check.py` output; do not recount by hand. Budget in words: answer 70, table 200, limits 60, decisions 30, record 50. Every fact names its source in plain words with its date, then the row id ("FDA 510(k) K261317, decided 14 May 2026"; "Pear 8-K, filed 7 April 2023 (SP-156) [WF]"); never a row id alone.

1. **Answer** (two or three sentences): per kind (call, selection), how many hit, missed, are open or cannot be resolved by your rules; the proposed outcomes awaiting your confirmation; the limit that most affects the read.
2. **Table:** Id · Call or selection · Your rule · Record now (identifier, date) · Outcome (yours, or proposed by your rule) · Flags.
3. **Limits:** change log began 12 October 2026 (R5); not measurable from the record; horizons not reached.
4. **Company status** for each selection that rests on a company: the status already read (`references/company-status.md` section 6) cited by filing or register name and date, or "Status: [GAP]: not read" with the newest stored filings named as the first to open. A product's current FDA listing holder is stated apart from the company that was authorized. Where a rule has two parts, each part is read on its own record.
5. **For you to confirm:** the proposed outcomes.
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line):** "Hold-up read draft for the owner. Outcomes by your rules; no benchmark. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Calls
| Id | Call (as made, date) | Horizon | Your resolution rule | Record now | Retrieved | Outcome (yours or proposed) | Evidence |
|---|---|---|---|---|---|---|---|
### Selections
| Id | Selection (as made, date) | Your hold-up rule | Record now | Retrieved | Outcome (yours or proposed) | Evidence |
|---|---|---|---|---|---|---|
### Not measurable from the record (needs your data)
### Counts by your recorded outcomes (script output)
| Kind | Hit | Miss | Open | Void | Not recorded |
|---|---|---|---|---|---|
Hit share with its denominator; no accuracy benchmark exists in the sources.
### Company status (selections resting on a company)
| Company | Status (filing or register, date, row) | What it does not mean | Current FDA listing holder of the product, if different |
|---|---|---|---|
### Gaps
### Calls made
### Record (the very last line)
Hold-up read draft for the owner. Outcomes by your rules; no benchmark. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
