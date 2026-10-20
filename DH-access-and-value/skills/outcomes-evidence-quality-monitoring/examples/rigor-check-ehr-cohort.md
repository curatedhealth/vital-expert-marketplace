# Worked run: rigor check of a published EHR cohort, then tally and repair

Run on 19 October 2026. A1 uses a real published study and live library calls; condensed outputs and the quoted passages are in `examples/live_calls_2026-10-19.json`. A2 and B1 use **illustrative** judgments and an illustrative rule (anonymized studies S1 to S4), written for this example; they are not an assessment of any published paper.

---

## A1 Study rigor check (short mode)

Request: "We want to cite Palacios et al. 2024 in our eating-disorder app's value dossier. How strong is the emergency department result?"

**Answer.** The paper describes a retrospective cohort in one US health system's electronic records, comparing patients given the app with "the control group in the year prior" (a historical comparator), adjusted by inverse probability of treatment weighting (abstract, Methods). The library labels it `cohort` (0.45) in one call and `preprint` (0.95) in another; the paper's methods decide. Tool: ROBINS-I (2016), at outcome level as EU JCA asks (ES-75, DOI 10.1136/bmj.i4919; ES-164). Facts to weigh most: confounding with a historical comparator, missing data (complete-case analysis), and selection of the reported result (no protocol or registration found). Facts only; the levels are your reviewers'.

| Domain | Facts from the paper (locator) | Reviewer level |
|---|---|---|
| Confounding | Weighting by inverse probability of treatment; comparator from the year before implementation (abstract, Methods) | |
| Selection of participants | Outcomes over 6 months after implementation against analogous data from the year prior (abstract) | |
| Missing data | "A complete case analysis was performed on the primary outcomes"; utilization analysis 1104 (app 165, usual care 939) (Methods) | |
| Measurement of outcomes | Emergency department visits from the health system's records; some partner programs "could not be extracted" (Discussion, limitations) | |
| Selection of the reported result | No protocol, analysis plan or registration statement found in the full text read; library found no ClinicalTrials.gov link `[GAP]` | |
| Other domains | Table 1 sets out a "Target trial protocol (specification and emulation)"; classification and deviations to be read there | |

Open items:
1. Registration not confirmed `[GAP]`: ask the authors or search ENCePP, which the library does not cover.
2. Conflicts as stated (Conflicts of Interest): three authors "are paid employees of Recovery Record, Inc, and hold shares in the company"; "Work contributed by JPK was done as a paid independent consultant". Facts for the reviewers, not a judgment.
3. Context: as non-randomized evidence, the GRADE starting point is low (ES-90, ES-100); the library's draft says the same and leaves every factor empty.

**Record.** Fact sheet for your reviewers. No judgment made. Clears it: owner not named. The record is built with verify.build_record once that named person clears it; until then, uncleared draft. AI-assisted draft.

Calls: `literature.get_record {doi: "10.2196/59145"}`; `literature.classify_study {record}`; `literature.find_trial {record}`; `verify.check_currency {doi: "10.2196/59145"}` (current, Crossref); `literature.grade_evidence {record, standard: "grade"}` (draft low). Full text: Europe PMC PMC11635337.

---

## A2 Study score (illustrative judgments and rule)

`python3 scripts/rigor_tally.py examples/illustrative_judgments.csv examples/illustrative_rule.json` gave `examples/illustrative_tally.md`:

| Study | Result | Tool | Overall | Score (your rule) |
|---|---|---|---|---|
| S1 | ED visits 6 months | ROBINS-I | Serious | 1.89 |
| S2 | Hypnotic prescriptions 9 months | ROBINS-I | Serious | 2.0 |
| S3 | Symptom change before-after | ROBINS-I | Critical | not computed |
| S4 | ISI at 8 weeks | RoB2 | Some concerns | 2.67 |

S3 is critical in confounding, so it is excluded from any synthesis (ES-77); five of its domains were not judged. ROBINS-I overall levels below critical follow the person's "least favorable domain" rule, which the sourced rows do not fix. S4 has two domains at "Some concerns": ES-74 lets the reviewers judge it High overall, and that call is theirs. Scores are the person's rule, not a validated score (HE-005, ES-94). Run with no rule, the same file gives "Your rule not given `[GAP]`" for S1 and S2 and no scores.

---

## B1 Evidence repair (illustrative rule: "no cited result at serious or critical risk"; owner named: Head of Evidence)

**Answer.** Not met for S1, S2 and S3. The weakest point is S2's reported result: its primary window changed after outcome access, a prespecification weakness no re-analysis can repair (HE-026, HE-028; Berger et al. 2017, DOI 10.1002/pds.4297). Options: a deviation statement now (HE-028); a new prespecified study in a different data source (HE-029); S3 needs a new design, not a re-analysis (ES-77, ES-78). Owner: Head of Evidence, as named.

**Record.** Repair draft. Rules and owners are yours. Clears it: owner not named. The record is built with verify.build_record once that named person clears it; until then, uncleared draft. AI-assisted draft.
