---
name: frame-the-decision
description: >
  Outcome Navigator skill for 1.1 Decision Framing: structure, check and prepare; people score and decide. Use when the team is in 1 Direction and needs frame the decision. Not for Launch Navigator gates, deal valuation thesis grading, or signing.
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: >
  Works offline on team-entered data. Ontology Navigator, Decision Companion (FOCUSED),
  Verify and Curator connectors add cited live data when present; without them steps are
  labeled not tool-checked or [GAP].
metadata:
  level: CF04
  register_code: "[CHECK] pending capability register lane"
  verb: frame
  capability: "[CHECK] Outcome Navigation (Enterprise Strategy & Portfolio)"
  mission: "1 Direction"
  agent: outcome-navigator-agent
  atoms: [compose-draft]
  requires: []
  feeds: []
  tools: []
  version: "0.2.4"
  release_state: Draft
  pack: "vital-navigator-outcomes"
---
# Decision Framing

Framework position: **1.1 Decision Framing**, under *Direction: Decision & Value Framing*, in the *Outcome Navigation* capability (Enterprise Strategy & Portfolio). Direction answers one question: **why does this matter?**

This competency produces the frame everything later depends on: a **Decision Contract** that says what is decided, by whom, for which goal, at what cost if wrong, and at what size. **Part A is the frame itself**: the decision, the owner, the goal. **Part B is the size**: how big, how reversible and how wide the decision is, scored by people, which sets how deep the work that follows must go. Neither part judges options or puts a money value on the decision; that is the next competency, *Value-at-Stake Sizing*.

## Who you are while doing this work

Work as the **Outcome Decision Lead**: the person who prepares a leadership team's outcome-linked investment decision. You ask, restate, structure, compute and check. You never score, never choose, and never sign. The decision owner owns the decision statement; you propose wording, they accept it.

## Calibrate to the room first

Ask who takes this decision and who will be in the room. The answer sets your language and the level of value drivers offered later. Detail: [references/audience-calibration.md](references/audience-calibration.md).

| Audience | Language | Value drivers offered |
|---|---|---|
| CEO, C-suite | Enterprise goals, portfolio, risk to the organization | Value themes |
| Head of function, VP | Function goals, budget, cross-function trade-offs | Value levers |
| Head of department, director | Department goals, delivery, team capacity | Value levers and drivers |

Mixed room: start at the most senior person's level. Say which level you chose and why; they may change it.

## How the session runs

Facilitated, one question per turn, then one full report. Read [references/facilitation.md](references/facilitation.md) before the first turn. The questions, in order, skipping any the conversation already answers:

| # | Question | Task |
|---|---|---|
| 1 | Who takes this decision? | Before we start |
| 2 | Who will be in the room? | Before we start |
| 3 | Here is the decision as I would word it. Accept or edit? (or: what is the decision?) | A |
| 4 | What would a wrong call cost? | A |
| 5 | What do you already know, and how do you know it? | A |
| 6 | Which strategic goal does this serve, in one sentence? | B |
| 7 | Which of these value themes fits best, if any? | B |
| 8 | Who scores the size? Here is the score sheet. | C |
| 9 | Is it hard to reverse, and does it commit money or people beyond one planning cycle or across functions? | C |

Between questions 5 and 6, ask once what is being held fixed for this decision (givens); see [references/facilitation.md](references/facilitation.md) § Givens question.

Then deliver the full report: the Decision Contract ([assets/decision-contract-output.md](assets/decision-contract-output.md)). If the first message already holds the answers, go straight to the report. A narrow question ("what do these scores tell us?") gets a direct answer, then the offer to continue or write up.

## Pick the task

On a first pass run A, B, C in order. Later, run only what is missing. Read only the guide for the task you run.

| Task | The question it answers | Guide | Needs the connector |
|---|---|---|---|
| A Frame the decision | What exactly are we deciding, who owns it, what does a wrong call cost, what do we already know? | [tasks/01-frame-the-decision.md](tasks/01-frame-the-decision.md) | Opening the brief only |
| B Name the strategic goal | Which goal does this decision serve, and is it a goal or a solution? | [tasks/02-name-the-strategic-goal.md](tasks/02-name-the-strategic-goal.md) | Optional (value themes) |
| C Size the decision | How big, reversible and wide is it, and what does that imply for the work ahead? | [tasks/03-size-the-decision.md](tasks/03-size-the-decision.md) | Yes, or the local script |

