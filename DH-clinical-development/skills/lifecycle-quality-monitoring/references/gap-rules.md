# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A research row states it | The fact plus the row id ("design reviews at major decision points, PL5") | None |
| Published method | The row is [PAPER] | "Repeat a phase rather than progress automatically (TM3), DOI 10.1136/bmj.n2061" | Cite the DOI once in prose, beside the row id in tables |
| Summarizer read | The row is [WF] (DTAC, DCB0129, ISO pages, IDEAL-D 2016) | "DTAC sections C1 to C4 and D1 (PL97, read through a summarizing fetch [WF])" | Do not quote as verbatim law; check the source page before relying on it |
| Abstract only | IDEAL-D 2016 (PL121), BCTTv1, Bellg 2004 | "Abstract only, read through a summarizing fetch (PL121 [WF])" | Do not build a rule on it |
| Nonbinding guidance | FDA guidance | "FDA recommends (nonbinding guidance, PL15)" | Do not present as law |
| Draft | PDURS (September 2023 draft) | "Draft, not for implementation (PL30)" | Do not plan on it as in force |
| Restated, not read | IMDRF N10 and N23 (only as restated in N12 and N41) | "As restated in N12 (PL54)" | Say the primary text was not read |
| Not in the sources | ISO 13485 7.3 subclause text, IEC 62304 and 82304-1 clause content, DCB0129 specification, IDEAL-D stages 1 to 4 for devices, any industry stage-gate model | "Not in this skill's sources `[GAP]`" | The person or the owner they name supplies it, or owner not named |

## Connector facts

| Situation | How to word it |
|---|---|
| A record holds an authorization | "FDA record DEN200026: De Novo, decision 15 June 2020 (regulatory-dh, retrieved 13 October 2026)" |
| `status` is a raw code | Give the pathway in words; "DENG" is FDA's De Novo granted code (register C3) |
| Predicate "[GAP]" | "Predicate not stored `[GAP]`"; never "no predicate" |
| No safety event returned | "No recall or alert in the store for this name `[GAP]`; a missing record is not evidence that nothing happened" |
| MAUDE counts | "N reports by date received; reports, not confirmed events" |
| Verify unverifiable or no verdict | "Verify returned no verdict; the rule rests on the passage read (row id)" |

## The person's facts

| Situation | How to word it |
|---|---|
| No stage model | "Stage model not stated `[GAP]`"; offer the sourced vocabularies as "proposed" |
| Gate criteria not stated | "Gate criteria not stated `[GAP]`"; B1 cannot mark pass or miss without them |
| Decider or attendees not named | "Owner not named" or "attendees not named"; ask. Never suggest a job title |
| Device status unknown | "Device status not stated `[GAP]`; `dh-regulatory-and-quality` regulatory-pathway-and-classification" |
| A status word with no work product | "Status given, no work product referenced; does not count as present" |
| No measures set | "Lifecycle measures not stated `[GAP]`"; A2 can still count, B1 cannot mark a miss |
| Days open asked against a norm | "No benchmark in the sources `[GAP]`; days open are facts from your log, judged by your rule" |
| Log row without dates | "Not stored in the log"; days open not computed for that stage |

## Never

- Never infer a product's reason for a submission, its market status or its commercial fate from a register record.
- Never mark a gate passed, a stage complete or a product ready.
- Never turn counts into a score, a rating or a ranking of teams or people.
- Never fill a date, a data cut, a decider, a criterion, a status or a threshold the person did not give; write "not given" and ask.
- Never carry facts from an earlier request; use only the inputs of the current request.
- Never judge a register record's relevance to the person's product; quote it with its retrieval date.
