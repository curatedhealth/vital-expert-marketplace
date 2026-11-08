# Workflow — claims-first pre-review (cut rounds before the board)

Sources: MedCom claims-matrix practice; Pulse/Revisto intake completeness (access date 8 November 2026).

1. Refuse empty submission packs (`templates/submission-pack-checklist.md`).
2. Build verbatim claims matrix with paragraph locators or `[GAP]` (`mlr-claims-matrix`).
3. Run structural align against person-supplied authorised-use text (`mlr_align_claims_offline.py`).
4. Run ISI / fair-balance heuristic (`check_isi_presence.py`) then `mlr-fair-balance-isi`.
5. Only then open Medical / Legal / Regulatory chairs.
6. Do **not** stamp approved. Prep statuses only.
