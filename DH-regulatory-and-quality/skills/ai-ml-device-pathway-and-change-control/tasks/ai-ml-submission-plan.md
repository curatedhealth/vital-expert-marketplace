# B1 AI/ML submission plan

Framework task: DH-03.03.1.1, Part B, task B1. Replaces the earlier "AI/ML Submission Assembly" section.

## What this task delivers

A plan draft that says what goes in which submission or agency interaction, per jurisdiction, ordered by dependency (what must exist before what), with the published clocks and fees beside each step and every decision point marked for the regulatory owner. It answers "what do we file, where, and in what order?" It stops before anything is sent.

Why it matters: an AI device carries two linked commitments, the device and its change plan. If the change plan's scope is settled after testing, testing gets redone; if a Pre-Sub is asked before the route is clear, its feedback answers the wrong question. Ordering by dependency avoids both.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director |
| Skill | DH-03.03.1.1 Part B, AI/ML submission plan |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/submission-mechanics.md`; `references/ai-ml-routes.md`; `references/pccp-structure.md` |
| Tools | A1's tools if no pathway map exists; `verify.build_record` on sign-off |
| Prompt | This guide |
| Template | `assets/submission-plan-output.md` |
| Input | The request and its context; the owner's route and class decisions (or the open options); the PCCP draft; target jurisdictions; named owners |
| Governance | `references/governance.md`; filing decisions and all regulator-facing wording stop for the regulatory owner |

## The rule that shapes this task: the owner decides, the plan shows the consequences

The person, through their regulatory owner, decides the route, the class, the PCCP scope, whether to seek Breakthrough designation, and the filing order. The model lays out the steps each choice implies, the dependencies, the published clocks and the open questions. Where the owner has not decided, the plan shows the branches side by side and does not pick. If the person asks the model to choose, it may give a "proposed" order with the dependency behind each step, and it does not treat it as the plan until the person confirms.

## Workflow

### Step 1. Gather the inputs

Use A1 (routes, dates, precedents) and A2 (PCCP draft) from the conversation. If A1 is missing, run it in short mode. A plan without a PCCP draft is possible; it says the PCCP scope is open and every step that depends on it waits.

### Step 2. Write back the decisions in hand

List what the owner has decided and what is open: intended use, class per jurisdiction, route, predicate, PCCP scope, Breakthrough, target markets, owners. Ask the person to confirm the list before planning. Open items become branches.

### Step 3. Build the dependency chain per jurisdiction

From `references/submission-mechanics.md`, "Ordering logic". For the US:

| Step | Depends on | Content | Published clock or fee | Row |
|---|---|---|---|---|
| Intended use and class view | Nothing | Owner's statement | | |
| Predicate or De Novo rationale | Intended use | From A1 precedents | | [RP US-05, US-09] |
| PCCP scope | Intended use, route | From A2 | | [AI US-08] |
| Breakthrough request (if chosen) | Intended use, condition | Q-Sub | Decision within 60 calendar days | [RP US-42] |
| Pre-Sub | Drafts of the above, testing plan | Questions on route, PCCP, testing | Feedback within 70 days | [RP US-31; AI US-10] |
| Testing | Pre-Sub feedback | Owner's protocols | | |
| Marketing submission | Testing, final PCCP | eSTAR for 510(k) and De Novo; PCCP as standalone versioned section | Goal: 95% within 90 FDA days (510(k)); observed average total days (latest FY); FY 2027 fee with small-business fee. Always print the percentage and the fiscal year. | [RP US-36 to US-38, US-46 to US-48, US-55, US-58; AI US-11] |

For the EU: notified body choice, written agreement, technical documentation with the AI Act requirements and Annex IV point 2(f) changes, assessment; the notified body timing figures are a contractor study and context only [RP EU-12, EU-44; AI EU-05, EU-29]. For the UK: CE acceptance (MDR devices until 30 June 2030 [RP UK-03]) or UKCA, and that no GB PCCP mechanism is in force [AI UK-04].

### Step 4. Place each content item in its submission

| Content | Where it goes | Row |
|---|---|---|
| PCCP | US marketing submission only (not authorized in a Pre-Sub); EU technical documentation under Annex IV point 2(f) once the AI Act applies; GB not yet | [AI US-09, US-10, EU-05; AI UK-04] |
| Software documentation (Basic or Enhanced) | US marketing submission | [RP US-25 to US-29] |
| AI-specific content | US marketing submission, following the draft lifecycle guidance (draft) | [AI US-19 to US-21] |
| Clinical evaluation | EU technical documentation, MDCG 2020-1 components | [RP EU-17, EU-18, EU-32] |
| Post-market monitoring plan | EU PMS plan, with AI elements integrable [AI EU-34]; US: a PMA may carry it as a condition of approval (draft guidance) [AI US-38] | [RP EU-16] |

### Step 5. Mark the stops

Every step that produces something for a regulator gets a stop line: "Stops for the regulatory owner: OWNER (or owner not named)". Every open decision from step 2 gets a line: what it blocks.

### Step 6. Offer the readiness check

Before filing, the readiness monitoring skill (task A1) checks the package for completeness against these same sources. Offer it in one line.

## Build the output

Follow `assets/submission-plan-output.md`. Short mode: the answer (the first three steps and what blocks them), one dependency table, the open decisions, the record line. Full mode adds the per-jurisdiction chains, the content placement table, clocks and fees, and sources.

## Before you hand it over

- Every step traces to a dependency, not a date. No calendar dates are invented; published clocks are stated as facts with rows.
- No decision is taken for the owner. Branches are shown side by side.
- Fees are FY 2027 rates with the row; review times say "FDA days" or "calendar days" as the row does.
- Nothing is labeled as filed, accepted or authorized.
- If it leaves the conversation, ask who clears it and call `verify.build_record`.

## Boundaries

- The model does not write Pre-Sub questions or cover letters for sending. If asked, it drafts topics labeled "draft for the owner".
- No forecast of the outcome of any review.
- Dossier assembly in detail belongs to the submission excellence competency (DH-03.03.4.1); quality-system work to the quality pack.
