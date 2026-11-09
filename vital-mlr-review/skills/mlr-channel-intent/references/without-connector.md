# Without connector — mlr-channel-intent

1. Compare declared channel to artefact signals (branding, ISI, claims).
2. If the supplied facts conflict (for example promotional signals against a declared scientific-exchange intent, with no unsolicited-request record) → `human_gate_required`.
2b. If the intent, posture or request record is simply not supplied — or only a delivery medium was named (email, print, congress) — that is not a conflict: write `not classified — pending: <items>`, ask for each item, `Status: findings_only` (finding-status-map rule 4, TEH-RDY-057/058).
3. Do not rewrite the piece; stamp and hand to human.
