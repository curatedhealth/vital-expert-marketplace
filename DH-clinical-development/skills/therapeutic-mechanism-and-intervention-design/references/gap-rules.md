# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A research row states it | The fact plus the row id ("refinement is rare during efficacy evaluation, TM13") | None |
| Published method | [PAPER] row | "ORBIT milestones set a priori (TM57), DOI 10.1037/hea0000161" | Cite the DOI |
| Abstract only or [WF] | BCT Taxonomy v1, Bellg 2004, GRADE EtD Part 1 | "BCT Taxonomy v1, abstract only (TM51): technique list not read, label not checked" | Accept the person's label as theirs |
| Regulation about a named classification | TM119 to TM130 | "882.5801 requires ... (TM120); whether it applies to your product is a regulatory question `[GAP]`" | `dh-regulatory-and-quality` regulatory-pathway-and-classification |
| Not in the sources | Effect sizes, milestones, thresholds, dose rules, BCT names, the BCW eight-step design process, newer De Novo summaries (882.5804, 880.5735, 886.5500 risk tables) | "Not in this skill's sources `[GAP]`" | Ask the person; for a review, `dh-clinical-development` literature-and-real-world-evidence-review |
| Engagement benchmark or retention target | Any "good" completion, retention or usage rate | "No source sets an engagement benchmark or retention target; the figure is yours `[GAP]`" (research file SE "Not sourced") | Ask the person for their definition of effective engagement (SE87) |
| [WF] FTC rows | SE109 to SE113, SE117, SE118 | "FTC staff report, read through a summarizing fetch tool [WF]; not a rule (SE110)" | The owner the person names for consumer-protection law |
| Non-binding texts | DHAC materials (SE22 to SE29), MDCG guidance (SE60 to SE66) | "FDA advisory committee advice, non-binding (SE25)"; "MDCG 2025-10, not legally binding (SE63)" | None |
| Secondary citation | SE34 | "MHRA's citation of Gomez-Bergin 2023; the study itself was not read" | None |

## Library facts

| Situation | How to word it |
|---|---|
| `get_authorization` has no intended use | "Intended use not on the library record; taken from the decision summary (TM132)" or `[GAP]` |
| `search_devices` returns nothing | "Not found in the library store; absence is not evidence the device does not exist `[GAP]`" |
| `find_trial` finds no registration | "No ClinicalTrials.gov link found by the library; absence is not evidence the trial is unregistered" |
| Verify returns "supported" or "partial" | Reported as support only when the passage was read and says the same thing (N3) |
| Verify rates a regulator PDF inadmissible | "Not checkable through Verify (C1); quoted from row TMnn, read 20 October 2026" |

## The person's facts

| Situation | How to word it |
|---|---|
| Link with no measure | "Measure not named `[GAP]`"; becomes an assumption in B1 and a check in the monitoring skill |
| Population or exclusion not stated | "For whom `[GAP]`"; ask |
| TIDieR item not described | "?" as the checklist instructs (TM36); never N/A unless the person says so |
| No milestone or threshold | Report the signal and measure; no stopping verdict |
| Mechanic with no intended use or justification | "Usage, not adherence (SE92)"; effective engagement open |
| Hazard with no mitigation or threshold | "Mitigation not given" or "threshold not given; you set it before launch (SE63)"; ask |
| No owner named | "Owner not named"; ask. Never suggest a job title |

## Never

- Never call a link proven, validated or evidence-based on a precedent or a Verify status alone.
- Never fill a dose, a milestone or a threshold from memory.
- Never read silence as "not applicable".
