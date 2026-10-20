# Output format: release and change decision

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/lifecycle_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 70, re-opened items 100, problems 80, regulatory questions 100, decisions 50, record 50.

1. **Answer** (two or three sentences): what the change re-opens, problems open on hazardous functions, which regulatory questions are open and for whom, the decisions you face. No go or no-go; no submission answer.
2. **Re-opened by this change:** Item · Why (rule) · Source (row).
3. **Problems:** Id · Effect · Status · Change or accepted by · Flags.
4. **Regulatory questions (for the regulatory owner):** Question · Your fact · Source (row).
5. **For you to decide:** go or no-go; who accepts each open item; submission or notification with the regulatory owner; decision date ("not given" until set).
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Release decision draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Baseline (most recently cleared or certified version, as the record states it)
### What this change re-opens
| Item | Why | Your scope | Source (row) |
|---|---|---|---|
### Problem resolution records
### Regulatory questions laid out (US software change guidance; 524B; PCCP; EU legacy devices)
| Question | Your fact | What the answer depends on | For | Source (row) |
|---|---|---|---|---|
### Release decision pack
### For you to decide
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Release decision draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
