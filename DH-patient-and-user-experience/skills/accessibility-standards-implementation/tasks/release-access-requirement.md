# B1 Release access requirement

Framework task: DH-02.04.1.1, Part B, task B1. Replaces the second half of the earlier "Access requirement" section (screens and exclusions) and the earlier one-line pass rule and owner sections.

## What this task delivers

A draft access requirement for one release: the target WCAG version and level the person sets, the screens and complete processes in scope, the exclusions they name with the basis for each, what the target leaves uncovered against the obligations mapped in A1, the content a conformance claim would need if they choose to make one, and, if asked, a ranking of open barrier fixes from the person's own scores. It answers "what will this release meet, and what does our choice leave open?"

Why it matters: conformance is for full pages and complete processes only (UX-STD-21, UX-STD-22). A requirement that lists screens but not the processes they sit in, or targets 2.1 while a buyer requires 2.2 (UX-UK-08, UX-UK-23), promises less than it looks.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Health Equity & Digital Access Lead (`health-equity-access-lead`) |
| Skill | DH-02.04.1.1 Part B, Release access requirement |
| Workflow | The steps below |
| Knowledge | A1 output; `references/obligation-map.md`; `references/barrier-criteria.md`; `references/data/wcag_criteria.csv` |
| Tools | `scripts/criteria_lookup.py`; `analytics.rice` (counted, optional, to rank fixes the person scored); `verify.build_record` for sign-off |
| Prompt | This guide |
| Template | `assets/release-access-requirement-output.md` |
| Input | The request and its context: A1 obligations, the person's target, screen and process list, exclusions and their basis, open barriers, scores if ranking is wanted, the accountable owner |
| Governance | `references/governance.md`; the person sets target, scope and exclusions; any published claim or burden determination stops for the owner |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. partner-prioritization runs the same ranking calculators but is scoped to partners and indications; call the calculator directly. |

## The rule that shapes this task: the person sets the requirement

The model lays out what each choice covers and leaves open. It does not pick the version, level, screens or exclusions. W3C advises 2.2 as the target (UX-STD-04): that is advice to quote, not a choice to make for them. If asked for a proposal, write one labeled "proposed", with the facts behind it.

## Read the request

- **Obligations.** A1 output if present; otherwise ask the A1 questions that decide the version.
- **Target.** Version and level, in the person's words.
- **Scope.** The screens in the release and the processes they belong to (sign-in, onboarding, booking, logging a dose). Ask for processes if only screens are given.
- **Exclusions.** What they will not meet in this release, and the basis they claim for each (a listed exception, a burden route, or simply "not in this release").
- **Ranking.** Only if asked and only with their scores.
- **Owner.** Who approves the requirement. If not named, "owner not named"; ask.
- **Mode.** Short for a direct question; full for the requirement document.

## Workflow

### Step 1. Write back the target and scope

Target version and level; screens; processes. Run `scripts/criteria_lookup.py target <version> <level>` for the criterion count. Flag any screen that belongs to a process not fully in scope: one page out of a process means no page in it conforms (UX-STD-22).

### Step 2. Lay the target against the obligations

For each obligation from A1, one line: what it cites, whether the person's target covers it, and the gap if not. Use `criteria_lookup.py diff` for the count and the criteria. Examples: a 2.1 AA target leaves the six new 2.2 A and AA criteria uncovered, which NHS and GDS require (UX-STD-07, UX-UK-08, UX-UK-23); a 2.2 target drops 4.1.1, which a 2.0 or 2.1 policy may still require to be tested and reported (UX-STD-08). State consequences; do not choose.

### Step 3. Exclusions and their basis

For each exclusion, write the basis the person gives and the row that defines it, or "no sourced basis: excluded from this release by the person's choice". Sourced routes: ADA and HHS 504 exceptions (UX-US-12, UX-US-20), the ADA minimal-impact provision (UX-US-13), burden determinations (UX-US-14, UX-EU-09, UX-UK-05), EAA content exclusions (UX-EU-08), PSBAR exclusions (UX-UK-04), Section 508 exceptions for non-web documents and software (UX-US-02, UX-US-03). A burden determination is the person's owner's, in writing where the row says so; the model never makes one.

### Step 4. Claim content, only if they will make a claim

A claim is optional; if made it needs the date, guideline title, version and URI, level, and the pages covered (UX-STD-23). Under the WAD and PSBAR, public bodies publish an accessibility statement with inaccessible parts and reasons (UX-EU-12, UX-UK-06). Draft the fields from the person's facts, labeled "draft for the owner"; publication stops for the owner.

### Step 5. Optional: rank open fixes the person scored

If asked what to fix first, ask for RICE inputs per fix: reach, impact (0.25, 0.5, 1, 2 or 3), confidence as a percent (0 to 100), effort. Write them back. Call `analytics.rice {initiatives: [{id, reach, impact, confidence, effort}]}`. Pass confidence as a percent: a fraction is silently divided by 100 (`references/tools.md`). Report the order and scores as the result of their inputs, not a recommendation. A fix on a day-one task or a process in scope is a fact to state beside the rank; the person decides whether it overrides the score.

### Step 6. Stops and the owner

Name the owner the person gave, or "owner not named". List what stops: approving the requirement, any published claim, statement, ACR or VPAT, any burden determination, any legal conclusion from A1.

## Build the output

Follow `assets/release-access-requirement-output.md`. Answer first: the target and scope as the person set them, and what the target leaves uncovered against their obligations. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Target, scope, exclusions and scores are the person's, and the output says so.
- Every process in scope is complete, or the gap is flagged.
- Every exclusion has a basis and row, or says it has no sourced basis.
- No statement that the release conforms; the claim fields, if any, are a draft for the owner.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Sets the requirement; checking the release against it is the monitoring skill (DH-02.04.1.2).
- No cost estimates: the rows hold none. A cost or effort score is the person's.
- Legal coverage and burden determinations are the owner's. Usability acceptance is UX 4.x.
