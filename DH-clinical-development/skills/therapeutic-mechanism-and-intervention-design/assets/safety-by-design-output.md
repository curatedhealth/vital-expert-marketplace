# Output format: safety by design (draft for the person)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** the hazards the design creates (count, and the ones the person marks first), mitigations still open, the safety and labeling elements for the regulation named by the owner the person names for regulatory status (or applicability `[GAP]`), and who decides (named, or "owner not named").
2. **Hazards:** table Hazard (person's words) · Source in the design (link, component or mechanic) · Mitigation (person's, or "not given") · Indicator and threshold for after launch (person's, set now, SE63, not legally binding) · Rows (each [PAPER] row with its own DOI; [WF] and non-binding rows labeled).
3. **Safety and labeling elements the special controls name:** two groups, "Safety controls" (software verification, validation, hazard analysis, validated model) and "Labeling", one line per element, quoted from the exact regulation, as context (SE1 to SE10).
3a. **Precedent record (only when the person names one):** risk rows (SE11, SE12, TM139), trial adverse events (SE14), evidence limits (SE15) and recalls with date, quoted. If the connector is unavailable, say in the body: "saved records of 20 October 2026, not rechecked live".
4. **Handoffs:** risk file to `dh-regulatory-and-quality` design-controls-and-risk-management; applicability to `dh-regulatory-and-quality` regulatory-pathway-and-classification; indicators to mechanism-validation-monitoring A4.
5. **Owner question (only if the person named no owner):** write "owner not named" and ask, before the record line: "Who owns the hazard list, the mitigations and the thresholds, and who owns regulatory status, and who clears this draft? A name or role in your words."
6. **Record (last line of the answer body):** "Safety-by-design draft. AI-assisted. No severity, probability, acceptability or threshold set by the model; nothing called safe." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
7. **Calls made (after the record line):** list.

## Full mode

### Answer
### Hazards by design source
| Hazard | Link, component or mechanic | Hazard source (section 1 row) | Mitigation | Type (design, software check, labeling, clinician step) | Indicator | Threshold (person's) | Rows |
|---|---|---|---|---|---|---|---|
### Safety controls and labeling elements the special controls name, in two groups (context; applicability is `dh-regulatory-and-quality` regulatory-pathway-and-classification's)
### Mitigation patterns in precedent records (context only)
### Expected side-effects (EU: documented and quantified, or not; the decision of the person and the owner they name for regulatory status, or owner not named, SE59)
### Precedent safety records (record facts with dates: risk rows, trial adverse events SE14, evidence limits SE15, recalls; if the connector is unavailable, "saved records of 20 October 2026, not rechecked live")
### Handoffs
### Gaps
### Owner question (only if the person named no owner; before the record line)
"owner not named", then: "Who owns the hazard list, the mitigations and the thresholds, and who owns regulatory status, and who clears this draft? A name or role in your words."
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
### Calls made (after the record line)
