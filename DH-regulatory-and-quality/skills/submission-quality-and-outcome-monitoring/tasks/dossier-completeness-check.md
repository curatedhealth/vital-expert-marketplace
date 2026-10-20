# A1 Dossier completeness check

Framework task: DH-03.03.4.2, Part A, task A1. Replaces the evidence half of "Submission Approval Outcome Monitoring".

## What this task delivers

A section-by-section check of a draft dossier the person supplies (an eSTAR export, a technical file index, a table of contents, or the documents themselves) against the content map for its route: present, present but a named sub-item not found, missing, or `[GAP]` not checkable, each with the source row. It answers "is anything missing before we submit?" It does not judge quality; the person does.

Why it matters: in FY 2025, 7.20% of 510(k)s and 10.61% of De Novos failed acceptance or technical screening on the first cycle (S-38, S-44); incomplete applications are one of the two main reasons EU notified bodies refuse MDR applications (25%, S-72, contractor study), and only 14 of 52 notified bodies report more than half of submissions complete (S-73).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`) |
| Skill | DH-03.03.4.2 Part A, Dossier completeness check |
| Workflow | The steps below |
| Knowledge | `references/content-maps.md` and `content-maps.json`; `references/submission-sources-supplement.md`; `references/REG_PATHWAYS_SUBMISSIONS.md`; `references/AI_ML_REGULATION.md` |
| Tools | None from the library; the person's draft is never sent to a library call |
| Prompt | This guide |
| Template | `assets/completeness-output.md` |
| Input | The draft (or its index), the route and class as decided, the documentation level and PCCP decision if US |
| Governance | `references/governance.md`; quality is the person's judgment |

## Read the request

- **The draft.** Ask for the index or the documents. If only a description is given, check the description and say so.
- **Route, class, level.** From the person or the conversation. If a choice is open, check against both options and say which lines differ.
- **Mode.** "Anything missing?" gets short mode; a pre-submission review gets full mode.

## Workflow

### Step 1. Pick the map

Take the route's section list from `content-maps.md` (or `content-maps.json`): 510(k) eSTAR (S-13), De Novo eSTAR (S-19), software overlay at the chosen level (S-01 to S-10), PCCP (AI US-11), EU Annex II and III (RP EU-13 to RP EU-16, S-49 to S-54). For a route whose content is not sourced (PMA, UKCA, Swiss specifics) say so and check only what is sourced.

### Step 2. Walk the draft against the map

For each map line, find the matching part of the draft and classify it with `references/gap-rules.md`: present (with location), present but a named sub-item not found, missing, applicability open, or `[GAP]` referenced file not supplied. Check the sub-items the sources name, for example:

- Software documentation level stated with a rationale (S-01).
- Under Basic, no SDS expected in the submission (S-06); under Enhanced, SDS and unit and integration test protocols and reports (S-06, S-08).
- Unresolved anomalies listed with their impact on safety and effectiveness (S-10).
- 510(k): predicate identified and differences discussed (S-14).
- De Novo: alternatives (S-22), proposed class (S-20), risks with mitigations and special controls if class II (S-21).
- EU: qualification rationale (S-50), class with the rule justified (RP EU-14), Basic UDI-DI (S-82), GSPR applicability with reasons (S-52), methods and standards applied (S-83), CER and CEP (S-54), PMCF plan and report or justification (S-54), PMS plan and PSUR or PMS report (RP EU-16), rationale where no new test was done (S-53).
- PCCP: a standalone, titled, versioned section flagged in the cover letter and table of contents (AI US-11).

### Step 3. Note what is outside the map

Sections in the draft that the map does not name: list them as "not in the source map; no finding". Human factors content now sits inside eSTAR (RP US-39); place it with the regulatory owner.

### Step 4. Hand quality to the person

For each present section, offer the source's own sub-items as a checklist the person can use to judge quality. Do not grade sections.

### Step 5. Route

Missing or thin sections go back to dossier assembly in the sibling skill (DH-03.03.4.1, task B1), clinical gaps to its task A2. Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.

## Build the output

Follow `assets/completeness-output.md`. Answer first: counts (present, thin, missing, open, not checkable) and the missing sections by name.

## Before you hand it over

- Every finding cites the map line and its row.
- No section is called adequate, weak or strong.
- Nothing from the draft went into a library call.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Completeness against sourced content, not a scientific or legal review.
- No prediction of acceptance, screening or review outcome.
- Drugs, biologics and wellness apps are out of scope.
