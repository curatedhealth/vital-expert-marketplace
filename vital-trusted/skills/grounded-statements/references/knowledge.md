# Knowledge: grounded-statements

This file is the single home for this skill's sourced rules, failure patterns, gap
wording and failure modes. Where the same rule or pattern appeared in more than one
earlier file, one copy is kept.

## Contents

- Part 1: Rules (sourced, with scope and confirmation status)
- Part 2: Failure patterns (before and after)
- Part 3: Gap rules (shared wording, with this skill's cases)
- Part 4: Failure modes (detection questions)

## Part 1: Rules

Each rule names its primary source, the date and how it was confirmed. A rule marked
`[CHECK]` has not yet been confirmed against the primary document and is applied as good
practice, not cited as a requirement (TR-H8).

Last reviewed: 20 October 2026.

| Id | Rule | Primary source | Status |
|---|---|---|---|
| R1 | For binary outcomes in a randomized trial, report both absolute and relative effect size, with each group's result and the precision of the estimate (for example a 95% confidence interval). | CONSORT 2025 statement, checklist item 26 (Nature Medicine, doi:10.1038/s41591-025-03635-5, supplementary table 1; published simultaneously in several journals, 2025). Replaces CONSORT 2010 item 17b. | Confirmed from the CONSORT 2025 supplementary checklist on 20 October 2026. Exact publication day `[CHECK]`. |
| R2 | In US direct-to-consumer promotional labeling and advertising, present probabilities as absolute frequencies or percentages; when a relative figure is used, give the corresponding absolute figures prominently; give control-group information where there is a control group. | FDA guidance, Presenting Quantitative Efficacy and Risk Information in Direct-to-Consumer (DTC) Promotional Labeling and Advertisements, first issued final June 2023; official copy dated December 2023, Revision 1 (fda.gov/media/169803). Non-binding guidance. | Confirmed 20 October 2026 from the official FDA copy, read during the honest-framing build (see `honest-framing/references/knowledge.md`, R1 to R3, for the sections used). Scope is US DTC; elsewhere apply as good practice only. |
| R3 | Report all other analyses, including subgroup and sensitivity analyses, distinguishing pre-specified from post hoc. | CONSORT 2025, item 28 (same source as R1). | Confirmed 20 October 2026. |
| R4 | Report all harms or unintended events in each group. | CONSORT 2025, item 27 (same source as R1). | Confirmed 20 October 2026. Used here only to stop harms being described for one arm as if for both. Balance of harms in a document is `balanced-evidence`. |
| R5 | A surrogate endpoint is a marker used in place of a clinical outcome; it is not itself a measure of how a patient feels, functions or survives. | FDA-NIH Biomarker Working Group, BEST (Biomarkers, EndpointS, and other Tools) Resource, NCBI Bookshelf NBK338448. | `[CHECK]`: definition wording and last-update date to be quoted from the resource; page could not be read on 20 October 2026. |
| R6 | Describe the effect being estimated in terms of population, variable (endpoint), handling of intercurrent events and the summary measure. | ICH E9(R1) addendum on estimands and sensitivity analysis. | `[CHECK]`: adoption date and section wording to be confirmed from the ICH document. |

### How to use these rules in output

- When a rule is confirmed, the repair note may cite it ("CONSORT 2025 item 26").
- When a rule is `[CHECK]`, state the practice without citing it as a requirement:
  "Absolute figures are given alongside the relative reduction so the size of the effect
  is clear."
- Never extend a rule beyond its scope. R2 is US direct-to-consumer; it is not a rule for
  a scientific publication or a non-US market.
- R1 and R2 ask for each group's result. They do not license adding a derived figure the
  person did not ask for. Give both arm rates; offer the difference, and add it only on
  request, labeled "calculated from the two figures you supplied".

## Part 2: Failure patterns

Each pattern: what it looks like, why it fails, before and after, and the rule it breaks.
All examples are invented for teaching; no real product, trial or person.

### Contents

- Fabrication F1–F7
- Business work B1–B6
- Numbers N1–N8
- Methods M1–M9

Pattern ids are for this file only. In what the person reads, describe the problem in
plain words (TR-H13).

### Fabrication

**F1 The helpful number.** A vague source statement becomes a precise figure.
Why: the figure is not in the source, so nobody can check it there.
Before: "Most patients responded (68%)." Source: "the majority of patients responded".
After: "Most patients responded [GAP: not supplied; response rate; supply the results table]." (TR-H1, TR-H2)

**F2 The invented superlative.** "First", "only", "largest", "leading" added for impact.
Why: superlatives are checked first in review and are rarely in the source.
Before: "the largest trial in this disease". After: "a phase 3 trial of 412 patients" (as supplied). (TR-H1)

**F3 The remembered guideline.** A guideline, recommendation or regulator decision named from memory.
Why: names, years and recommendation grades drift; the reviewer needs the document.
Before: "recommended first line by the 2024 society guideline". After: "[GAP: not supplied; guideline and recommendation; supply the guideline]". (TR-H1, TR-H8)

**F4 The phantom citation.** A reference that looks real but was not supplied.
Why: invented citations are the most damaging fabrication; they look like evidence.
Before: "(Smith et al., 2023)". After: cite only supplied sources; otherwise a gap. (TR-H1)

**F5 The supplied mechanism.** A reason or mechanism the source does not state.
Before: "Because it blocks the receptor, symptoms improved within days." After: "Symptoms improved by week 2" (as supplied), mechanism omitted or sourced. (TR-H1)

**F6 The quote that was a paraphrase.** Quotation marks around words the source did not use.
After: quote exactly or remove the quotation marks. (TR-H1)

**F7 The undated "current".** "Current standard of care", "latest data", "now approved" with no date.
After: date it from the source, or `[GAP: out of date or unclear date; …]`. (TR-H1)

### Business work

Patterns most common in board updates, business reviews, brand plans and value stories.

**B1 The forecast that became an actual.** A plan or forecast figure written as if achieved.
Before: "Q4 sales reached CHF 5.1 million." Source: "Q4 forecast CHF 5.1 million".
After: "Q4 sales are forecast at CHF 5.1 million." (TR-H1)

**B2 Share change in percent.** "Market share grew 20%" when it went from 10% to 12%.
After: "Market share rose from 10% to 12%." If the person asks for the change, it is 2 percentage points, labeled as calculated from the two figures they supplied. (TR-H13)

**B3 Mismatched periods.** This quarter compared with last year's full-year average, or
year to date compared with a full year.
After: compare like with like and name both periods. (TR-H1)

**B4 The invented cause.** "Sales rose because of the new campaign" when the notes only
show both happened.
After: "Sales rose in the quarter the campaign launched [GAP: not supplied; analysis
linking the two; supply it, or keep this as timing only]." (TR-H1)

