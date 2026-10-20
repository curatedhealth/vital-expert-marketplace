# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A research row states it | The fact plus the row id ("US results are due no later than 1 year after primary completion, CV145") | None |
| Inference row | The research file marks the row "(inference)" | "Vendor funding totals are claims (DL-125 (inference))" | Say it is a reading, not a quoted rule |
| Published method | The row is [PAPER] | "Evidence DEFINED plans updates every 6 to 12 months (DL-113), DOI 10.1038/s41746-023-00836-5" | DOI once in prose, beside the row id in tables |
| Voluntary framework | NICE ESF | "Not mandated for NHS commissioners (HE-079)" | Do not present as a requirement |
| Not in the sources | A benchmark pace of evidence maturity, a typical time from registration to results for digital health, Evidence DEFINED checklist items, valuation effects of evidence | "Not in this skill's sources `[GAP]`" | The person's rule judges it |

## Connector facts

| Situation | How to word it |
|---|---|
| Score moved, change class METHOD or COVERAGE | "The score moved from 33 to 40 with no change in evidence inputs: the assessable maximum changed (90 to 100)" |
| Score moved, change class INPUT | "One more product-linked study with results posted in the library (0 to 1); record not yet read" |
| Change class RESOLUTION | "The two runs resolved to different references or companies; not comparable as a trend" |
| Inputs missing from one output | "Inputs are in one output only (compare_portfolio gives points, not inputs); inputs not compared" |
| No change recorded | "No change recorded in the library's log since DATE (log started 12 October 2026); not evidence that nothing happened" |
| Source not loaded | "Companies House not loaded ('API key not yet provisioned', 19 October 2026) `[GAP]`" |
| Verify unverifiable | "Verify returned no verdict; the claim rests on the passage read (source name and date, then row id)" |
| Company status not read | "Status: [GAP]: not read. Open: EDGAR filings for CIK N (8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15); Companies House status; German insolvency notices" (`company-status.md`) |
| Form 15 or Form 25 found | "Form 15 filed DATE: SEC reporting stopped; not dissolution (DL-149 (inference))"; "Form 25 filed DATE: exchange listing ended; not dissolution (DL-144)" |
| Field absent from the saved record | "Not in the record"; never 0, "none" or "US company" (an authorization country is not the company's country) |
| Period before the change log | "The library's change log began on 12 October 2026; for the earlier part of the period, the company's dated filings and authorization records are the source" |
| Safety events `none_found` | "None found in the loaded enforcement source, retrieved 19 October 2026; not proof of none" |

## The person's facts

| Situation | How to word it |
|---|---|
| Only one snapshot | "Earlier run not given `[GAP]`"; offer to save today's run as the baseline |
| Snapshots with different references | Ask which reference the person tracks; compare only like with like |
| No measures set | "Monitoring measures not stated `[GAP]`"; A2 can still classify changes, B1 cannot mark a trigger |
| No confirmed level | "Earlier level not confirmed by you `[GAP]`"; a proposed level is not a baseline |
| Reread date | "Not given"; ask. Never supply one |
| Days or months compared with a norm | "No benchmark in the sources `[GAP]`; your rule judges it" |

## Never

- Never infer why a trial stopped, why a listing changed, or what a company intends.
- Never turn a difference into a rating, ranking or value statement.
- Never fill a date, a data cut, a trigger, a level or a threshold the person did not give; write "not given" and ask.
- Never carry facts from an earlier request; use only the inputs of the current request.
