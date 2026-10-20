# Output format: adoption rule and metric sheet

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap and end with the same record line.

## Short mode (default for a direct question)

1. **Answer:** the rule in one sentence: "Adopted = [ROLE] who [TASK EVENT] in production within [W, yours] days of training; reported as [numerator]/[denominator]; your rule is [SHARE, yours]." Blanks stay as "ask".
2. **Definitions used:** one per metric, with its row (for example adoption CS34 or CS28; penetration CS39; maintenance CS26 or CS40). Name the other framework's definition once.
3. **Not adoption:** logins, sessions, attendance (one line).
4. **Data needed:** the log event, the roster, training dates; gaps marked.
5. **Stops:** a rule written into a contract or an NHS commissioning profile (CS61) goes to that document's owner.
6. **Record:** "Adoption rule draft. Window, share and denominator are yours." Then who clears it: "Cleared by NAME; the record is built with `verify.build_record` once NAME clears it", or, with no name, "uncleared draft". AI-assisted.
7. One line offering the full version.

## Full mode

### Answer

### The rule
| Field | Value | Whose |
|---|---|---|
| Task event in production | | task card |
| Level (staff, patients, settings) | | yours |
| Denominator | trained / eligible / settings approached | yours |
| Window after training (days) | | yours |
| Share that counts as met | | yours |
| Maintenance horizon (months) | | yours |
| Old step to watch | | yours |

### Metric sheet
| Metric | Definition | Numerator / denominator | Row |
|---|---|---|---|

### NHS usage profile (if applicable)

### Optional acceptability reading (SUS, context only)

### Gaps

### Calls made

### Record
Adoption rule draft. AI-assisted. Cleared by NAME (as the person named them); the record is built with `verify.build_record` once NAME clears it. With no name: uncleared draft.
