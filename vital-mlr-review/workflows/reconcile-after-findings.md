# Workflow — reconcile after chair findings

Use when compile shows conflicts or a chair requested substantive claim edits.

1. Open `templates/reconciliation-loop.md`.
2. For each finding: note whether claim text / evidence locator / ISI pairing changes.
3. **Claim text or authorised-use bind changed** → re-queue `mlr-claims-matrix` then `mlr-medical-chair` (and Legal if comparative).
4. **ISI / prominence only** → `mlr-fair-balance-isi` + `mlr-regulatory-chair`.
5. **Misleadingness / comparative only** → `mlr-legal-chair`.
6. Re-run `mlr-compile` + `mlr_validate_packet_offline.py`.
7. Do not skip to board-prep with unresolved conflict slots.

Stamp READY-local. Never approve.
