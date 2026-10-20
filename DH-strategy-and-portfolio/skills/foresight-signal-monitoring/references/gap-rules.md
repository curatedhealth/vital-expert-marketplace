# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Library facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Found | The record was reread | Fact, identifier, event date, source, "as of" retrieval date | None |
| Changed on reread | The record now states something else | "On DATE the record read X; on the reread it reads Y" | Q7 fails for that signal; the person decides what follows |
| Lookup missed | A name search returned nothing on reread | "The name search returned no row; names differ across registers" | Retry by identifier |
| Not covered | The register is not loaded (UK device registration, CH, Companies House) | "The library does not load SOURCE" | Check the authority |
| Field not stored | EU decision date, AI or PCCP status, 8-K item number | "FIELD not stored `[GAP]`" | Open the source record |
| Log not started | Regulatory change log "has not started" | "The change log has not started for this scope; this is not 'no change'" | Reread dated records |
| Before the log | Company change log began 12 October 2026 | "The library change log cannot show DATE to 12 October 2026" | Read the company's dated filings and authorizations |

Never turn any of these into "no change", "still holds", "nothing happened" or "not authorized".

## Calls and selections

| Situation | How to word it |
|---|---|
| Resolution rule not given | "Not resolvable: resolution rule not given"; a proposed rule is labeled and not applied until confirmed |
| Horizon not reached | "Open: horizon DATE not reached" |
| The record cannot measure it (adoption, revenue, clinical effect, user satisfaction) | "Not measurable from the record; needs your data" |
| Outcome recorded without evidence | "Outcome recorded without evidence `[GAP]`"; ask for the record |
| Rests on a company still existing | Company status line from the status already read (`company-status.md` section 6, cited by filing name and date, for example "Pear 8-K, filed 7 April 2023 (SP-156) [WF]"), or "Status: [GAP]: not read" with the filings to open |

## Measures

| Situation | How to word it |
|---|---|
| Benchmark asked for (industry accuracy, target hit rate, acceptable false-positive rate) | "No benchmark in the sources `[GAP]`"; the pass rule is yours |
| Scoring rule for probabilities | "Your method"; the arithmetic is shown on your numbers |
| Row marked [WF] | "Read through a summarizer; re-check before external use" |
| Row marked "(inference)" | Row id followed by "(inference)", every time it is cited |

## The person's facts

| Situation | How to word it |
|---|---|
| Pass rule not given | "Pass rule not given: nothing marked passed or failed"; ask |
| Owner not given | "Owner not named" and ask; never suggest a job title |
| Reread date not given | "Not given" and ask; a reread date earlier than the read date is stated as a fact, never as urgency |
| Follow-up rule relative to the review ("within 30 days of the review") and no review date given | Keep the rule in the person's words; "review date not given", ask; no calendar date |
| Owner in the log differs from the owner the person names for that kind of row | Show both names in that row and ask which applies; never choose |
| A date, data cut, threshold or status not given | "Not given" and ask; never supply one |

## Never

- Never resolve a call or pass a signal from memory or press.
- Never score a person, a team or a forecaster.
- Never compare the person's log with a benchmark that no source sets.
