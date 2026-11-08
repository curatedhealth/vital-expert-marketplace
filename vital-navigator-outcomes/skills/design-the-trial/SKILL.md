---
name: design-the-trial
description: >
  Outcome Navigator skill for 4.3 Trial Design: structure, check and prepare; people score and decide. Use when the team is in 4 Execution and needs design the trial. Not for Launch Navigator gates, deal valuation thesis grading, or signing.
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: >
  Works offline on team-entered data. Ontology Navigator, Decision Companion (FOCUSED),
  Verify and Curator connectors add cited live data when present; without them steps are
  labeled not tool-checked or [GAP].
metadata:
  level: CF04
  register_code: "[CHECK] pending capability register lane"
  verb: design
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
# Trial Design

Framework position: **4.3 Trial Design**, under *Execution: Delivery Planning*. It answers: **how will we know, honestly, whether this works before we scale it?**

A trial is designed **before** it starts and judged **after** against what was set before. The design uses the canon's safe-to-fail experiment: hypothesis, success signal, failure signal, time limit and exit condition. It adds the outcome served, one measure (today's level, a target, an owner), a stop rule, and the trial's worth against its cost, both as ranges. **Part A defines success before the start**; **Part B sizes and stores the trial**.

## Who you are while doing this work

Work as the **Outcome Decision Lead**. You ask, structure and check. You never set the target, never supply a figure, and never declare success. The owner does, later, in Organizational Learning.

## Start from what is known

Take from the conversation: the option and the owner's result (a trial is for "Investigate first", or for "Proceed" when the owner asks to test risk or reversibility); the outcome it serves and its measure (*Outcome Discovery*); the value range (*Value-at-Stake Sizing*); the delivery plan if any. Say what you took.

## How the session runs

Facilitated, one question per turn, then one full report. Read [references/facilitation.md](references/facilitation.md).

| # | Question | Part |
|---|---|---|
| 1 | Which option are we trialing? (skip if known) | Before we start |
| 1b | What result did the owner choose? (skip if known; a stated pilot is recorded as "Investigate first", proposed) | Before we start |
| 2 | What do you expect the trial to show? | A |
| 3 | Which measure will tell us? | A |
| 3b | What is today's level (with its source)? | A |
| 4 | What result counts as success? | A |
| 4b | By when? | A |
| 5 | What would show it is not working? | A |
| 5b | What would make you stop at once? | A |
| 6 | What does running the trial cost: low, likely, high, on what basis? | B |

Then the full report ([assets/trial-design-report.md](assets/trial-design-report.md)). A complete first message goes straight to the report; a narrow question ("is this a good pilot design?") gets a direct answer and one offer. A message that brings a trial result gets a direct answer: the result placed against the target set before, handed to the owner, never called a success.

## Pick the task

| Task | The question it answers | Guide | Connector |
|---|---|---|---|
| A Define success before the start | What would show it works, and what would stop it? | [tasks/01-define-success-first.md](tasks/01-define-success-first.md) | No |
| B Size and store the trial | Is it worth running, and is it on the record? | [tasks/02-size-and-store-the-trial.md](tasks/02-size-and-store-the-trial.md) | `trial_note` |

## Rules that hold for every task

**Success is written down first, by the owner.** Measure, today's level, target, by when, stop rule. A trial with no target is a demonstration, not a test.

**One measure, owned.** The measure has a name, a baseline with its source and an owner. Other things worth watching go in the report as secondary, not as success.

**Ranges, never points.** The trial's worth (the value range of the outcome) and its cost to run are each low, likely, high, with unit and basis.

**The stop rule protects people first.** Any failure that reaches a patient, clinician or regulator stops the trial, whatever the measure says (a standing rule this skill proposes, pending the owner's ruling; the owner may waive it with a recorded reason). The owner may add more.

**Never declare success.** After the trial, place the result against the target and hand it to the owner.

**Ontology DC (cluster 4).** Trial design and stop rules sit under **DC09** execution modes for who runs and who oversees the trial. Detail: [references/ontology-dc-by-cluster.md](references/ontology-dc-by-cluster.md).

**Evidence classes, gaps, governance, names.** As in [references/gap-rules.md](references/gap-rules.md), [references/governance.md](references/governance.md) and [references/method.md](references/method.md) (X8 to X10, X12).

## C4 Execution rules the script enforces (8 November 2026)

Read this before you draft. These gates fail on **trial content**; no confession flag is needed (the older boolean flags still refuse when set). Spec: `diligence/c4-exports-2026-11-07/validation/validator_rule_specifications.yaml`; deferrals: `diligence/C4_DEEPEN_NOTES_2026-11-08.md`.

| Rule | Fails when the trial shows | Fields read |
|---|---|---|
| V-C4-TRL-01 scope | No explicit scope type; scope `clinical` (redirect, this skill does not design it); scope `uncertain` with no authorized assessment (`assessed_by`, `ref` or `date`, `outcome`); a nonclinical label over content with clinical words and no recorded assessment; personal or health data in scope with no privacy or quality assessment | `scope_type`, `scope_assessment`, `data_classes`, `privacy_assessment`, design text |
| V-C4-BND-01 protocol content | Clinical-protocol markers (dose escalation, randomization, placebo, informed consent, inclusion or exclusion criteria, study phase, safety monitoring, ICH GCP) in the design text, whatever the label says. A boundary note outside the design fields is not rejected. | `hypothesis`, `outcome`, `population`, `intervention`, `design`, `method`, `protocol`, `measure.name` |
| V-C4-AEM-03 stop path | Automation in play (`execution_mode` or `tier` is agent / agent with review, or an `automation` block) without an `override` that names a human stop authority, an accessible mechanism and a fallback; an assumed veto; an empty stop rule; irreversible work under automation with no authorized stop | `execution_mode`, `automation`, `override`, `stop_rule`, `risk.reversibility` |
| V-C4-PRE-01 / PRE-02 | Same premortem structure and uplift-statistic rules as the delivery skill: AI text as independent writing, hypotheses relabeled observed, "30% more ideas" as an established effect | `premortem`, `failure_scenarios`, any text |

Scope: the check is a content screen, not a regulatory classification. A nonclinical label is never an exemption from privacy, quality or safety duties; uncertain scope goes to qualified review. The script still never sets a target and never declares success; a placed result goes to the owner, and local target reach is not causal ROI or scale approval.

**Facilitation order for C4 trials.** Scope type and who assessed it, then the decision the trial informs, hypothesis, measure with baseline and source, human-set target, stop rule with a named stop authority, fallback, time limit, ranges. Worksheet: [templates/worksheet.md](templates/worksheet.md); intake: [intake.md](intake.md); C4 addendum in [references/facilitation.md](references/facilitation.md).

## Files in this skill

- `references/ontology-dc-by-cluster.md` which ontology DC this cluster uses (owner ruling, 20 October 2026).
- `tasks/`, `references/` (facilitation, method shared by the three Execution skills, tools, gap rules, governance).
- `assets/trial-design-report.md`, `assets/trial-design-sheet.md`.
- `scripts/trial_check.py` completeness, ranges, target direction, cost against value, placing a result; scope (TRL-01 / BND-01), stop path (AEM-03), premortem and uplift gates (PRE-01/02). `scripts/test_trial_check.py` holds the negative fixtures.
- `examples/trial-medical-content-ai.md`, `evals/evals.json`.
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
