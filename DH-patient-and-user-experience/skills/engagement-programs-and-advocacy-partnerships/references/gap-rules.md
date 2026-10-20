# Gap rules

A gap is information. Name its reason, because each reason leads to a different next step.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A research row states it | The fact plus its row id ("2026 cap $623 per patient, CP-US-27") | None |
| Industry code | The row is [INDUSTRY] | "EFPIA Code 2026 [INDUSTRY], a self-regulatory code, not law (PE-71)" | Ask whether the company is bound by it |
| Read by a fetch tool | The row is [WF] | "FTC guidance as read by a fetch tool (PC-US-73 [WF])" | Recheck the page before quoting it outside the conversation |
| Quote cut short | The row quotes part of a list | "Further EFPIA agreement elements not in the quoted text `[GAP]`" | Read the code |
| Market not in the research | A market without rows (for example France, Japan) | "Rules for this market are not in this skill's sources `[GAP]`" | The person's legal owner |
| Opinion binds one requestor | An OIG advisory opinion | "AO 19-02 binds only its requestor (CP-US-43); shown as the safeguards OIG weighed" | None |
| Yearly figure | The safe-harbor cap | "$623 for calendar year 2026 (CP-US-27); recheck the OIG figure for another year" | Read OIG's inflation page for that year |

## The person's facts

| Situation | How to word it |
|---|---|
| Role, payment or approver of patient-facing words not stated | "Not stated `[GAP]`"; ask once for all three |
| Company's code membership not stated | Lay out each code as conditional: "if the company is bound by the ABPI Code ..." |
| Whether the company is a covered entity, business associate or processor | "For your privacy owner `[GAP]`"; lay out each case |
| Support value per patient not given | "Value not stated `[GAP]`"; never estimate a retail value |
| No owner named | Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title. |
| No scores for B1 options | No ranking; lay out the facts and ask the person to score |

## Library facts

| Situation | How to word it |
|---|---|
| `audit_claims` reports no authorization by name | "The library did not find the authorization by name; rerun with the identifier" (see `tools.md`) |
| `audit_claims` label with intended purpose `[GAP]` | "Label not readable: the record holds no intended purpose" |
| Library returned 502 or 503 twice | "The library did not answer; nothing was counted" |

## Never

- Never fill a rule, a cap, a code element, an owner, a value or a score from memory.
- Never treat a missing row as "allowed" or "not required".
- Never treat a value under the cap, or a favorable opinion for someone else, as protection.
