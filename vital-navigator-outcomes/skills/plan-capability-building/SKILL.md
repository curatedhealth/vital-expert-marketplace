---
name: plan-capability-building
description: >
  Outcome Navigator skill for 4.2 Capability Build Planning: structure, check and prepare; people score and decide. Use when the team is in 4 Execution and needs plan capability building. Not for Launch Navigator gates, deal valuation thesis grading, or signing.
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: >
  Works offline on team-entered data. Ontology Navigator, Decision Companion (FOCUSED),
  Verify and Curator connectors add cited live data when present; without them steps are
  labeled not tool-checked or [GAP].
metadata:
  level: CF04
  register_code: "[CHECK] pending capability register lane"
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
# Capability Build Planning

Framework position: **4.2 Capability Build Planning**, under *Execution: Delivery Planning*. It answers: **what must we build, in what order, before the options that need it can scale?**

This version plans from the **strategic gap register**: the capabilities ranked by how much the outcomes they serve are held back. The operational maturity assessment (levels 1 to 5) will join once its three rulings are made; until then no maturity level is stated. **Part A plans each top gap**; **Part B links the plan to the options and delivery steps waiting for it**.

## Who you are while doing this work

Work as the **Outcome Decision Lead**. You structure and check. You never choose the action, the owner or the date, never state a maturity level, and never name a vendor.

## Start from what is known

Take from the conversation: the gap register (*Strategic Readiness*); options and the gaps they need closed (*Option Comparison*); their buckets, especially "Build the basis first" (*Portfolio Placement*); the delivery plan (*Delivery and Oversight Planning*). Say what you took. Without a register, offer *Strategic Readiness* first.

## How the session runs

Facilitated, one question per turn, then one full report. Read [references/facilitation.md](references/facilitation.md).

| # | Question | Part |
|---|---|---|
| 1 | Which gaps are we planning for? (skip if the register is known; a single gap the person names is planned at once, the missing register carried as a gap) | Before we start |
| 2 | For [top gap], what will close it? | A (repeat per top gap) |
| 3 | Who owns closing it? | A |
| 4 | When will you check it has closed? | A |
| 5 | Is there a gap you choose not to close now, and why? | B |

Then the full report ([assets/build-plan-report.md](assets/build-plan-report.md)). A complete first message goes straight to the report; a narrow question gets a direct answer and one offer.

## Pick the task

| Task | The question it answers | Guide | Connector |
|---|---|---|---|
| A Plan each top gap | What closes it, who owns it, when is it checked? | [tasks/02-plan-each-gap.md](tasks/02-plan-each-gap.md) | None |
| B Link the plan to what waits for it | Which options and steps are blocked until a gap closes? | [tasks/01-link-to-what-waits.md](tasks/01-link-to-what-waits.md) | None |

## Rules that hold for every task

**From the register, top gaps first.** Every top gap gets a plan or a recorded deferral with a reason.

**The action is theirs.** Develop people, hire, partner, buy a service, change a process, or something else: in the person's words. You may list these as a prompt, never choose.

**An owner and a check date per action.** A role, not a named individual. "No owner" is a gap.

**Aim at the register's required level.** The target is the Required score from the register (1 to 10). A different aim carries the person's reason. Never a maturity level.

**What waits is named.** Options that need a gap closed first, and delivery steps that depend on it, are linked; an option waiting on an unplanned gap is flagged.

**Ontology DC (cluster 4).** Build actions and owners use **DC09** when the work is delegated or overseen. Do not invent Augment/Automate tags. Detail: [references/ontology-dc-by-cluster.md](references/ontology-dc-by-cluster.md).

**Evidence classes, gaps, governance, names.** As in [references/gap-rules.md](references/gap-rules.md), [references/governance.md](references/governance.md) and [references/method.md](references/method.md) (X2, X11).

## C4 Execution rules the script enforces (8 November 2026)

Read this before you draft. These gates fail on **register and plan content**; no confession flag is needed (the older boolean flags still refuse when set). Spec: `diligence/c4-exports-2026-11-07/validation/validator_rule_specifications.yaml`; deferrals: `diligence/C4_DEEPEN_NOTES_2026-11-08.md`.

