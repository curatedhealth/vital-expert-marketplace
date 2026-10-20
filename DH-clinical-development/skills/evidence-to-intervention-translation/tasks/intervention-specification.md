# A2 Intervention specification

Framework task: DH-01.01.4.1, Part A, task A2. Replaces the earlier "Intervention rule" section (DH-01.01.4.1.2).

## What this task delivers

A specification draft that turns sourced claims into what the product does: the program theory (components, mechanisms, context, proximal and distal outcomes), the intervention described item by item against TIDieR, the behavior change functions each component serves, every decision rule written with its decision point, options, tailoring variables, rule and missing-data behavior, and the user-facing text that goes with each rule, matched to its source. Each element traces to a claim in the A1 map; anything that does not is open.

Why it matters: several FDA special controls for software therapies require a model of therapy validated "as implemented by the device" and software documentation showing the device implements it (TM120, TM121, TM127 to TM129). A specification that names the model, the components and the rules is the bridge between the evidence and the software requirements.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Validation Director (`clinical-validation-director`) |
| Skill | DH-01.01.4.1 Part A, Intervention specification |
| Workflow | The steps below |
| Knowledge | `references/intervention-spec-rules.md`; rows TM4 to TM14, TM19, TM20, TM22 to TM36, TM39 to TM53, TM54 to TM76, TM77 to TM90, TM119 to TM130, TM134, TM142, TM149, TM150 |
| Tools | None required. `scripts/spec_check.py` on the specification JSON. A1's tools only if a component lacks a claim |
| Prompt | This guide |
| Template | `assets/intervention-spec-output.md` |
| Input | The request and its context: the A1 claim map, the treatment manual or protocol being translated, the features planned, the population and the regimen the person intends |
| Governance | `references/governance.md`; the person chooses the mechanism, components, dose and permissible variation |
| Catalogue job | none |

## Read the request

- **What is being translated.** A face-to-face therapy into an app (as reSET translated the community reinforcement approach, TM133), an existing app into a new population (TM20), or a new intervention from theory.
- **Claim map.** If A1 has not been run, run it in short mode first for the claims the components rest on.
- **Development stage.** Which framework the person works in, if any: MRC/NIHR phases (TM2), ORBIT phases (TM54 to TM64) or MOST (TM66 to TM76). Ask; do not assign one, and do not write "none required": if the person did not say, it is "not given".
- **Adaptive features.** Does anything change by person, time or state? If yes, Step 5 applies in full.

## Workflow

### Step 1. Write the program theory

Lay out the five parts the MRC/NIHR framework names (TM6, DOI 10.1136/bmj.n2061): key components, how they interact, mechanisms (causal links from components to outcomes, TM8), the contextual features that influence the mechanisms (TM9), and the outcomes. Fill each from the person's material and the A1 sources; leave the rest `[GAP]`. Label the whole "program theory: hypothesis until tested" (TM7). A logic model diagram may be offered; it carries the same label.

### Step 2. Describe the intervention by TIDieR

Fill items 1 to 9 and 11 (TM22 to TM30, TM32, DOI 10.1136/bmj.g1687). Fill each item first from what the person describes (procedures, who provides, how, where, when and how much, tailoring); an item the person described is filled even when the claim behind it is open, and the open claim is marked in the Status column. When a clinician-delivered manual becomes an app, item 5 (who provided) changes from clinician to app; say so. For example, a manual the person describes as "6 weekly sessions: sleep restriction, stimulus control, cognitive restructuring, sleep hygiene, relapse prevention" with "windows adapted weekly from the sleep diary" fills item 4 (procedures: the five components), item 5 (clinician to app), item 6 (app), item 8 (6 weekly sessions) and item 9 (weekly window from the diary), with the thresholds inside item 9 still open. In the spec JSON, write a described item's text and add "[GAP]" only for the part still open: the script counts it filled, with open parts. Items 10 and 12 cannot be completed before delivery (TM34); say so. Item 2 is where the mechanism is stated (TM23); item 8 is the dose (sessions, schedule, duration, intensity, TM29); item 9 is tailoring (TM30). Use N/A only where an item does not apply (TM36). For a German DiGA, the application also states aim, mode of action, content, the sources of medical content and the minimum duration of use (TM149, TM150).

