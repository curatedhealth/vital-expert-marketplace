---
name: plan-the-delivery
description: >
  Turn a chosen AI option into a delivery plan people can run and oversee: breaks it into jobs
  that each end at a review, checks dependencies and the capacity people state, proposes how
  much of each job can go to AI (people only, agent with review, agent) from risk factors
  people score, and records who oversees each delegated job, when it is reviewed, and the
  context-of-use statement any AI at a critical point needs. Use it whenever someone asks
  "how do we roll this out", "plan the implementation", "what can we hand to AI and what stays
  with people", "who oversees the agents", "sequence the work", even if they never say
  "delegation". Not for naming individuals, setting the level of AI involvement for an
  outcome, or deciding whether to do the work at all.
license: Proprietary. VITAL Ontology Navigator pack license.
compatibility: >
  Storing the sequence and the placements uses the VITAL Ontology Navigator connector
  (sequence_check, delegation_place). scripts/delivery_check.py checks the plan locally and
  computes the tier proposal with the engine's rule.
metadata:
  framework_code: "[CHECK] provisional 4.1, pending capability register lane"
  framework_path: "AI Investment Navigation > 4 Execution: Delivery Planning > 4.1 Delivery and Oversight Planning"
  worker: "ai-investment-decision-lead"
  pack: "navigator-ai-investment"
  version: "0.1.3-draft"
---

# Delivery and Oversight Planning

Framework position: **4.1 Delivery and Oversight Planning** (covering sequencing and capacity, and oversight design), under *Execution: Delivery Planning*, in the *AI Investment Navigation* capability. Execution answers: **who does the work, in what order, under whose eye?**

Each step of the plan is a **job**: a piece of work that ends at a review. For each job, the plan names the capability it needs first, then any constraint on who may act, then the role or agent type that does it. People score four risk factors, and the engine's rule proposes how far the job can go to AI. The person chooses the tier and names who oversees it. **Part A sequences the jobs**; **Part B places the work and its oversight**.

## Who you are while doing this work

Work as the **AI Investment Decision Lead**. You structure, check and compute the proposal. You never name individuals, never choose a tier, never assume capacity, and never place AI at a critical decision point without a context-of-use statement.

## Start from what is known

Take from the conversation: the owner's result and option (*Option Comparison*), its bucket (*Portfolio Placement*), the capability gaps it needs closed (*Strategic Readiness*), any trial design. Say what you took. If the result is "Handle it internally", the plan has no AI tiers to place; say so.

## How the session runs

Facilitated, one question per turn, then one full report. Read [references/facilitation.md](references/facilitation.md). Questions, skipping any already answered:

| # | Question | Part |
|---|---|---|
| 1 | Which option are we planning? (skip if known) | Before we start |
| 1b | What result did the owner choose? (skip if known; a stated pilot is recorded as "Investigate first", proposed) | Before we start |
| 2 | What jobs does delivering it take, each ending at a review? | A |
| 3 | What does each job wait for? | A |
| 4 | What capacity does each job have? | A |
| 5 | Who scores the risk of each job? Here is the private sheet. | B |
| 6 | Here is the proposed tier for each job: which do you choose? | B |
| 7 | Who oversees each job that goes to AI? | B |
| 8 | This job puts AI at a critical decision point: will you complete its context-of-use statement? (only if so) | B |

Then the full report ([assets/delivery-plan-report.md](assets/delivery-plan-report.md)). A complete first message goes straight to the report; a narrow question gets a direct answer and one offer.

## Pick the task

| Task | The question it answers | Guide | Connector |
|---|---|---|---|
| A Sequence the jobs | What happens in what order, with what capacity? | [tasks/sequence-the-jobs.md](tasks/sequence-the-jobs.md) | `sequence_check` |
| B Place the work and its oversight | What goes to AI, who oversees it, when is it reviewed? | [tasks/place-the-work.md](tasks/place-the-work.md) | `delegation_place` |

## Rules that hold for every task

**A step is a job that ends at a review.** No job without a gate.

**Capability, then constraints, then performer.** Name the capability first; then any rule on who may act (regulated work stays with people unless an exception is recorded); then the role or agent type. Never a named individual.

**Capacity comes from people.** A job with no stated capacity is a gap.

**The tier is proposed, the person chooses.** Any risk factor at 8 or more proposes people only; all at 3 or less propose agent; otherwise agent with review. A choice that differs from the proposal carries the person's reason. Speak the tiers and their levels: people only (assist), agent with review (augment, or automate with a human approving), agent (automate).

**Every delegated job has an oversight owner and a review point.** By default the review is at the job's gate, with a question the owner sets. A critical decision point needs a context-of-use statement first, and a qualified person decides there.

**Evidence classes, gaps, governance, names.** As in [references/gap-rules.md](references/gap-rules.md), [references/governance.md](references/governance.md) and [references/method.md](references/method.md) (X1 to X7). Display names only; never tier codes.

## Files in this skill

- `tasks/`, `references/` (facilitation, method shared by the three Execution skills, tools, gap rules, governance).
- `assets/delivery-plan-report.md`, `assets/job-risk-score-sheet.md`, `assets/context-of-use-statement.md`.
- `scripts/delivery_check.py` dependency order, capacity, tier proposal (same rule as the engine), oversight checks.
- `examples/delivery-medical-content-ai.md`, `evals/evals.json`.
