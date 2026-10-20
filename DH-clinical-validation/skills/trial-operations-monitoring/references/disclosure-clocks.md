# Registration and results clocks

Interpretive reference for task A2. CV rows are in `clinical-study-and-rwe-research.md`. Each clock is a fact about a date; whether the rule applies to the person's trial is the call of the owner the person names for registration, or owner not named.

## United States: 42 CFR Part 11 (law; read from the annual edition revised as of 1 October 2025, later amendments not reflected)

| Clock | Rule | Row |
|---|---|---|
| Which trials | Applicable device clinical trials: prospective controlled studies of health outcomes for 510(k), PMA or HDE devices, excluding small feasibility studies. Applicable drug clinical trials: controlled investigations other than phase 1. | CV142, CV143 |
| Registration | No later than 21 calendar days after the first participant is enrolled. | CV141 |
| Primary completion date | The date the final participant was examined or treated for final primary outcome data collection, completed or terminated. | CV144 |
| Results | No later than 1 year after the primary completion date. | CV145 |
| Delayed results | With a certification for a product not yet approved or cleared: 30 days after approval, clearance or a 210-day withdrawal; in all cases no later than 2 years after the certification. | CV146 |
| Extensions | For good cause, requested through ClinicalTrials.gov before the deadline; more than one allowed. | CV147 |
| Results content | All-cause mortality table; non-serious adverse events above 5 percent in any arm; protocol and statistical analysis plan with approved amendments. | CV148 |
| Updates | For trials initiated on or after 18 January 2017: registration information at least every 12 months; recruitment status within 30 days of a change. | CV149 |

## European Union: Regulation (EU) No 536/2014 (law; original Official Journal text)

The Regulation is on clinical trials on medicinal products for human use (CVB7). Device investigations: EU MDR rules not sourced `[GAP]`.

| Clock | Rule | Row |
|---|---|---|
| End of trial | Last visit of the last subject, or a later point the protocol defines. | CV150 |
| End-of-trial notice | Through the EU portal within 15 days of the end of the trial in each Member State, and for the last Member State or third country. | CV151 |
| Results summary | Within one year of the end of the trial in all Member States, with a lay summary (Annexes IV and V); later only for scientific reasons stated in the protocol. | CV152 |
| Clinical study report | Within 30 days after the marketing authorization decision or withdrawal, if the trial supports one. | CV153 |
| Halted trials and interim results | A halt not resumed within two years becomes the end date; a protocol-specified interim analysis triggers a results summary within one year of that date. | CV154 |
| Pediatric timeline | Not in Article 37 as read; from Commission guidance not downloaded. | `[GAP]` |
| Dates of application and transition | Not stated as facts here. | `[GAP]` |

## Journals and funders

| Clock | Rule | Row |
|---|---|---|
| ICMJE registration | At or before first patient consent; the date materials were first submitted counts. Stricter than US law. | CV132 |
| ICMJE data sharing | Statement required in results manuscripts since 1 July 2018; trials enrolling from 1 January 2019 include a data sharing plan in registration. | CV135, CV136 |
| Registry results are not prior publication | Results posted as a brief structured abstract or tables in a qualifying registry. | CV137 |
| WHO joint statement (18 May 2017) | Signatory funders work toward 12 months from primary completion for registry summary results and 24 months (indicative) for journal publication. A funder pledge, not law. | CV140 |

## How to state a clock

"Results under 42 CFR 11.44(a) are due 1 year after the primary completion date you gave (30 September 2025), so on 30 September 2026; not recorded as submitted; the date passed 19 days before 19 October 2026 (CV145). Check whether a delay certification or an extension applies (CV146, CV147)." Never call a clock "missed" or a trial "non-compliant": the owner the person names for registration, or owner not named decides that, with the registry record in hand.

## What the library can and cannot tell you

`literature.find_trial` returns registration status, phase, sponsor and linked publications, but no registration, start, primary completion or results-posted dates (`references/tools.md`). Every date in a clock comes from the person or from the registry page they check.
