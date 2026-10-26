# Changelog

## 0.3.15 (2026-10-26, built by Claude, not committed)

From the six-arm test (skills +2.3 DQ on plain, +1.25 on expert prompt; connector ±0 on coaching with ~30k extra tokens and ~25% of calls returning warnings).
- DC-H18: save quietly in as few calls as possible (target one per turn; `decision_status` only every few turns); never tell the person something was saved; check the conversation before following `floor.next` (no re-asking); pre-mortem, owner/first step and review saved in the turn given; repair warnings silently.
- Never store `[GAP]` or "not given yet" as a value; missing fields are left out (headers, governance lines and status task updated).
- facilitator and where-to-start: "Method lens" section folding in the expert-prompt principles (DQ, WRAP, biases, pre-mortem, roles), since expert prompt + skills scored best.

## 0.3.14 (2026-10-26, built by Claude, not committed)

Wires the skills to connector 0.3.2 (round 6). Every new field is optional; with connector 0.3.1 the skills behave as 0.3.13.
- DC-H18 (new): use `decision_status.floor` (`next`, `ready_to_invite_choice`, item labels); say `message_for_person` when present; save as you go so the record never lags; save the choice the moment it is stated; store the lean (`make_decision.lean`) and key-assumption checks (`gather_intelligence.key_assumptions`).
- facilitator status.md: follows `floor.next`, speaks labels not ids.
- brief compile.md: reads back `person_summary_markdown` (no watermark, no tool names).
- tradeoff grid.md: rank-only criteria (`{name, rank}`), never equal weights; says `weights_missing` message.
- gather-intelligence notes.md: stores key assumptions.
- make-decision record.md: stores the lean; a lean never completes the decision.

Held-out benchmark (0.3.13, S13–S18, blind, two grader models): product vs plain +3.6 DQ (95% CI 2.9–4.3, 24/24 wins); product vs expert prompt +0.04 (−0.5 to +0.7, equivalent); guardrails 6.9 vs 6.3 of 8. Saved-record completeness about 11/16 checklist items; 0.3.14 targets that gap.

## 0.3.13 (2026-10-25, built by Claude, not committed)

Dev iteration 7: D 0.3.12 level with the expert prompt (15.2 vs 15.0) but asked for the choice at reply 16–19, cutting off commitment items.
- DC-H16 pace: count replies; frame/options/what matters by reply 10; closing sequence from reply 11–12; explicit choice by about reply 15; three replies reserved for read-back + confidence, owner + first step, review + revisit; nice-to-haves never push the choice past reply 16.

## 0.3.12 (2026-10-25, built by Claude, not committed)

Dev iteration 6 (blind 3-way, two grader models): plain 11.8, expert prompt 15.25, D 0.3.11 15.4 (weakest link 1.9 vs 1.6; guardrails best; first place 6–6). Remaining gaps: base rate only volunteered, pre-mortem without an early sign, no explicit read-back, revisit condition and first step missing.
- DC-H16: ask the base rate outright and hold it against the goal; a failure without a sign is followed by "what is the first thing you would notice?"; post-choice turns are read-back + confidence, owner + first step, review date + "what would make you look sooner?".

## 0.3.11 (2026-10-25, built by Claude, not committed)

Dev iteration 5 (blind graded, two grader models): D 0.3.10 reached parity with the expert prompt (DQ 15.1 vs 14.9, 6–6 preferences) but lost on guardrails: steering in read-backs, invented content in the record (roles, computed nets, unstated reasons, "test run"), equal weights assumed, and review/revisit cut off by late closing.
- DC-H17 (new): neutral mirror (no singling out, no "the numbers support"); clean record (only what was said or returned).
- DC-H16: weights fallback by ranking, never assumed equal; anchor source check; start the closing sequence by about the twelfth exchange.

## 0.3.10 (2026-10-25, built by Claude, not committed)

Dev iteration 4: D asked for the lean and then ran the pre-mortem and dissent after it, so post-choice items (owner, confidence, review) were cut off.
- DC-H16 closing sequence: failure + early sign and dissent first; then lean → key-assumption check on the lean → explicit "Which option do you choose?".

## 0.3.9 (2026-10-25, built by Claude, not committed)

Dev iteration 3: after the choice D 0.3.8 spent turns on "is that the decision?" and missed review (6/6), owner and confidence (3/6); decider/deadline sometimes never asked.
- make-decision record.md: a stated choice is the explicit choice; store at once; read back and ask confidence in the same reply; then owner + first step; then review date + revisit condition.
- DC-H16 (1): the frame includes who decides (one named person) and by when.

