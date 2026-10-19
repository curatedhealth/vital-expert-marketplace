# Output format: training task cards and plan

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap and end with the same record line.

## Short mode (default for a direct question)

1. **Answer:** the task card for the role asked about (role, task, steps the user performs, out of scope this session, what training cannot supply (CS19), kept even when the steps are [GAP]), or the cards in one table.
2. **Plan elements not covered:** at most five, each with its row (for example ESF Standard 20, CS65). Label NICE items "checklist" outside NHS buyers.
3. **Device note (only if the person said it is a device):** customer training should match validated training (CS80); a training change goes to the regulatory owner (UX-US-49). If training is proposed to fix an error: design first, training last (UX-US-33, CS77, CS78, CS79); stops for the regulatory and design owners.
4. **Gaps:** workflow, device status, validated training, as applicable.
5. **Record:** "Training plan draft. Clinician-facing material goes to its editorial owner." Then who clears it: "Cleared by NAME; the record is built with `verify.build_record` once NAME clears it", or, with no name, "uncleared draft". AI-assisted.
6. One line offering the full version.

## Full mode

### Answer

### Task cards
| Role (your words) | CFIR role (CS18) | Task (day-one workflow) | Steps the user performs | Out of scope this session | What training cannot supply (CS19) |
|---|---|---|---|---|---|

### Plan against sourced expectations
| Element | Status in your plan | Row |
|---|---|---|
| Training need in the pathway | covered / not covered / not stated | CS58 |
| End-user training approach and limits communicated | | CS65 |
| Training and staffing cost in budget impact | | CS63 |
| Expected usage profile | | CS61 |
| NHS assurance and clinical safety (DTAC, DCB0160) [WF] | | CS69 to CS71 |
| Customer HIPAA workforce training (theirs) | | CS82, CS83 |

### Device check (if applicable)
| Fact | Consequence for your plan | Row |
|---|---|---|

### Field events for your product (if called)
| Date | Severity | What the record states | Task card touched, per the summary |
|---|---|---|---|
Source: openFDA enforcement report as held by the library; record not linked. Absence is not evidence of no events.

### Stops for the accountable owner

### Gaps

### Calls made

### Record
Training plan draft. AI-assisted. Cleared by NAME (as the person named them); the record is built with `verify.build_record` once NAME clears it. With no name: uncleared draft.
