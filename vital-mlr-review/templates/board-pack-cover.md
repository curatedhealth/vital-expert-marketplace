# Board pack cover (prep only — never approval)

| Field | Value |
|---|---|
| Artefact id / version | |
| Jurisdictions | |
| Audience / channel | |
| Channel-intent gate | treat_as_promo · treat_as_scientific_exchange · treat_as_med_info · human_gate_required · [GAP] |
| Ruleset ids | |
| MLR status (allowed only) | findings_only · revise · human_gate_required · prep_complete |
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
- If **US** promotional material and company SOP requires **FDA Form 2253** (or successor postmarketing submission): **human owns filing after clearance**. READY does not file, does not invent a submission id, and must keep the prep-only reviewed flag false. See `../references/post-clearance-deferred.md`.
- Multi-market packs: do not assume US filing rules apply to DE/UK/EU/CH rows.

## Closing

Liability: This prepares material for human MLR review. It is not medical, legal, or regulatory approval.

Stamp: `python ../tools/stamp_ready_line.py --skill mlr-board-prep --letter-lines`
