# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Library facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Found | A peer, authorization or listing row exists | Fact, date, source URL, "as of" retrieval date | None |
| Lookup missed | The screen counts authorizations for a company but the per-peer device search returned nothing (company name used as the query) | "Screen lists products P with N authorizations; the device lookup by company name returned no row" | Look up a product by name with `name` or `regulatory-dh.search_devices` |
| Covered, absent | The jurisdiction or scheme is loaded but holds no row for this peer | "Not in the library's copy of SCHEME (N listings, loaded DATE)" | Check the authority |
| Not covered | Not loaded (listing count 0, posture `gap`, or listed under `not_loaded`) | "The library does not load SOURCE: REASON" | The library cannot answer; check the authority |
| Code-based route | A US code route (DMHT, RPM) lists codes, not products | "This route pays a practitioner's service by code; product listing does not apply" | Market Access pack for eligibility |

Never turn any of these into "not authorized", "not reimbursed", "no competitor" or "empty market".

## Requirement facts

| Situation | How to word it |
|---|---|
| A row states it | The rule plus the row id |
| Not sourced in the research (employer channel, app store, NHS framework lots, DCB clause text, DiGA framework thresholds) | "Not in this skill's sources `[GAP]`" and name the owner who would know |
| Row marked [WF] | State the rule and "read through a summarizer; re-check the source before external use" |
| Row marked [INDUSTRY] | "Industry code, not law" |
| Draft or proposal (FDA payor draft June 2026, SIUU not yet implementable) | "Draft, not in force as of the research read on 19 October 2026" |

## The person's facts

| Situation | How to word it |
|---|---|
| Intended use or device status not stated | "Intended use not stated `[GAP]`"; no positioning line until it is |
| No scores for B1 | No ranking. Lay out facts per segment and ask the person to score |
| No owner for a motion | "Owner not named" and ask; never suggest a job title |
| No cleared claim list for B2 | Write the line without claims of effect, and mark claims `[GAP]` |

## Never

- Never fill a peer's outcome, revenue, price or strategy from memory.
- Never fill a payer route, rule or threshold from memory.
- Never treat a missing row as "not required" or "not there".
