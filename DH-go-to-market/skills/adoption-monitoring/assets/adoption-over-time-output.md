# Output format: adoption and penetration over time

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap and end with the same record line.

## Short mode (default for a direct question)

1. **Answer:** for each site (or role), the latest period: adoption (adopted/trained), penetration (active/eligible), old-step users (and how many of them also did the task); and your rule's verdict (met or missed, with numbers) if you set one, otherwise "no rule set".
2. **Trend:** the period where adoption or penetration moved most, with both numbers.
3. **After training:** month-by-month share of adopters still doing the task, labeled usage, not training retention.
4. **Eligible not trained:** count per site.
5. **Data checks and gaps.**
6. **Record:** "Adoption read on your data. Roles and ids only. No clinical meaning." Then who clears it: "Cleared by NAME; the record is built with `verify.build_record` once NAME clears it", or, with no name, "uncleared draft". AI-assisted.
7. One line offering the full version.

## Full mode

### Answer

### By period
| Site / role | Period | Eligible | Trained | Adoption (adopted/trained) | Penetration (active/eligible) | Active/trained | Old-step users | Old step, also task |
|---|---|---|---|---|---|---|---|---|
Definitions: adoption CS34 (or CS28); penetration CS39.

### Against your rule
| Site / role | Window (days, yours) | Met within window / window elapsed | Not yet elapsed | Your share | Verdict |
|---|---|---|---|---|---|

### After-training activity
| Site / role | Month after training | Adopters active / adopters observed |
|---|---|---|

### Maintenance (if you set a horizon)

### What it means for you

### Data checks

### Gaps

### Record
Adoption read. AI-assisted. Cleared by NAME (as the person named them); the record is built with `verify.build_record` once NAME clears it. With no name: uncleared draft.
