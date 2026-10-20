# Output format: session record and coverage

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap and end with the same record line.

## Short mode (default for a direct question)

1. **Answer:** coverage per site and role in one table, every rate with numerator and denominator: in role, attended, completed once, attended not completed, not recorded, not attended.
2. **Trainers and champions:** designated per site, and whether each completed the task once (by id, not name).
3. **Who was missed:** by role and site.
4. **Against your rule:** met or missed only if you set a share; otherwise "no rule set".
5. **Gaps:** roster, task card, completion not recorded.
6. **Record:** "Session record draft on your data. Roles and ids only." Then who clears it: "Cleared by NAME; the record is built with `verify.build_record` once NAME clears it", or, with no name, "uncleared draft". AI-assisted.
7. One line offering the full version.

## Full mode

### Answer

### Coverage
| Site / role | In role | Attended | Completed once | Attended, not completed | Not recorded | Not attended | Trainers |
|---|---|---|---|---|---|---|---|
Attendance is not completion. "Not recorded" is not counted as done.

### Trainers and champions (CS45, CS46)
| Site | Designated id | Completed the task once |
|---|---|---|

### Data checks

### What it means for you

### Gaps

### Record
Session record draft. AI-assisted. Cleared by NAME (as the person named them); the record is built with `verify.build_record` once NAME clears it. With no name: uncleared draft.
