# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A research row states it. | The fact plus the row id (for example "patient engagement tool cap $623 for 2026, CP-US-27"). | None. |
| Code, not law | The row is marked [INDUSTRY]. | "AdvaMed Code [INDUSTRY], a code, not law (PC-US-94)." | None; never present it as a legal requirement. |
| Summarizer-read | The row is marked [WF]. | Say the rule rests on a page read through a summarizer. | Re-read the page before relying on it outside the conversation. |
| Not sourced | No row covers the point (for example UK rules on NHS discounts, the warranties safe harbor text). | "Not in this skill's sources `[GAP]`." | The person's compliance, legal or regulatory owner. |
| Applicability | A row applies only if a fact the rows cannot settle holds (for example whether a Federal program pays for the item). | "Applies if [fact]; [fact] as the person's compliance owner determines `[GAP]`." | Ask the owner. |

## Customer success measures

No primary or peer-reviewed source defines customer health, renewal rate, renewal risk, churn, net revenue retention, expansion readiness, time to value or NPS as a renewal predictor for digital health (`customer-success-research.md`, "Not sourced"). Therefore:

- Never give a benchmark, a typical rate or a "healthy" range for any of them.
- Ask for the person's definition and rule; label it owner-stated.
- The register starter rules (`starter-rules.md`) may be offered for the person to adopt.

## The person's facts

| Situation | How to word it |
|---|---|
| No horizon or as-of date | Ask. The script will not run without them. |
| No readiness or risk rule | Show the facts per account; leave the verdict column blank and ask for the rule. |
| No owner named | Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title. |
| Result the account has seen is not recorded | "Result seen by the account: not recorded `[GAP]`." |
| Contract or data terms not supplied | "BAA or processor terms not seen `[GAP]`." Never assume they cover the new use. |
| Evidence described but not shown | "Described, not seen." |
| No scores for B1 ranking | No ranking. Lay out the facts per action and ask for scores. |

## Library facts

| Situation | How to word it |
|---|---|
| No authorization returned | "No authorization in the library for this reference; absence is not evidence of none." |
| Claim labels from `audit_claims` | Not used as findings (`tools.md`). |
| A call fails (for example a 503) | Say so, continue on the references, and do not retry more than once. |

## Never

- Never fill a definition, threshold, rule, owner, score or price from memory.
- Never treat a missing row as "allowed".
- Never treat an unexpired contract as evidence that an account will renew.
