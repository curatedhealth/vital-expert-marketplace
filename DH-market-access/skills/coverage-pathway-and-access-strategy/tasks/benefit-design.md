# B2 Benefit design

Framework task: DH-03.01.4.1, Part B, task B2.

## What this task delivers

A plan for turning coverage into patients actually using the product: the access journey in each covered country, stage by stage, with the rule that governs each stage, where patients are known to drop out, the levers the company can pull at each stage, and what to measure. The company chooses the levers; this task makes the journey, the drop-offs and the options explicit and sourced.

Why it matters: a listing is not uptake. In Germany, for example, the insurers' own report counts activation codes that were issued and never redeemed. Coverage that patients do not reach, or abandon, earns nothing and builds no outcome evidence, and in Germany outcome data now feeds the price.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.4.1 Part B, Benefit design |
| Workflow | The steps below |
| Knowledge | `references/requirements/access-after-listing.md` (who can trigger access, mechanics to first use, post-listing obligations, official uptake figures); the country requirements files; published studies found through the literature tools |
| Tools | `literature.search_literature`, `literature.get_record`, `literature.grade_evidence` for published evidence on uptake and adherence; Verify on literature claims (literature sources are admissible, unlike register pages); A1 tools if coverage status is not yet in the conversation |
| Prompt | This guide |
| Template | `assets/benefit-design-output.md` |
| Input | The request and its context; the coverage status (A1) or chosen routes (B1); the product's intended users, indication, and how it is delivered |
| Governance | `references/governance.md` |

## Workflow

### Step 1. Start from what is covered

Use the A1 status or B1 routes in the conversation. If neither exists, ask which countries and routes are in scope, or run A1 in short mode. Benefit design is only for routes that are covered or about to be.

### Step 2. Lay out the access journey per country

Use these stages, renamed if the country's process differs:

| Stage | The question |
|---|---|
| Eligibility | Which patients does the coverage include (indication, age, contraindications as listed)? |
| Trigger | Who can start access: which clinicians may prescribe, and can the patient obtain it another way (for example insurer approval with proof of indication in Germany)? |
| Activation | What happens between the trigger and first use (for example an insurer-issued activation code; a telemonitoring operator setting the patient up)? |
| Sustained use | What keeps a patient using it to the end of the course? |
| Reporting and renewal | What the company must report after listing (for example outcome measurement in Germany; data during an early-funding period in France), and what a renewal or follow-on decision needs |

For each stage, take the rule from `access-after-listing.md` and cite its row. Where the file marks a point "not sourced", say so in the stage and name the authority to check.

### Step 3. Find where patients drop out

Use official uptake figures from `access-after-listing.md` first (they say where the system loses patients, for example codes issued but never redeemed). Then run at most two `literature.search_literature` queries on uptake, adherence or prescribing barriers for this product category or indication (for example "DiGA prescription barriers physicians", "digital CBT-I adherence dropout"). Open the strongest records with `literature.get_record`, grade them with `literature.grade_evidence`, and use only what a record states. Attach each drop-off to a stage. A stage with no evidence of drop-off is marked as unknown, not as fine.

### Step 4. Lay out levers per stage

For each stage with a known or likely drop-off, list the options the company controls, each tied to the barrier it addresses and the evidence for that barrier. Typical lever families (use only those that fit the evidence):

- Trigger: making prescribing easy for the clinicians the rules allow to prescribe; supporting the approval route where one exists.
- Activation: shortening the steps from prescription or code to first use.
- Sustained use: onboarding and adherence features, clinician touchpoints.
- Reporting: building the data collection the post-listing obligations require into the product from the start.

Do not attach effect sizes to levers unless a graded study states one for a comparable product. Do not rank levers unless the person asks; if they do, use the B1 method (they score, `analytics.mcda` ranks).

### Step 5. Say what to measure

For each stage, one measure the company can track (for example share of activation codes redeemed; share completing the course; data completeness for the outcome report). Measures are named, not given target values.

### Step 6. Check the literature claims

For each claim that rests on a study: call `verify.qualify_source` with its DOI or PMID, then `verify.check_claim` with the claim, the quoted passage from the record (abstract or title text, verbatim) and the source object `qualify_source` returned. Passing bare DOIs to `verify.verify_text` currently returns "unverifiable" for everything (see `references/tools.md`). Register facts are not sent to Verify. Remove or mark `[GAP]` anything that comes back unsupported.

## Build the output

Follow `assets/benefit-design-output.md`. A direct question gets short mode; a plan to share gets full mode.

## Before you hand it over

- Every rule and figure carries its source and date; literature claims carry their record and grade.
- If it will leave the conversation, ask who clears it and call `verify.build_record` with that person in `cleared_by`; otherwise label it an uncleared draft.

## Boundaries

- The company chooses the levers. The model lays out options and evidence.
- Any material aimed at prescribers or patients that states a benefit (education content, campaign wording, claims in onboarding) stops for regulatory review before use: promotion of medical devices is regulated, and claims of benefit route to the regulatory owner (`references/governance.md`).
- No patient-level decisions and no protected health information.
- No invented effect sizes, uptake targets or forecasts.
- Drugs, biologics and wellness apps are out of scope.
