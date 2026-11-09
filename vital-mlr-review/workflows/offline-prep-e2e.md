# Workflow — offline prep end-to-end (no keys)

Stamp every close `READY-local · not tool-checked · not metered`. Never approve.

**Inputs (MLR-H1, TEH-RDY-017):** never create stand-in packets, placeholder versions, or chair decisions to make a tool run. When a step's input (artefact version, a chair packet, the validated compile output) is not supplied, stop at that step, say what is missing, close with `Status: findings_only` (or `human_gate_required` when the request asks to approve or clear, or to bypass any hard rule MLR-H1–H8, including an AI owner request — precedence rule 1, `../references/finding-status-map.md`), and do not call later tools — never `mlr_build_prep_record`.

1. **Route** — `mlr-capability-map`
2. **Channel gate** — `mlr-channel-intent` → `python tools/channel_intent_gate.py`
3. **Intake** — `mlr-intake` → `python tools/mlr_intake_offline.py` (jurisdictions required)
4. **Claims matrix** — `mlr-claims-matrix` → `python tools/mlr_claims_matrix_offline.py`
5. **Chairs (parallel prep)** — `mlr-medical-chair` · `mlr-legal-chair` · `mlr-fair-balance-isi` · `mlr-regulatory-chair`
6. **Compile** — `mlr-compile` → validate + conflict matrix offline CLIs
7. **Optional VERIFY packet** — `mlr-verify-handoff` (does not call VERIFY)
8. **Board pack** — `mlr-board-prep` → `render_board_pack.py` + `mlr_build_prep_record_offline.py` with named human

Reconciliation: if claim text changes after chairs, use `workflows/reconcile-after-findings.md` and `templates/reconciliation-loop.md`.

**Stop here for READY.** Regulator submission filings and archival are human ops after clearance (name Form 2253 only when US is a supplied market or the person asks) — see `workflows/post-clearance-human-ops-deferred.md`. Do not invent a filing step.

**Close stamp (TEH-RDY-030):** the stamp names the last skill actually run in this answer. When the workflow stops early (a gate, a missing input), stamp the skill where it stopped — never a later skill that did not run.
