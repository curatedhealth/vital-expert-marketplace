# Saved live outputs (copied, not re-run)

Origin: copied unchanged on 20 October 2026 from the dh-regulatory-and-quality build (`merged/dh-regulatory-and-quality/skills/document-and-change-control/examples/live/`, all retrieved 19 October 2026) and, for `safety_events_uk_software_2026-10-19.json`, from the dh-patient-and-user-experience build (`clinical-workflow-ux-design/examples/live/safety_events_uk_software.json`, retrieved 19 October 2026, renamed with its date). The connector was disconnected during this build, so no new call was made. Each file states its own call and arguments.

| File | Call |
|---|---|
| `list_jurisdictions_2026-10-19.json` | `regulatory-dh.list_jurisdictions {}` |
| `safety_events_QRX_2026-10-19.json` | `regulatory-dh.search_safety_events {jurisdiction: "US", product_code: "QRX", limit: 10}` |
| `safety_events_other_2026-10-19.json` | five calls, including `{jurisdiction: "US", product: "software", since: "2025-01-01", limit: 10}` |
| `safety_events_uk_software_2026-10-19.json` | `regulatory-dh.search_safety_events {product: "software", jurisdiction: "UK", limit: 10}` |
| `authorization_K252818_K222888_2026-10-19.json` | `search_devices` and `get_authorization` for K252818 and K222888 |
| `verify_build_record_refusal_2026-10-19.json` | `verify.build_record` with a non-human `cleared_by` (refused) |