## 0.3.8 (2026-10-25, built by Claude, not committed)

Dev iteration 2 on the semantic simulator (v3): D 0.3.7 drew out 83/102 facts vs the expert prompt's 92; misses concentrated on option ratings (4/6), the hidden fact that changes the answer (3/6) and the review date (5/6), and it invited the choice earlier.
- DC-H16: after weights, the person rates each option (1–5); for the lead option ask "what has to be true for this to work, and has anyone checked it?"; the choice is invited only after ratings and that assumption check.
- DC-H16: after the choice, the next three turns are confidence, owner + first step, review date + revisit condition, with the read-back folded in.

## 0.3.7 (2026-10-25, built by Claude, not committed)

Dev iteration 1 (sessions S7–S12, D vs expert prompt E): 0.3.6 invited the choice as soon as the person pushed, so adversarial and cooperative people chose early and poorly (6/6 poor choices, 55 vs 75 facts drawn out).
- DC-H16 pacing: pressure is not readiness. Under pressure ask the one question most likely to change the answer (vanishing options, "what do you know that I don't"). Invite the choice only with ≥3 options including one the person generated, what matters said, and a failure or disconfirming condition asked, or when the record is requested. A spontaneous early choice gets one "before you lock it" question.
- widen-options: open widening questions only, vanishing options first; no yes/no "should we add do nothing?"; no study citations in speech.

## 0.3.6 (2026-10-25, built by Claude, not committed)

Hardening from the decision-quality sample test (A plain vs E expert prompt vs D product, S4–S6; see dc-bench-sample-dq-report.md).
- DC-H8: the plain equivalents no longer tell the coach to say "the companion", "Navigator's ranking" or "practice session"; graders flagged all three as jargon.
- DC-H15 (new): keep the machinery backstage. Never offer depth levels, modes, stages or tools by name; propose the depth in plain words and carry on; tool steps are silent.
- DC-H16 (new): decision-quality floor before the choice. Goal and stakes, three or more options, a disconfirming condition and base rate, weights before comparing, one failure with an early sign, and named dissent, one per turn. After the choice: confidence, owner, first step, revisit condition.
- DC-H16 pacing (added after the dev re-run, untested): the floor is a checklist, not a sequence; ask an item at most twice; invite the choice once options and what matters exist, or when the person pushes; no cited studies or guessed pronouns.
- frame-decision size.md: the 2x2 maps to rigor ids backstage; one plain-language proposal replaces the menu of levels; the authority question is asked only when it matters.
- make-decision final-check.md: plain wording ("a pull in our thinking"), and the open floor items come first.

## 0.3.5 (2026-10-25)

Hardening from the four-arm review (see dc-bench-protocol-v1.md §3).
- DC-H8: list of words never said to the person (`[GAP]`, tool names, codes, stage ids, "skill", "not tool-checked") with plain equivalents.
- `[GAP]` is now the stored marker only: SKILL.md headers, all 20 output assets and all gap-rules files say "not given yet" to the person.
- DC-H12: vague dates (month, season, "Q1") are asked about before saving; a first-name-only person is saved as said, marked incomplete, and asked about once.
- DC-H13 (new): say saved only after a tool result shows it; on a refusal, change the input or ask, never resend unchanged; with no connector, say nothing is saved.
- DC-H14 (new): optional fields never block a read-back or a store.
- make-decision record.md: read back as soon as the choice and decider are given.
- learning-loop retro.md: what_happened / process_quality_note / outcome_vs_process mapping.
- facilitator ask.md: with a passive person, name the next Playbook move and ask the starting question.
- facilitator status.md: say "not given yet" instead of `[GAP]`.

## 0.3.4 (2026-10-25)

Fixes from the blind re-grade on 0.3.3 (with 47/54 vs without 25/54), applied and re-graded by Claude until every case scored 2. Final six-skill score 58/58 with skill vs 31/58 without. Report: `docs/decision-companion/WITH_WITHOUT_0.3.4_2026-10-25.md`.

### Skills
- **record-dissent** `tasks/capture.md`, `references/tools.md`: a stated dissent is stored as a participant note in the same turn, with no probe first. The schema probe runs only before writing `dissent[]` onto make_decision when the connector version is unknown. A person who names the old connector / v0.2 gets notes only and no probe.
- **tradeoff** `tasks/grid.md`: end each turn with exactly one question.
- **handoff-navigator** `tasks/call.md`:
  - A null or role-only rater gets only "who gave those ratings?".
  - `rater_issues` with only `cell_missing` names the missing cells and asks to rate them or leave them out.
  - A mapping already chosen means one `methods_mcda_rank` call per rater this turn.
  - With no mapping yet, show the args in full and ask the mapping question.
  - One question per turn.

