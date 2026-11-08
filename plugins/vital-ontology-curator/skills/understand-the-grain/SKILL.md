---
name: understand-the-grain
description: Explain Curator datapoint grain — subject_family+code × vp_code × value_kind × measure_kind × provenance. Never overwrite ontology catalogue.
---

# Understand the grain

Ontology catalogue = master data. Curator tips = versioned observations.

**Grain:** `subject_family` + `subject_code` × `vp_code` × `value_kind` × `measure_kind` × provenance → tip → source.

Bound tips require `vp_code`. Unbound leads may omit VP until bind.

VP MEASURES all families: vd, jt, ph, sv, cf, de, rl, al, wp, product, competitor.

Six dimensions via `value_kind`: financial($V), operational(OV), clinical(CV), risk(RV), capability(KV), stakeholder(XV).

Read `references/grain-card.md` and the Enrichment Contract before capturing.
