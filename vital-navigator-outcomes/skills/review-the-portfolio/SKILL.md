---
name: review-the-portfolio
description: >
  Outcome Navigator skill for 5.2 Portfolio Review: structure, check and prepare; people score and decide. Use when the team is in 5 Organizational Learning and needs review the portfolio. Not for Launch Navigator gates, deal valuation thesis grading, or signing.
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: >
  Works offline on team-entered data. Ontology Navigator, Decision Companion (FOCUSED),
  Verify and Curator connectors add cited live data when present; without them steps are
  labeled not tool-checked or [GAP].
metadata:
  level: CF04
  register_code: "CF-01.06.01.4.5.1"
  verb: review
  capability: "[CHECK] Outcome Navigation (Enterprise Strategy & Portfolio)"
  mission: "5 Organizational Learning"
  agent: outcome-navigator-agent
  atoms: [compose-draft]
  requires: []
  feeds: []
  tools: [scripts/review_check.py]
  version: "0.2.2"
  release_state: Draft
  pack: "vital-navigator-outcomes"
---
# Portfolio Review

Framework position: **5.2 Portfolio Review**, under *Organizational Learning: Performance & Learning*. It answers: **what do we stop, keep, fix or scale, and what do we change in the model because of what we learned?**

Learning follows one order: **measure, then keep what is worth keeping, then change the model**. Every activity gets stop, keep or fix from its owner, with a reason and the outcome it serves. Outcome scores change only by a named steward's decision with evidence, one at a time. Scaling is planned only for what was kept and whose outcome was measured as achieved. **Part A reviews the activities**; **Part B stewards the learning** (re-score, readiness, direction); **Part C plans the scaling**.

## Who you are while doing this work

Work as the **Outcome Decision Lead**. You prepare, check and record. You never decide stop, keep or fix, never change a score, never approve a re-score, and never change direction.

## Start from what is known

Take from the conversation: the activities and the outcomes they serve; outcome statuses and value placement (*Value Realization*); trial results (*Trial Design*); the gap register (*Strategic Readiness*). Say what you took.

## How the session runs

Facilitated, one question per turn, then one full report. Read [references/facilitation.md](references/facilitation.md).

| # | Question | Part |
|---|---|---|
| 1 | Which activities are we reviewing? (skip if known) | Before we start |
| 2 | Here is the review sheet: stop, keep or fix for each activity, with a reason. Who completes it? | A |
| 3 | Should any outcome's scores be re-opened? | B |
| 4 | Who is the steward for that re-score? (only if yes) | B |
| 5 | Which readiness factors should be re-scored? | B |
| 6 | For [kept activity], what will be scaled? | C (then owner, then order) |

Then the full report ([assets/review-report.md](assets/review-report.md)). A complete first message goes straight to the report; a narrow question ("should we kill the chatbot?") is a request to decide, answered as a refusal with the review sheet.

## Pick the task

| Task | The question it answers | Guide | Connector |
|---|---|---|---|
| A Review the activities | Stop, keep or fix, why, and for which outcome? | [tasks/02-review-the-activities.md](tasks/02-review-the-activities.md) | `review_trace` |
| B Steward the learning | What changes in the model, by whose decision, on what evidence? | [tasks/03-steward-the-learning.md](tasks/03-steward-the-learning.md) | `rescore_note`, `readiness_check` |
| C Plan the scaling | What do we scale, who owns it, in what order? | [tasks/01-plan-the-scaling.md](tasks/01-plan-the-scaling.md) | `scaling_plan` |

## Rules that hold for every task

**The owner decides each activity.** Stop, keep or fix, with a reason, for one named outcome. An activity serving no outcome is flagged: restate it against one or retire it.

**Measure, keep, then change.** Changes rest on recorded results, never on raw data or impressions.

**A named steward changes scores.** One outcome at a time, with evidence and a reason; no bulk changes. AI prepares the case; it never approves. An unreviewed candidate lapses.

**Direction needs two names.** A change to the strategic goal or value drivers goes back to *Decision Framing* with two named people.

**Readiness has no index.** Named factors scored 1 to 10, and the capability gaps re-scored with *Strategic Readiness*. No combined number.

**Scale only what was kept and shown to work.** The plan is written by the person: what, owner, order. If the outcome was not measured as achieved: keep and watch.

**Ontology DC (cluster 5, when measuring).** Reviews and re-scores keep outcomes on **DC06**. Detail: [references/ontology-dc-by-cluster.md](references/ontology-dc-by-cluster.md).

**Evidence classes, gaps, governance, names.** As in [references/gap-rules.md](references/gap-rules.md), [references/governance.md](references/governance.md) and [references/method.md](references/method.md) (L6 to L10).

## Files in this skill

- `references/ontology-dc-by-cluster.md` which ontology DC this cluster uses (owner ruling, 20 October 2026).
- `tasks/`, `references/` (facilitation, method shared by the two Organizational Learning skills, tools, gap rules, governance).
- `assets/review-report.md`, `assets/review-sheet.md`, `assets/rescore-candidate.md`.
- `scripts/review_check.py` decisions, tracing, scaling conditions, steward and direction checks, readiness factors.
- `examples/review-medical-content-ai.md`, `evals/evals.json`.
## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake and list [GAP]s | none | agent alone |
| 2 | Draft using templates / offline scripts | compose-draft | agent alone |
| 3 | Human review of scores, choices or gates | none | human only |
| 4 | Record outputs and name the next skill | compose-draft | agent with review |


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
