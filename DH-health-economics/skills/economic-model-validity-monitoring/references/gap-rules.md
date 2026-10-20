# Gap rules

A gap is information, not an apology. Each reason leads to a different next step.

| Class | When | How to word it | Next step for the person |
|---|---|---|---|
| Person's rule not yet set | An acceptance rule, a monitoring trigger, an owner or the decision-maker the model is checked against | "Acceptance rule for reporting: not set `[GAP]`; findings listed without a verdict." | Ask once; a proposed rule is labeled "proposed" with its row. |
| Not in the document | A CHEERS item or reference-case element the script or reading did not find | "Item 28 conflicts of interest: not found in the description; check the full report." | The person checks the full document; absence from a summary is not absence from the model. |
| Item not sourced | A CHEERS item whose wording the research file does not hold, or a validation checklist from the paywalled ISPOR texts | "Items 1 to 3: wording not sourced here `[GAP]`; check the CHEERS 2022 checklist." | Read the checklist (DOI 10.1177/23814683211061097). |
| Model not available | Only a summary was supplied, so verification by recomputation is not possible | "Verification: inputs and calculations not supplied `[GAP]`." | Supply the model file or the input table. |
| Observed data missing | No real-world value to compare an assumption with | "Observed GP saving: no data yet `[GAP]`." | The person's data or a study (dh-health-economics DH-01.07.3). |
| Rule in conflict or draft | NICE thresholds (PMG36 versus PMG48); AMCP 6.0 draft rows | "Two written NICE ranges, open conflict (HE-050, HE-051, HE-074)." | The person chooses which to report against. |
| Tool failed | HTTP 422, 400 or 503 | "Budget impact calculator rejected the payload (HTTP 422); recomputed with the scenario modeler." | Fallback in `tools.md`. |

## Never

- Never turn "not found in the description" into "the model does not do this".
- Never fill an unsourced CHEERS item, a validation checklist item, an observed value or an acceptance rule from memory.
- Never give a CHEERS score or a validity grade.

When a source is open access, read the full text before marking a field `[GAP]` from its abstract.
