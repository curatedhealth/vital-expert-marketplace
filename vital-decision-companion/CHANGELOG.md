# Changelog

## 0.3.6 (2026-10-25, Lane B round 5)

Connector contract round 5 (works on 0.3.1 today; uses 0.3.2 fields when present).

- **R14 `message_for_person`:** DC-H8 and every `references/tools.md` Connector version block — say the person sentence when present; on 0.3.1 translate the code with the DC-H8 list; never print the code.
- **R10 pre-mortem:** offer `remove_index` + `by` for coach-created wrong/blank rows; never remove without the person's say (`tasks/capture.md`, tools reference).
- **R15 `decision_export`:** brief fills omitted stored data from export (0.3.2+) or `decision_status` (0.3.1) and says so in plain words; decision-check prefers the export over inferring from status.
- **R13:** decision-check and implement-plan must not treat "implement complete" as progress while no choice is recorded.
- **Evals:** frame-decision b5 (R14), premortem b5 (R10), brief b4 (R15).
- **Lint d:** skill prose must not instruct printing `[GAP]`, a refusal code, or a tool name in a reply (storage markers and DC-H8 never-lists allowed). Brief R7 / tools table use "not given yet" for the person.
- `validate.py` allows `decision_export`; `KNOWN_TOOL_ARGS` includes `remove_index` / `replace_index`.
- Marketplace sync at 0.3.6 (single ship after 0.3.5 land).

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
