---
name: plan-the-delivery
description: >
  Outcome Navigator skill for 4.1 Delivery and Oversight Planning: structure, check and prepare; people score and decide. Use when the team is in 4 Execution and needs plan the delivery. Not for Launch Navigator gates, deal valuation thesis grading, or signing.
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: >
  Works offline on team-entered data. Ontology Navigator, Decision Companion (FOCUSED),
  Verify and Curator connectors add cited live data when present; without them steps are
  labeled not tool-checked or [GAP].
metadata:
  level: CF04
  register_code: "CF-01.06.01.4.1.1"
  verb: plan
  capability: "[CHECK] Outcome Navigation (Enterprise Strategy & Portfolio)"
  mission: "4 Execution"
  agent: outcome-navigator-agent
  atoms: [compose-draft]
  requires: []
  feeds: []
  tools: []
  version: "0.2.2"
  release_state: Draft
  pack: "vital-navigator-outcomes"
---
# Delivery and Oversight Planning

Framework position: **4.1 Delivery and Oversight Planning** (covering sequencing and capacity, and oversight design), under *Execution: Delivery Planning*, in the *Outcome Navigation* capability. Execution answers: **who does the work, in what order, under whose eye?**

Each step of the plan is a **job**: a piece of work that ends at a review. For each job, the plan names the capability it needs first, then any constraint on who may act, then the role or agent type that does it. People score four risk factors, and the engine's rule proposes how far the job can go to AI. The person chooses the tier and names who oversees it. **Part A sequences the jobs**; **Part B places the work and its oversight**.

## Who you are while doing this work

Work as the **Outcome Decision Lead**. You structure, check and compute the proposal. You never name individuals, never choose a tier, never assume capacity, and never place AI at a critical decision point without a context-of-use statement.

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
| A Sequence the jobs | What happens in what order, with what capacity? | [tasks/02-sequence-the-jobs.md](tasks/02-sequence-the-jobs.md) | `sequence_check` |
| B Place the work and its oversight | What goes to AI, who oversees it, when is it reviewed? | [tasks/01-place-the-work.md](tasks/01-place-the-work.md) | `delegation_place` |

## Rules that hold for every task

**A step is a job that ends at a review.** No job without a gate.

**Capability, then constraints, then performer.** Name the capability first; then any rule on who may act (regulated work stays with people unless an exception is recorded); then the role or agent type. Never a named individual.

**Capacity comes from people.** A job with no stated capacity is a gap.

**The tier is proposed, the person chooses.** Any risk factor at 8 or more proposes people only; all at 3 or less propose agent; otherwise agent with review. A choice that differs from the proposal carries the person's reason. Speak the tiers as people only, agent with review, or agent (connector strings). Map them to **DC09** execution modes when the person sets who initiates and who executes; keep **DC05** intervention levels on the option from cluster 3. Never rename a DC09 tier as ASSIST, AUGMENT or AUTOMATE.

**Every delegated job has an oversight owner and a review point.** By default the review is at the job's gate, with a question the owner sets. A critical decision point needs a context-of-use statement first, and a qualified person decides there.

**Ontology DC (cluster 4).** Delivery tiers and oversight use **DC09 AI Execution Modes** (who initiates / who executes). Keep DC05 intervention levels from cluster 3 on the option; do not rename DC09 tiers as ASSIST/AUGMENT/AUTOMATE. Detail: [references/ontology-dc-by-cluster.md](references/ontology-dc-by-cluster.md).

**Evidence classes, gaps, governance, names.** As in [references/gap-rules.md](references/gap-rules.md), [references/governance.md](references/governance.md) and [references/method.md](references/method.md) (X1 to X7). Display names only; never tier codes.

## C4 Execution rules the script enforces (8 November 2026)

Read this before you draft. These gates fail on **plan content**; no self-confession flag is needed (the older boolean flags still refuse when set). Spec: `diligence/c4-exports-2026-11-07/validation/validator_rule_specifications.yaml`; deferrals: `diligence/C4_DEEPEN_NOTES_2026-11-08.md`.

