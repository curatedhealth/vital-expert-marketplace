# Output format: session evidence

Short mode: 450 words maximum, counted without the calls list and tables' source column. Every other table cell counts. Before handing over, count the words of the answer above "Calls made" (for example with `wc -w`) and state nothing over 450. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Use only these sections, in this order. One line per item; no context paragraphs and no explanatory bullets. Tables at most five rows; quotes at most ten words; each row id once. The format fits under 450 words when followed.

1. **Answer** (at most 70 words): sessions held vs planned by group; the stops hit by the most participants, by group; any stop on a flagged critical task; SUS by group with n. If board, investor or regulator wording was asked for: one line declining the claim, then a one-line "draft for the owner" with measured figures, n and round only.
2. **Stops:** Stop · Participants by group · Task · One quote · Critical (yours).
3. **SUS** (if scored): Group or round · n · Mean · Range. Exclusions in one line. One context line: 68 (SD 12.5), UX-M-08; 76.64, UX-M-09 ([PAPER], DOI 10.2196/37290), "context, not a target".
4. **Method flags:** one line: employees, think-aloud, and an employee who is a group's only completer of a critical task.
5. **For the owner:** one line naming the critical-task stops, with no use-error or severity label.
6. **Record:** "Session evidence draft, AI-assisted. Clearer: [name you give, or not named]. The record is built with verify.build_record once that named person clears it; until then this is an uncleared draft."
7. One line offering the full version.

## Full mode

### Answer

### Source
Log file or summary, sessions, dates, as-of.

### Participants per group
| Group | Sessions | Planned (yours) | Note |
|---|---|---|---|

### Outcomes per task
| Task | Critical (your flag) | Completed | Stopped | Assisted | Other labels |
|---|---|---|---|---|---|

### Stops
| Stop | Participants (distinct) | By group | Tasks | Their words |
|---|---|---|---|---|

### Method flags
Employees; think-aloud sessions; training timing (UX-US-41, UX-US-45, UX-US-40).

### SUS
| Group or round | n | Mean | Median | SD | Min | Max |
|---|---|---|---|---|---|---|
Excluded responses and reasons. Context figures with basis (UX-M-08 to UX-M-10, [PAPER], DOI 10.2196/37290). No adjective bands, no pass mark unless yours.

### Saturation note
Whether the last sessions added new stops (PE-09).

### For the owner
Critical-task stops, unlabeled as to use error or severity.

### Gaps

### Record
Session evidence draft. Counts, not conclusions. AI-assisted. Clearer: NAME, or not named. The record is built with verify.build_record once that named person clears it; until then this is an uncleared draft.
