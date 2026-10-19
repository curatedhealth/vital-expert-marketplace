# Gap rules

A gap is information. Name the reason, because each reason leads to a different next step.

## Source facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A row states it. | The fact plus the row id (for example "think-aloud not acceptable in validation, UX-US-40"). | None. |
| Guidance, not law | FDA or MHRA guidance, NHS policy, GRIPP2 or the UK Standards. | "FDA recommends", "NHS guidance", "reporting checklist", never "required" (UX-US-26, UX-UK-14, UX-UK-25, PE-65). | None. |
| Restated, not read | A figure quoted by another source (Sauro and Lewis via Hyzy). | "As cited by Hyzy et al. (UX-M-08); the original was not read." | Read the original before relying on it outside the conversation. |
| Not sourced | No row covers it (quality scales for research, SUS bands, benchmarks for insight closure). | "Not in this skill's sources `[GAP]`." | The person's rule. |

## The person's data

| Situation | How to word it |
|---|---|
| No insight log | "No insight log `[GAP]`"; offer the columns from `scripts/research_log.py trace` or the sibling's B1. |
| No change log | Trace stops at decisions; "shipped status not measured `[GAP]`". |
| Insight with no date | "Raised date not recorded"; excluded from age, counted in status. |
| Session role not recorded | "Role not recorded `[GAP]`"; the session is not counted in any group. |
| No rule or threshold | Report the number; no verdict. Ask for the rule. |
| No owner named | Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title. |
| No forum or date | "Not set"; never propose one. |
| No scores for ranking | No ranking. Ask for scores. |

## Library facts

| Situation | How to word it |
|---|---|
| Guidance passage without a source URL | Do not use it. |
| Verify "supported" for a claim the passage does not state in the same direction | Do not accept it (register N3). |

## Never

- Fill a rule, threshold, owner, forum, date or score from memory.
- Treat a missing insight log as "nothing to act on", or few open insights as good research.
