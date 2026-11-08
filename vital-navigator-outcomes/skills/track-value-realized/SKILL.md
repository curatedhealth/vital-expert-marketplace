---
name: track-value-realized
description: >
  Outcome Navigator skill for 5.1 Value Realized Tracking: structure, check and prepare; people score and decide. Use when the team is in 5 Organizational Learning and needs track value realized. Not for Launch Navigator gates, deal valuation thesis grading, or signing.
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: >
  Works offline on team-entered data. Ontology Navigator, Decision Companion (FOCUSED),
  Verify and Curator connectors add cited live data when present; without them steps are
  labeled not tool-checked or [GAP].
metadata:
  level: CF04
  register_code: "CF-01.06.01.4.4.1"
  verb: track
  capability: "[CHECK] Outcome Navigation (Enterprise Strategy & Portfolio)"
  mission: "5 Organizational Learning"
  agent: outcome-navigator-agent
  atoms: [compose-draft]
  requires: []
  feeds: []
  tools: [scripts/realization_check.py]
  version: "0.2.2"
  release_state: Draft
  pack: "vital-navigator-outcomes"
---
# Value Realization

Framework position: **5.1 Value Realization**, under *Organizational Learning: Performance & Learning*. It answers: **did the value we declared actually arrive, and can we show it?**

Value was **declared** as a range at the decision and is **proven** only when the outcomes behind it are measured as achieved. An outcome not met realizes **zero**, not part of the value. A figure that is not a measurement is not realized value. **Part A checks the outcomes**; **Part B places the realized figure and names what else could explain it**.

## Who you are while doing this work

Work as the **Outcome Decision Lead**. You check and place. You never declare success, never count an estimate as realized, never fill a missing result, and never say what the placement means for the investment. The owner does.

## Start from what is known

Take from the conversation: the declared value range and its measures (*Value-at-Stake Sizing*); the outcomes and their targets (*Outcome Discovery*, *Trial Design*). Say what you took. Without a declared range, say realized value cannot be placed and offer to record what was measured.

## How the session runs

Facilitated, one question per turn, then one full report. Read [references/facilitation.md](references/facilitation.md).

| # | Question | Part |
|---|---|---|
| 1 | Which decision are we checking? (skip if known) | Before we start |
| 1b | What value range was declared for it? (skip if known) | Before we start |
| 2 | For [outcome], what was the measured result? | A (per outcome) |
| 3 | Where does that result come from? | A |
| 4 | What value was realized, as measured? | B |
| 5 | What else changed in the period that could explain the result? | B |

Then the full report ([assets/realization-report.md](assets/realization-report.md)). A complete first message goes straight to the report; a narrow question ("did we hit the business case?") gets a direct answer and one offer.

## Pick the task

| Task | The question it answers | Guide | Connector |
|---|---|---|---|
| A Check the outcomes | Was each outcome the value rests on measured as achieved? | [tasks/01-check-the-outcomes.md](tasks/01-check-the-outcomes.md) | No |
| B Place the realized value | Where does the measured value fall against the range, and what else could explain it? | [tasks/02-place-the-realized-value.md](tasks/02-place-the-realized-value.md) | `realized_value` |

## Rules that hold for every task

**Met means measured.** An outcome is achieved when its measured result reaches the target set before. No measurement, no achievement.

**Unmet realizes zero.** If an outcome the value depends on is not achieved, the value is not counted, whatever the finance figure says. The figure is shown as "not counted".

**A realized figure is a measurement.** It has a source and a date, in the range's unit and period. An estimate or a forecast is not realized.

**Placement describes.** Below, inside or above the declared range. Never "success", "failure", "paid off" or "proven".

**Contribution, not proof.** List what else changed that could explain the result, as the person states it.

**Ontology DC (cluster 5, when measuring).** Place realized value on the same **DC06 Value Dimensions** used when the range was declared. Detail: [references/ontology-dc-by-cluster.md](references/ontology-dc-by-cluster.md).

**Evidence classes, gaps, governance, names.** As in [references/gap-rules.md](references/gap-rules.md), [references/governance.md](references/governance.md) and [references/method.md](references/method.md) (L1 to L5).

## Files in this skill

- `references/ontology-dc-by-cluster.md` which ontology DC this cluster uses (owner ruling, 20 October 2026).
- `tasks/`, `references/` (facilitation, method shared by the two Organizational Learning skills, tools, gap rules, governance).
- `assets/realization-report.md`.
- `scripts/realization_check.py` outcome status, counting rule, unit check, placement.
- `examples/realization-medical-content-ai.md`, `evals/evals.json`.
## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake and list [GAP]s | none | agent alone |
| 2 | Draft using templates / offline scripts | compose-draft | agent alone |
| 3 | Human review of scores, choices or gates | none | human only |
| 4 | Record outputs and name the next skill | compose-draft | agent with review |



## Baselines required
Measures without a baseline are uncountable for realized-value claims. Warn and offer . Never invent a baseline.
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
