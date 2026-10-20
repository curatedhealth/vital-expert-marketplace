# A2 Registration and results clocks

Framework task: DH-01.02.3.2, Part A, task A2 (part of old DH-01.02.3.2.1 Trial Execution Quality Monitoring).

## What this task delivers

A dated table of the registration, update, end-of-trial and results clocks that may apply to the trial, each computed from the dates the person gives, with what the registry record in the library shows beside it. It answers "which disclosure dates apply to us, and where does each stand?"

Why it matters: the clocks differ by source and anchor. US law counts results from the primary completion date (CV145); the EU CTR counts from the end of the trial in all Member States (CV152); ICMJE wants registration before first consent, which is stricter than the US 21 days (CV132, CV141).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Informatics Lead (`clinical-informatics-lead`) |
| Skill | DH-01.02.3.2 Part A, Registration and results clocks |
| Workflow | The steps below |
| Knowledge | `references/disclosure-clocks.md`; rows CV132 to CV154, CVB7 |
| Tool | `literature.find_trial` (registry record and linked publications); `literature.search_literature` only when there is no NCT number; `scripts/trial_ops_metrics.py clocks` |
| Catalogue job | None |
| Prompt | This guide |
| Template | `assets/registration-and-results-clocks-output.md` |
| Input | The request and its context: NCT or EU trial number, product type, jurisdictions, and the dates: first consent, first enrollment, registration submitted, last update, recruitment status change, primary completion, end of trial per Member State, results submitted |
| Governance | `references/governance.md` |

## Read the request

- **Which rules could apply.** US applicable clinical trial (device or drug, CV142, CV143)? EU trial under Regulation 536/2014 (CVB7)? Journal publication planned (ICMJE)? A funder that signed the WHO joint statement? The model lists the candidates; whether each applies is the call of the owner the person names for registration, or owner not named.
- **Which dates exist.** A clock without its start date is `[GAP]`.
- **Mode.** Short for one clock, full for a disclosure tracker.

## Workflow

### Step 1. Read the registry record

Call `literature.find_trial {nct_id: "<NCT>"}`. Record `status`, `phases`, `sponsor`, retrieval time and each linked publication (DOI, journal or preprint). Say that the library returns no registration, completion or results-posted dates (`references/tools.md`). If the person has only a paper, call `find_trial {record}` with its PMID; a miss means no link in the library's sources, not "unregistered".

### Step 2. Take the dates

Put the person's dates into one list. If a status from Step 1 contradicts them (registry says COMPLETED, person gives no primary completion date), ask.

### Step 3. Compute the clocks

With code execution, write the dates as JSON and run `python3 scripts/trial_ops_metrics.py clocks <trial.json>`; otherwise compute by hand from `disclosure-clocks.md`. For each clock: the rule and row, the date, and the position at the as-of date ("submitted on or before", "not recorded as submitted; date passed N days before as-of", "not yet due; N days from as-of"). For US results, add the delay-certification and extension routes as facts (CV146, CV147). For the EU, add the lay summary (CV152) and the halted-trial rule if relevant (CV154).

### Step 4. Publications

From Step 1, list linked publications and whether each is a preprint. If the trial has no NCT number, run `literature.search_literature {query: "<trial title or acronym>", limit: 10}` and list matches as candidates the person confirms. Set them beside the WHO indicative 24 months (CV140), labeled a funder pledge, not law.

### Step 5. What it means for the person

State consequences from the rules only: for example, results content under US law includes the protocol and statistical analysis plan with amendments (CV148), so those documents must be ready when the results are. Never say "late" or "non-compliant"; say where the date stands and that the owner the person names for registration, or owner not named decides.

## Build the output

Follow `assets/registration-and-results-clocks-output.md`. Answer first: the clocks whose dates have passed without a recorded submission, and the next one by date. Then the clock table, the registry record, publications, gaps.

## Before you hand it over

- Every date is the person's or the registry's, labeled which.
- Every clock carries its row and whether it is law, a journal policy or a funder pledge.
- No clock is called missed; no applicability is decided.
- Record line present.

## Boundaries

- No registry or portal submission, no extension request: those stop for the owner.
- Device investigation disclosure rules in the EU are `[GAP]`.
- Results interpretation and publication strategy: the evidence communication skill (DH-01.02.2).
