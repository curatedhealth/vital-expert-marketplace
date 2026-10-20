# Output format: AI system and harm map

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/subgroup_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 60, system 50, harm and groups 120, rules 130, record 45.

1. **Answer** (two sentences): the decision, the error that harms whom, groups compared and unseen, and the earliest-dated rule in your market with its standing.
2. **The system (your words):** purpose, decision, role (informs, augments, replaces), users, setting, markets. Missing: "not given".
3. **Harm and groups:** Error · Who bears it · Groups compared · Groups unseen ([GAP]: not visible in this data).
4. **Rules that may apply:** Rule · What it asks · Standing and date · Source and rows (source name and date in plain words, row id after; DOI for [PAPER]). Your markets only; drafts labeled; "applies to you: for your legal owner".
5. **Routed out:** device or AI Act status: dh-regulatory-and-quality ai-ml-device-pathway-and-change-control.
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "AI system and harm map draft. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### The system (your words)
### The error that harms, and who bears it
### Groups: compared, unseen, not recorded
| Group | Visible in the data | Compared | Note |
|---|---|---|---|
### Bias sources to look for
| Source of bias | Where it could enter your system | Source and rows |
|---|---|---|
### Events on comparable devices (only if you named them)
| Device | Event as the record states it | Date | Source and rows |
|---|---|---|---|
Excluded (not about these devices): N.
### Rules that may apply, by market and role
| Market | Rule | What it asks | Standing and date | Applies to you | Source and rows |
|---|---|---|---|---|---|
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
AI system and harm map draft. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
