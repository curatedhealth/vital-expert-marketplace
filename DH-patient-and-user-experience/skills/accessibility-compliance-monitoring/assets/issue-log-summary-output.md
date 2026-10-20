# Output format: issue log summary and age

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question; 250 to 450 words)

1. **Answer:** open in-target issues, how many on day-one tasks, the oldest open age to the as-of date, and the biggest difference the target makes (issues outside it).
2. **Frame:** target, as-of date, issues in the log, day-one definition.
3. **Open in target (compact):** by your severity labels (count, median and oldest age) and by W3C level.
4. **Day-one issues:** id, criterion and level, age.
5. **Outside the target:** id, criterion, reason.
6. **How the log was built:** counts by method; the automated-coverage note if scans dominate; "a criterion with no issue logged is not a pass".
7. **Data problems:** listed, not corrected.
8. **Record:** "Log summary draft on your data. Severity and status are yours. Not a conformance statement. AI-assisted. To be cleared by NAME; the record is built with verify.build_record once NAME clears it." Until a named person clears it: "Uncleared draft." Who clears it: the owner the person named, in their words, or "owner not named". The record is built with `verify.build_record` once that named person clears it; until then the line reads "uncleared draft".
9. One line offering the full version.

## Full mode

### Answer

### Frame
| Item | Value |
|---|---|

### Open in target
| Severity (your label) | Open | Median age (days) | Oldest (days) |
|---|---|---|---|

| W3C level | Open |
|---|---|

### Open in-target issues (day-one first, then oldest)
| id | Screen | Task | Day one | Criterion | Level | Severity (yours) | Age (days) | Found by |
|---|---|---|---|---|---|---|---|---|

### Outside the target
| id | Criterion | Reason | Other obligation that names it |
|---|---|---|---|

### How the log was built

### Data problems

### Calls and script run
Command, version of the criteria table, as-of date.

### Record
Draft. No issue closed by the model; no conformance statement. AI-assisted. Names who clears it (the owner the person named, or "owner not named"); the record is built with `verify.build_record` once that named person clears it. Until then: "Uncleared draft."
