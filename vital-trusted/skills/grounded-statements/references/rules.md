# Primary rules this skill enforces

Each rule names its primary source, the date and how it was confirmed. A rule marked
`[CHECK]` has not yet been confirmed against the primary document and is applied as good
practice, not cited as a requirement (TR-H8).

Last reviewed: 20 October 2026.

| Id | Rule | Primary source | Status |
|---|---|---|---|
| R1 | For binary outcomes in a randomized trial, report both absolute and relative effect size, with each group's result and the precision of the estimate (for example a 95% confidence interval). | CONSORT 2025 statement, checklist item 26 (Nature Medicine, doi:10.1038/s41591-025-03635-5, supplementary table 1; published simultaneously in several journals, 2025). Replaces CONSORT 2010 item 17b. | Confirmed from the CONSORT 2025 supplementary checklist on 20 October 2026. Exact publication day `[CHECK]`. |
| R2 | In US direct-to-consumer promotional labeling and advertising, present probabilities as absolute frequencies or percentages; when a relative figure is used, give the corresponding absolute figures prominently; give control-group information where there is a control group. | FDA guidance, Presenting Quantitative Efficacy and Risk Information in Direct-to-Consumer (DTC) Promotional Labeling and Advertisements, first issued final June 2023; official copy dated December 2023, Revision 1 (fda.gov/media/169803). Non-binding guidance. | Confirmed 20 October 2026 from the official FDA copy, read during the honest-framing build (see that skill's rules.md for the sections used). Scope is US DTC; elsewhere apply as good practice only. |
| R3 | Report all other analyses, including subgroup and sensitivity analyses, distinguishing pre-specified from post hoc. | CONSORT 2025, item 28 (same source as R1). | Confirmed 20 October 2026. |
| R4 | Report all harms or unintended events in each group. | CONSORT 2025, item 27 (same source as R1). | Confirmed 20 October 2026. Used here only to stop harms being described for one arm as if for both. Balance of harms in a document is `balanced-evidence`. |
| R5 | A surrogate endpoint is a marker used in place of a clinical outcome; it is not itself a measure of how a patient feels, functions or survives. | FDA-NIH Biomarker Working Group, BEST (Biomarkers, EndpointS, and other Tools) Resource, NCBI Bookshelf NBK338448. | `[CHECK]`: definition wording and last-update date to be quoted from the resource; page could not be read on 20 October 2026. |
| R6 | Describe the effect being estimated in terms of population, variable (endpoint), handling of intercurrent events and the summary measure. | ICH E9(R1) addendum on estimands and sensitivity analysis. | `[CHECK]`: adoption date and section wording to be confirmed from the ICH document. |

## How to use these rules in output

- When a rule is confirmed, the repair note may cite it ("CONSORT 2025 item 26").
- When a rule is `[CHECK]`, state the practice without citing it as a requirement:
  "Absolute figures are given alongside the relative reduction so the size of the effect
  is clear."
- Never extend a rule beyond its scope. R2 is US direct-to-consumer; it is not a rule for
  a scientific publication or a non-US market.
