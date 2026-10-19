# Output format: sales enablement plan (leave-behind, roster, field stops)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** whether the leave-behind can be built from approved claims (sections `[GAP]` named), roster coverage against the person's pass rule (or "no pass rule given"), and the activities that stop.
2. **Leave-behind and objection outline:** Section or objection · Approved claim ids · Status (filled or `[GAP]`).
3. **Roster:** Role · Uses · Briefer · Date (yours) · Status. Roles not briefed with the reason.
4. **Field activities that stop:** Activity · Elements the rows set · Rows · Owner.
5. **Record:** "Enablement plan draft. Content, roster and dates are yours; material approval and field activities stop for the owners named." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer

### Leave-behind draft
Format and audience. Each section with the approved claims quoted by id. Required statements carried with the content (limits, labeled indication, pre-use information) with rows. Screen result from `scripts/claim_screen.py` if run. Labeled "draft for approval by OWNER".

### Objection responses
| Objection (yours) | Approved claim ids, quoted | Required statements | Status (filled, `[GAP]`, route to authorized personnel) |
|---|---|---|---|
Method, not a sourced rule: responses use approved claims only.

### Enablement roster
| Role | Uses | Briefer (yours) | Date (yours) | Format | Status | Note |
|---|---|---|---|---|---|---|

### Pass rule check
| Rule (yours) | Result | Roles |
|---|---|---|

### Field activities that stop for compliance or legal
| Activity | Elements the rows set | Rows | Open questions for the owner | Owner |
|---|---|---|---|---|
No activity is described as protected or allowed.

### Ranking (only on your scores)
Tool, your numbers, result labeled as your ranking.

### Stops for the accountable owner

### Gaps

### Calls made

### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
