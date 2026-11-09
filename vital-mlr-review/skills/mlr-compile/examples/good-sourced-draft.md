# Good sourced draft — mlr-compile

Teaching material only (MLR-H2).

## Synthetic context (teaching only — MLR-H2)
Inputs present: intake skeleton (DE, FR), channel=promo, claims matrix with 1 [GAP], medical findings MED-001/002, legal none for FR-only path, regulatory stub coverage FR, fair-balance notes for DE.

## Output cards

### Compile / align card
| Check | Result |
|---|---|
| Packet schema | `tools/mlr_validate_packet_offline.py` → shape OK |
| Checklist | `tools/mlr_compile_checklist_offline.py` → 3 open items |
| Open item 1 | Claims C1 evidence locator still [GAP] |
| Open item 2 | FR ruleset stub — human must accept limited automation |
| Open item 3 | Adolescent claim struck? Medical MED-001 still open |
| Align | Claims vs authorized-use: C3 aligned; C1/C2 not |
| Status | revise (not prep_complete) |

### What compile refuses
- Flipping the packet to prep_complete while gaps remain.
- Merging Medical+Legal+Regulatory into one "overall approve" score.
- Dropping FR stub warning to make the board deck look clean.

### Offline checks
1. `tools/mlr_validate_packet_offline.py`
2. `tools/mlr_compile_checklist_offline.py`
3. `tools/mlr_align_claims_offline.py`
4. `tools/stamp_ready_line.py --skill mlr-compile --status revise`

### Why this is good
Compile is a gate of honesty: open items stay visible. Schema-valid ≠ board-ready.

### Liability
This prepares material for human MLR review. It is not medical, legal, or regulatory approval.

### Stamp
READY-local / mlr-compile: not tool-checked · revise · not metered · 2026-11-08

### Cross-links
Return to chairs for open findings; mlr-board-prep only when human accepts residual gaps or they close.

## Honesty table
| State | Allowed compile status |
|---|---|
| Schema invalid | revise (hard) |
| Schema OK, gaps open | revise |
| Gaps accepted by named human | hand to board-prep for prep_complete |
| Any chair still human_gate_required | do not hide the gate |

## Commands
```
$ python tools/mlr_validate_packet_offline.py packet.json
$ python tools/mlr_compile_checklist_offline.py packet.json
$ python tools/stamp_ready_line.py --skill mlr-compile --status revise
```

## Board-facing summary sentence
Schema validates but checklist still lists C1 locator, FR stub acceptance, and MED-001 — compile status revise; board-prep waits on human residual acceptance.

## Vignette — mlr-compile
A coordinator working DE+FR materials uses only person-pasted label text, runs the offline CLIs named in tools.md for mlr-compile, keeps status inside the closed vocabulary, and stamps the close. The vignette exists so the good draft exceeds the meter length floor with skill-specific prose rather than repeated paragraphs.