### Step 3. Name the behavior change functions

Where the product aims to change behavior, map each component to the COM-B source it targets (capability, opportunity, motivation, six subcomponents, TM40 to TM44, DOI 10.1186/1748-5908-6-42) and the intervention function it performs (nine functions, TM46 to TM48; one component may serve several, TM50). If the person names specific behavior change techniques, BCT Taxonomy v1 has 93 techniques in 16 groups (TM51), but the full list was not read: label any technique name as the person's, with "BCTTv1 abstract only" (TM51 to TM53).

### Step 4. Fix the dose and regimen

From the A1 sources, copy the dose that was tested (sessions, schedule, duration). The product dose is the person's; where it differs from the tested dose, mark the difference for B1. Several classifications require labeling of the regimen or of treatment length supported by clinical testing (TM126, TM130); whether they apply is a question for the owner the person names for regulatory status, or owner not named.

### Step 5. Write each decision rule

For every place the product decides what to show, when, or to whom, write the five parts (TM77 to TM82, TM89, DOI 10.1007/s12160-016-9830-8): decision point, intervention options, tailoring variables (active or passive, TM81), the rule linking them, and what the rule does when tailoring data are missing (TM89). Add the proximal outcome each option aims at, including engagement and fatigue (TM84, TM87). Note that an unreliable or invalid tailoring variable can make a rule little better than random or counterproductive (TM88): name the measurement evidence the person holds for each variable, or `[GAP]`. Each rule traces to one or more claims in A1. A rule resting on a [GAP] or refused claim is not written; it is listed as blocked (old DH-01.01.4.1.1 rule).

### Step 6. Write the user-facing text for each rule

For each rule, draft the text the user sees, matched to the source's population, verb and caveats. Mark it "draft for the owner". Where the source hedges ("might", "may not"), keep the hedge or flag it for the owner. The text is checked by the fidelity skill later.

### Step 7. Separate core from adaptable

Name, as "proposed", which components are core (fidelity expected) and which may vary, and the permitted and prohibited variation (TM11, TM12, TM117). Standardizing function rather than form is an option the source names (TM12). The person decides. This becomes the input to the fidelity rules in DH-01.01.4.2.

### Step 8. Run the check

Write the specification as JSON in the shape `scripts/spec_check.py` documents and run `python3 scripts/spec_check.py SPEC.json`. Report the open counts and every flagged rule. The count is a reading aid, not a quality score.

## Build the output

Follow `assets/intervention-spec-output.md`. Answer first: what the specification covers, how many TIDieR items and rule parts are open, which rules are blocked, and the decisions waiting for the person. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The program theory is labeled a hypothesis; no component is called effective.
- Every rule has its five parts or the open part is named; every rule traces to a sourced claim or is listed as blocked.
- The population and dose in the specification are compared with the source's; differences go to B1.
- BCTTv1 and other abstract-only rows are labeled when applied.
- Each [PAPER] paper cited has its DOI once in prose, and every table cell that cites a [PAPER] row carries that row's own DOI; abstract-only and [WF] rows carry their label each time.
- No date, data cut, version, threshold or status appears that the person did not give ("not given" and ask); no fact comes from an earlier, separate request.
- The record line is the last line of the answer body (the calls list, if any, follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Software requirements, design inputs and traceability records: `dh-regulatory-and-quality` design-controls-and-risk-management. This specification is an input to them, not the record.
- The rule engine and personalization algorithm: `dh-digital-therapeutic-design` (old pack), heading DH-01.06.1 Personalization Engine; the platform: heading DH-01.06.4 DTx Architecture.
- Optimization trials, micro-randomized trials and their protocols: `dh-clinical-development` study-protocol-and-endpoint-design; this task only names the design option (TM71, TM90).
- Whether a classification regulation and its special controls apply: `dh-regulatory-and-quality` regulatory-pathway-and-classification.
- Usability of the delivery and workflow design: `dh-patient-and-user-experience` clinical-workflow-ux-design.
