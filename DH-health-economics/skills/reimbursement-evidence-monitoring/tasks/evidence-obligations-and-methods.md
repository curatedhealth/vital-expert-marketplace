# A2 Evidence obligations and methods currency

Framework task: DH-01.07.1.2, Part A, task A2.

## What this task delivers

Two dated tables. First, the evidence obligations running for the person's product: each outcome a decision asked to be generated, the window it sits in, and whether the person's records show it being collected. Second, the methods changes since the person's model or evidence package was built that the body applies to their topic, each with what it touches in the model; plus a currency check on the studies the model rests on. It answers "what evidence do we still owe, and is our economic case still built on current methods and current papers?"

Why it matters: early-use recommendations come with named outcomes and a window, and NICE may withdraw a recommendation where a company is not engaging in evidence generation or the evidence will not resolve the uncertainties (`EN-2`). A model built before 27 August 2026 with 3L utilities, or one citing a superseded threshold, can be out of step for a new topic while still valid for an ongoing one (`HE-062`, `HE-063`).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-01.07.1.2 Part A, Evidence obligations and methods currency |
| Workflow | The steps below |
| Knowledge | `references/methods-changes.md`; `references/decision-evidence-sources.md`; `references/access-monitoring-sources.md` (EN rows) |
| Tools | `literature.get_record` and `verify.check_currency` per study the model rests on; A1's tools if no decision log exists; `scripts/decision_evidence_log.py --share` only when the person chooses that formula; `verify.build_record` on clearance |
| Prompt | This guide |
| Template | `assets/obligations-methods-output.md` |
| Input | The request and its context: A1 log (or the decisions), the person's evidence-generation plan and records of what is collected, the model's build date, topic dates, target bodies, the DOIs of the studies the model uses |
| Governance | `references/governance.md` |
| Catalogue job | None. `evidence-table` (available) can grade the studies but does not check currency against methods changes (`references/tools.md`) |

## Read the request

- **Obligations or methods, or both.** "What do we still owe NICE" is obligations; "is our model still current" is methods; a review asks for both.
- **Dates.** The model's build date and each topic's start or launch date decide which changes apply. Without them, show both branches and mark `[GAP]`.
- **Records.** What the person's data collection shows per asked outcome. Without records, every outcome is `[GAP]`, which is correct.

## Workflow

### Step 1. List the obligations

From A1 (or by running A1 in short mode), take for each decision the outcomes asked, verbatim, and the window. For each outcome, mark collected, not collected or `[GAP]` from the person's records. State the window with its source: the guidance's own period, and the evidence generation plan's period where the plan states one, or the PMG48 default of 3 years from publication (`HE-072`, `EN-1`), counted from a stated date to the as-of date. Where the guidance and its plan give different periods (HTG675: review within 4 years, plan period 3 years), show both with their sources and say NICE decides. Never say a window has passed when its start date is not stated. Add the facts that frame it, as facts: NICE can withdraw an early-use recommendation on listed grounds (`EN-2`); technologies that complete evidence generation are re-evaluated, and companies may submit evidence early at monitoring touchpoints (`EN-3`). If the person wants a share collected, use their formula (with code execution, `--share`), labeled as their score.

### Step 2. List the methods changes that apply

From `references/methods-changes.md`, take the changes dated after the model's build date for the bodies in scope, and test each against the topic's dates: PMG51 applies to HealthTech topics launched after 27 August 2026, not to ongoing ones (`HE-062`, `HE-063`); PMG48 and its transitional rules (`HE-066`); the open NICE threshold conflict (`HE-074` against `HE-050`, `HE-051`); IQWiG 8.0 (`HE-108`, `HE-113`); AMCP 6.0 final not read (`HE-131`); JCA device rules and AI principles (`HE-100`, `ES-158`, `ES-169`); CHEERS 2022 (`HE-001`). For each that applies, say what in the model it touches.

### Step 3. Check the studies

For each DOI the model rests on: `literature.get_record`, then `verify.check_currency {doi}` (retracted, corrected, superseded, withdrawn). Never send a methods page URL to `check_currency`: it returns "not checked" with `current: false` (`references/tools.md`). A study that is corrected or retracted is a finding for the owner; what to do is theirs.

### Step 4. Say what it means

In facts: which asked outcomes are not shown as collected and how much of each window has passed; which methods changes touch the model and which do not apply; which studies changed status. Route: updating the model or plan to `reimbursement-evidence-support` (A2, B1) and the pack's economic modeling competency (DH-01.07.2); new data collection to the pack's outcomes research competency (DH-01.07.3); any report to NICE stops for the owner.

## Build the output

Follow `assets/obligations-methods-output.md`. Answer first: the obligation most at risk on the facts (window passed share, outcomes not shown) and the methods change that touches the model most directly. Short mode keeps both tables trimmed to the person's topic.

## Before you hand it over

- Each asked outcome quoted; each window with its source and dates.
- Each methods change with its date, instrument and row, and whether it applies to this topic.
- No "the model is out of date" or "the recommendation will be withdrawn": facts and the owner's decision.
- Short mode counted: 450 words or fewer.
- Record line present.

## Boundaries

- No evidence-generation report written for NICE beyond a labeled draft for the owner.
- No study design: dh-clinical-validation `study-protocol-and-endpoint-design`; no model rebuild: DH-01.07.2.
- No listing status or clocks of review: dh-market-access.
