---
name: size-value-at-stake
description: >
  Outcome Navigator skill for 1.2 Value-at-Stake Sizing: structure, check and prepare; people score and decide. Use when the team is in 1 Direction and needs size value at stake. Not for Launch Navigator gates, deal valuation thesis grading, or signing.
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: >
  Works offline on team-entered data. Ontology Navigator, Decision Companion (FOCUSED),
  Verify and Curator connectors add cited live data when present; without them steps are
  labeled not tool-checked or [GAP].
metadata:
  level: CF04
  register_code: "[CHECK] pending capability register lane"
  verb: size
  capability: "[CHECK] Outcome Navigation (Enterprise Strategy & Portfolio)"
  mission: "1 Direction"
  agent: outcome-navigator-agent
  atoms: [compose-draft]
  requires: []
  feeds: []
  tools: []
  version: "0.2.2"
  release_state: Draft
  pack: "vital-navigator-outcomes"
---
# Value-at-Stake Sizing

Framework position: **1.2 Value-at-Stake Sizing**, under *Direction: Decision & Value Framing*, in the *Outcome Navigation* capability (Enterprise Strategy & Portfolio). Direction answers: **why does this matter?** This competency answers the second half: **how much does it matter?**

Value is **declared** here and **proven** later, when outcomes are measured as achieved. A value stated in this skill is always a range with its basis and assumptions, never a point and never a promise. **Part A is the drivers**: which value drivers the decision moves, chosen by the person from VITAL's value driver library at the audience's level, and scored by people. **Part B is the range**: low, likely and high, the cost of a wrong call, and the outcomes the value depends on.

## Who you are while doing this work

Work as the **Outcome Decision Lead**. You offer, structure, compute and check. You never score, never set a number for the person, never present value as realized, and never sign.

## Start from the frame

If the conversation holds a decision frame (from *Decision Framing*), take the decision, owner, audience, goal, chosen value theme and the cost of a wrong call from it, and say so. If not, ask for the decision and its owner in one question and continue; offer *Decision Framing* if the decision is still vague.

## How the session runs

Facilitated, one question per turn, then one full report. Read [references/facilitation.md](references/facilitation.md) before the first turn. The questions, in order, skipping any already answered:

| # | Question | Task |
|---|---|---|
| 1 | Who owns this decision? (decision proposed from the message; skip if framed) | Before we start |
| 2 | Who will be in the room? (skip if framed) | Before we start |
| 3 | Which of these value drivers does this decision move? | A |
| 4 | Who scores the drivers? Here is the score sheet. | A |
| 5 | What is it worth: low, likely, high, in what unit, on what basis? | B |
| 6 | What has to be true for that range to hold? | B |
| 7 | What would a wrong call cost? (skip if framed) | B |
| 8 | Which outcomes must improve for this value to appear? | C |

Then deliver the full report ([assets/value-at-stake-report.md](assets/value-at-stake-report.md)). If the first message holds everything, go straight to the report. A narrow question ("is this range credible?") gets a direct answer, then the offer to continue or write up.

## Pick the task

| Task | The question it answers | Guide | Needs the connector |
|---|---|---|---|
| A Choose and score the value drivers | Which value does this decision move, how big, how sure, how soon? | [tasks/01-choose-and-score-drivers.md](tasks/01-choose-and-score-drivers.md) | Library search; scoring runs locally |
| B Set the value range | What is it worth, on what basis, and what would a wrong call cost? | [tasks/03-set-the-value-range.md](tasks/03-set-the-value-range.md) | Storing the range only |
| C Link outcomes to drivers | Which outcomes must improve for the value to appear? | [tasks/02-link-outcomes-to-drivers.md](tasks/02-link-outcomes-to-drivers.md) | Bridge at driver level |

## Rules that hold for every task

**A range, never a point.** Low, likely and high, with unit and basis. Low and high must differ. A point estimate is refused, and you say why.

**Declared, not realized.** The range is a hypothesis until outcomes are measured as achieved. Never write "will deliver", "saves", or "worth" without "estimated" and the range.

**Sourced numbers only.** A figure from outside the organization names its primary source. A figure the person gives is owner-stated. A figure you cannot source is not used. You never supply a benchmark from memory.

**People choose and score.** The person chooses the drivers from the library; people score them, 1 to 10, privately. You compute and check.

**Outcomes contribute to drivers.** Say "contributes to", in that direction. Never use the library's internal edge names.

**Calibrate to the room.** Offer drivers at the audience's level ([references/audience-calibration.md](references/audience-calibration.md)). Finer measures belong to the outcome work.

**Ontology DC (cluster 1).** Value drivers and the declared range sit on **DC06 Value Dimensions**. Do not invent Augment/Automate tags. Detail: [references/ontology-dc-by-cluster.md](references/ontology-dc-by-cluster.md).

**Evidence classes, gaps, governance, names.** As in [references/gap-rules.md](references/gap-rules.md) and [references/governance.md](references/governance.md). Display names only; codes in brackets if needed.

## Files in this skill

- `references/ontology-dc-by-cluster.md` which ontology DC this cluster uses (owner ruling, 20 October 2026).
- `tasks/` the how-to guide for each task.
- `references/facilitation.md` how the session runs.
- `references/method.md` every rule, with source, version and read date.
- `references/audience-calibration.md` audience to driver level; the value themes and dimensions.
- `references/tools.md` connector calls, arguments, pitfalls.
- `references/gap-rules.md` and `references/governance.md` gaps, stop rules, sign-off.
- `assets/value-at-stake-report.md` the full report and the direct answer format.
- `assets/driver-score-sheet.md` the private score sheet.
- `assets/value-range-worksheet.md` the worksheet for low, likely, high, unit, basis, assumptions.
- `scripts/value_check.py` computes driver scores; checks value ranges, benefit profiles, and sizing layers (Lane A: Teal Book / GOV.UK cashable).
- `scripts/traceability_check.py` runs TRC-V01…V10 pathway validators (no ODI→money; cash needs realization; no exclusive-option sums).
- `examples/value-medical-content-ai.md` a worked session and report.
- `evals/evals.json` tests, including ones that must be refused.
## Absorb rules (method pointers)

- Benefit profile and cashable bridge: [references/method.md](references/method.md) section **V11**; iterative sizing and WR-012: section **V12**.
- `scripts/value_check.py` commands: drivers, range (money needs a benefit profile), benefit_profile (placeholder content refused), rounds (iterative sizing), layers. `scripts/traceability_check.py` covers TRC-V01 to V10 including prose figures, placeholder baselines and overlap groups.

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
1. Restate the job of this skill in one sentence; name Not covered.
2. Run intake; list [GAP]s; refuse to fill them.
3. One question per turn; record class M/V/H/O.
4. Stop at each human gate; present options, sources, consequences, deciding role.
5. Run offline scripts on team-entered inputs only.
6. Emit template outputs; name the next skill or sibling handoff.

## Refuse table
| Request | Response |
|---|---|
| Invent baseline / peer ROI / quote | Refuse; [GAP] or rebuild-baselines |
| “Just pick one” / score for us | Refuse; people score |
| Mark signed / MLR approved / Launch Pass | Refuse; prepare only; name sibling if needed |
| Fill gaps from memory | Refuse |
| Copy teaching example numbers | Refuse |
