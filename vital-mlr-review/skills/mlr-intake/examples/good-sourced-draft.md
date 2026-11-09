# Good sourced draft — mlr-intake

Teaching material only (MLR-H2).

## Synthetic context (teaching only — MLR-H2)
- Person named markets: Germany (DE), Switzerland (CH). United States was never offered.
- Audience: HCP. Channel: promotional (person-declared after channel gate elsewhere).
- Artefact: leave-behind PDF v0.9-draft, sha256 teaching-hash-intk-01.
- Authorized-use (DE, pasted Fachinformation excerpt): "Zur Behandlung von Erwachsenen mit Typ-2-Diabetes mellitus…"
- Authorized-use (CH, pasted Swissmedic label excerpt): "Indiziert zur Behandlung von Erwachsenen mit Typ-2-Diabetes…"
- Missing: full current Fachinformation PDF → tagged [GAP] on DE label basis, not invented.

## Output cards

### Intake card
| Field | Value |
|---|---|
| Markets | DE, CH (explicit; no US default) |
| Audience / channel | HCP / promotional |
| Artefact | leave-behind v0.9-draft |
| Label basis DE | Fachinformation excerpt provided; full SmPC PDF [GAP] |
| Label basis CH | Swissmedic excerpt provided |
| Ruleset coverage (offline list) | DE=full (rulesets/de_amg.json), CH=stub |
| Status | findings_only |
| Tool mode | READY-local · not tool-checked |

### What this card refuses
- Inventing a US market because "most packs start there."
- Treating ruleset stub for CH as full coverage.
- Filling the missing DE Fachinformation from memory or web scrape without the person pasting text.
- Any status other than findings_only / revise / human_gate_required / prep_complete.

### Deterministic checks run
1. `scripts/check_jurisdictions.py` → markets present, non-empty, no silent US inject.
2. `tools/mlr_intake_offline.py` → packet skeleton with gaps array.
3. `tools/mlr_list_rulesets_offline.py` → coverage map DE=full CH=stub.
4. `tools/stamp_ready_line.py --skill mlr-intake --status findings_only`

### Why this is good
Markets stay person-supplied. Gaps are named, not filled. Chairs are not blended. Offline path is complete without a `vmlr_` key.

### Liability
This prepares material for human MLR review. It is not medical, legal, or regulatory approval.

### Stamp
READY-local / mlr-intake: not tool-checked · findings_only · not metered · 2026-11-08

### Cross-links
Next: mlr-channel-intent (if channel ambiguous) → chairs → mlr-compile → mlr-board-prep.

## Worked micro-protocol
1. Ask for markets as ISO codes; reject empty.
2. For each market, require authorized-use paste or mark [GAP].
3. Run offline intake + ruleset list; print coverage table.
4. Refuse to proceed to chairs if zero markets.
5. Hand channel ambiguity to mlr-channel-intent without guessing.

## Sample offline transcript (synthetic)
```
$ python tools/mlr_intake_offline.py --markets DE,CH --audience hcp --channel promo
ok gaps=["de_fi_pdf_missing"]
$ python tools/mlr_list_rulesets_offline.py
DE=full CH=stub
$ python tools/stamp_ready_line.py --skill mlr-intake --status findings_only
READY-local / mlr-intake: not tool-checked · findings_only · not metered · 2026-11-08
```

## Anti-patterns called out
- "Default US then add EU later."
- Filling Fachinformation from model memory.
- Mixing Medical findings into the intake card body.

## Board-facing summary sentence
Intake locked DE+CH, promo HCP leave-behind v0.9-draft, DE FI PDF still [GAP], CH ruleset stub disclosed — ready for channel confirmation and chairs, not for board ownership yet.
