# Workflow — offline prep end-to-end (no keys)

Stamp every close `READY-local · not tool-checked · not metered`. Never approve.

1. **Route** — `mlr-capability-map`
2. **Channel gate** — `mlr-channel-intent` → `python tools/channel_intent_gate.py`
3. **Intake** — `mlr-intake` → `python tools/mlr_intake_offline.py` (jurisdictions required)
4. **Claims matrix** — `mlr-claims-matrix` → `python tools/mlr_claims_matrix_offline.py`
5. **Chairs (parallel prep)** — `mlr-medical-chair` · `mlr-legal-chair` · `mlr-fair-balance-isi` · `mlr-regulatory-chair`
6. **Compile** — `mlr-compile` → validate + conflict matrix offline CLIs
7. **Optional VERIFY packet** — `mlr-verify-handoff` (does not call VERIFY)
8. **Board pack** — `mlr-board-prep` → `render_board_pack.py` + `mlr_build_prep_record_offline.py` with named human

Reconciliation: if claim text changes after chairs, use `workflows/reconcile-after-findings.md` and `templates/reconciliation-loop.md`.

**Stop here for READY.** Form 2253 / archival filing are human ops after clearance — see `workflows/post-clearance-human-ops-deferred.md`. Do not invent a filing step.
