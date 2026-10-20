# A2 Personalization rule specification

Framework task: DH-01.06.1.1, Part A, task A2. Carries the old tasks "DH-01.06.1.1.1 Adaptive Logic Design", "DH-01.06.1.1.2 Personalisation Model Development" and "DH-01.06.1.1.3 Tailoring Rule Validation" (old titles in their original spelling).

## What this task delivers

The personalization engine of a digital therapeutic or digital health product written as a specification a rule engine can implement: for each decision point, the allowed options, the tailoring variables and how they are measured, the decision rule, what the rule does when tailoring data are missing, the proximal outcome and the engagement or fatigue outcome; a gap check of that table (`scripts/model_check.py rules`); the safety boundaries the person sets for a model that keeps learning; and the experiment that would test each rule (micro-randomized trial or MOST). It answers "what exactly does our engine decide, from what, within which bounds, and how do we test that the rules do what we think?"

Why it matters: "when one or more tailoring variables are measured unreliably, the decision rule will perform little better than randomly selecting an intervention option" (Nahum-Shani et al. 2018, DOI 10.1007/s12160-016-9830-8, TM88). A rule with no missing-data behavior, or one that can deliver an option outside the allowed set, is unsafe drift waiting to happen.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `behavior-change-designer` (old DH-01.06.1.1.1); `ai-ml-governance-director` (old DH-01.06.1.1.2 and .3). Work as an engine specification analyst who writes the person's rules down and checks them |
| Skill | DH-01.06.1.1 Part A, Personalization rule specification |
| Workflow | The steps below |
| Knowledge | `references/personalization-rules.md`; rows TM30, TM38, TM66 to TM90, TM141 to TM143, DA-48, DA-63, DA-67, EU-05, US-03 to US-13, US-31; `references/governance.md` |
| Tools | `scripts/model_check.py rules`, `words`. No library call |
| Prompt | This guide |
| Template | `assets/personalization-rule-specification-output.md` |
| Input | The request and its context: the product and its distal outcome, the decision points, options, tailoring variables and their sources, the rules as the team wrote them (or a rule table CSV: decision_point, tailoring_variables, measurement_validity, options_allowed, options_in_rule, option_on_missing, proximal_outcome, engagement_outcome), safety bounds, whether the engine learns after release, markets |
| Governance | `references/governance.md`; the person sets every bound and objective |
| Catalogue job | none (no saved `list_jobs` entry for personalization design; needs a live check) |

## The rule that shapes this task: the person's rules, written down exactly

The model writes the team's rules as they gave them, fills nothing in, and flags every element the rows say a specification needs. It never invents an option, a dose, a bound or an efficacy claim; any proposal is labeled "proposed" and not added to the table until the person confirms. The therapeutic content and its claims stay with `dh-clinical-development` therapeutic-mechanism-and-intervention-design.

## Workflow

### Step 1. Distal outcome and decision points (old "Adaptive Logic Design")

Write the distal outcome (TM83) and each decision point (TM78) in the person's words. Rules already named are listed as named; missing rules are `[GAP]`. No efficacy claim is added (old guardrail: "Do not invent an efficacy claim").

### Step 2. The rule table (old "Personalisation Model Development")

For each decision point: allowed options (TM79), tailoring variables and whether each is from active or passive assessment (TM80, TM81), the measurement validity the person states (TM88), the decision rule (TM82), the option on missing data (TM89), the proximal outcome (TM84) and the engagement or fatigue outcome (TM87). With a CSV, run `python3 scripts/model_check.py rules --rules RULES.csv` and report flags R0 to R7 verbatim. Each flag is a specification gap, never a safety verdict. Where the person's rule uses a learned model (a classifier or a policy that is trained), say so and send its development and validation to A1 and B1 of this skill.

### Step 3. Safety boundaries the person sets

Write down the bounds the person gives: options never delivered, maximum frequency or dose per period, who can change a rule. If the engine keeps learning after release, add the EU AI Act duty on feedback loops (Article 15(4), DA-63) and bias examination where outputs feed future inputs (Article 10(2)(f), DA-48), with the date they apply to AI in Annex I devices, 2 August 2028 as amended by Regulation (EU) 2026/1744 (DA-67). PCCP guiding principle 1 includes mechanisms to detect and revert a failing change (US-31). Bound values are "not given" unless the person gives them.

### Step 4. How each rule will be tested (old "Tailoring Rule Validation")

Name the test design the person chooses for each rule: a micro-randomized trial randomizes options at decision points to estimate causal effects on proximal outcomes (TM90); MOST runs an optimization trial on components against an optimization objective, then evaluates the package (Collins, Kugler and Gwadz 2016, DOI 10.1007/s10461-015-1145-4, TM66 to TM73, TM76; Guastaferro and Collins 2021, DOI 10.1177/26334895211054363, TM74, TM75). Say that comparisons from a deployed log where the rule chose the option are descriptive, not causal (TM90). The objective and the acceptance rule are the person's. Monitoring the deployed rules is `model-performance-and-drift-monitoring` (this pack) A2.

### Step 5. Change control route

If the product is, or may be, a device and the rules or the learned model will change after release, say that whether those changes fit a PCCP (US-03 to US-13) or an EU pre-determined change (Article 43(4), EU-05) is `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control. Report TIDieR item 9 for planned tailoring (TM30) when the person is writing a protocol or paper.

## Build the output

Follow `assets/personalization-rule-specification-output.md`. Answer first: how many decision points, how many flags and the ones that matter most (missing-data rule absent, options outside the allowed set), the bounds still not given, and the test design for each rule (or "not given"). Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/model_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every option, rule, bound and objective is the person's or labeled "proposed"; nothing proposed is in the table.
- Every flag comes from the script output or a stated fact.
- No efficacy, safety or engagement claim is made.
- Every fact names its source and date in plain words with the row id after it; [PAPER] rows carry the DOI.
- `python3 scripts/model_check.py words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Therapeutic mechanism, engagement mechanics and safety by design of the intervention: `dh-clinical-development` therapeutic-mechanism-and-intervention-design.
- Evidence behind a feature or claim: `dh-clinical-development` evidence-to-intervention-translation.
- Platform architecture and the release pipeline that ships the rules: `medical-software-lifecycle-and-delivery` (this pack).
- PCCP or pre-determined changes: `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control.