### Evals
- record-dissent b3: version unknown, so the probe is expected; new b4: old connector named, so notes only (`forbidden_calls`).
- handoff-navigator b2: scenario with a chosen mapping and scores, expecting calls; new b5: no mapping yet (`forbidden_calls: methods_mcda_rank`).
- `with_without_result` updated on the six run skills.

### Scripts
- `validate.py` reads `PLUGIN_VERSION` from `plugin.json` instead of a hard-coded string.
- `build_plugin_skills.py` PLUGIN_VERSION 0.3.4.

## 0.3.3 (2026-10-25)

Fixes from the blind re-grade on pack 0.3.2 (with 44/54 vs without 24/54) plus Round 4 live practice findings that affect skill copy.

### B1 Skill fixes

- **frame-decision b4** — after `people_decision: true`, say only: "I've flagged this as a people decision; the connector's notice will follow." No HR/legal/AI Act wording and no who/when question until the connector warning returns (then read verbatim). R7 only if the connector is silent.
- **record-dissent b3** — schema probe is its own turn: `decision_status {include_schemas: true}`, say "Checking whether this connector can store dissent on the decision", stop. Choose merge vs notes only after reading `make_decision.optional`.
- **handoff-navigator** — if `mcda_rank_args` omit `alternatives[].scores` (live R1), fall back to `cells`; never invent scores.

### B2 Eval fixes

- make-decision b4 prompt carries prior read-back (Agency B / Maria Lopez).
- tradeoff b7 prompt includes the new value 2; tradeoff b2 uses `forbidden_calls: ["methods_mcda_rank"]`.
- handoff-navigator b3/b4: packet already in prompt; `forbidden_calls` for `methods_mcda_rank`.
- frame-decision b3: no invented `authority_mode: "consult"`; no call; ask for named decider.
- make-decision b5: `decision_status` moved to `allowed_calls`.

### B3 Eval schema and lint

- Behavioural cases may use `expected_call`, `allowed_calls`, and `forbidden_calls`.
- `validate.py`: (a) warn when no-call language conflicts with `expected_call` (unless the named tool is the probe call); (b) literal `expected_call` values must appear in prompt or `scenario`; (c) "earlier"/"prior read-back" prompts need prior context.

### B4 Staging smoke (B6)

- Transcript: `docs/decision-companion/SMOKE_v0.3_PLUGIN_0.3.3_2026-10-25.md` (stage_order, role_only_name, cell_replaced by name, dissent merge, mcda_rank_args / cells fallback).

### B5 Marketplace

- Sync script commit subject reads version from `plugin.json` (no longer hard-coded 0.3.1).
- Pack stamped **0.3.3**; sync to `curatedhealth/vital-expert-marketplace`.

### Acceptance

- `validate.py` OK at 0.3.3; routing harness flags still **20/20**.
- Blind re-grade of the six skills on 0.3.3 is for Claude (frame-decision b4 and record-dissent b3 target score 2).

### Post-B6 edge walk (same pack, 25 October 2026)

- B6 **PASS** on live edge session `f680b34a-165a-45c2-bc11-41b7d00b5809` (connector product_version 0.3.1, supabase). Transcript: `docs/decision-companion/SMOKE_v0.3_PLUGIN_0.3.3_2026-10-25.md`.
- **Contract:** advise/inform/implement entries may be string or `{name, status: "unverified_person"}` — recorded in `CONTRACT_CHANGES.md`; daii (+ implement-plan) accept both when reading.
- R1 scores still absent on edge; cells fallback remains required.

## 0.3.2 (2026-10-25)

Fixes from the with/without-skill run on pack 0.3.1 (47/54 with vs 29/54 without). Report: `docs/decision-companion/WITH_WITHOUT_0.3.1_2026-10-25.md`.

### B1 Skill fixes