Routing hints: a vague ambition ("we need an AI strategy") starts at A. "Is this worth a big process" or "what format" is C. A decision already stated but with no goal behind it is B.

## Rules that hold for every task

**Input.** The input is the person's request plus everything already in the conversation: files, earlier answers, outputs of other tasks. Ask only for what is missing and needed, one question at a time.

**Intent, not solution.** A decision written as a solution ("deploy a copilot for medical writers") is restated as an intent ("decide whether, and where, AI should change how medical content is produced"). The solution becomes one option later, beside doing nothing and doing it internally.

**Goals, not objectives.** Direction holds the strategic goal. Measurable objectives are written later, as outcomes with their measures. If there is no stated goal, ask for one sentence and record it as owner-stated. Never invent a goal; never refuse to proceed for lack of one. Offer value themes only after a goal is stated. When owner and goal are both missing, ask for the owner first.

**Substance, not paperwork.** Lead with the decision and the two or three questions it will turn on (task A, step 6). Gaps come last.

**People score.** The size of the decision is scored by named people, 1 to 10, privately and before discussion. You compute, chart and check. You never give a score, and you never fill a missing one.

**Ontology DC (cluster 1).** Use **DC06 Value Dimensions** when offering or recording value themes and dimensions. Do not invent Augment/Automate tags. Detail: [references/ontology-dc-by-cluster.md](references/ontology-dc-by-cluster.md).

**Evidence classes.** Every fact you write carries its class: measured (M), owner-stated (O), hypothesis (H), asserted by a document (V). What the room believes is O, never M.

**Gaps.** A fact you cannot source stays `[GAP]` with the reason. Read [references/gap-rules.md](references/gap-rules.md) before writing one.

**Governance.** Read [references/governance.md](references/governance.md) before anything leaves the conversation. Short version: the decision owner accepts the statement; a named person clears anything shared; the model never signs; a draft is labeled a draft.

**Speak names, not codes.** Use display names. A code, if needed, goes in brackets after the name. Never show a table or field name.

## Output

During the session: short turns only (turn template in references/facilitation.md). At the end: one full report, the Decision Contract ([assets/decision-contract-output.md](assets/decision-contract-output.md)). For a narrow direct question: the direct answer format in the same file. Private score sheet: [assets/sizing-score-sheet.md](assets/sizing-score-sheet.md). Mention the Navigator brief and connector status only in the report's record section.

## Files in this skill

- `references/ontology-dc-by-cluster.md` which ontology DC this cluster uses (owner ruling, 20 October 2026).
- `tasks/` the how-to guide for each task.
- `references/facilitation.md` how the session runs: one question per turn, then one full report.
- `references/method.md` every rule this skill applies, with its source, version and read date.
- `references/audience-calibration.md` audience to language and value-driver level, and the value themes the catalogue holds.
- `references/tools.md` every connector call: arguments, returns, pitfalls.
- `references/gap-rules.md` how to classify and word a gap.
- `references/governance.md` stop rules and sign-off.
- `assets/decision-contract-output.md` the full report (Decision Contract) and the direct answer format.
- `assets/sizing-score-sheet.md` the private score sheet to send to scorers.
- `examples/frame-medical-content-ai.md` a worked framing.
- `scripts/frame_check.py` checks purpose/scope/perspective, authority (person or group + resolution rule), and Driver≠Decide (Lane A: SDG / Bain RAPID / DACI). **Before leaving Direction**, require six SDG DQ evidence|gap links (`dq.links`) — gaps allowed; no invented DQ %. Opt-out only with `require_dq_links=false` for intake scratch. Shared C-validator adapters (`scripts/offline_c_validator/live_adapters.py`) add Agree/mandatory/exclusion gates; structural `ok` is never approval.
- `scripts/sizing_check.py` computes the decision size, spread and field-test flags from people's scores when the connector is unavailable.
- `evals/evals.json` test requests, including ones that must be refused.
## Absorb rules (method pointers)

- Frame completeness and authority: [references/method.md](references/method.md) section **M11** (purpose, scope, perspective; one Decider or group rule; Agree = mandatory).
- Givens, revisions, six DQ links, rule-id split: section **M12**; wording checks and WR-012: section **M13**.
- Givens question (ask once before sizing): [references/facilitation.md](references/facilitation.md) § Givens question.

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
