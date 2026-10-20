# Output format: increment and gate evidence plan

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with a tool (the answer without the calls list, piped to `wc -w`), not by estimate. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, the "Full version on request" line. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** the increment in one line (user, task, build), the next gate, and the first missing element by dependency. Two sentences.
2. **Increment:** in scope; outside it; accepted by (person's words, or "owner not named"). Any clinical claim not in the evidence plan, flagged.
3. **Evidence for the next gate:** table Element · Named by (row, DOI beside any TM or PL110 to PL120 row) or set by you · Work product that shows it · Present, missing or [GAP] · Supplied by (named, or "owner not named"). At most eight rows.
4. **Attendees:** as named, or "attendees not named"; one line on PL1 and independence as a risk-proportionate choice (PL2, PL66, PL67).
5. **Routed:** one line each, pack and skill: `dh-regulatory-and-quality` design-controls-and-risk-management; `dh-regulatory-and-quality` regulatory-pathway-and-classification (or regulatory-submission-and-dossier); `dh-clinical-development` study-protocol-and-endpoint-design for any clinical claim; `dh-patient-and-user-experience` patient-and-clinician-user-research; `dh-access-and-value` coverage-pathway-and-access-strategy for a DiGA listing route.
6. **Gaps and stops.**
7. **Record (last line of the answer body):** "Gate evidence plan draft for OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
8. **Calls made (after the record line):** list (often none).

## Full mode

### Answer
### Increment
| In scope | Outside | Acceptor |
|---|---|---|
### Gate by gate
| Gate | Element | Source or person | Rows | Work product | Status | Supplied by |
|---|---|---|---|---|---|---|
### Dependencies
### Attendees and independence
### Routed to other packs
### Gaps
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
### Calls made (after the record line)
