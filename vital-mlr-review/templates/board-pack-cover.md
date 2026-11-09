# Board pack cover (prep only — never approval)

| Field | Value |
|---|---|
| Artefact id / version | |
| Jurisdictions | |
| Audience / channel | |
| Channel-intent gate | treat_as_promo · treat_as_scientific_exchange · treat_as_med_info · human_gate_required (judgment call only, including mixed promotional / medical-information content, TEH-RDY-061) · provisional: <decision> — pending: <items> (TEH-RDY-062) · not classified — pending: <items> (content incomplete, no reading) · [GAP] |
| Intent / medium | intent (rule-pack channel) as supplied · medium recorded, never binds a pack (TEH-RDY-057) |
| Ruleset ids | |
| MLR status (allowed only) | findings_only · revise · human_gate_required · prep_complete — re-derived from the packet's findings; when the packet's own status differs, show both: "Packet says <x>; findings support <y>" (TEH-RDY-063) |
| Claims matrix attached? | yes / no / [GAP] |
| Fair-balance / ISI card attached? | yes / no / [GAP] |
| Chair packets present (M / L / R) | |
| Compile / conflict matrix | |
| VERIFY | live · handoff packet only · not tool-checked · N/A |
| Named human (`cleared_by.name`) | |
| Company SOP pointer | |

## Packet index

- Intake card
- Channel-intent card
- Claims matrix
- Medical / Legal / Regulatory findings
- Fair-balance / ISI checklist
- Compile conflict matrix
- Prep record pointer (local `ready-sessions/` when offline)

## Human gate reminders

- READY does **not** approve copy. Humans and company MLR own clearance.
- Only when US is a supplied market (or the person asks): `[DEFERRED] Form 2253 — out of READY scope`; if company SOP requires it after clearance, a **named human owns filing**. Otherwise write "regulator submission filings are deferred" (TEH-RDY-031). READY does not file, does not invent a submission id, and must keep the prep-only reviewed flag false. See `../references/post-clearance-deferred.md`.
- Multi-market packs: one row per supplied market; do not apply one market's filing rules to another market's row (TEH-RDY-024).

## Closing

Liability: This prepares material for human MLR review. It is not medical, legal, or regulatory approval.

Stamp: `python ../tools/stamp_ready_line.py --skill mlr-board-prep --letter-lines`
