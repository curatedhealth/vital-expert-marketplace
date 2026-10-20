# A2 Harmonized evidence plan

Framework task: DH-03.03.2.1, Part A, task A2. Replaces the earlier "Harmonised Evidence Planning" section.

## What this task delivers

A plan that says which of the person's evidence can serve which regions, under which conditions, and what each region still needs: the IMDRF documents the evidence is organized on and their reported adoption, the foreign clinical data rules that apply, the shared technical file core, and the regional additions and gaps. It answers "how much of our evidence can we reuse, and what is missing per region?"

Why it matters: evidence is the slowest part of a multi-region plan. A study designed without the strictest region's conditions in mind (ethics review, data validation, disaggregation, equivalence data access) can be unusable in that region and has to be repeated.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director |
| Skill | DH-03.03.2.1 Part A, Harmonized evidence plan |
| Workflow | The steps below |
| Knowledge | `references/evidence-reuse.md`; `references/jurisdiction-requirements.md`; the A1 map if the conversation holds one |
| Tools | None required. `regulatory-dh.retrieve_guidance` only to find a document name (`references/tools.md`) |
| Prompt | This guide |
| Template | `assets/evidence-plan-output.md` |
| Input | The request and its context: target regions, the classes argued in A1, the evidence held or planned (each study: design, where it ran, GCP basis, device version, population) |
| Governance | `references/governance.md` |

## Read the request

- **Evidence inventory.** For each study or data set: what it shows, where and when it ran, ethics review and consent, whether the studied device version is the one being submitted, and how data are broken down. Ask for what is missing; mark the rest "not described `[GAP]`".
- **Regions and classes.** From A1, or ask.
- **Equivalence.** Whether the person plans to rely on another device's data, and whether they have access to it.

## Workflow

### Step 1. Organize the evidence on shared principles

Map each piece of evidence to the three N41 components (valid clinical association, analytical or technical performance, clinical validation or performance) (JX-04, JX-05), which MDCG 2020-1 also uses (EU-32, EU-33, IM-03). An empty component is a gap in every region that reports implementing N41 (JX-09).

### Step 2. Check reported adoption per region

From `evidence-reuse.md` section 1, state for each target region whether it reports implementing N12, N41, N47 and N56 fully, partly or not, citing N84 as self-reported (JX-06). Where a region reports "partly" or "not", say the shared structure may need regional adjustment; do not invent what the adjustment is.

### Step 3. Foreign clinical data

For each study, check it against each region's rule (section 2): for the FDA, the 812.28 conditions (ethics committee review before the study, consent, FDA able to validate data, identical device or described differences) (JX-15 to JX-19); for the TGA, Declaration of Helsinki and ICH GCP and ISO 14155:2020 (JX-25); for Health Canada, a summary of studies from any country and a disaggregation statement (JX-26, JX-27). For an EU equivalence claim, list the three characteristic groups, the "no clinically significant difference" test and data access (JX-21 to JX-24). Mark each study per region: usable as is, usable if a named condition is shown, or `[GAP]` where the rule was not read.

### Step 4. The shared file and the regional additions

From section 3, set out the shared core (description, software V&V, risk management, clinical evaluation) and the regional wrapper and additions: eSTAR and the documentation level for the US; Annex II and III with the clinical evaluation plan and PMS plan for the EU; the IMDRF Table of Contents and the disaggregation statement for Canada; the same-device statement and audit readiness for Australia. Say plainly that the EU, UK, Switzerland, Japan and Australia report not implementing the IMDRF Table of Contents (JX-11).

### Step 5. Gaps per region

List, per region, the evidence or document that is missing or that does not meet a condition, with the row behind it. A gap in the person's evidence is a planning item, not a verdict on the product.

## Build the output

Follow `assets/evidence-plan-output.md`. Answer first: what can be reused widely, what cannot, and the one or two conditions that decide it. Then the reuse matrix and the gaps per region. Short mode for direct questions.

## Before you hand it over

- Every rule cites its row; adoption is labeled "as reported in N84".
- Reuse is "subject to the regulator's conditions", never "accepted".
- No ISO or IEC clause is quoted.
- A claim about a study's finding is made only from a passage the person supplied or a record read in full that states the finding in the same direction; Verify's word-overlap result alone is not enough (register item N3).
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Planning only. Study design belongs to clinical validation (DH-01.02); dossier assembly belongs to DH-03.03.4.
- No statement that the evidence is sufficient: sufficiency is the regulator's and the notified body's call.
- Drugs, biologics and wellness apps are out of scope.
