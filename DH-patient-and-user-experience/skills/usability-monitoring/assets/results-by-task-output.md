# Output format: usability results by task

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** critical tasks with use errors ("k of n"), the person's severity, and any validation condition not met.
2. **Frame:** build tested, test kind, dates, user groups, success label.
3. **By task (compact):** Task · Critical (yours) · Participants · Use errors k of n · Returned to old step · Severity as assigned.
4. **Test conditions:** met / not met / not stated, each with its row (validation only).
5. **SUS (if collected):** mean and SD per group; benchmarks labeled context and as one published meta-analysis, Hyzy et al. 2022 [PAPER] (UX-M-08, UX-M-09).
6. **Flags:** rows without severity, employees, think-aloud.
7. **Open questions (at most three).**
8. **Record:** "Results summary on your log. Counts only; no verdict. Uncleared until a named person clears it through verify.build_record. AI-assisted."
9. One line offering the full version.

## Full mode

### Answer

### Frame
| Item | Value |
|---|---|

### Results by task
| Task | Critical (person) | Participants | Outcomes (person's codes) | Use errors | Returned to old step | Severity as assigned |
|---|---|---|---|---|---|---|

### Non-success rows by severity (as assigned)
| Severity | Task | Participant | Group | Outcome | Note |
|---|---|---|---|---|---|

### Participants by group
| Group | Participants | Person's minimum, if set |
|---|---|---|

### Test conditions
| Condition | Status | Evidence | Row |
|---|---|---|---|

### SUS
| Group | n | Mean | SD | Min | Max |
|---|---|---|---|---|---|
Context, not targets: general mean 68 (SD 12.5) (UX-M-08); digital health apps 76.64 (SD 15.12), 68.05 (SD 14.05) excluding physical-activity apps (UX-M-09). Source check if run: calls and status.

### Findings
| # | Task | Finding (fact) | Count | Row |
|---|---|---|---|---|

### Gaps

### Record
Results summary. No statement that the product is usable, validated or safe. AI-assisted. Cleared by NAME through verify.build_record, or "uncleared draft" until a named person clears it.
