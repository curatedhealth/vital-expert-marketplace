---
name: identify-datapoint
description: >
  Suggest subject × VP × dimension × measure_kind candidates from quote/URL/hints
  using curator_identify_grain or offline script. Read-only; does not write catalogue.
license: Proprietary. VITAL Ontology Curator pack license.
metadata:
  level: CF04
  register_code: "CF-01.06.01.curator.identify"
  verb: identify
  agent: ontology-curator-agent
  tools: [curator_identify_grain]
  version: "0.2.0"
  release_state: Pilot
  pack: "vital-ontology-curator"
---
# Identify datapoint

## Competent output
- Candidates with `subject_family`, `subject_code`, `vp_code`, `value_kind`, `measure_kind`, confidence, reasons.
- APQC / ODI / market hints called out when quote signals them.
- Steward confirms before propose/bind.

## Steps
| # | Step | Autonomy |
|---|---|---|
| 1 | Call `curator_identify_grain` (quote, url, subject_hint, vp_hint) | agent alone |
| 2 | Or run `scripts/identify_grain_offline.py` offline | agent alone |
| 3 | Present candidates; never auto-bind | agent alone |
| 4 | Steward confirms | human |

## Hard rules
- Do not invent catalogue rows. Do not approve. Do not call Vital Verify.
