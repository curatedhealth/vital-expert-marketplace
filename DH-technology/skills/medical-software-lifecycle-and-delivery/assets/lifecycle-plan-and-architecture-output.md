# Output format: lifecycle plan and architecture

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/lifecycle_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 70, items 120, plans and documents 100, gaps 60, record 50.

1. **Answer** (two or three sentences): the class as you stated it (or "class: not given"), item and flag counts from the inventory check, document elements missing or in draft, and the biggest open item. No class assigned.
2. **Items with flags:** Id · Item · Origin · Flag in words (for example "end of support 31 March 2026, before your read date") · Source (row).
3. **Plans and documents:** each plan your procedure requires, present, draft or missing, tied to the version; FDA elements missing or in draft at the level you stated (FDA premarket software guidance, PL15).
4. **Gaps:** class definitions not in the sources; any component, flow, region or scale figure not given.
5. **Calls made**, then one line offering the full version.
6. **Record (the very last line, nothing after it):** "Lifecycle plan draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Class and hazards (verbatim from you)
### Software items and SOUP inventory
| Id | Item | Origin | Identity fields (EN-026) | Support level and end of support (EN-054) | Class (yours) | Hazard | Flags |
|---|---|---|---|---|---|---|---|
### Recall records of comparable software (only if run; title, date, class as the record states; no relevance judgment)
### Lifecycle plans (your procedure's list)
| Plan | Document | Version | Present, draft or missing | Product version |
|---|---|---|---|---|
### FDA software documentation elements (level: yours)
| # | Element | Document | Status | Level note | Source (row) |
|---|---|---|---|---|---|
### Architecture: components and data flows (as you named them)
### Device function and other functions (PL24 to PL27)
### Placement, scale and operations
| Workload | Region | Account | Data class | Store | Backup location | Source (row) |
|---|---|---|---|---|---|---|
Scale unit, number, first-failure component (yours or "not given"); health signal, paging rule, runbook or [GAP].
### EU and UK rows (if named)
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Lifecycle plan draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