**B5 The meeting quote nobody said.** Notes say "payer concerned about budget"; the draft
says "the payer told us the price is too high".
After: report the notes' wording and attribute it as the notes do. (TR-H1)

**B6 The rounded total.** Regional figures that do not add up to the stated total, with no
explanation.
After: fix the arithmetic or note "totals may not add due to rounding". (TR-H1)

### Numbers

**N1 Relative only.** "Reduced the risk by 50%" with no absolute figures.
Why: a 50% relative reduction can mean 2% to 1% or 40% to 20%. The reader cannot judge size.
After: "Events occurred in 1.0% of the treatment arm and 2.0% of placebo (relative reduction 50%, as reported)." The difference in points is offered, not added, unless the person asks. (R1, R2)

**N2 Percent for percentage points.** "Response rose by 10%" when it went from 30% to 40%.
After: "rose from 30% to 40%". A difference in points is given only when asked, and labeled as calculated. (R1)

**N3 The missing frame.** A figure with no population, arm, timepoint or denominator.
After: "38% of patients in the treatment arm at week 24 (n = 206)". (TR-H1)

**N4 Two values for one quantity.** Enrollment 412 in the summary and 408 in the methods.
After: restore the source value; if the source itself differs (randomized vs analyzed), say which. (TR-H1)

**N5 Flattering rounding.** 0.046 written as "p < 0.04"; 14.6% written as "15%" in one place and "14%" in another.
After: report as the source does, consistently. (TR-H1)

