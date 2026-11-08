# vital-ontology-curator

Claude plugin SSOT for Ontology Curator method + steward pipeline.

Connector host: `vital-ontology-curator` (`vcur_` key). Contract: `../../ENRICHMENT_CONTRACT.md`.

## Skills

| Skill | Role |
| --- | --- |
| understand-the-grain | Doctrine: subject × VP × dimension × measure_kind |
| identify-datapoint | Suggest bind via `curator_identify_grain` / offline script |
| classify-incoming | Steward classify |
| file-and-process | Capture + process leads |
| pull-evidence | Source fetch path |
| steward-decide | Named decide (R1/C11) |
| enrich-record | Tip enrichment cards (APQC/ODI) |
| collect-apqc-benchmark | Lane A |
| collect-odi-preference | Lane C |
| bind-vp-and-subject | Bind UNBOUND → bound |
| coverage-and-gaps | Enrichment coverage |
| handoff-from-navigator | Entry from Outcome Navigator |

Navigator pack keeps **handoff-to-curator** only for steward work.
