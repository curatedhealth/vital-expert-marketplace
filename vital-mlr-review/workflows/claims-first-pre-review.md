# Workflow — claims-first pre-review (cut rounds before the board)

Sources: MedCom claims-matrix practice; Pulse/Revisto intake completeness (access date 8 November 2026).

1. Refuse empty submission packs (`templates/submission-pack-checklist.md`).
2. Build verbatim claims matrix with paragraph locators or `[GAP]` (`mlr-claims-matrix`).
3. Run structural align against person-supplied authorised-use text (`mlr_align_claims_offline.py`).
4. Run ISI / fair-balance heuristic (`check_isi_presence.py`) then `mlr-fair-balance-isi`.
5. Only then open Medical / Legal / Regulatory chairs.
6. Do **not** stamp approved. Prep statuses only.

**Inputs (MLR-H1, TEH-RDY-017):** never create stand-in packets, placeholder versions, or chair decisions to make a tool run. When a step's input (artefact version, a chair packet, the validated compile output) is not supplied, stop at that step, say what is missing, close with `Status: findings_only` (or `human_gate_required` when the request asks to approve or clear, or to bypass any hard rule MLR-H1–H8, including an AI owner request — precedence rule 1, `../references/finding-status-map.md`), and do not call later tools — never `mlr_build_prep_record`.

**Close stamp (TEH-RDY-030):** the stamp names the last skill actually run in this answer. When the workflow stops early (a gate, a missing input), stamp the skill where it stopped — never a later skill that did not run.
