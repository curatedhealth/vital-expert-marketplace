# Output format: launch measures

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** the measures against your thresholds (met, missed, not measured, no threshold), period and as-of date in one line.
2. **Measures:** table ID · Measure · Value · Your rule · Result.
3. **Unapproved claim uses:** date, rep id, account, claim id; or "none recorded" or "not measured".
4. **Briefing status:** people not briefed, with the reason (past your due date, no due date), kept apart from meeting outcomes.
5. **Gaps:** at most three lines.
6. **Record:** "Computed from your records (FILES, PERIOD). Thresholds are yours." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer

### Measure sheet (yours)
| ID | Label | Metric | Record | Period | Comparison | Threshold | Owner |
|---|---|---|---|---|---|---|---|

### Results
| ID | Value | Basis (records, denominator, as-of) | Result |
|---|---|---|---|

### Claim use
| Claim id | Uses | On approved list |
|---|---|---|

### Roster
| Role | Person (id) | Briefer | Due (yours) | Status |
|---|---|---|---|---|

### Meetings by person
| Person (id) | Held | Cancelled or no-show |
|---|---|---|

### Column mapping from your export

### What touches a rule
Unapproved claim uses and recorded free items, with rows; stops for B1.

### Gaps

### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
