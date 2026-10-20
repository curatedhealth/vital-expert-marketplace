# Output format: study plan

Short mode: 450 words maximum, counted without the calls list and tables' source column. Every other table cell counts. Before handing over, count the words of the answer above "Calls made" (for example with `wc -w`) and state nothing over 450. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Use only these sections, in this order. One line per item; no context paragraphs and no explanatory bullets. Tables at most five rows; quotes at most ten words; each row id once. The format fits under 450 words when followed.

1. **Answer** (at most 70 words): the decision the study serves, "formative user research" (or, if the request is validation, the boundary line naming `dh-regulatory-and-quality`), groups with the numbers the person set, and the one open point that blocks the plan.
2. **Participants:** Group · Number (yours, or "not set") · One note with its row id. One row per group.
3. **Methods and tasks:** one line, with session mode (in person, remote, unmoderated). Critical tasks only as the owner flagged them, otherwise "not flagged". Remote consent and recording rules: `[GAP]` unless a row covers them.
4. **Similar-product events** (only if the library was called): one line, what the records state, with title, date and class.
5. **Ethics screen:** at most three one-line facts with row ids, then "Determination: your IRB, ethics committee or named reviewer".
6. **Open questions:** at most two, one line each.
7. **Record:** "Study plan draft, AI-assisted. Clearer: [name you give, or not named]. The record is built with verify.build_record once that named person clears it; until then this is an uncleared draft."
8. One line offering the full version.

## Full mode

### Answer

### Decision and question
| Item | Value |
|---|---|
| Decision the study serves | |
| Research question | |
| Participant and task | |
| What this study will not answer | |
| Kind of work | Formative user research (UX-US-29, UXR-03) |

### User groups and numbers
| Group | Number (yours) | Rationale (yours) | Context rows |
|---|---|---|---|

### Protocol elements (UXR-02)
| Element | Content |
|---|---|
| Purpose, goals and priorities | |
| Portion of the UI (incl. labeling, training material) | |
| Scenarios and tasks | |
| Participants | |
| Data collection methods | |
| Data analysis methods | |
| How results will be used | |

### Known problems with similar products (if the library was used)
| Record (title, date, class) | What its summary states | Proposed scenario |
|---|---|---|

### Ethics screen
| Question | Fact | Row |
|---|---|---|
Determination: your IRB, ethics committee or named reviewer.

### Data handling
Pseudonymous codes only; recordings stay with your research operations.

### Validation boundary
What would be needed if this were validation (UX-US-34 to UX-US-41), as a draft for your regulatory or human factors owner, only if asked.

### Gaps

### Calls made

### Record
Study plan draft. No claim of usability, safety or validation. AI-assisted. Clearer: NAME, or not named. The record is built with verify.build_record once that named person clears it; until then this is an uncleared draft.
