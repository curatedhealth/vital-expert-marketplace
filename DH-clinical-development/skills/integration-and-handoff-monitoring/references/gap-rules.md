# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A research row states it | The fact plus the row id ("a design review includes representatives of the functions concerned with the stage, PL1") | None |
| Published method | The row is [PAPER] | "IDEAL-D consensus fallback (PL120), DOI 10.1097/SLA.0000000000004907" | Cite the DOI |
| Abstract-only or [WF] | BCTTv1, Bellg 2004, GRADE EtD Alonso-Coello rows (TM107, TM108), DTAC (PL97 to PL100), ISO pages (PL106 to PL109), IDEAL-D 2016 (PL121) | "Read through a summarizer [WF] (PL98); re-check before relying on it" | Say so every time it is applied |
| Nonbinding guidance | FDA guidance (multiple function, Q-Sub, PDURS draft) | "FDA recommends (nonbinding guidance, PL26)" | Do not present as law |
| Draft | PDURS (PL30) | "Draft guidance, September 2023, not for implementation (PL30)" | Do not plan on it as in force |
| Pre-QMSR wording | 820.30 references in older guidance | "Written before the QMSR; read 820.30(g) as ISO 13485 7.3.7 (PL12)" | State the current basis |
| Analogy | Pre-Sub minutes (PL41), IDEAL-D consensus (PL120), EtD conclusions (TM112) used for an internal record | "Modeled on PL41; a rule for FDA meetings, not for internal decisions" | Label as pattern |
| The person's rule | Received, late, due dates, period, categories, CTQ marking, owners, look-again dates, any score formula or target | "The person's rule, in their words (O)"; if absent: "Rule not set `[GAP]`; the person sets it" | Ask the person |
| Not in the sources | ISO 13485 7.3.8 transfer text, IEC 82304-1 clause content, DCB0129 Clinical Safety Officer and hazard log, RACI or escalation methods, handoff metrics | "Not in this skill's sources `[GAP]`" | Route or ask; never fill from memory |

## Library facts

| Situation | How to word it |
|---|---|
| `get_authorization` returns identity, class, product code and regulation number only | "Authorization record as stored (retrieved [date]); intended use and decision summary text not in the record `[GAP]`" |
| Status shown as "DENG" | "De Novo granted (the record's raw FDA code DENG)" |
| A recall row | Quote the record's summary; "the library row does not state a cause beyond what is quoted; FDA's recall page may hold a root-cause category not read here `[GAP]`". Do not judge whether it bears on the person's product |
| MAUDE counts | "Reports by date received; counts are reports, not confirmed events" (as the tool states) |
| `retrieve_guidance` returns nothing | "No guidance passage in the library `[GAP]`; rule taken from row PLn" |
| Verify rates an FDA PDF "inadmissible, no provenance" | "Verify could not qualify the FDA page (register C1); the rule rests on the research row read from the raw file" |
| `find_job` and `list_jobs` show no fitting job | Catalogue job: none |

## The person's facts

| Situation | How to word it |
|---|---|
| Sender or receiver not named | "Receiver not named `[GAP]`"; scored "not measurable" whether or not it has arrived (the script checks this before open or received), and the answer asks the person who receives it |
| Received date but no named recipient | "Receipt not shown `[GAP]`"; scored "not measurable", never "received" |
| Received by someone other than the named receiver | Quote both names; "not measurable" under the default rule unless the person's rule says otherwise |
| No due date | "No due date `[GAP]`"; "not measurable" for lateness |
| No received rule confirmed | "Received rule not set `[GAP]`"; run A1 before scoring |
| Blocked decision not stated | "Blocked decision not stated `[GAP]`"; without it, this is a task, not an integration point |
| No owner for a dependency | "Owner not named"; ask. Never suggest a job title |
| No late path | "Late path not stated `[GAP]`"; ask the receiving function |
| A meeting with no decision | "No decision recorded; not a joint decision" |
| A function's agreement not shown | "Agreement of [function] not recorded `[GAP]`" |

## Never

- Never fill a date, a data cut, an owner, a receiver, a threshold, a status or a decision from memory or by inference; write "not given" and ask.
- Never treat absence of a record as absence of an event or a device.
