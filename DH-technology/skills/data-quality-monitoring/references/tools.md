# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them. Counted calls draw on the library key's monthly allowance; a call that returns an error says "Nothing was counted".

**How this file was built.** The connector was disconnected during this build (20 October 2026; a tool search for the library returned no tools), so no call was made. Every behavior below comes from live outputs saved on 19 October 2026 by earlier builds, copied into `examples/live/` (file named on each entry, read 20 October 2026). Where a tool has no saved output for this skill's use, the step is marked **needs a live check**. This skill runs on the person's own data through `scripts/dq_check.py`; the library holds no data quality tool and is used only to read a published method the person names and to clear the record.

## literature.search_literature and literature.get_record (counted; A2 step 5, optional)

- Saved: `literature_search_2026-10-19.json` (a digital CBT for insomnia query, limit 8): 32 hits, 29 after merge, 8 returned; off-topic records ranked in; `trial_ids` empty on every RCT (register N8). `get_record_malloy.json` (`{doi: "10.1177/20552076231219117"}`): design label wrong (scoping review stored as `systematic_review`); excerpt is the introduction only.
- Use here: to read a data quality method the person names (for example a paper on a harmonized data quality framework) by DOI. **Needs a live check** for that query type. A method statement is quoted only from a passage read in the paper.

## verify.qualify_source then verify.check_claim (counted)

- Saved: `qualify_source_fabbri.json` (tier "gold", score 67) and `check_claim_fabbri.json`: `check_claim` with only `{doi, source_id}` returned 502 (nothing counted); passing the full `qualify_source` result worked (register C18); a figure and its reversal both returned "supported" on word overlap (register N3); the returned citation lacked DOI, authors and year (C18).
- Rule: accept a published statement only from a passage you read, in the same direction.

## verify.build_record (counted)

- Saved: `verify_build_record_refusal.json`: `{cleared_by: {name: "Claude"}}` returned "build_record refuses a record without a human cleared_by.name". Call it only when an output leaves the conversation and the person names who clears it.

## Catalogue jobs

- `list_jobs_2026-10-19.json` lists no job for data quality rules, runs or repairs. Every task's formula row says "Catalogue job: none".

## Not used here

- `analytics.*`: no tool runs data quality checks; `scripts/dq_check.py` does.
- `regulatory-dh.*`, `diligence-dh.*`, `market-access-dh.*`: no data quality use.
- Every `watch_*` tool: never called. Monitoring is by dated reruns the person schedules.

## Steps that need a live check

- `literature.get_record` on a data quality method paper the person names (A2 step 5).