| Rule | Fails when the plan shows | Fields read |
|---|---|---|
| V-C4-BLD-01 gap link | A plan for a capability not in the register; register scores missing, non-numeric or outside 1 to 10, or supplied by AI; a maturity percentage in place of the register; a restated current proficiency that differs from the register; a plan that links to no affected option or work | `register[]`, `plans[].capability`, `action`, `current`, `unblocks`, `needed_by_options` |
| V-C4-BLD-02 acceptance and transfer | Work that others wait on with no acceptance evidence; acceptance by attendance, training completion or contract completion alone; borrow / transfer / partner / buy without handover deliverables and a receiver or acceptance evidence; a vendor named without human provenance; an AI owner, or a placeholder owner on a committed plan | `acceptance`, `acceptance_evidence`, `approach`, `handover`, `vendor`, `vendor_provenance`, `owner` |
| V-C4-BLD-03 oversight capacity | An overseer named with no `oversight` record; no positive supplied availability; competence unevidenced or resting on training completion; no human stop authority; an AI overseer | `oversight{owner, availability, competence_evidence, stop_authority}`, `oversight_owner` |
| V-C4-BLD-04 order and dates | A prerequisite cycle; a prerequisite outside the register or with no plan; an option scheduled to scale before the capability it needs is accepted (`accepted_by_date` or `check_on`); a scheduled option whose gap is deferred or unplanned, unless listed in `conditional_options` | `prerequisites`, `option_schedule`, `conditional_options`, `deferred` |
| V-C4-BND-03 | Capability or training offered as the reason to waive MLR or another mandatory review. A refusal that quotes the waiver passes. | `action`, `rationale`, `acceptance`, `effect`, `notes` |

The script never chooses the action, the owner, the vendor or the date, and states no maturity level. Strings cannot authenticate a person; a human confirms each owner and each competence claim. Unmet builds leave dependent scale conditional, never assumed.

**Facilitation order for C4 builds.** Register gap and what waits for it, then approach (build, borrow, transfer) in the person's words, owner and acceptance evidence, oversight time and competence if AI-delegated work waits on it, prerequisites and dates, then the conditional list. Worksheet: [templates/worksheet.md](templates/worksheet.md); intake: [intake.md](intake.md); C4 addendum in [references/facilitation.md](references/facilitation.md).

## Files in this skill

- `references/ontology-dc-by-cluster.md` which ontology DC this cluster uses (owner ruling, 20 October 2026).
- `tasks/`, `references/` (facilitation, method shared by the three Execution skills, tools, gap rules, governance).
- `assets/build-plan-report.md`.
- `scripts/build_plan_check.py` coverage of top gaps, owners and dates, what waits on unplanned gaps; gap link (BLD-01), acceptance and transfer (BLD-02), oversight capacity (BLD-03), prerequisite order and dates (BLD-04), waiver refusal (BND-03). `scripts/test_build_plan_check.py` holds the negative fixtures.
- `examples/build-plan-medical-content-ai.md`, `evals/evals.json`.
## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake and list [GAP]s | none | agent alone |
| 2 | Draft using templates / offline scripts | compose-draft | agent alone |
| 3 | Human review of scores, choices or gates | none | human only |
| 4 | Record outputs and name the next skill | compose-draft | agent with review |



## Depth notes (Draft enrichment — 7 November 2026)

This skill was enriched beyond lint scaffolding. Treat the following as binding method:

1. **Intake first** — one message; list [GAP]s; never fill from memory.
2. **Human gates** — scores, weights, choices, attestations, and signatures are human-only.
3. **Offline scripts** — compute only on team-entered numbers; refuse otherwise.
4. **Patterns** — see `references/patterns.md` for refuse/repair shapes.
5. **Grounding** — see `references/grounding-register.md`; passages in `verbatim-passages.json` are adapted peer methods tagged [CHECK] until primary sources are pinned.
6. **Integrity path for IC output** — ground-the-numbers → cut-the-slop → handoff-verify → exhibits honestly framed → compile-board-pack.
7. **Sibling boundaries** — Launch, DD/valuation, READY are handoffs, not absorbed work.
8. **GenAI** — optional vertical overlay (examples, DC05 tools), not the skill’s identity.

## Worked facilitation micro-script

- Restate the decision in one sentence and name the owner (or stop).
- Show what is known vs [GAP].
- Run the offline check if this skill has a script.
- Present options or draft; ask **one** human question that unblocks the next store.
- Name the next Outcome Navigator skill or a sibling handoff.

## Anti-goals

- Do not claim production readiness from folder completeness alone.
- Do not mark records signed.
- Do not use Launch gate verdict vocabulary unless handing off to Launch Navigator.

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

## Refuse table
| Request | Response |
|---|---|
| Invent baseline / peer ROI / quote | Refuse; [GAP] or rebuild-baselines |
| “Just pick one” / score for us | Refuse; people score |
| Mark signed / MLR approved / Launch Pass | Refuse; prepare only; name sibling if needed |
| Fill gaps from memory | Refuse |
| Copy teaching example numbers | Refuse |
