# A1 Objectives, benefits and roadmap

Framework task: DH-01.05.4.1 folded into this competency, Part A, task A1. Carries the old tasks "DH-01.05.4.1.1 Operating Model Design", "DH-01.05.4.1.2 Roadmap & Milestone Planning" and "DH-01.05.4.1.3 Execution Governance".

## What this task delivers

From the strategy the person has chosen: the objectives written back with the SMART elements present or missing; a benefits register in the columns the UK benefits guidance lists (benefit, linked objective, owner, baseline, target, measure, dates); milestones with owners, due dates and explicit dependencies; the governance cadence and decision forum the person sets; and the pass rule for each benefit, milestone and experiment, written by the person before anything is scored. It answers "what exactly did we commit to, and how will we know?"

Why it matters: a review against rules written after the results is a story, not a check. The UK benefits guidance asks for each benefit's owner, baseline, target and metric to be fixed by the full business case (SP-102, SP-104, UK public-sector guidance), and the old pass-rule tasks said the same: "Do not score a unit before this rule exists."

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `chief-compliance-officer-digital-health` (old DH-01.05.4.1.1 and DH-01.05.4.1.3); `behavior-change-designer` (old DH-01.05.4.1.2). Work as a strategy delivery analyst who structures the person's plan |
| Skill | DH-01.05.4.1 in this competency, Part A, Objectives, benefits and roadmap |
| Workflow | The steps below |
| Knowledge | `references/execution-frameworks.md` sections 1 to 3; rows SP-061, SP-090 to SP-108, SP-170 to SP-176 |
| Tools | None. `scripts/execution_check.py benefits` and `milestones` validate the files once written (flags only, no rule is set) |
| Prompt | This guide |
| Template | `assets/objectives-benefits-and-roadmap-output.md` |
| Input | The request and its context: the chosen strategy and options (from `strategic-vision-and-options`, this pack, or the person), objectives, benefits, baselines, targets, measures, milestones, owners, due dates, dependencies, cadence, pass rules |
| Governance | `references/governance.md`; every target, rule, owner and date is the person's |
| Catalogue job | none (`list_jobs_2026-10-19.json` lists no execution or benefits job) |

## Read the request

- **The chosen strategy.** Take it as the person states it, or from the sibling skill's decision record. If no choice has been made, route to `strategic-vision-and-options` (this pack).
- **What the person has.** Objectives, benefits, milestones, dates. Keep them verbatim.
- **What is missing.** Baselines, targets, owners, measures, dates, pass rules: "not given"; ask. Do not fill.
- **Proposals.** Only if asked: a measure, an objective wording, a register layout, a cadence, each labeled "proposed".

## Workflow

### Step 1. Objectives

Write each objective verbatim, linked to the strategy line it serves. For each, the SMART elements present or "not given" (SP-092, UK public-sector guidance used as a checklist). The baseline is business as usual (SP-093), the person's figure or "not given".

### Step 2. Benefits register

One row per benefit, in the columns of the script's `benefits` input: id, benefit, objective, owner, measure, direction, baseline and date, target and date, pass rule, reread date, source of the measure. These follow the register fields in SP-104 (UK commercial benefits guidance). Name the five benefits stages (identification, valuation, planning, realization, review, SP-100) only to show where each row stands. If the person applies an optimism-bias adjustment (SP-096), keep both their unadjusted and adjusted target, labeled as theirs. If they ask for the standard uplift, quote the bounds table for the project type they name (`execution-frameworks.md` section 1: software and ICT are equipment/development, 54% duration and 200% capital expenditure upper, 10% and 10% lower, SP-172, SP-173), the method (start at the upper bound, reduce only for factors managed, SP-175), the guidance's 2003 age (SP-170), and that no bound exists for benefits shortfall or operating costs other than outsourcing, where switching values are used instead (SP-176). All UK public-sector guidance; the uplift applied and the project type are the person's.

### Step 3. Milestones and dependencies

One row per milestone, in the columns of the script's `milestones` input: id, milestone, objective, owner, due, evidence of completion, depends on, pass rule elements, recheck date. Check that every dependency points at an existing milestone and that no milestone is due before one it depends on; report each as a fact. If the person gives no milestones, list the milestones their own strategy lines imply (for "two regions": a contract and a go-live per region; for a time-saving objective: a baseline measurement before the change), each labeled "proposed", with owner, due date, evidence and pass rule "not given"; none is applied until the person confirms.

### Step 4. Option tests still running

For each option test carried from `strategic-vision-and-options` A2: the question, prespecified endpoint, success criterion, decision rule and the date it was written, in the columns of the script's `experiments` input. A test without them is flagged now, not after the result (SP-115, FDA wording for device early feasibility studies, borrowed as a checklist).

### Step 5. Governance cadence and pass rules

The forum, the cadence and the reread dates are the person's. The pass rule for each row is the person's, written now: for a benefit, the share of planned change that counts as met (for example "at least 0.5 of the planned change by the reread date"); for a milestone, which elements count (owner, evidence, on time); for a test, the decision rule. The UK benefits note's 12-month review convention (SP-105) is context, labeled UK public-sector guidance; the person's dates govern. If the person uses a balanced scorecard, its perspectives are theirs; the healthcare reviews found no agreement on perspectives and many studies at high risk of bias (SP-107, DOI 10.3390/ijerph191610291; SP-108, DOI 10.1186/s12913-021-07452-7).

### Step 6. Validate the files

With code execution, save the three CSVs and run `python3 scripts/execution_check.py benefits --register REG.csv --as-of DATE`, `milestones --log LOG.csv --as-of DATE` and `experiments --log EXP.csv`. Report the flags (E1 to E7, M1 to M6, X1 to X6) as what is still missing before the first read.

## Build the output

Follow `assets/objectives-benefits-and-roadmap-output.md`. Answer first: how many objectives, benefits, milestones and tests the plan holds (proposed ones counted separately), how many have a pass rule written before scoring, and what is missing most. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/execution_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every objective, target, owner, date, cadence and pass rule is the person's or "not given"; proposals are labeled "proposed".
- UK guidance rows are labeled UK public-sector guidance.
- No benchmark appears as a target.
- Dependencies are checked and reported as facts.
- `python3 scripts/execution_check.py words ANSWER.md` prints "within the short-mode cap".
- Every fact names its source and date in plain words with the row id after it; "(inference)" rows carry the label each time.
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Choosing the strategy or the options: `strategic-vision-and-options` (this pack).
- Product lifecycle stage gates: `dh-clinical-development` clinical-product-lifecycle-and-stage-gates.
- Customer implementation plans: `dh-go-to-market` customer-implementation-planning.
