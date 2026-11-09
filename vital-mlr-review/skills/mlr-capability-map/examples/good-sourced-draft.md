# Good sourced draft — mlr-capability-map

Teaching material only (MLR-H2).

## Synthetic context (teaching only — MLR-H2)
Operator asks: "What can this pack do for a DE+CH HCP leave-behind before the board?"
No artefact body yet — map skills and refuse approval language.

## Output cards

### Capability map card
| Skill | Job | Not for |
|---|---|---|
| mlr-intake | Markets, channel, label excerpts, ruleset coverage | Approving copy |
| mlr-channel-intent | Promo vs scientific-exchange gate | Medical accuracy |
| mlr-claims-matrix | Claim ↔ evidence locator grid | Legal misleadingness alone |
| mlr-fair-balance-isi | ISI / fair-balance presence & placement notes | Writing new ISI text as approved |
| mlr-medical-chair | Label / clinical accuracy findings | Legal privacy / comparative ads |
| mlr-legal-chair | Misleadingness, comparative, privacy | Clinical dose accuracy |
| mlr-regulatory-chair | Format, ISI process, pre-approval ceremony | Medical efficacy judgment |
| mlr-compile | Align + validate packet shape | Board ownership |
| mlr-verify-handoff | Passage / source proof via VERIFY when keyed | Standing in for chairs |
| mlr-board-prep | Named-human prep record | AI as cleared_by |

### Routing note
Eleven skills, one funnel. Ask which market and channel first; never default United States. Host reasoner selects skill; this map only orients.

### Offline checks
- `tools/mlr_list_rulesets_offline.py` — show which markets have full vs stub rulesets before promising depth.
- `tools/stamp_ready_line.py --skill mlr-capability-map --status findings_only`

### Why this is good
Names every skill's job and its hard boundary. No "we can clear this for you." No marketplace publish claim (Pilot).

### Liability
This prepares material for human MLR review. It is not medical, legal, or regulatory approval.

### Stamp
READY-local / mlr-capability-map: not tool-checked · findings_only · not metered · 2026-11-08

### Cross-links
Operator picks mlr-intake when markets are known; otherwise stay on the map until jurisdictions are explicit.

## Operator FAQ (synthetic answers)
Q: Can this pack clear my banner? A: No. Never-approve; chairs emit findings only.
Q: Do I need MCP keys? A: Offline CLIs work; keys add tool-checked mode.
Q: Where does Form 2253 live? A: Deferred in Pilot — Regulatory records [DEFERRED].
Q: Who owns privacy on a leave-behind form? A: mlr-legal-chair.
Q: Who owns HbA1c vs label? A: mlr-medical-chair.

## Funnel sketch
capability-map → intake → channel-intent → claims-matrix ∥ fair-balance-isi → medical ∥ legal ∥ regulatory → compile → verify-handoff → board-prep

## Offline orientation command
```
$ python tools/mlr_list_rulesets_offline.py
$ python tools/stamp_ready_line.py --skill mlr-capability-map --status findings_only
```

## Board-facing summary sentence
Pack orients eleven Pilot skills; operator must pick intake next once markets are known; no path here grants promotional clearance.
