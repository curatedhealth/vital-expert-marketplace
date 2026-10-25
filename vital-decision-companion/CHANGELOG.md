# Changelog

## 0.3.0 (2026-10-25)

Generated changes. If `plugin/vital-decision-companion` is produced by the repo generator, port these changes to the generator or they will be overwritten on the next build.

### Fixed
- **P1** Tool names in tasks now match the connector (`decision_bias_check`, `decision_build_brief`, `decision_daii_plan`, `decision_attach_notes`, `decision_tradeoff_matrix`, `decision_widen_options`, `decision_usecase_card`). A lint checks every backticked tool name.
- **P2** classify confirm falls back to `decision_run_stage` on how_to_decide when `confirmed`/`confirmed_by` are not in the schema. A host schema change in `decision-companion.ts` is still needed.
- **P3** learning-loop sends `authored_by`, expectations (expected outcome, probability, key assumptions) and a new retrospective task (AAR, process/outcome 2x2, double-loop question).
- **P4** gather-intelligence completes its stage with knowns, unknowns and a disconfirming question after the notes.
- **P6** handoff-navigator explains how to build the `methods_mcda_rank` call, the 0–4 scale check (the person chooses the mapping) and one call per rater.
- **P7** Routes and descriptions no longer use invented names. Routes changed in make-decision, where-to-start, premortem, tradeoff, implement-plan: `routing_harness_passed` is false until the harness is re-run.
- **P9** The closing line appears only with a compiled brief, a hand-off packet, a readiness check, or when the person asks whether this is the decision.
- **P12** Licence set to proprietary (UNLICENSED, Vital.Expert).

### Added
- Four skills: `frame-decision` (DC-1.0), `record-dissent` (DC-4.5), `implement-plan` (DC-5.2), `decision-check` (DC-6.0).
- Playbook stage content in widen-options, make-decision (final check task), bias (by-stage prompts task, decision fatigue marked contested), premortem, daii, tradeoff (weights and scale before ratings, private ratings), each with sources.
- **P8/P11** Evals: held-out requests with no route fragment, near misses naming the sibling skill, and behavioural cases for every skill, including compensation for connector defects D1, D2, D5, D8, D9, D12, D13, D16.
- `validate.py` lint (outside the package): required files, frontmatter, tool names, task listing, route fragments, route collisions, eval sections.

### Not yet done
- `ran_with_and_without_skill` stays false: no model-versus-model run yet.
- P10 boilerplate in task Formula and Companion tables is kept for the file contract.
