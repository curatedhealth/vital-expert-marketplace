# Output format: release evidence read

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/evidence_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 70, read 30, items 170, unseen groups 40, events 50, record 45.

1. **Answer** (two sentences): counts by status (present, missing, not yet applicable, not assessable); the missing and not-assessable items by name; groups still unseen; the flag that most limits the read. No "compliant" or "ready".
2. **Read (yours):** release model version, read date, index file. Missing: "not given".
3. **Items not present:** Item · Status · Why (flag in words) · Evidence record id and date · Source and rows.
4. **Not yet applicable:** item and the date it applies, with the instrument.
5. **Groups not seen at test time, still not tested:** one line each.
6. **Since release** (only for a device you named): events as the records state them, with the excluded count.
7. **Calls made** (script command and library calls), then one line offering the full version.
8. **Record (the very last line, nothing after it):** "Release evidence read draft. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Read (yours)
### Every item
| Item | Requirement | Status | Evidence record id | Evidence date | Flags | Source and rows |
|---|---|---|---|---|---|---|
### Groups not seen at test time
### Post-release events (device you named)
| Device | Event as the record states it | Date | Source and rows |
|---|---|---|---|
Returned, not about these devices: N. MAUDE counts: reports, not confirmed events.
### What the read cannot show
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Release evidence read draft. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
