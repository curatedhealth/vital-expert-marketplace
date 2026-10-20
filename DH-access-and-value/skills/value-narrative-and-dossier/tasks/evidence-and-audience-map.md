# A1 Evidence and audience map

Framework task: DH-01.07.4.1, Part A, task A1. Replaces the old "Value audience" task and the evidence intake the old "Value narrative" task assumed.

## What this task delivers

Two tables. The **claim register**: every value claim the person wants to carry, each with its source, the passage read, the Verify status, whether the passage was read in the same direction, and the certainty a person assigned to that outcome. The **audience map**: for each audience the person names, the framework that applies, what it expects, and which claims meet that expectation or leave a gap.

Why it matters: a payer, an NHS commissioner and an HTA body read the same trial differently, and a claim that drifts from its passage (a wider population, a secondary outcome that did not move) is a misleading statement in every market (PC-US-03, PC-EU-02). The map is the floor the dossier and the narrative stand on.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-01.07.4.1 Part A, Evidence and audience map |
| Workflow | The steps below |
| Knowledge | `references/audience-frameworks.md`; `references/certainty-and-wording.md`; `references/gap-rules.md` |
| Tool | `literature.get_record`, `literature.search_literature` (only for records the person has not named), `literature.check_retraction`, `literature.build_evidence_table`; `verify.qualify_source`, `verify.check_claim`; `verify.build_record` when a named person clears it |
| Prompt | This guide |
| Template | `assets/evidence-map-output.md` |
| Input | The request and its context: product, cleared or certified intended use per market, the claims, the studies (DOI, PMID or document), the audiences, any certainty ratings already made |
| Governance | `references/governance.md` |
| Catalogue job | `evidence-table` (available; the one-call option for the evidence rows). The same-direction reading in Step 3 remains the method. |

## Read the request

- **Audiences.** Use the ones the person names. "Payers" in the US means the payor audience of PC-US-34; ask whether a health system or an NHS commissioner is also meant. If none is named, ask once.
- **Intended use per market.** If missing, `[GAP]`, and every claim is provisional.
- **Claims.** Take the person's claim list. The model does not add claims. If the person gives only a study, ask which results they want to carry, or list the primary outcome as stated in the abstract and label the list "proposed".
- **Certainty.** Ask whether a person or a published review has rated certainty per outcome (GRADE). If not, the column stays `[GAP]`.
- **Review needed?** If the person wants the body of evidence found and appraised, point to dh-clinical-development (literature-and-real-world-evidence-review) and use its output here.
- **Short or full?** "Which of our claims hold" is short; "evidence map for the dossier" is full.

## Workflow

### Step 1. Resolve each study

Call `literature.get_record` with the DOI, PMID or PMCID. Keep identifiers, authors, venue, year. Check the design against the paper, not the label (register N8: protocols come back as `rct`, a published article as `preprint`). Note `trial_ids`; if empty, take the registration number from the paper and say it came from there.

### Step 2. Get the passage

Use the passage the person supplies, or read the abstract or full text. The `get_record` excerpt can stop before the Results; never check a claim against an aim or design sentence. Record the locator (section and source). When a source is open access, read the full text before marking any field `[GAP]` from the abstract or the library excerpt.

Then read the study's Interventions or Methods section and record the intervention tested, in the paper's words. Ask the person to confirm it is their product and version; if not confirmed, mark the claim 'evidence for the intervention as tested, not yet confirmed as this product' `[GAP]`. Record any author conflict the paper discloses, quoted from the paper. Do not name a product from memory.

### Step 3. Check every claim

1. `verify.qualify_source` with the DOI (pass `question`).
2. `verify.check_claim` with `claim {text}`, `passage {text, locator}` and the full source object.
3. Read the passage yourself. Mark "same direction" only if it states the claim for the same population, comparator, outcome and time point. Overlap scores do not decide (register N3).
4. A "supported" that fails your reading is held, with the mismatch named ("population widened"). An "unsupported" or "partial" where the passage states the opposite is reported as "passage states the opposite".

If code execution is available, `scripts/claim_register.py` builds the register from the check results and your readings.

### Step 4. Currency

Call `literature.check_retraction` per DOI. Say which source answered (Crossref only, on 19 October 2026). A retracted or corrected record is flagged and its claims held (ES-119, ES-121).

### Step 5. Certainty per outcome

Write the certainty the person or the named review assigned, per outcome (ES-96), with who assigned it and any explanation for a rating below high (ES-99). Do not call `grade_evidence` to fill this column; if the person asks for a starting point, give the ES-90 starting level and label it "starting level only, not a rating".

### Step 6. Map the audiences

For each audience, open `references/audience-frameworks.md` and write what the framework expects (with rows) and which claims meet it. Typical gaps: an NHS commissioner expects a budget impact analysis for every tier (HE-087); a US payor dossier's economic section applies only to an approved product (HE-132, AMCP 6.0 draft); an EU JCA carries no economic evaluation (HE-094). The ESF tier and the AMCP dossier type are the person's to confirm. For a US payor audience, end the audience-fit paragraph with the guidance status (PC-US-47: 2018 final in force; June 2026 revised draft not final).

## Build the output

Follow `assets/evidence-map-output.md`. Answer first: which claims can be carried, for whom, and the main gap.

## Before you hand it over

- Every carried claim has a passage read in the same direction; every held claim names why.
- No certainty came from a tool; empty ratings are `[GAP]`.
- AMCP rows are labeled "AMCP 6.0 draft".
- Count the words in short mode.
- Record line from `references/governance.md`.

## Boundaries

- No new claims from the model. No review method here (dh-clinical-development, literature-and-real-world-evidence-review).
- No statement that the product is effective or cost-effective.
- Payer routes and HTA submission requirements: dh-access-and-value.
