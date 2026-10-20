# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Library facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Found | A register, publication or company row exists | Fact, event date, source URL, "as of" retrieval date | None |
| Lookup missed | A name search returned nothing, but the product may be stored under another spelling or maker string | "The name search 'X' returned no row; the store spells names differently across registers" | Retry with the maker, the K number or the Basic UDI-DI |
| Covered, absent | The register is loaded and holds no row for this item | "Not in the library's copy of REGISTER (N rows, loaded DATE)" | Check the authority |
| Not covered | The register is not loaded (UK device registration, CH, Companies House; CA rows excluded by the software filter) | "The library does not load SOURCE: REASON" | Check the authority directly |
| Field not stored | The row exists but the field does not (EU decision date, AI or PCCP status, intended use, 8-K item number) | "FIELD not stored in the library row `[GAP]`" | Open the source record |
| Log not started | A regulatory change log returns "no watch is registered for this scope; the change log has not started" | "The change log has not started for this scope; this is not 'no change'" | Read dated records with `search_devices` or `get_pathway_precedents` |
| Before the log | A company change log began on 12 October 2026 and the window starts earlier | "The library change log began 12 October 2026; it cannot show DATE to 12 October 2026" | Read the company's dated filings and authorizations for that window |

Never turn any of these into "no competitor", "nothing new", "no change", "not authorized" or "empty field".

## Signals and leads

| Situation | How to word it |
|---|---|
| Press release, news, vendor deck or conference claim | "Lead, not a signal: RECORD not read `[GAP]`"; name the record that would confirm it |
| Record read but undated | "Undated record: not a signal until its date is found" |
| A trend asked for without signals | "No signals behind this reading yet"; list the records to read |
| A reading the model offers | "Proposed reading", with the signal ids it rests on and those that cut against it |

## Requirement and method facts

| Situation | How to word it |
|---|---|
| A row states it | The rule plus the row id |
| Not in the research (scenario method, disruption index, signal strength scores, digital health success rates, market sizes, optimism bias percentages, ESF tier names, WHO CDI codes) | "Not in this skill's sources `[GAP]`" |
| Row marked [WF] | State the rule and "read through a summarizer; re-check the source before external use" |
| [PAPER] row | Row id plus the DOI of that row's own paper |
| Draft or pilot (FDA AI lifecycle draft, MHRA PCCP draft not yet published, TAP pilot, IDAP pilot closed) | "Draft (or pilot), status as read on DATE" |
| Row marked "(inference)" | Row id followed by "(inference)", every time it is cited |

## The person's facts

| Situation | How to word it |
|---|---|
| Scope, horizon or filters not given | "Not given"; ask once; any proposal is labeled "proposed" |
| Current play not given (B1) | "Current play not given `[GAP]`"; no implication written |
| No scores for a ranking | No ranking. Lay out facts per option and ask the person to score |
| Weights do not sum to 1 | Say so and ask; do not normalize silently |
| No owner | "Owner not named" and ask; never suggest a job title |
| A date, data cut, threshold or status not given | "Not given" and ask; never supply one |

## Never

- Never fill a decision date, a clearance, an AI or PCCP status, a trial result or a company status from memory.
- Never treat a missing row as "not there" or an empty log as "no change".
- Never give a probability, a date of arrival, a market size or a success rate as the person's.
