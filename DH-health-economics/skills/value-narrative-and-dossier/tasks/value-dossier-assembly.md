# A2 Value dossier assembly

Framework task: DH-01.07.4.1, Part A, task A2. Replaces the old tool skill "DH-01.07.4.1.4 Value dossier".

## What this task delivers

A dossier draft, section by section, built only from elements a sourced row names (`references/dossier-elements.md`): for each section, what it holds, what the person has supplied, which checked claims from A1 fill it, and what is still `[GAP]`. For an NHS commissioner, the same work against the ESF standards.

Why it matters: a dossier is HCEI when it goes to a US payor (PC-US-06, PC-US-36), so every input and assumption must meet the evidence standard (PC-US-39) and carry its context (PC-US-40). A dossier with an invented section, or a claim that drifted from its passage, is a liability, not a deliverable.

## The catalogue job

The library's `value-dossier` job ("Payer value dossier outline") is open to design partners only (`status: design_partners`, `startable: false`, no tools listed; measured 19 October 2026). Do not start it. Tell the person in one line, then build the dossier with the direct calls below.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-01.07.4.1 Part A, Value dossier assembly |
| Workflow | The steps below |
| Knowledge | `references/dossier-elements.md`; `references/audience-frameworks.md`; `references/certainty-and-wording.md`; A1 output |
| Tool | A1's calls for any claim not yet checked (`literature.get_record`, `verify.qualify_source`, `verify.check_claim`); `literature.build_evidence_table` for the clinical evidence table; `literature.check_retraction` per DOI; `verify.build_record` when cleared. `analytics.budget-impact-model` only on the person's numbers (returned HTTP 422 on 19 October 2026) |
| Prompt | This guide |
| Template | `assets/dossier-output.md` |
| Input | The request and its context; cleared status and intended use per market; A1's claim register; the person's economic evaluation and BIA if any; the audience |
| Governance | `references/governance.md`; every dossier stops for the owner the person names for regulatory or legal review, or owner not named |
| Catalogue job | `value-dossier`: design partners only, not startable. `evidence-table` (available) can produce the clinical evidence rows; the checks below still apply. |

## Read the request

- **Audience and market.** US payor or formulary committee: AMCP elements and HCEI rules. NHS commissioner: ESF standards. EU HTA body or HAS or IQWiG: the clinical part only, plus the national economic rows; submission mechanics go to dh-market-access.
- **Cleared status.** Decides the dossier type (HE-133, AMCP 6.0 draft): A unapproved product, B approved product, C unapproved use. Types A and C carry no economic value assessment (HE-132) and follow 502(gg) (PC-US-08 to PC-US-10).
- **What the person has.** An economic model, a BIA, a review. The skill does not build the model (DH-01.07.2) or run the review (dh-clinical-validation, literature-and-real-world-evidence-review).
- **Short or full?** "What goes in our dossier" is short (the skeleton with status per section); "draft the dossier" is full.

## Workflow

### Step 1. Run A1 if it has not run

The dossier carries only claims from A1's register marked "may enter". If A1 has not run, run its Steps 1 to 5 for the claims the person wants in the dossier.

### Step 2. Set the skeleton

From `references/dossier-elements.md`, list the elements that apply to this audience and dossier type, each with its rows. Do not add a section no row names. If the person asks for one (for example an executive summary), add it labeled "proposed".

### Step 3. Fill the clinical evidence section

Call `literature.build_evidence_table` with the records, the passages you read and the PICO question. Use it for identifiers and authors only; take effects, confidence intervals and population from the passage (the tool cut the effect mid-word and returned population `[GAP]`). Add the certainty column from A1 (a person's rating, or `[GAP]`). Follow the Summary of Findings elements where the person wants a table (ES-97, ES-98).

### Step 4. Fill the economic sections (type B, or ESF)

Use the person's evaluation. Check it against the rows as a list, not a score: perspective, horizon, discount rate with reasons (HE-007; AMCP 6.0 draft HE-136); outcomes (HE-137); BIA horizon, population, PMPM and total (HE-138); modifiable model (HE-139); CHEERS items (HE-001 to HE-014, [PAPER] DOI 10.1177/23814683211061097; CHEERS is not a score, HE-005); for ESF, standards 17 and 18 (HE-087 to HE-091). Each item is "present", "absent" or "not checkable from what was supplied". If the person has no BIA and gives numbers, try `analytics.budget-impact-model` once; on HTTP 422, do the arithmetic in the conversation (BIA II elements, HE-019, [PAPER] DOI 10.1016/j.jval.2013.08.2291), labeled hypothesis. No threshold is applied by the skill; for NICE HealthTech the written threshold conflicts between PMG48 and PMG36 (HE-074) and the committee's is the one that counts.

### Step 5. Write the required context and statements

For a US payor: study design, generalizability, limitations, sensitivity analyses, balanced presentation (PC-US-40); the statement of material differences from labeling where applicable (PC-US-04); for types A and C, the not-cleared statement, development stage and factual results only (PC-US-45, PC-US-44); for an uncleared use of a cleared product, the cleared indication and labeling (PC-US-46). The dossier type (A, B or C) is set from HE-133 (AMCP 6.0 draft), never from a CFL row (PC-US-22 to PC-US-31). The guidance status line (PC-US-47) is required in every US payor dossier output, short mode included.

### Step 6. Gaps and decisions

List every section still `[GAP]` with who fills it, and every decision for the owner.

## Build the output

Follow `assets/dossier-output.md`. Answer first: dossier type, sections ready, sections open, and the stop.

## Before you hand it over

- No section without a row; "proposed" where the person asked for one.
- Every clinical claim from A1's "may enter" list; no tool grade as certainty.
- AMCP rows labeled "AMCP 6.0 draft"; CHEERS and ISPOR rows with DOI.
- Label the whole dossier "draft for the owner"; record line.

## Boundaries

- The skill does not submit a dossier, or send it to a payer or HTA body.
- HTA submission formats (NICE, G-BA, HAS, JCA dossier templates), DiGA applications and payer negotiation: dh-market-access.
- Model building: DH-01.07.2. Literature review: dh-clinical-validation (literature-and-real-world-evidence-review).
