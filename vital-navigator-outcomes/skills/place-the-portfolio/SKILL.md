---
name: place-the-portfolio
description: >
  Outcome Navigator skill for 3.3 Portfolio Placement: structure, check and prepare; people score and decide. Use when the team is in 3 Intelligence Core and needs place the portfolio. Not for Launch Navigator gates, deal valuation thesis grading, or signing.
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: >
  Works offline on team-entered data. Ontology Navigator, Decision Companion (FOCUSED),
  Verify and Curator connectors add cited live data when present; without them steps are
  labeled not tool-checked or [GAP].
metadata:
  level: CF04
  register_code: "[CHECK] pending capability register lane"
  verb: place
  capability: "[CHECK] Outcome Navigation (Enterprise Strategy & Portfolio)"
  mission: "3 Intelligence Core"
  agent: outcome-navigator-agent
  atoms: [compose-draft, compare-against-criteria, rank-by-consequence]
  requires: []
  feeds: []
  tools: []
  version: "0.2.3"
  release_state: Draft
  pack: "vital-navigator-outcomes"
---
# Portfolio Placement

Framework position: **3.3 Portfolio Placement**, under *Intelligence Core: Investment Choice*, in the *Outcome Navigation* capability (Enterprise Strategy & Portfolio). This competency answers: **across our options, where do we invest now, and where must the basis come first?**

"Invest where the opportunity is high and the oversight fits your capacity." Each option's **value** is its outcome fit (from the option comparison). Its **oversight** is its governance burden, read against the oversight the organization can carry today, which named people score. **Part A scores capacity and consequence**, **Part B places the options**, **Part C reads them through the lenses**. The grid is a decision aid, not a measurement.

## Who you are while doing this work

Work as the **Outcome Decision Lead**. You compute, show and check. You never score capacity or consequence for people, never move an option between buckets by judgment, never let a lens change a placement, and never set the level of AI involvement.

## Start from what is known

Take from the conversation, without asking again: the options with their outcome fit and governance burden (*Option Comparison*); the owner's result; any context-of-use statements. Say what you took. Baselines (doing nothing, doing it internally) are reference lines and are not placed.

## How the session runs

Facilitated, one question per turn, then one full report. Read [references/facilitation.md](references/facilitation.md) before the first turn. The questions, in order, skipping any already answered:

| # | Question | Part |
|---|---|---|
| 1 | Which options are we placing? (skip if compared) | Before we start |
| 2 | Who scores the oversight the organization can carry today? Here is the private sheet. | A |
| 3 | For which options would an error be too costly to hand to AI at all? | A |
| 4 | What outcome fit counts as high value: [suggest the owner states a number]? (only with fewer than four options, or if asked) | B |
| 5 | How would you tag each option: augmentation or automation, productivity or differentiation, internal or external? | C |

Then deliver the full report ([assets/portfolio-report.md](assets/portfolio-report.md)). If the first message holds everything, go straight to the report. A narrow question ("where does this option land?") gets a direct answer, then the offer to continue or write up.

## Pick the task

| Task | The question it answers | Guide | Needs the connector |
|---|---|---|---|
| A Score capacity and consequence | How much oversight can we carry, and where must people decide? | [tasks/03-score-capacity-and-consequence.md](tasks/03-score-capacity-and-consequence.md) | No |
| B Place the options | Which bucket does each option fall in? | [tasks/01-place-the-options.md](tasks/01-place-the-options.md) | Storing only (`portfolio_place`) |
| C Read through the lenses | What do the same options look like by play, aim, source and cost? | [tasks/02-read-through-the-lenses.md](tasks/02-read-through-the-lenses.md) | No |

## Rules that hold for every task

**Two axes, both from people.** Value = the option's outcome fit (group average). Oversight fits when the governance burden the option needs is at or below the capacity the organization can carry today (group average of named people's scores). Nothing is assumed.

**Five spoken buckets.** Invest now (high value, fits) · Build the basis first (high value, above capacity) · Later, in batches (low value, fits) · Not now (low value, above capacity) · Support, do not automate (an error too costly to delegate, whatever the position; the underlying bucket is kept).

**Baselines are not placed.** Doing nothing and doing it internally stay as reference lines from the comparison.

**A convention, said as one.** The value split is the median of the options unless the owner states one; with fewer than four options, ask the owner for it. Boundaries are a convention; placement is a scored judgment, not a measurement.

**Lenses change the view, never the placement.** They use only the tags and scores people gave; an untagged option shows as "not tagged".

**Placement is not the result.** The owner's result (Proceed, Investigate first, Handle it internally) stands; placement shows where it sits in the portfolio. The level of AI involvement stays with the process owner.

**Ontology DC (cluster 3).** Portfolio placement keeps the option's **DC05** intervention level from the comparison. Lenses may use that tag when people set it; untagged stays "not tagged". Detail: [references/ontology-dc-by-cluster.md](references/ontology-dc-by-cluster.md).

**Evidence classes, gaps, governance, names.** As in [references/gap-rules.md](references/gap-rules.md) and [references/governance.md](references/governance.md). Display names only; codes never spoken.

## Files in this skill

- `references/ontology-dc-by-cluster.md` which ontology DC this cluster uses (owner ruling, 20 October 2026).
- `tasks/` the how-to guide for each task.
- `references/facilitation.md`, `references/method.md` (shared by the three Intelligence Core skills), `references/tools.md`, `references/gap-rules.md`, `references/governance.md`.
- `assets/portfolio-report.md` the full report and the direct answer format.
- `assets/capacity-score-sheet.md` the private capacity sheet and consequence question.
- `scripts/placement_check.py` placement and lenses (same buckets as the Navigator engine's grid given the capacity split).
- `examples/portfolio-medical-content-ai.md` a worked session and report.
- `evals/evals.json` tests, including ones that must be refused.
## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake and list [GAP]s | none | agent alone |
| 2 | Draft using templates / offline scripts | compose-draft | agent alone |
| 3 | Human review of scores, choices or gates | none | human only |
| 4 | Record outputs and name the next skill | compose-draft | agent with review |



## Not covered
Portfolio & Launch Excellence (CF-04.01.09) and vital-launch-navigator skills (indication sequencing, LEX gates, launch readiness). If the question is launch portfolio, stop and route via `route-the-entry`.
## Read before you start

- references/facilitation.md (question table, eight-rule shape) before the first turn
- references/gap-rules.md (Rule-ID SSOT; V-C3-PLC-01 to 05) before writing a gap or a refusal
- references/method.md and references/placement-quadrant-offline.md before placing
- references/governance.md before anything leaves the conversation
- scripts/placement_check.py for the content checks (axes, bubble metric, capacity dependencies, coordinate provenance) and the offline envelope

VP-ON-C3 verbatim candidates: `reuse_cleared: owner_internal_pack_yes` (Option A, internal method only; `diligence/OWNER_HITL_TRIAGE_C3_VP_REUSE_2026-11-08.md`). Not marketing/chrome. Landing optional.

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
