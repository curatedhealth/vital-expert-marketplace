# A1 Submission quality check

Framework task: DH-03.01.3.2, Part A, task A1.

## What this task delivers

The person's draft dossier, checked item by item against the body's sourced checklist: each item present, missing or `[GAP]`, with where in the draft it sits; then a list of findings the owner should look at, each tied to the rule it rests on. It answers "is our draft complete, and what should we look at before it goes?" It does not answer "is it good": that judgment belongs to the person and their regulatory lead.

Why it matters: the bodies' own figures show that files stop on completeness first. In 2025, 69 percent of LPP and intra-GHS requests to CNEDiMTS were suspended at least once for incompleteness, 51 percent for administrative reasons only (`FR24`). In Germany an incomplete file has up to three months to be completed before refusal (`DE22`), and a withdrawal still costs up to 75 percent of the fee (`DE26`).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.3.2 Part A, Submission quality check |
| Workflow | The steps below |
| Knowledge | `references/submission-checklists.md`; `references/hta-submissions-sources.md`; `references/requirements/`; the evidence map from the preparation skill if present |
| Tools | None for completeness. For claims in the draft: `verify.qualify_source`, `verify.check_claim`. `verify.build_record` on clearance |
| Prompt | This guide |
| Template | `assets/quality-check-output.md` |
| Input | The draft dossier or its section list, the body and route, the person's own review criteria if they have any |
| Governance | `references/governance.md` |

## The rule that shapes this task: findings, not scores

Completeness is a fact: an item the checklist names is in the draft or it is not. Everything beyond that is a finding the person weighs. You may say "the draft claims an organizational benefit; no organizational endpoint is named in section 4 (`FR25`)". You may not say "section 4 is weak" or give any score. If the person has written their own quality criteria, check the draft against those criteria in their words, and mark each met, not met or `[GAP]`; the criteria remain theirs.

## Read the request

- **Body and route.** One checklist per route (DiGA permanent or trial; LPPR, PECAN, LATM; NICE evidence response; Medicare NCD). If unclear, ask.
- **The draft.** A file, pasted sections, or a section list. If only a section list, the check covers presence only and says so.
- **Mode.** "Is it complete" is short mode. A pre-filing review pack is full mode.

## Workflow

### Step 1. Load the checklist

Copy the route's items from `references/submission-checklists.md`, with row ids and the read date. Formal-completeness conditions first (DiGA: portal, gematik confirmation, BSI certificate, D1 to D3; PECAN: Sésame templates and Convergence filing, F3; LATM: ANS certificate, F4). For NICE there is no dossier; check the readiness items N1 to N7 instead (`UK2`).

### Step 2. Mark each item

For each item: present (quote the heading or page where it sits), missing, or `[GAP]` (the draft does not let you tell). For the DiGA content items, use the list in `DE3`: the PICO-style summary, ICD-10-GM patient groups (`DE9`), positive care effects split by type, studies or data analyses, the independent evaluating institution, data-processing locations, interoperability standards, liability insurance and actual prices.

### Step 3. List findings against the rules

Read the evidence sections against the rules in `references/hta-submissions-sources.md` and list what a reviewer at the body would see as open, each as a finding with its row. Common ones:
- DiGA: endpoints that are staff workload or economic indicators (`DE8`); a study outside Germany with no transferability case (`DE12`, `DE13`); no registry entry or late publication (`DE14`); no use-duration data (`DE15`); a trial application without an independent evaluation concept or analysis plan (`DE19`, `DE20`).
- LPPR: no comparator justification or no comparative data, which generally means no ASA (`FR4`); a "light" dossier outside the listed situations (`FR5`); device description, clinical data or vigilance data thin (the causes HAS found in 2023, `FR7`).
- PECAN and LATM: organizational claims without an organizational endpoint (`FR25`); a therapeutic and telemonitoring device with one dossier instead of two (`FR8`).
- NICE: an economic model that is not fully executable with full code access; no confidential-information checklist (`UK3`).
A finding states the fact and the rule. It does not rank or grade.

### Step 4. Check the claims the draft makes, if asked

For each key claim the person wants checked: `verify.qualify_source` on the study DOI, then `verify.check_claim` with the claim, the results sentence quoted verbatim with its locator, and the source. Read the passage yourself: `check_claim` matches words and has returned "supported" for a claim and its negation (`references/tools.md`). Report "checked" only when the passage states the finding in the same direction.

### Step 5. Say what blocks filing

Order the missing items by dependency: formal completeness first, then content items, then findings. State facts only: for example, "without the gematik confirmation the application is not formally complete (`DE29`)". Whether to file is the person's decision.

## Build the output

Follow `assets/quality-check-output.md`. Answer first: complete or not against the sourced checklist, how many items missing or `[GAP]`, and the formal-completeness blockers. Then the checklist table, the findings with rows, and claim checks.

## Before you hand it over

- Every item and finding carries its row and read date.
- No score, grade or quality adjective about the person's work.
- The person's own criteria, if used, are quoted in their words.
- Any wording for the body, including fixes to the draft, is labeled a draft for the owner.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- No rewriting of the dossier unless asked, and then as a labeled draft.
- No prediction of the body's opinion.
- Drugs, biologics and wellness apps are out of scope.
