# Output format: mapping, workflow and standards read

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/integration_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 70, map 110, workflow 110, standards 80, record 50.

1. **Answer** (two or three sentences): exact-match and unmatched rates with numerator, denominator and your definition, against your threshold or "not given"; disagreements and reviewer flags; workarounds per step; the standards item that most affects the integration; read date (yours, or "not given").
2. **Map:** Rate · Numerator / denominator · Your threshold · Met, not met, or not given; then disagreement rows and flags R1 to R4.
3. **Step:** Step · Designed action · Done · Skipped · Replaced; workarounds quoted with observation id; time range with n (W1 where n is one).
4. **Standards:** Fact · Date or status as read · Rows (only items the integration relies on).
5. **Calls made**, then one line offering the full version.
6. **Record (the very last line, nothing after it):** "Integration read draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Map sample (size, draw method, rate definitions and threshold, yours)
### Map rates and review
| Rate | Numerator / denominator | Your threshold | Result |
|---|---|---|---|
### Disagreements, reviewer flags and error classes by map version (Kahn categories, DOI at first use)
### Workflow: designed versus observed
| Step | Designed action | Done | Skipped | Replaced |
|---|---|---|---|---|
### Workarounds (verbatim) and time ranges with n
### Standards currency read (as read on 19 and 20 October 2026)
| Fact | Date or status as read | Rows |
|---|---|---|
### Proposals, not rules
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Integration read draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
