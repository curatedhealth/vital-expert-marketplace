# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Requirement facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A row states it. | The fact plus the row id ("WCAG 2.1 A and AA from 11 May 2027 for HHS recipients with 15 or more employees, UX-US-16, moved by the HHS interim final rule, UX-US-18"). | None. |
| Criterion level only | The criterion and level are in `data/wcag_criteria.csv` but its text is not quoted in a row. | "4.1.2 Name, Role, Value, Level A (wcag_criteria.csv); criterion text not quoted here `[GAP]`." | Read it at the W3C page. |
| Inference | The rule follows from definitions, not from a stated rule (EAA and health apps). | "Inference from the EAA definitions, not a stated rule (UX-EU-04)." | The person's legal owner decides. |
| Interim or proposed | An interim final rule (ADA and HHS 504 dates) or a proposal (HTI-5). | "Interim final rule; a later final rule could change it." or "Proposed only, not in force." | Check the Federal Register before relying on it outside the conversation. |
| Not checked | A row says it was not checked (EN 301 549 V4.1.1 in the OJ, national EAA transposition, national WAD lists of public bodies). | "Not checked in this skill's sources `[GAP]`." | The person's legal owner, or a later research pass. |
| Jurisdiction not in the rows | Any market other than US, EU and UK (for example Canada, Switzerland, Australia). | "Accessibility law for this market is not in this skill's sources `[GAP]`." | Ask the legal owner. |

## The person's facts

| Situation | How to word it |
|---|---|
| Role not stated (agency, public entity, HHS recipient, contractor, private seller) | Ask. If unknown: "applies if you are ... `[GAP]`". Never infer the role from the product. |
| Population or employee count not stated | Give both dates with their thresholds; ask which applies. |
| Target version and level not set | No target is chosen for them. Lay out what each obligation cites; ask. |
| Screen list not given | No conformance scope. Ask for the screens and processes in the release. |
| Assistive method not named | Ask which method the requirement names. Do not pick one. |
| No owner named | Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title. |
| No scores for ranking | No ranking. Lay out the facts per barrier and ask for scores. |

## Library facts

| Situation | How to word it |
|---|---|
| Guidance passage without a source URL | Do not use it. |
| Verify rates a W3C page inadmissible | Cite the row; say "Verify cannot check W3C text today (register C1)". |
| Verify returns "partial" or "supported" | Accept only after reading the passage in the same direction as the claim (register N3). |

## Never

- Never fill a rule, date, criterion text, role, owner or score from memory.
- Never treat a missing row as "not required".
- Never treat an issue not found, a passing scan, or a missing complaint as evidence of conformance.
