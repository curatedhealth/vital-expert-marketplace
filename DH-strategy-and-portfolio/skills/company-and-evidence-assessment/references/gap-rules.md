# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A research row states it | The fact plus the row id ("Form D is due within 15 days after the first sale, DL-002") | None |
| Inference row | The research file marks the row "(inference)" | "A Form D does not show valuation or investor names (DL-018 (inference))" | Say it is a reading, not a quoted rule |
| Published method | The row is [PAPER] | "Level 4 needs two or more high-quality RCTs (DL-112), DOI 10.1038/s41746-023-00836-5" | DOI once in prose, beside the row id in tables |
| Industry body | DiMe framework (DL-122) | "An industry body's framework (DL-122, DOI 10.1038/s41598-025-21996-2)" | Do not present as a standard |
| Voluntary framework | NICE ESF | "Not mandated for NHS commissioners (HE-079)" | Do not present as a requirement |
| Not in the sources | Evidence DEFINED checklist items, Companies House PSC rules, CFIUS fees and timelines, national FDI laws, state health privacy laws, market size, valuation multiples, return benchmarks, funding totals by sector | "Not in this skill's sources `[GAP]`" | The person or the owner they name supplies it, or owner not named |

## Connector facts

| Situation | How to word it |
|---|---|
| A record holds an authorization | "FDA record DEN200026: De Novo, granted, 15 June 2020 (diligence-dh, retrieved 19 October 2026)" |
| `status` is "DENG" | "De Novo, granted" (raw code DENG, register C3) |
| Company not resolved | "Lookup missed for 'HelloBetter' (no exact match); not evidence that the company has no record. Try the legal name or an FDA, EUDAMED or SEC identifier." |
| A source not loaded | "Companies House not loaded in the library ('API key not yet provisioned', 19 October 2026) `[GAP]`" |
| No registered study linked | "No registered study linked in the loaded sources (clinicaltrials, 128 records on 19 October 2026); published trials may exist outside it `[GAP]`" |
| `funding` "[GAP]" beside Form D rows | "Form D filings stored (dates, amounts as stated); private rounds not in the library `[GAP]`" |
| Score excludes a component | "Reimbursement excluded from the score ('no reimbursement source is loaded'); excluded, not zero" |
| Combined filing names | "Two filing names combined by the library; a proposal until you validate it" |
| Guidance store empty | "No guidance passage returned ('no passage retrieved in this namespace'); the rule rests on the row read" |
| Verify unverifiable or no verdict | "Verify returned no verdict; the claim rests on the passage read (source name and date, then row id)" |
| Company status not read | "Status: [GAP]: not read. Open: EDGAR filings for CIK N (8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15); Companies House status; German insolvency notices" (`company-status.md`) |
| Form 15 or Form 25 found | "Form 15 filed DATE: SEC reporting stopped; not dissolution (DL-149 (inference))"; "Form 25 filed DATE: exchange listing ended; not dissolution (DL-144)" |
| Field absent from the saved record | "Not in the record"; never 0, "none" or "US company" (an authorization country is not the company's country) |
| Period before the change log | "The library's change log began on 12 October 2026; for the earlier part of the period, the company's dated filings and authorization records are the source" |
| Safety events `none_found` | "None found in the loaded enforcement source, retrieved 19 October 2026; not proof of none" |

## The person's facts

| Situation | How to word it |
|---|---|
| No company reference | Ask for one: legal name, brand, FDA submission number, LEI, EUDAMED SRN or SEC filer number |
| Unpublished target or data-room name | Ask before sending it to the library |
| No diligence criteria | "Diligence criteria not stated `[GAP]`"; offer source-named elements as "proposed"; B1 cannot mark met or not met without them |
| No framework chosen | Offer the fitting framework as "proposed" with its limits |
| A vendor or data-room figure | "Your figure (source as you named it); not checked against a primary filing" |
| No decision stated | "Decision not given"; never write one |

## Never

- Never infer revenue, runway, valuation, customers, outcomes or intent from a record.
- Never call a missing record a negative fact.
- Never turn the library score into a framework level, a rating or a ranking.
- Never fill a date, a data cut, a decider, a criterion, a status or a threshold the person did not give; write "not given" and ask.
- Never carry facts from an earlier request; use only the inputs of the current request.