| Rule | Fails when the plan shows | Fields read |
|---|---|---|
| V-C4-DEL-02 capacity | Concurrent steps put more demand on one resource than the supplied availability (overlap by `window` dates, else by dependency graph); mixed units on one resource; negative or non-finite demand; a window that ends before it starts; a plan marked feasible while a step has no capacity | `resources[].available_fte`, step `capacity` ("0.5 FTE role", "N hours per week"), `effort_fte`, `demand`, `resource`, `window`, `capacity_verdict` |
| V-C4-DEL-02 unknown | Not a refuse: availability not supplied is reported as `capacity_assessment: unknown` with `capacity_unknown[]`. Unknown is never feasible. | same |
| V-C4-DEL-03 owner | An AI/agent actor, a declared agent type, or an AI provenance in `owner`, `oversight_owner`, `accepted_by`, `approved_by`, `reviewer`, `owner_type`, `assigned_by`, `selected_by`; performer and overseer the same actor; a placeholder (TBD, team, unassigned) presented as accepted. `[GAP]` is an honest gap, not a fail. | step owner fields, `agent_types` |
| V-C4-AEM-03 stop path | An agent tier on irreversible work (reversibility 3 or less, or `irreversible: true`) with no `override` carrying a human `authority`, a `mechanism` and a `fallback`; an assumed veto is not a path | step `choice`, `risk.reversibility`, `override` |
| V-C4-PRE-01 premortem | No failure prompt; AI text recorded as independent human writing; AI or unevidenced scenarios relabeled observed or fact; unlabeled AI suggestions; "complete" with no independent human contribution or round-robin | `premortem{failure_prompt, contributions[], ai_suggestions[], round_robin_done, status}`, `failure_scenarios[]` |
| V-C4-PRE-02 uplift | A "N% more ideas / fewer failed projects" premortem statistic stated as an established effect. A refusal that quotes the number, or a claim with `primary_source_ref` and `bounded_attribution`, passes. | any text in the payload |

The script proposes and checks; it never names an owner, never picks a tier, never sets capacity. Identity strings cannot be authenticated here: a person confirms every named owner. Output adds `capacity_assessment` (`feasible_on_supplied_data`, `unknown`).

**Facilitation order for C4 delivery.** Dependencies first, then capacity per resource with its availability evidence, then risk scoring (people), then tier choice (person), then owner and oversight, then the stop path for any irreversible agent work, then the premortem (independent human writing before any AI suggestion). Worksheet: [templates/worksheet.md](templates/worksheet.md); intake: [intake.md](intake.md); script walk-through: [references/facilitation.md](references/facilitation.md) (C4 addendum).

## Files in this skill

- `references/ontology-dc-by-cluster.md` which ontology DC this cluster uses (owner ruling, 20 October 2026).
- `tasks/`, `references/` (facilitation, method shared by the three Execution skills, tools, gap rules, governance).
- `assets/delivery-plan-report.md`, `assets/job-risk-score-sheet.md`, `assets/context-of-use-statement.md`.
- `scripts/delivery_check.py` dependency order, time-phased capacity (DEL-02), owner and oversight gates (DEL-03), stop-path (AEM-03), premortem and uplift gates (PRE-01/02), tier proposal (same rule as the engine). `scripts/test_delivery_check.py` holds the negative fixtures.
- `examples/delivery-medical-content-ai.md`, `evals/evals.json`.
## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake and list [GAP]s | none | agent alone |
| 2 | Draft using templates / offline scripts | compose-draft | agent alone |
| 3 | Human review of scores, choices or gates | none | human only |
| 4 | Record outputs and name the next skill | compose-draft | agent with review |



## Dependency-first plan
Produce `templates/dependency-view.md` (feeds `design-decision-exhibits`). Not a Launch LEX gate framework.
## Method anchoring
This skill belongs to Outcome Navigator under Enterprise Strategy & Portfolio. Method rules are in `references/method-standards.md`. Failure modes are in `references/failure-modes.md`. GenAI is one vertical overlay (examples and optional DC05 bindings), not a scope limit.

## Connectors
| Connector | Use for | Never for | Without it |
|---|---|---|---|
| Ontology Navigator | catalogue/methods/decide tools on team-entered numbers; draft record | scoring for a person; signing | offline scripts + markdown templates |
| Decision Companion (FOCUSED) | dissent, premortem, widen-options, tradeoff (optional) | naming a winner | question lists in tasks |
| Verify | admit source; quote-check claims | inventing a figure | label not tool-checked; run honesty cut by hand |
| Curator | evidence tips with record ids | inventing when empty | [GAP] |

## Quality bar
- People decide; the assistant structures, computes from entered numbers, and checks.
- Every missing fact is [GAP]; nothing is filled from memory.
- Deliverables use templates; exhibits that go to IC pass honest framing.
- Claim-bearing packs route through integrity skills before seal.

## Worked facilitation micro-script

See Depth notes and tasks. Ask one question per turn. Stop at human gates.

## Refuse table
| Request | Response |
|---|---|
| Invent baseline / peer ROI / quote | Refuse; [GAP] or rebuild-baselines |
| “Just pick one” / score for us | Refuse; people score |
| Mark signed / MLR approved / Launch Pass | Refuse; prepare only; name sibling if needed |
| Fill gaps from memory | Refuse |
| Copy teaching example numbers | Refuse |
