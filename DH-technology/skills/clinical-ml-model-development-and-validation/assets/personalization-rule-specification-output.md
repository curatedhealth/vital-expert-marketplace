# Output format: personalization rule specification

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/model_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build line 3 from `scripts/model_check.py rules` output; do not recount by hand. Budget in words: answer 60, distal outcome 30, rule table 150, bounds 60, tests 60, record 45.

1. **Answer** (two sentences): decision points, flag count and the flags that matter most, bounds not given, test design per rule or "not given".
2. **Distal outcome and decision points:** yours, verbatim.
3. **Rule table (script output):** Decision point · Tailoring variables · Options allowed · On missing data · Proximal outcome · Flags.
4. **Bounds you set:** options never delivered, maximum frequency or dose, who may change a rule; "not given" where missing; feedback-loop duty if the engine learns (EU AI Act Article 15(4), DA-63; applies from 2 August 2028 for Annex I devices, DA-67).
5. **How each rule is tested:** micro-randomized trial or MOST (yours); deployed-log comparisons are descriptive (TM90).
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Personalization specification draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Distal outcome (TM83) and decision points (TM78), your words
### Rule table (yours, as written)
| Decision point | Tailoring variables (active or passive) | Measurement validity | Options allowed | Rule | On missing data | Proximal outcome | Engagement or fatigue outcome |
|---|---|---|---|---|---|---|---|
### Specification flags (script output; gaps, not a safety verdict)
| Flag | Decision point | What is missing | Rows (DOI for [PAPER]) |
|---|---|---|---|
### Bounds you set
### If the engine keeps learning (EU AI Act Articles 10(2)(f) and 15(4); PCCP principle 1, US-31)
### Test design per rule (MRT, TM90; MOST, TM66 to TM76)
| Rule | Design (yours) | Proximal outcome | Optimization objective (yours) | Rows |
|---|---|---|---|---|
### Change control route (`dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control)
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Personalization specification draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
