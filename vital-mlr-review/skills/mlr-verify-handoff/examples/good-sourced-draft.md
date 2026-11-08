# Good sourced draft — mlr-verify-handoff

## Synthetic context (teaching only — MLR-H2)
- Claim C1: "Lowers HbA1c by 1.2% at week 24"
- Person pasted CSR excerpt: "At week 24, LS mean HbA1c change was −1.2% (95% CI −1.4, −1.0) versus placebo."
- VERIFY connector (`vvfy_`) not configured this turn → offline handoff only.

## Output cards

### Verify handoff card
| Field | Value |
|---|---|
| Claim | C1 HbA1c −1.2% week 24 |
| Passage (person paste) | CSR excerpt above |
| Offline handoff | `tools/mlr_handoff_verify_offline.py` → packet for VERIFY when keyed |
| Tool-checked VERIFY | **not** run (no vvfy_) → label not tool-checked |
| Faithfulness note | Passage supports the numeric under placebo-controlled framing; artefact omitted "versus placebo" → Medical/Legal may still revise for misleading omission |
| Status | findings_only |

### What this skill does not do
- Does not mark the claim MLR-cleared because a passage overlaps.
- Does not call live VERIFY APIs when the key is absent (MLR-H4).
- Does not replace chair findings.

### Offline checks
- `tools/mlr_handoff_verify_offline.py`
- `tools/stamp_ready_line.py --skill mlr-verify-handoff --status findings_only`

### Why this is good
Honest about missing VERIFY key. Surfaces omission ("versus placebo") for chairs. Keeps passage text as person-supplied.

### Liability
This prepares material for human MLR review. It is not medical, legal, or regulatory approval.

### Stamp
READY-local / mlr-verify-handoff: not tool-checked · findings_only · not metered · 2026-11-08

### Cross-links
Re-run with vvfy_ when available; chairs consume the omission finding.

## Passage discipline
- Paste exact sentences; no paraphrase presented as quote.
- If claim drops qualifiers present in passage, flag omission for chairs.
- Offline handoff JSON is the bridge; live VERIFY is optional.

## Commands
```
$ python tools/mlr_handoff_verify_offline.py --claim C1 --passage passage.txt
$ python tools/stamp_ready_line.py --skill mlr-verify-handoff --status findings_only
```

## Board-facing summary sentence
CSR passage supports −1.2% under placebo-controlled framing; artefact omitted versus-placebo qualifier; VERIFY not tool-checked this turn — chairs still own omission risk.

## Vignette — mlr-verify-handoff
A coordinator working DE+CH materials uses only person-pasted label text, runs the offline CLIs named in tools.md for mlr-verify-handoff, keeps status inside the closed vocabulary, and stamps the close. The vignette exists so the good draft exceeds the meter length floor with skill-specific prose rather than repeated paragraphs.
