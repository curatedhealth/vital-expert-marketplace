# Output format: objectives, benefits and roadmap

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/execution_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 60, objectives 70, benefits 100, milestones 80, rules and cadence 40, optimism bias (only if asked) 40, missing 25, record 45.

1. **Answer** (two sentences): counts of objectives, benefits, milestones and tests in the plan; how many have a pass rule written before scoring; what is missing most.
2. **Objectives:** each verbatim with SMART elements present or "not given" (HM Treasury Green Book, 5 February 2026, SP-092; UK public-sector guidance).
3. **Benefits register:** Id · Benefit · Objective · Owner · Baseline · Target · Measure · Your rule. Only rows tied to the question.
4. **Milestones:** Id · Milestone · Owner · Due · Depends on · Your rule elements; dependency problems one line each. If you gave none: the milestones your strategy lines imply, each labeled "proposed", with owner, due date, evidence and rule "not given".
5. **Cadence and rules:** your forum, cadence and reread dates; "not given" where missing; the UK 12-month review convention only as context (UK Benefits Measurement Guidance Note, May 2021, SP-105).
6. **Optimism bias** (only if asked): the bounds for the project type you name, the method and the guidance's age (HM Treasury optimism bias supplementary guidance, 2003, Table 1, SP-172, SP-173, SP-175, SP-170); "the uplift you apply is yours".
7. **Still missing before the first read:** flags from `scripts/execution_check.py`, one line each.
8. **Calls made**, then one line offering the full version.
9. **Record (the very last line, nothing after it):** "Execution plan draft. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Objectives
| Objective (your words) | Strategy line | Specific | Measurable | Achievable | Realistic | Time-limited |
|---|---|---|---|---|---|---|
### Benefits register (columns follow SP-104, UK public-sector guidance)
| Id | Benefit | Objective | Owner | Measure | Direction | Baseline (date) | Target (date) | Your rule | Reread date | Source |
|---|---|---|---|---|---|---|---|---|---|---|
### Milestones and dependencies
| Id | Milestone (yours, or proposed) | Objective | Owner | Due | Evidence of completion | Depends on | Your rule elements | Recheck date |
|---|---|---|---|---|---|---|---|---|
### Option tests still running
| Id | Option | Question | Endpoint | Success criterion | Decision rule (date written) |
|---|---|---|---|---|---|
### Optimism bias bounds you asked about (UK public-sector guidance; the uplift applied is yours)
| Project type (yours) | Upper bounds, duration and capital expenditure | Lower bounds | Method and age | Source and rows |
|---|---|---|---|---|
### Governance cadence (yours)
### Flags still open
### Calls made
### One line offering anything not shown
### Record (the very last line)
Execution plan draft. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
