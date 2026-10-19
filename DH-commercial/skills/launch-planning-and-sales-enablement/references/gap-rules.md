# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A research row states it | The fact plus the row id ("annual registration 1 October to 31 December, CP-US-72") | None |
| Industry code | The row is marked [INDUSTRY] | "AdvaMed Code [INDUSTRY], not law (PC-US-91)" | Apply as the person's policy choice, not as a legal duty |
| Summarized source | The row is marked [WF] | "FTC guidance as read through a summarizing tool [WF] (PC-US-72); re-check on the page before quoting" | Read the page before external use |
| Version caveat | A row says its text may be superseded (UCPD 2005 text; HWG change of 26 June 2026 not yet documented; payor guidance draft) | State the version read and the caveat in one line | Check the current version before relying on it outside the conversation |
| Draft or not implementable | Draft guidance, or SIUU "not for current implementation" | "Draft, not final" or "final but not for current implementation (PC-US-56)" | Do not plan on it as in force |
| Market not in the research | Switzerland, or any market without rows | "Launch rules for this market are not in this skill's sources `[GAP]`" | Ask the person's regulatory or legal owner |
| Clause not readable | DTAC criteria, DCB0129 or DCB0160 clauses | "Clause not sourced; rows rest on NHS England guidance pages `[GAP]`" | Read the standard |

## Library facts

| Situation | How to word it |
|---|---|
| Peer not returned by `get_launch_sequence` | "Not found in the library under this name `[GAP]`; absence is not evidence the product has no listing or authorization." Try the exact stored name from `find_scheme_precedents` or the FDA number. |
| `changed_on` without a status | "Changed on DATE (source); status after the change not stated `[GAP]`." |
| DiGA history | "The library stores a day-zero snapshot; transitions before 15 October 2026 are `[GAP]` unless a dated BfArM file is returned." |
| EU record without decision date | "On the EU market per EUDAMED (library copy); decision date not stored `[GAP]`." |
| UK or Swiss authorization | "The library loads no UK device registrations and no Swiss records `[GAP]`." |
| Readiness criterion `[GAP]` | Say which input was missing (note, route, authorization) and who supplies it. |
| Claim label from `audit_claims` | "Connector label: exceeds_record (the library holds no intended purpose text)." Never a finding. |

## The person's facts

| Situation | How to word it |
|---|---|
| Authorization or intended use not shown | "Authorization not shown `[GAP]`"; claims stay unflagged against labeling until the labeling text is supplied |
| No evidence source for a claim | "No source given `[GAP]`"; the claim stays off the approved list |
| No owner named | "Owner not named"; ask. Never suggest a job title |
| No briefing date or briefer | Leave it blank and ask; never pick a date |
| No pass rule for readiness | Report status per prerequisite; no verdict |
| Prerequisite described but not shown | "Stated, not seen" |

## Never

- Never fill a rule, date, authorization, claim source, owner or briefing date from memory.
- Never treat a missing row or record as "not required" or "not authorized".
- Never treat the connector's `met_count` as readiness.
