# Output format: release controls and acceptance

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/subgroup_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 70, rule 40, groups 110, acceptance 60, controls 100, decisions 40, record 45.

1. **Answer** (two sentences): groups meeting and not meeting your rule with counts, the computed change for each miss, misses with an acceptor and written reason, and the missing control that most limits the record. No release call.
2. **Your rule:** verbatim, with the date written. None: "blocking rule not given [GAP]".
3. **Against your rule:** Group · Value (count) · Reference · Met or not · Change that would meet it (computed, not a target).
4. **Acceptance:** Group · Acceptor (yours, or owner not named) · Written reason · Release waits (yours, or not given).
5. **Controls:** Control · Present, missing, not given · Standing and date · Source and rows. Your markets only.
6. **For you to decide:** each with its facts.
7. **Calls made** (script command), then one line offering the full version.
8. **Record (the very last line, nothing after it):** "Release control draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Your blocking rule (verbatim, date written)
### Results against your rule
| Group | Value (count) | Reference | Gap on the harmful side | Met, not met, not measurable | Change that would meet it (computed) |
|---|---|---|---|---|---|
### Acceptance of differences
| Group | Acceptor | Written reason required | Release waits | Duty placed beside it (for your legal owner) | Source and rows |
|---|---|---|---|---|---|
### Controls that go with the release
| Area | Control | Present, missing, not given | Standing and date | Source and rows |
|---|---|---|---|---|
### Monitoring after release (yours: measure, owner, frequency, trigger)
### For you to decide
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Release control draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
