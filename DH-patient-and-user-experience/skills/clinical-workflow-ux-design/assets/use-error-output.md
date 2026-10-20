# Output format: use-error and critical-task analysis

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** critical tasks as the person marked them; any with no control or a training-only control; the one decision needed and whose it is.
2. **Frame:** tasks, populations, market, definition used (FDA UX-US-28, MHRA UX-UK-18), the person's severity scale.
3. **Use errors (compact):** Task · Use error · Harm · Severity (yours) · Critical (yours) · Control · Type (design / protective / information) · Status (in build / designed, not in build / needs data / no control [GAP]).
4. **Prompts from field events (if run):** title, date, class as the record states; the misread it prompts. "Sorting is ours; no inference about that product."
5. **Stops:** open items for the risk owner (named, or "owner not named").
6. **Record:** "Use-error analysis draft. Severity and criticality are yours. Uncleared until a named person clears it through verify.build_record. AI-assisted."
7. One line offering the full version.

## Full mode

### Answer

### Frame
| Item | Value |
|---|---|

### Use errors by task
| Task | Population | Use error (misread or action) | Possible harm | Severity (person) | Critical (person) | Control | Control type (UX-US-33) | Status | Rows |
|---|---|---|---|---|---|---|---|---|---|

### Device failures moved out
Wrong results caused solely by a device fault (UX-US-27, UX-UK-15), for the person's risk file.

### Comparable field events (optional)
| Product (as the record states) | Event date | Class or alert type | What the summary says | Prompt for this design | Source |
|---|---|---|---|---|---|

Calls made: list each with arguments.

### Proposed controls
Labeled "proposed", in FDA's order of preference, with rows.

### Open items and stops
| Item | Why open | Owner (person's words) |
|---|---|---|

### Gaps

### Record
Use-error analysis draft. Not a risk acceptance. AI-assisted. Cleared by NAME through verify.build_record, or "uncleared draft" until a named person clears it.