**N6 Counts that do not add up.** Subgroups summing to more than the total; percentages that do not match their counts.
After: recompute from supplied counts; flag the source inconsistency if it is in the source. (TR-H7)

**N7 The underived NNT.** An NNT stated without its inputs, or computed from a relative figure.
After: remove the unsupported NNT and give the arm rates. Derive an NNT only when the person asks, from arm rates only, labeled as calculated, with inputs and timepoint. (R1)

**N8 Significance as size.** "Highly significant" used to mean a large effect.
After: give the effect size and its interval; describe significance only as the source does. (R1)

### Methods

**M1 Upgraded design.** Single-arm described as controlled; observational as a trial; open-label as blinded.
After: the design exactly as the source names it. (R6)

**M2 Subgroup as population.** A subgroup result presented as the overall result.
After: "In the pre-specified subgroup of patients aged 65 and over…", with whether it was pre-specified. (R3)

**M3 Secondary as primary.** A secondary endpoint result presented as the main finding while the primary is omitted.
After: lead with the primary result as reported; give secondary results as secondary. (R6)

**M4 Surrogate as outcome.** A biomarker or response result written as a clinical benefit.
Before: "improved survival" from a response-rate result. After: "improved response rate; survival data [GAP: not supplied; survival results; supply the survival analysis]". (R5)

**M5 Association as cause.** "Reduced hospitalizations" from an observational association.
After: "was associated with fewer hospitalizations". (R6)

**M6 Non-significant as no difference or as a trend.** "No difference" or "trend toward benefit" where the source says neither.
After: report the estimate and interval and the source's own wording. (R1)

**M7 Conflated studies or timepoints.** Results from two studies, or two timepoints, merged into one sentence.
After: one study and one timepoint per statement. (TR-H1)

**M8 Harms for one arm as if for both.** Adverse event rates from the treatment arm stated without the comparator's.
After: give both arms as the source reports them. (R4)

**M9 A small panel as everyone.** "Physicians prefer option A" from 8 of 12 advisory
board members, or "patients find it easy" from a small survey.
After: "8 of 12 advisory board members preferred option A." (TR-H1)

## Part 3: Gap rules

> **Where the marker belongs.** Use the `[GAP: …]` marker only inside a drafted deliverable. In notes, open-item lists and explanations, write the gap as a plain sentence ("Still missing: …, from …"). See `trusted-capability-map/references/knowledge.md` (Part 2).

Same format and classes as every TRUSTED skill:
`[GAP: <class>; <what is missing>; <what would close it>]`

| Class | Typical case in this skill |
|---|---|
| `not supplied` | A figure, design detail, guideline or citation the draft needs and the material lacks |
| `conflicting` | Two supplied sources give different values for the same quantity |
| `out of date or unclear date` | "Current", "latest" or "now" with no date in the source |
| `not checkable here` | Whether a sentence matches its passage word for word, when no passage was supplied |
| `needs a decision` | Which population, endpoint or timepoint the person wants reported, when the material holds several |

Wording rules:

- Name the exact item: "95% CI for the primary endpoint at week 52", not "statistics".
- Never hint at a value inside a gap.
- "The source does not report X" is a finding only when the complete source was supplied
  and read. Otherwise use `not supplied`.

## Part 4: Failure modes

Skill-specific rows for this skill. FM-08 is shared by every skill and covers Prove honesty.

| Id | Failure mode | Detection question | Documented for | Source | Status |
|---|---|---|---|---|---|
| FM-GS-01 | Model-memory fill | Was a gap filled from training knowledge not the passage? | Grounding | TR-H1 | VERIFIED practice |
| FM-GS-02 | Exploratory as primary | Was a secondary/exploratory result stated as the primary finding? | Hierarchy | TRUSTED grounded | [CHECK] |
| FM-GS-03 | Silent on non-significant primary | Was a failed primary endpoint omitted beside a positive secondary? | Completeness | TRUSTED grounded | PARTIAL |
| FM-08 | Hand-check result treated as world-truth | Is a hand-check result described as "true in the world"? | Prove honesty | TR-H3 | VERIFIED |
