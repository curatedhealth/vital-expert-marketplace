# Output format: study quality check

Short mode: 450 words maximum, counted without the calls list and tables' source column. Every other table cell counts. Before handing over, count the words of the answer above "Calls made" (for example with `wc -w`) and state nothing over 450. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Use only these sections, in this order. One line per item; no context paragraphs and no explanatory bullets. Tables at most five rows; quotes at most ten words; each row id once. The format fits under 450 words when followed.

1. **Answer** (at most 70 words): whether the method and sample support the claim. If the claim is validation, safety or "easy to use", the stop line comes first and names `dh-regulatory-and-quality`.
2. **Sample fit:** Group · Planned · Held · Note (wrong-role sessions, employees, an employee who is a group's only completer of a critical task). One row per group.
3. **Method fit:** at most three lines, one per claim checked, each with its row ids.
4. **Protocol and reporting:** one line listing absent UXR-02 elements and unreported GRIPP2 short-form items (if patients were partners).
5. **Open questions:** at most two, one line each.
6. **Record:** "Study check draft, AI-assisted. Clearer: [name you give, or not named]. The record is built with verify.build_record once that named person clears it; until then this is an uncleared draft."
7. One line offering the full version.

## Full mode

### Answer

### Frame
| Item | Value |
|---|---|
| Study | |
| Claim checked | |
| Criteria in scope | |

### Sample fit
| Criterion | Evidence | Row |
|---|---|---|

### Findings and the sessions behind them
| Finding | Role named in the question | Sessions behind it (by group) | Wrong-role sessions | Still stands |
|---|---|---|---|---|

### Method fit
| Claim | Method used | Rows | Supported / not supported / stops for the owner |
|---|---|---|---|

### Protocol elements (UXR-02)
| Element | Present / partial / absent | Where |
|---|---|---|

### GRIPP2 short form (if patients were partners)
| Item | Reported / not reported | Where |
|---|---|---|
No total; a reporting checklist, not a score.

### Ethics record
Determination on file: yes / no; by whom.

### Gaps

### Calls made

### Record
Study check draft. Not a grade. No statement that research suffices for validation or that the product is usable. AI-assisted. Clearer: NAME, or not named. The record is built with verify.build_record once that named person clears it; until then this is an uncleared draft.
