# Issue log summary: target WCAG 2.2 Level AA, as of 2026-10-19
Criteria in target: 55. Issues in log: 12.
Open and in target: 7 (4 on day-one tasks).
Open in-target age (days to 2026-10-19): median 34, oldest 160.

## Status (as logged)
- open: 9
- closed: 2
- fixed: 1

## Scope against the target
- in target: 10
- not in WCAG 2.2 (4.1.1 Parsing removed in 2.2; test and report only if a 2.0 or 2.1 policy applies): 1
- above target (Level AAA in WCAG 2.2; target AA): 1

## Open in target by severity (the person's labels)
- blocker: 2 open, median age 93.5 days, oldest 111
- high: 2 open, median age 23.5 days, oldest 34
- medium: 2 open, median age 19.5 days, oldest 21
- low: 1 open, median age 160 days, oldest 160

## Open in target by W3C level
- Level A: 2
- Level AA: 5

## Open in-target issues (day-one first, then oldest)
| id | screen | task | day one | criterion | W3C level | severity (logged) | age days | found by |
|---|---|---|---|---|---|---|---|---|
| A11Y-04 | Medication list | Log a dose | yes | 4.1.2 Name, Role, Value | A | blocker | 111 | assistive_tech |
| A11Y-01 | Sign in | Sign in | yes | 3.3.8 Accessible Authentication (Minimum) | AA | blocker | 76 | manual |
| A11Y-03 | Medication list | Log a dose | yes | 2.5.8 Target Size (Minimum) | AA | high | 34 | manual |
| A11Y-11 | Onboarding | Create account | yes | 3.3.7 Redundant Entry | A | high | 13 | user_research |
| A11Y-07 | Settings | Change reminders | no | 1.4.11 Non-text Contrast | AA | low | 160 | automated |
| A11Y-05 | Symptom diary | Record a symptom | no | 1.3.4 Orientation | AA | medium | 21 | manual |
| A11Y-06 | Symptom diary | Record a symptom | no | 2.5.7 Dragging Movements | AA | medium | 18 | user_research |

## Outside the target (kept, not counted above)
- A11Y-08 4.1.1 Parsing: not in WCAG 2.2 (4.1.1 Parsing removed in 2.2; test and report only if a 2.0 or 2.1 policy applies); status open
- A11Y-10 1.4.6 Contrast (Enhanced): above target (Level AAA in WCAG 2.2; target AA); status open

## How the log was built (found_by)
- manual: 4
- automated: 5
- assistive_tech: 1
- user_research: 2

Criteria in target with no issue logged: 45 (not passes; not tested unless a test record says so).

## Data problems in the log
- A11Y-12: logged level AA but W3C level for 1.1.1 in WCAG 2.2 is A
- A11Y-12: status 'fixed' counted as closed but no valid closed date; whether it is closed is the person's call

## Notes
- Severity is the person's label, counted as logged; the script does not judge it.
- A criterion with no issue logged is not a pass: the log records issues found, not tests run.
- Automated tests check only part of what needs testing (references UX-UK-24, UX-US-78); counts by found_by show how the log was built.
- No conformance statement: WCAG conformance is for full pages and complete processes (UX-STD-21, UX-STD-22) and needs a test record, not an issue log.
