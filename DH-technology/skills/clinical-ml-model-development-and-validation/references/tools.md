# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). The connector was not connected when this skill was built (20 October 2026), so no call was made for this build. Every behavior below comes from live outputs saved on 19 October 2026 by earlier builds, copied into `examples/live/` with their file names. Any step without a saved output is marked "needs a live check".

Most of this skill's work runs on the person's own files with `scripts/model_check.py` and on the rules in `references/`. The library holds no model performance data, no AI or PCCP field on device records, and no guidance passages for AI validation (see below).

## regulatory-dh.search_devices (counted)

- Saved: `examples/live/search_devices_aidoc_2026-10-19.json`, `{query: "Aidoc", jurisdiction: "all", limit: 10}` (called 19 October 2026).
- Returns, per record: product, manufacturer, jurisdiction, pathway, risk_class, status, decision_date, submission_date, product_code, regulation_number, predicate_references, source_url, retrieved_at. Example: K261317, BriefCase-Triage, Aidoc Medical, Ltd., 510(k) "Substantially Equivalent", decision 14 May 2026, product code QAS.
- Use: to read the person's own authorization or a named comparable device before writing the intended use. Pitfalls: the record has no AI flag, no PCCP field, no validation data and no intended-use text; never infer from a record that a device uses AI, has a PCCP, or was validated in a given way. Manufacturer spellings differ ("Aidoc Medical , Ltd.").

## regulatory-dh.retrieve_guidance (counted)

- Saved: `examples/live/guidance_and_verify_2026-10-19.json`. `{query: "predetermined change control plan artificial intelligence"}` and `{query: "AI Act high-risk medical device"}` returned no passage; `{query: "PCCP"}` returned five passages that read as Health Canada guidance with no source URL or date.
- Use: do not use it for validation or PCCP rules. Rules come from `references/`. Register item C6.

## verify.qualify_source, verify.check_claim (counted)

- Saved: `verify.qualify_source {url: "https://www.fda.gov/media/166704/download"}` (FDA PCCP guidance) returned tier "inadmissible", "no provenance" (`guidance_and_verify_2026-10-19.json`). Regulator texts cannot be checked through Verify today (register C1); the rows carry URL, quote and read date.
- For a [PAPER] row (TRIPOD+AI, PROBAST+AI, Davis 2017): `verify.qualify_source {doi}` then `verify.check_claim {claim, passage: {text, locator}, source}` with the full qualify_source object (register C18). Accept "supported" only after reading the passage in the same direction (register N3). Needs a live check for every DOI in this skill.

## verify.build_record (counted)

- Saved: `examples/live/verify_build_record_refusal_2026-10-19.json`: a call with `cleared_by.name` "Claude" and role "model" was refused: "build_record refuses a record without a human cleared_by.name". The record needs the named person who clears it.

## literature.search_literature, literature.get_record (counted)

- No saved output for this skill's papers. Needs a live check: `literature.get_record {doi: "10.1136/bmj-2023-078378"}` (TRIPOD+AI) and `{doi: "10.1136/bmj-2024-082505"}` (PROBAST+AI). Register N8: design labels from `classify_study` and grades from `grade_evidence` must be checked against the paper.

## Catalogue jobs

The saved `list_jobs` of 19 October 2026 (`examples/live/list_jobs_2026-10-19.json`) shows no job for model validation, model documentation or personalization design. The `evidence-table` job (`literature.*`) exists in the Evidence and Reimbursement suite; it is not used here. Catalogue job: none. Whether a technology suite has jobs today needs a live check (`list_jobs`).

## Not called

`watch_*` tools (never), `analytics.*` (this skill ranks nothing), `regulatory-dh.search_safety_events` (post-market reading belongs to `model-performance-and-drift-monitoring`, this pack).
