# Output format: cadence, outcome and governance read

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/adoption_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build lines 2 to 5 from `scripts/adoption_check.py` output; do not recount by hand. Budget in words: answer 70, cadence 70, outcome 90, agreement 60, governance 70, record 45.

1. **Answer** (two sentences): the cadence flags that matter, the bet metric difference with comparison type and flags, agreement and the share of variations with a reason, and the governance flags. No verdict, no causal claim.
2. **Cadence:** issue · due · sent · data timestamp · flags (C1 to C7).
3. **Bet metric:** group · window · users · units · rate; difference "arithmetic on your file, not evidence that the product caused it"; flags O1 to O5; adoption beside it (Proctor 2011, CS32, DOI 10.1007/s10488-010-0319-7).
4. **Agreement:** agreed · varied · not recorded (denominators); reasons as recorded (DECIDE-AI, DA-82, DOI 10.1136/bmj-2022-070904); "high agreement is not accuracy".
5. **Governance:** metric or publisher · flags (G1 to G4, P1 to P3); facts beside them for the market in the request.
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Cadence, outcome and governance read draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Read date, window and the bet as funded
### Issue cadence
| Issue | Period end | Due | Sent | Data timestamp | Status | Flags |
|---|---|---|---|---|---|---|
### Bet metric against its comparison
| Group | Metric | Window | Users | Units | Outcome count | Rate |
|---|---|---|---|---|---|---|
### Adoption beside the outcome (from A1)
### User agreement and reasons for variation
| Reason (as recorded) | Cases |
|---|---|
### Timestamps on the clinical step against your stale rule
### Certification status
| Metric | Status | Version certified, current | Formula changed | Dashboards | Flags |
|---|---|---|---|---|---|
### Publish rights
| Publisher | Role at grant | Role now | Last reviewed | Flags |
|---|---|---|---|---|
### Ongoing duties for the owner you name (market in the request)
| Duty | Source and date | Rows | Status |
|---|---|---|---|
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Cadence, outcome and governance read draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
