---
name: identify-datapoint
description: Suggest subject × VP × dimension × measure_kind candidates from quote/URL/hints using curator_identify_grain or offline script.
---

# Identify datapoint

1. Call `curator_identify_grain` with quote, url, subject_hint, vp_hint.
2. Or run `scripts/identify_grain_offline.py`.
3. Present candidates with confidence + reasons.
4. Steward confirms before `curator_propose_change` / bind.

Do not invent catalogue rows. Do not approve.
