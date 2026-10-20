# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Requirement facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A research row states it. | The fact plus the row id (for example "breach notice to the covered entity at most 60 calendar days after discovery, CS102"). | None. |
| Summarizer read [WF] | The row was read through a fetch tool (CS69, CS70, CS71). | State the fact and "(read through a summarizer, [WF])". | Re-check against the page before relying on it outside the conversation. |
| Guidance, not the standard | A CP-UK row rests on an NHS England page summarizing DCB0129, DCB0160 or DTAC. | "Per NHS England guidance (CP-UK-09); the standard's text was not read." | Read the standard or ask the site's clinical safety lead. |
| Not sourced | No row covers it (for example DCB0160 clause content, US state privacy law, a market outside US, EU, England). | "Not in this skill's sources `[GAP]`." | Ask the legal, privacy or clinical safety owner. |
| Framework, no threshold | The person asks for a CFIR, NASSS or RE-AIM "pass" level. | "The framework gives definitions, not thresholds (CS3, CS51); the threshold is yours." | Ask for their rule. |

## The person's facts

| Situation | How to word it |
|---|---|
| Market or site type not stated | Ask. Without it, the contract and data steps cannot be chosen. |
| No owner for a step | Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title. |
| No date | "unset". Never pick a date, never propose one. |
| Module not agreed by the site | Leave it out of scope and list it as "not agreed by the site". |
| No go-live bar | Offer the starting list in `go-live-bar-elements.md`, labeled "starting list"; the bar stays the person's. |
| No site approver | "site approver not named"; ask. |
| No scores for a rollout ranking | No ranking. Lay out facts per option and ask the person to score. |
| Device status, class or marking unknown | "Regulatory status not stated `[GAP]`"; belongs to the regulatory owner. |

## Library facts

| Situation | How to word it |
|---|---|
| Literature record without a passage stating the finding | Do not use it as evidence; the title alone is not a finding. |
| `check_claim` returns "supported" | Accept only if the passage read states the finding in the same direction (register N3). |
| No safety events returned | "No events in the library for this query; absence is not evidence of no events." |

## Never

- Fill a requirement, date, owner, score, target or clause text from memory.
- Treat a missing row as "not required".
