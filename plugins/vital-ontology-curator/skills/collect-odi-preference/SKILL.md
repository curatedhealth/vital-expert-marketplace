---
name: collect-odi-preference
description: Lane C — collect JT ODI importance/satisfaction/opportunity tips with body.odi card.
---

# Collect ODI preference

Opportunity = Importance + max(Importance − Satisfaction, 0).

1. Bind JT subject_code + ODI VP.
2. Record importance, satisfaction, opportunity, sample_n, segment, instrument in `body.odi`.
3. Use measure_kind `odi_importance` / `odi_satisfaction` / `odi_opportunity`.
4. Never write into catalogue `odi_*` columns.
