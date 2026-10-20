# Output format: control, threat model and consent assurance

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/secops_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 70, controls 120, threat model 60, consent 110, record 50.

1. **Answer** (two or three sentences): controls proven as stated, proven (artifact read), unproven and contradicted; open threats by hop and whether the model is dated; consent steps described, broader and missing; withdrawal jobs that still ran. No verdict.
2. **Controls not proven:** Id · Claimed control · Cites · Status · What the clause requires · Gap class (yours, or "not given") · Rows.
3. **Threat model currency:** design version matched, triggers recorded since, open threats by hop.
4. **Consent text versus practice:** Step · Purpose · Result · What it may touch (for your legal owner) · Rows; withdrawal jobs that still ran.
5. **Calls made**, then one line offering the full version.
6. **Record (the very last line, nothing after it):** "Assurance read draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Read date and files read
### Claimed control versus artifact (script output)
| Id | Claimed control | Cites | Artifact | Status | Flags | Rows |
|---|---|---|---|---|---|---|
### Gaps by citation (what the clause requires, what the artifact shows, your gap class)
### Threat coverage by hop and model currency (design version, triggers, who watches)
### Consent text versus practice (script output)
| Step | Purpose | Data class | Recipient | Result | Rules it may touch | Rows |
|---|---|---|---|---|---|---|
### Withdrawal test (script output)
### Proposals (labeled "proposed")
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Assurance read draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
