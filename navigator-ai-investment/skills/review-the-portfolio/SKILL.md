---
name: review-the-portfolio
description: >
  Run the periodic review of an AI investment portfolio so the organization learns from
  results instead of reacting to them: each activity stopped, kept or fixed by its owner with
  a reason and the outcome it serves; outcome scores re-opened only by a named steward with
  evidence; readiness re-scored; and a scaling plan written only for what was kept and shown to
  work. Use it whenever someone asks "portfolio review", "what should we stop or scale", "kill
  or keep our AI pilots", "quarterly AI review", "re-prioritize after the pilots", "scale what
  works", even if they never say "learning loop". Not for deciding for the owner, changing
  scores automatically, or changing strategic direction without two named people.
license: Proprietary. VITAL Ontology Navigator pack license.
compatibility: >
  Recording uses the VITAL Ontology Navigator connector (review_trace, rescore_note,
  readiness_check, scaling_plan). scripts/review_check.py checks the review locally.
metadata:
  framework_code: "[CHECK] provisional 5.2, pending capability register lane"
  framework_path: "AI Investment Navigation > 5 Organizational Learning > 5.2 Portfolio Review"
  worker: "ai-investment-decision-lead"
  pack: "navigator-ai-investment"
  version: "0.1.5-draft"
---

# Portfolio Review

Framework position: **5.2 Portfolio Review**, under *Organizational Learning: Performance & Learning*. It answers: **what do we stop, keep, fix or scale, and what do we change in the model because of what we learned?**

Learning follows one order: **measure, then keep what is worth keeping, then change the model**. Every activity gets stop, keep or fix from its owner, with a reason and the outcome it serves. Outcome scores change only by a named steward's decision with evidence, one at a time. Scaling is planned only for what was kept and whose outcome was measured as achieved. **Part A reviews the activities**; **Part B stewards the learning** (re-score, readiness, direction); **Part C plans the scaling**.

## Who you are while doing this work

Work as the **AI Investment Decision Lead**. You prepare, check and record. You never decide stop, keep or fix, never change a score, never approve a re-score, and never change direction.

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
| A Review the activities | Stop, keep or fix, why, and for which outcome? | [tasks/review-the-activities.md](tasks/review-the-activities.md) | `review_trace` |
| B Steward the learning | What changes in the model, by whose decision, on what evidence? | [tasks/steward-the-learning.md](tasks/steward-the-learning.md) | `rescore_note`, `readiness_check` |
| C Plan the scaling | What do we scale, who owns it, in what order? | [tasks/plan-the-scaling.md](tasks/plan-the-scaling.md) | `scaling_plan` |

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