- **tradeoff b5** — on `invalid_cell` for value, same-turn resend with `value` (not `score`); name the fixed cell; ask only if the value is unknown. Worksheet Winner section always says the grid has no winner.
- **make-decision b4** — after read-back, explicit yes means call `decision_run_stage` now with `confidence_pct`; do not ask again.
- **record-dissent b2** — exactly one question: "Who confirms there is no dissent?" Store nothing until named.
- **record-dissent b3** — first `decision_status {include_schemas: true}`; merge path iff `no_dissent_attested_by` in optional; always keep participant note; never `replace:true`.
- **frame-decision b4** — send `people_decision: true` first; no paraphrase before the tool; read connector warning verbatim; else R7 as skill notice.
- **handoff-navigator b3** — cells-only: build per-rater args, show them, ask scale mapping, call only after the person answers.

### B2 Eval fixes

- frame-decision b2/b4, handoff-navigator b3, tradeoff b5, make-decision b4, record-dissent b3: `expected_call` + `fail_if` in the tradeoff-b1 shape.

### B3 With/without flags

- Six skills (`tradeoff`, `make-decision`, `frame-decision`, `learning-loop`, `record-dissent`, `handoff-navigator`): `ran_with_and_without_skill: true` + `with_without_result` pointing at the report. Other 14 remain false.

### B4 Lint

- `validate.py`: (a) WW flag requires result + report path; (b) warn if behavioural names a tool without `expected_call` (error in 0.4); (c) `expected_call` keys checked against contract / known tool args.

### B5 Routing harness

- Re-run 25 October 2026: **20/20 PASS**. All skills `routing_harness_passed: true`.

### B6 Staging smoke (acceptance 3)

- Pending Lane A deploy to staging. Transcript path when done: `docs/decision-companion/SMOKE_v0.3_PLUGIN_0.3.2_<date>.md` (stage_order, role_only_name, cell_replaced, dissent[] merge, mcda_rank_args).

### Acceptance

- Item 1 (v0.2 live smoke): PASS — `docs/decision-companion/SMOKE_v0.2_PLUGIN_0.3.1_2026-10-25.md`.
- Item 2 (with/without): recorded for six skills; B1 cases to be re-graded on 0.3.2.
- `validate.py` OK at 0.3.2.

## 0.3.1 (2026-10-25)

Skills aligned to connector v0.3.0 / content 2026-10-26.1 and the frozen §2 contract (Lane B). `_contract/stage_schemas.json` copied from `docs/stage_schemas_v0.3.0.json`. Route pad/collision fixes: daii `who decides in the words of the room` (no longer steals frame-decision); decision-check and implement-plan should_trigger pads. Plugin harness + validate green (no xfail).

### Fixed (PL1–PL11)

- **PL1 tradeoff** — ratings send `{option, criterion, value, rater}`; criteria `direction`; scale only when not 1–5; handle invalid_cell, rater_missing, role_only_name, cell_replaced.
- **PL2 frame-decision** — complete on statement, goal, decider, deadline; rigor once else change_rigor; people_decision warning.
- **PL3 make-decision** — `confidence_pct`; stage_order / unknown_option / role_only_name.
- **PL4 learning-loop** — `success_signal` only; retro merge fields + note.
- **PL5 widen-options** — removed obsolete R9; store widening answers; status cross-check for stale widen flag.
- **PL6** — removed all obsolete connector-gap version strings.
- **PL7 handoff-navigator** — prefer mcda_rank_args[]; else cells; scale_note; stop on rater_issues.
- **PL8 classify** — confirm paths; never claim type without decision_status.decision_type.
- **PL9 decision-check** — required_stages_unmet, daii_valid, options cross-check; brief marks as evidence.
- **PL10 record-dissent** — notes always; make_decision dissent only on merge semantics; never replace:true.
- **PL11** — README / catalogue say 20 skills; plugin version 0.3.1; connector compatibility table.

### Added

- Per-skill **Connector version** blocks in `references/tools.md`.
- `skills/_contract/stage_schemas.json` (from Lane A stage_schemas).
- Extended `scripts/validate.py`: contract payload keys, ban on obsolete version strings, behavioural code coverage.

### Evals / harness

- Behavioural evals updated for real field names and codes (including PL1 `value` regression).
- Tradeoff b1 tightened with `expected_call` / `fail_if` (Maria Lopez Cost cells).

### Acceptance

- **Item 1 (live smoke vs connector v0.2):** PASS — session `a82ba355-f85d-44d0-a6a1-e4d90d7910ef` on `mcp.vital.expert` (25 October 2026). Transcript: `docs/decision-companion/SMOKE_v0.2_PLUGIN_0.3.1_2026-10-25.md`.

## 0.3.0 (2026-10-25)

Four new skills (frame-decision, record-dissent, implement-plan, decision-check), held_out / near_miss / behavioural evals, validate lint. See git history for full P1–P12 notes.
