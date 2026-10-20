# A2 Intervention components

Framework task: DH-01.01.2.1, Part A, task A2. Replaces the earlier "Intervention component" section (DH-01.01.2.1.2, register CF-12.01.01.2.1.2).

## What this task delivers

A component table in which each component is tied to one link of the A1 mechanism, described by the TIDieR items, labeled with its intervention function, and, where it adapts to the user, specified as decision points, options, tailoring variables and decision rules with a missing-data rule. Each component carries its permitted and prohibited variation as the person sets them. Components that cannot be tied to a link are listed as left out of this version or proposed for removal.

Why it matters: specific interventions are more likely to be delivered with fidelity than vague ones (TM106), and what is fixed must be agreed before delivery (TM11, TM117). A component without a link cannot be tested and cannot be defended.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Validation Director (`clinical-validation-director`) |
| Skill | DH-01.01.2.1 Part A, Intervention components |
| Workflow | The steps below |
| Knowledge | `references/component-rules.md`; `references/precedents.md`; rows TM11, TM12, TM19, TM20, TM21 to TM36, TM45 to TM53, TM59, TM66 to TM90, TM104 to TM106, TM117 |
| Tools | `regulatory-dh.get_authorization` and `regulatory-dh.search_safety_events` for a named precedent's components; `analytics.mcda` or `analytics.rice` only to rank components the person scored; `scripts/mechanism_map_check.py` |
| Prompt | This guide |
| Template | `assets/intervention-components-output.md` |
| Input | The request and its context; the A1 chain (run A1 in short mode first if none exists); the feature list; any adaptive logic; delivery setting |
| Governance | `references/governance.md`; the person decides what ships, what may vary and the optimization objective |
| Catalogue job | none |

## Read the request

- **Mechanism.** Is there an A1 chain? If not, write one in short mode first, or ask for the outcome and the intended change.
- **Features.** The person's list, verbatim, with versions if they have them.
- **Adaptive logic.** Does anything change by user data (difficulty, timing, content)? Which data drive it?
- **Delivery.** App only, or with a clinician step, a sensor, a reward system, a drug?
- **Version.** Which version are we specifying? Components left out are left out of that version.

## Workflow

### Step 1. Tie each feature to one link

For each feature, name the link it serves (component to action, action to change, change to outcome). One feature may serve one link; if it serves several, say which is primary. A feature tied to no link goes to the "not tied" list (old task rule; TM8). The person decides whether it ships.

### Step 2. Describe each component by TIDieR

Fill items 1 to 9 and 11 for each component (component-rules section 2; TM22 to TM32). Items 10 and 12 are not completed for a design (TM34). Mark unreported items "?" (TM36). For dose (item 8), state the person's schedule; never supply one. Where a precedent is named, show its stated dose as context only (reSET: 4 lessons per week, 10 to 20 minutes each, TM134; EndeavorRx: about 25 minutes per day, 5 days per week, TM142).

### Step 3. Name the function, and the techniques if the person uses them

Label each component with one or more of the nine intervention functions (TM46 to TM48, TM50). If the person labels techniques with BCT Taxonomy v1, keep their labels and say the taxonomy was read from the abstract only, so labels are not checked here (TM51 to TM53).

### Step 4. Specify adaptive components

For each adaptive component, write decision points, options, tailoring variables (active or passive), the decision rule, the proximal outcome and the rule's behavior when tailoring data are missing (component-rules section 4; TM77 to TM89). Flag any tailoring variable with no stated reliability or validity as an assumption for B1 (TM88). Building the engine belongs to `dh-digital-therapeutic-design` (heading DH-01.06.1 Personalization Engine).

### Step 5. Fixed and variable

Ask the person which function each component must keep and what may vary by site, user or version (TM11, TM12, TM117). Write their answer; where they have none, list the question as open. Never decide it.

### Step 6. What went wrong in a precedent's components (when one is named)

Call `regulatory-dh.search_safety_events {product_code: "<code>"}` for the precedent. Quote any recall summary that names a component, with its date and class, exactly as the record states it; for PWE, both 7 June 2021 recalls describe the contingency management reward granted "regardless of the UDS results". Do not judge whether a recall bears on the person's product. As context only: 882.5801 asks that the software be described and verified (TM121), and FDA's reSET mitigation named software V&V that the model was correctly implemented (TM139).

### Step 7. Left out of this version, and ranking

List components not tied to a link and any the person chooses to defer, each with the reason in the person's words. If the person wants candidates ranked, ask for their criteria, weights and scores and call `analytics.mcda {options, criteria, weights, scores}` or `analytics.rice` on exactly those; show the inputs and say the tool ranks the person's scores (C17, N5). If the person wants an optimization objective, offer the MOST form ("most effective that can be delivered in under one hour", TM75) for them to fill.

### Step 8. Check the structure (optional, with code execution)

Run `python3 scripts/mechanism_map_check.py MAP.json` on the component table as JSON. It lists components with no link, adaptive components with no missing-data rule, TIDieR items still "?", and components with no fixed function stated.

## Build the output

Follow `assets/intervention-components-output.md`. Answer first: how many components tie to a link, which do not, and the biggest open item. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every component names its link, or sits on the "not tied" list.
- No dose, schedule or variation rule was supplied by the model; proposals are labeled.
- BCT Taxonomy v1 labels are the person's, and the abstract-only limit is stated.
- Precedent facts are quoted from their records, with row or call.
- Every [PAPER] row id carries its own paper's DOI: once in prose at first use, and in every table cell that holds it, even if given earlier; rows from different papers each keep their own DOI. Abstract-only and [WF] rows carry their label every time they are applied.
- No job title appears that the person did not use; owners are the person's words or "owner not named". No date, data cut, threshold or status appears that the person did not give or a record does not state.
- The record line is the last line of the answer body (the calls list, if any, follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Personalization engines and platform architecture: `dh-digital-therapeutic-design` (headings DH-01.06.1 Personalization Engine and DH-01.06.4 DTx Architecture).
- Recording components as design inputs, and change control between versions: `dh-regulatory-and-quality` design-controls-and-risk-management and document-and-change-control.
- Usability of the delivery mechanism: `dh-patient-and-user-experience` clinical-workflow-ux-design; human-factors validation: `dh-regulatory-and-quality` regulatory-submission-and-dossier.
- Describing the intervention in a protocol (SPIRIT item for interventions): `dh-clinical-development` study-protocol-and-endpoint-design, which this table feeds.
