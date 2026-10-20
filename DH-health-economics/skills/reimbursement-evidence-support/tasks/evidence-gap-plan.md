# B1 Evidence gap plan and economic section

Framework task: DH-01.07.1.1, Part B, task B1. Replaces the earlier "Access dossier item" section: the economic section of a dossier or evidence response is drafted here, from what A2 found shown, together with the plan for what is not.

## What this task delivers

Two things the person decides on. First, a gap plan: every open item from A2, grouped by what blocks what, with the sourced options for closing each and what each option can and cannot give; ordering beyond dependency is the person's, and a ranking is run only on scores the person gives. Second, a draft economic section for a named body, built only from items shown and claims checked in A2, labeled "draft for the owner". It answers "what do we fix first, how, and what can we truthfully say in the economic section today?"

Why it matters: teams fix the visible gap, not the blocking one. A new utility study changes nothing if the comparator evidence is missing; a polished dossier section that claims "cost saving" from a cost interval crossing zero is the first thing a committee reads against the company.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-01.07.1.1 Part B, Evidence gap plan and economic section |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/evidence-gap-options.md`; `references/body-economic-standards.md`; `references/governance.md` |
| Tools | `verify.qualify_source` and `verify.check_claim` for any claim not checked in A2; `analytics.mcda` or `analytics.rice` only on scores the person gives; `verify.build_record` on clearance |
| Prompt | This guide |
| Template | `assets/gap-plan-output.md` |
| Input | The request and its context; A2 results (run A2 first in short mode if absent); the body the section is for; the person's priorities, scores and named owners |
| Governance | `references/governance.md`; people decide order, options and wording |
| Catalogue job | None startable. `value-dossier` (dossier skeleton with checked claims) is design-partner only (`references/tools.md`) |

## The rule that shapes this task: people decide

You lay out options and dependencies; the person chooses. You never pick which gap to close, never set a priority score, and never decide that a departure is acceptable. Any sequence beyond the dependency order is labeled "proposed" with the fact behind it, and not used until the person confirms. Every sentence of the economic section is a draft for the owner.

## Workflow

### Step 1. Gather A2

Use A2 from the conversation. If A2 is missing, run it in short mode for the named body. A plan without A2 is not possible: say so. When the person summarizes A2 instead of pasting it, ask for the DOI of the analysis or take it from the conversation, and confirm each stated gap against the source before grouping. Report a mismatch (for example 'non-UK value set' when the paper used SF-6D with UK weights, a mapping departure under `HE-045`) instead of planning around it. Always list the comparator as an open scope item unless A2 settled it.

### Step 2. Group the open items by dependency

Place each open item (not shown, departure, `[GAP]`) at its level from `references/evidence-gap-options.md`: scope facts, clinical effect, utilities and costs, model result, reporting. Say what each blocks. For example: a missing comparative effect against the comparator the body uses blocks the model result and every economic claim resting on it.

### Step 3. Lay out the options per item

For each item, the sourced options with what each gives and its limit: early-use simplified models (`HE-069`), switching values (`HE-077`), value of information (`HE-031`, [PAPER] DOI 10.1016/j.jval.2020.01.001, abstract only), a registered hypothesis-evaluating real-world study (`HE-025` to `HE-030`, [PAPER] DOI 10.1002/pds.4297), EQ-5D-5L with the body's value set (`HE-058`, `HE-106`), a BIA with the body's elements (`HE-088`, `HE-112`, `HE-122`), a reference-case analysis in the body's perspective (`HE-035`), CHEERS items (`HE-001`). For NICE early use, say which uncertainties could be resolved within 3 years (`HE-072`), from the person's facts; "cannot be resolved within 3 years" is a fact about the plan, not a verdict on the product. Study design points to dh-clinical-validation `study-protocol-and-endpoint-design`, reviews to dh-clinical-validation `literature-and-real-world-evidence-review`; model build to the pack's economic modeling competency (DH-01.07.2).

### Step 4. Order within a level, only if the person asks

If the person wants a ranking, ask them to score each gap on criteria they choose (for example effect on the decision, cost, time to evidence). Run `analytics.mcda` with their scores and weights, or `analytics.rice` with their reach, impact, confidence (as a percent) and effort. Report the rank and, worked by hand, the weight at which two adjacent gaps would swap. Never fill a missing score; the tool refuses one.

### Step 5. Draft the economic section

For the named body, draft only from A2's shown items and checked claims:
- What was evaluated: evaluation type, perspective, horizon, discounting, utilities and value set, as the material states them, with any departure named as such.
- What it shows: the source's own figures with intervals and the verbatim passage reference, never rounded into a stronger statement.
- What is open: each `[GAP]` and not-shown item from A2, and the plan line for it.
- Uncertainty: the switching values and one-way results on the person's numbers, labeled hypotheses.
Unchecked claims are left out with the reason. A gap the person stated but A2 did not confirm goes in the draft as '[unconfirmed: stated by the team]', never as fact. No sentence says the product is cost-effective or cost saving in your voice; where the source's authors concluded that, quote them, attributed. Label the section "Draft for [owner as named]: not for submission". For an EU JCA dossier, there is no economic section: say so (`HE-094`).

### Step 6. Route

Name the owner the person gave for each open item, or "owner not named". Route submission mechanics and wording to dh-market-access (`payer-engagement-and-hta-submission`, B1), the clinical review to dh-clinical-validation `literature-and-real-world-evidence-review`, and the tracking of how the body treated the evidence to the sibling skill (`reimbursement-evidence-monitoring`).

## Build the output

Follow `assets/gap-plan-output.md`. Answer first: the blocking gap and the one decision the person faces. Short mode: the dependency table (item, blocks, options in one line), the decision, the first three lines of the draft section. Full mode adds the option detail, any ranking and the full draft section.

## Before you hand it over

- Every option carries its row and, for [PAPER] rows (for example `HE-001`, `HE-018`, `HE-025` to `HE-031`), its DOI in the table cell. For NICE early use, list `HE-068`, `HE-069` and `HE-031` (VOI, abstract only) whenever the model result is open.
- Order beyond dependency is the person's or labeled "proposed".
- The draft section uses only shown items and checked claims, with figures as the source states them.
- The section is labeled a draft for the owner; nothing is filed or sent.
- Short mode counted: 450 words or fewer.
- Record line present.

## Boundaries

- No filing, no evidence response sent, no wording placed before a body.
- No pricing, threshold price or contract terms: dh-market-access.
- No claim of clinical benefit beyond checked passages; clinical claims go to the owner the person names for clinical claims, or owner not named; marketing claims to dh-commercial.
