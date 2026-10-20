# Issue log summary: target WCAG 2.1 Level AA, as of 2026-10-19
Criteria in target: 50. Issues in log: 12.
Open and in target: 4 (1 on day-one tasks).
Open in-target age (days to 2026-10-19): median 135.5, oldest 230.

## Status (as logged)
- open: 9
- closed: 2
- fixed: 1

## Scope against the target
- not in WCAG 2.1 (first appears in WCAG 2.2): 5
- in target: 6
- above target (Level AAA in WCAG 2.1; target AA): 1

## Open in target by severity (the person's labels)
- blocker: 1 open, median age 111 days, oldest 111
- medium: 1 open, median age 21 days, oldest 21
- low: 2 open, median age 195.0 days, oldest 230

## Open in target by W3C level
- Level A: 2
- Level AA: 2

## Open in-target issues (day-one first, then oldest)
| id | screen | task | day one | criterion | W3C level | severity (logged) | age days | found by |
|---|---|---|---|---|---|---|---|---|
| A11Y-04 | Medication list | Log a dose | yes | 4.1.2 Name, Role, Value | A | blocker | 111 | assistive_tech |
| A11Y-08 | Settings | Change reminders | no | 4.1.1 Parsing | A | low | 230 | automated |
| A11Y-07 | Settings | Change reminders | no | 1.4.11 Non-text Contrast | AA | low | 160 | automated |
| A11Y-05 | Symptom diary | Record a symptom | no | 1.3.4 Orientation | AA | medium | 21 | manual |

## Outside the target (kept, not counted above)
- A11Y-01 3.3.8 Accessible Authentication (Minimum): not in WCAG 2.1 (first appears in WCAG 2.2); status open
- A11Y-03 2.5.8 Target Size (Minimum): not in WCAG 2.1 (first appears in WCAG 2.2); status open
- A11Y-06 2.5.7 Dragging Movements: not in WCAG 2.1 (first appears in WCAG 2.2); status open
- A11Y-09 3.2.6 Consistent Help: not in WCAG 2.1 (first appears in WCAG 2.2); status closed
- A11Y-10 1.4.6 Contrast (Enhanced): above target (Level AAA in WCAG 2.1; target AA); status open
- A11Y-11 3.3.7 Redundant Entry: not in WCAG 2.1 (first appears in WCAG 2.2); status open

## How the log was built (found_by)
- manual: 4
- automated: 5
- assistive_tech: 1
- user_research: 2

Criteria in target with no issue logged: 44 (not passes; not tested unless a test record says so).

## Data problems in the log
- A11Y-12: logged level AA but W3C level for 1.1.1 in WCAG 2.1 is A
- A11Y-12: status 'fixed' counted as closed but no valid closed date; whether it is closed is the person's call

## Notes
- Severity is the person's label, counted as logged; the script does not judge it.
- A criterion with no issue logged is not a pass: the log records issues found, not tests run.
- Automated tests check only part of what needs testing (references UX-UK-24, UX-US-78); counts by found_by show how the log was built.
- No conformance statement: WCAG conformance is for full pages and complete processes (UX-STD-21, UX-STD-22) and needs a test record, not an issue log.
