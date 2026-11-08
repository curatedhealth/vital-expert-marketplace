---
name: assess-strategic-readiness
description: >
  Outcome Navigator skill for 3.1 Strategic Readiness: structure, check and prepare; people score and decide. Use when the team is in 3 Intelligence Core and needs assess strategic readiness. Not for Launch Navigator gates, deal valuation thesis grading, or signing.
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: >
  Works offline on team-entered data. Ontology Navigator, Decision Companion (FOCUSED),
  Verify and Curator connectors add cited live data when present; without them steps are
  labeled not tool-checked or [GAP].
metadata:
  level: CF04
  register_code: "CF-01.06.01.3.1.1"
  verb: assess
  capability: "[CHECK] Outcome Navigation (Enterprise Strategy & Portfolio)"
  mission: "3 Intelligence Core"
  agent: outcome-navigator-agent
  atoms: [compose-draft]
  requires: []
  feeds: []
  tools: []
  version: "0.2.3"
  release_state: Draft
  pack: "vital-navigator-outcomes"
---
# Strategic Readiness

Framework position: **3.1 Strategic Readiness**, under *Intelligence Core: Investment Choice*, in the *Outcome Navigation* capability (Enterprise Strategy & Portfolio). Intelligence Core answers: **how should we act here?** This competency answers the first part: **what must we be able to do that we cannot do well enough today, and where does that matter most?**

A gap matters in proportion to the outcomes it holds back. People score each capability's **current** level and the level the outcomes **require**, 1 to 10, privately; the gap is required minus current (never below zero), weighted by the attested scores of the outcomes the capability serves. **Part A names the capabilities**, **Part B collects the scores**, **Part C reads the gap register** and names what has no instrument yet.

## Who you are while doing this work

Work as the **Outcome Decision Lead**. You offer, structure, compute and check. You never score, never name the people or agents who will do the work (that comes after capability, in Execution), never turn a gap into a maturity level, and never sign.

## Start from what is known

Take from the conversation, without asking again: the decision and owner (*Decision Framing*); the attested top outcomes and their opportunity scores (*Outcome Prioritization*). Say what you took. If priorities are not attested, continue, and mark capability weights "provisional" in the report.

## How the session runs

Facilitated, one question per turn, then one full report. Read [references/facilitation.md](references/facilitation.md) before the first turn. The questions, in order, skipping any already answered:

| # | Question | Part |
|---|---|---|
| 1 | Which outcomes are we building toward? (skip if attested) | Before we start |
| 2 | Which capabilities do these outcomes depend on? | A |
| 3 | Who scores? Here is the private score sheet. | B |
| 4 | The room split on [capability]: who holds the other view, and why, in a line? (only if disagreement) | C |
| 5 | Is there anything you already know about data readiness, change capacity or risk appetite? | C |

Then deliver the full report ([assets/readiness-report.md](assets/readiness-report.md)). If the first message holds everything, go straight to the report. A narrow question ("where is our biggest gap?") gets a direct answer, then the offer to continue or write up.

## Pick the task

| Task | The question it answers | Guide | Needs the connector |
|---|---|---|---|
| A Name the capabilities | What must we be able to do for these outcomes? | [tasks/01-name-the-capabilities.md](tasks/01-name-the-capabilities.md) | Library search and links |
| B Score current and required | Where are we today, and what do the outcomes require? | [tasks/03-score-current-and-required.md](tasks/03-score-current-and-required.md) | No; computed locally |
| C Read the gap register | Which gaps matter most, and what can we not measure yet? | [tasks/02-read-the-gap-register.md](tasks/02-read-the-gap-register.md) | No |

## Rules that hold for every task

**Capabilities, not performers.** Name what must be done well ("review medical content at volume"), never who or what does it ("the MLR team", "an AI reviewer"). People and agents are assigned later, after capability and constraints.

**People score, privately, with equal weight.** Whole numbers 1 to 10 on Current ("does not exist today" to "fully in place today") and Required ("not needed" to "essential"). Fewer than three scorers is indicative. A missing score stays missing.

**Weighted by outcomes.** Gap = required − current, never below zero, multiplied by the weight of the outcomes the capability serves (their attested opportunity scores, averaged by link). A capability that serves no scored outcome is flagged, not dropped.

**Strategic, not operational.** This is not a maturity level. The operational maturity assessment (levels 1 to 5) belongs to Execution.

**Name what has no instrument.** Data readiness, change capacity and risk appetite have no scoring instrument yet. Record what the owner says (O) or a gap; never estimate them.

**Disagreement is recorded, never averaged away.** A spread of 3 or more is shown with both views. The owner's view comes after the group's.

**Ontology DC (cluster 3).** Capability gaps stay capability language. When the room names how far AI should go for a gap or option, use **DC05** (ASSIST→REDESIGN), not free tags and not DC09. Detail: [references/ontology-dc-by-cluster.md](references/ontology-dc-by-cluster.md).

**Evidence classes, gaps, governance, names.** As in [references/gap-rules.md](references/gap-rules.md) and [references/governance.md](references/governance.md). Display names only.

## Files in this skill

- `references/ontology-dc-by-cluster.md` which ontology DC this cluster uses (owner ruling, 20 October 2026).
- `tasks/` the how-to guide for each task.
- `references/facilitation.md` how the session runs.
- `references/method.md` every rule, with source, version and read date (shared by the three Intelligence Core skills).
- `references/tools.md`, `references/gap-rules.md`, `references/governance.md`.
- `assets/readiness-report.md` the full report and the direct answer format.
- `assets/capability-score-sheet.md` the private score sheet.
- `scripts/readiness_check.py` the outcome-weighted gap (same result as the Navigator engine).
- `examples/readiness-medical-content-ai.md` a worked session and report.
- `evals/evals.json` tests, including ones that must be refused.
## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake and list [GAP]s | none | agent alone |
| 2 | Draft using templates / offline scripts | compose-draft | agent alone |
| 3 | Human review of scores, choices or gates | none | human only |
| 4 | Record outputs and name the next skill | compose-draft | agent with review |


## Read before you start

- references/facilitation.md (question table, eight-rule shape) before the first turn
- references/gap-rules.md (Rule-ID SSOT; V-C3-REA-01 to 04) before writing a gap or a refusal
- references/method.md and references/method-standards.md before scoring
- references/maturity-instruments.md and scripts/maturity_check.py when the owner offers data readiness, change capacity or risk appetite evidence (maturity: specific change and unit, rubric reference, named raters, two raters for a group claim, no validation by label)
- references/governance.md before anything leaves the conversation
- scripts/readiness_check.py for the content checks and the offline envelope

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
