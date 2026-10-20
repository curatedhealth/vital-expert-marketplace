# Saved live outputs (origin of each file)

The VITAL connector was disconnected when this skill was built on 20 October 2026. These files are copies, unchanged, of live library outputs saved by earlier builds. Each was read on 20 October 2026. Call dates are inside each file (19 October 2026 unless stated; device rows carry their own `retrieved_at`). Illustrative inputs (MCDA scores, RICE inputs, scenario and tornado parameters) were typed for measurement and are nobody's numbers.

| File | Call(s) | Copied from (under /mnt/user-data/outputs/) |
|---|---|---|
| list_jurisdictions_2026-10-19.json | regulatory-dh.list_jurisdictions | ai-ml-device-pathway-and-change-control/examples/live/ |
| search_devices_aidoc_2026-10-19.json | regulatory-dh.search_devices {query: "Aidoc", jurisdiction: "all", limit: 10} | ai-ml-device-pathway-and-change-control/examples/live/ |
| search_devices_eu_2026-10-19.json | regulatory-dh.search_devices, EU: "Briefcase", "stroke", "Viz" | ai-ml-device-pathway-and-change-control/examples/live/ |
| search_devices_brainomix_2026-10-19.json | regulatory-dh.search_devices {query: "Brainomix", software_only: "false", limit: 25} (all 19 rows; 4 US rows under QAS) | cross-region-compliance-monitoring/examples/live/ (added 20 October 2026) |
| find_predicates_K261317_2026-10-19.json | regulatory-dh.find_predicates {reference: "K261317"} (predicate chain back to DEN170073, ContaCT, Viz.Al, Inc.) | ai-ml-device-pathway-and-change-control/examples/live/ (added 20 October 2026) |
| pathway_precedents_QAS_2026-10-19.json | regulatory-dh.get_pathway_precedents {product_code: "QAS", jurisdiction: "US"} | ai-ml-device-pathway-and-change-control/examples/live/ |
| get_deltas_QAS_2026-10-19.json | regulatory-dh.get_deltas {since: "2026-09-01", product_code: "QAS", jurisdiction: "US"} | ai-ml-readiness-monitoring/examples/live/ |
| safety_events_QAS_2026-10-19.json | regulatory-dh.search_safety_events {product_code: "QAS"} | ai-ml-readiness-monitoring/examples/live/ |
| register_deltas_2026-10-19.json | regulatory-dh.get_register_deltas and get_deltas (Brainomix; QAS; EMDN Z11030592) | cross-region-compliance-monitoring/examples/live/ |
| literature_search_2026-10-19.json | literature.list_sources and literature.search_literature (digital CBT for insomnia) | literature-and-real-world-evidence-review/examples/live/search_2026-10-19.json |
| diligence_get_deltas_BigHealth_Akili.json | diligence-dh.get_deltas {companies: ["Big Health, Inc.", "Akili Interactive Labs, Inc."], since: "2025-01-01"} | pipeline-and-market-monitoring/examples/live/ |
| analytics_calls_2026-10-19.json | analytics.scenario-modeler and analytics.risk-tornado (also budget-impact-model and vba-price-anchor, not used here) | economic-model-development/examples/live/ |
| mcda_partner_options.json | analytics.mcda (illustrative scores) | investment-memo-and-decision-record/examples/live/ |
| rice_percent_confidence.json | analytics.rice (confidence as a percent) | design-system-development/examples/live/ |
| list_jobs_2026-10-19.json | list_jobs (catalogue) | company-and-evidence-assessment/examples/live/ |
| verify_build_record_refusal.json | verify.build_record with a non-human clearer | pipeline-and-market-monitoring/examples/live/ |
