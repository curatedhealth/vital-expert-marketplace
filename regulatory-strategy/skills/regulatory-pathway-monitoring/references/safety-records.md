# Reading safety records

Interpretive reference for task A2. Row prefixes: VG and QS = `quality-systems-sources.md`; RP = `reg-pathways-sources.md`. All rows read 19 October 2026.

## What the library holds

| Source | What a row is | What it is not |
|---|---|---|
| FDA enforcement recalls (`fda_recall`) | A recall whose product text mentions software, algorithm, application, firmware or app, with the event date, the recall classification as the source labels it ("Class II"), and the firm's stated reason. | Not the device class. FDA's definitions of recall classes are not in the research rows `[GAP]`; quote the label, do not explain it from memory. |
| MAUDE counts (`maude_counts`) | Number of reports received per product code per year. The tool's own basis: "counts are reports, not confirmed events". | Not a count of incidents, injuries or failures. Not attributable to one product when a code holds several. |
| MHRA alerts | Medical safety alerts matched by manufacturer name or software terms. | Not GB registrations. |
| Swissmedic field safety actions | Not loaded `[GAP]`. | |
| EUDAMED vigilance | Not available: the vigilance module is not yet live (RP EU-38). | |

## Rules for describing a record

1. Quote the record's own words for what happened. "The firm's stated reason: 'Due to a software issue, patients with a urine drug screen (UDS) received access to a contingency management wheel spin ... regardless of the UDS results.'" Do not paraphrase into a cause.
2. Name the product the record names. A search by product code can return recalls for products in other codes from the same manufacturer (a QVO search returned two reSET recalls; reSET's record is in code PWE). Check each row's product before attributing it.
3. No causal claims. A recall, a report or an alert does not establish that the device caused harm. A MAUDE report is a report.
4. No rates without a denominator. Recalls and reports per product have no installed base in the library; never turn a count into a rate or a comparison of safety between products.
5. Absence is a gap. No row means none in the library's copy, never "no safety issues".

## Regulatory clocks the person's own events run on (for context, not for public records)

| Event | EU (MDR) | GB | US |
|---|---|---|---|
| Serious incident, general | Immediately once causality is established or reasonably possible, no later than 15 days after awareness (VG4) | 15 days (VG28) | 30 calendar days (VG17) |
| Serious public health threat | 2 days (VG5) | 2 days (VG28) | 5 work days where remedial action is needed (VG18) |
| Death or unanticipated serious deterioration | 10 days (VG6) | 10 days (VG28) | 30 calendar days (VG17) |
| Corrections and removals | FSCA reported in advance except in urgency (VG8) | | 10 working days from initiation (VG22) |

Counting: EU deadlines are calendar days with awareness as day 0 (VG12); awareness is when the first employee or representative receives the information (VG11). Software-relevant MDCG points: harm from decisions based on incorrect device output is indirect harm and reportable when it meets serious incident criteria (VG14); a software error giving an incorrect assessment is a malfunction example (VG15). US software points: a change pushed to installed software is a correction (VG25); a correction or removal not reported to FDA still needs a recorded justification reviewed by a designated person (VG24); MDR event files document the reasoning behind each reportable or non-reportable decision (VG21). Improvements that do not reduce a risk to health are exempt (VG23). Trends in non-serious incidents are reported under the method set in the PMS plan (VG9).

These clocks apply to the person's own vigilance system. Whether an event is reportable is decided by the person's vigilance owner; this skill never decides it.

## Other public monitoring sources (not in the library)

- FDA Data Dashboard: inspections, compliance actions, recalls by year and classification (QS50).
- Form 483 observation spreadsheets FY 2006 to FY 2025; not a complete list of observations (QS51 to QS54).
