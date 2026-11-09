# Good sourced draft — mlr-claims-matrix

Teaching material only (MLR-H2).

## Synthetic context (teaching only — MLR-H2)
- Markets: DE, CH.
- Claims extracted from leave-behind (person-highlighted):
  1. "Lowers HbA1c by 1.2% at week 24"
  2. "Better GI tolerability than Product Y"
  3. "Once-daily oral dosing"

## Output cards

### Claims matrix card
| # | Claim text | Evidence locator | Market notes | Status |
|---|---|---|---|---|
| C1 | Lowers HbA1c by 1.2% at week 24 | Study NCT-TEACH-001 CSR §3.2 page 41 [person paste pending] | DE/CH: need label-consistent endpoint language | revise — locator [GAP] |
| C2 | Better GI tolerability than Product Y | Head-to-head not in supplied label excerpts | Comparative → Legal chair + Medical | human_gate_required |
| C3 | Once-daily oral dosing | Matches DE Fachinformation posology excerpt line 12 | OK structurally vs pasted label | findings_only |

### Align note
Structural alignment only against pasted authorized-use text and person-supplied locators. No efficacy clearance. Comparative claim C2 cannot be "supported" by inventing a trial.

### Offline checks
1. `tools/mlr_claims_matrix_offline.py` on claims JSON → rows with gap flags.
2. `tools/mlr_align_claims_offline.py` against authorized-use excerpts.
3. `tools/stamp_ready_line.py --skill mlr-claims-matrix --status revise`

### Why this is good
Every claim has a locator or an explicit [GAP]. Comparative ads route to Legal. Numbers are not invented to fill CSR gaps.

### Liability
This prepares material for human MLR review. It is not medical, legal, or regulatory approval.

### Stamp
READY-local / mlr-claims-matrix: not tool-checked · revise · not metered · 2026-11-08

### Cross-links
Medical chair owns C1 clinical fit; Legal owns C2; Regulatory owns ISI adjacency for claim blocks.

## Row quality bar
- Atomic: one numeric or one qualitative assertion per row.
- Locator: doc id + section + page/line OR explicit [GAP].
- Market notes: DE vs CH language differences called out when pastes differ.
- Dual-route flag for comparative rows.

## Synthetic align output
```
C3 once-daily → aligned with DE FI §4.2
C1 −1.2% → locator gap
C2 better GI vs Y → human_gate_required (Legal)
```

## Commands
```
$ python tools/mlr_claims_matrix_offline.py --in claims.json
$ python tools/mlr_align_claims_offline.py --claims claims.json --label de_fi.txt
$ python tools/stamp_ready_line.py --skill mlr-claims-matrix --status revise
```

## Board-facing summary sentence
Three atomic claims: C1 locator gap, C2 comparative gated for Legal, C3 structurally aligned to DE posology — matrix status revise until C1 closes.
