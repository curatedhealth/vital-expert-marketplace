# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them. Counted calls draw on the library key's monthly allowance; a call that returns an error says "Nothing was counted".

**How this file was built.** The connector was disconnected during this build (20 October 2026), so no call was made. Every behavior below comes from live outputs saved on 19 October 2026 by earlier builds, copied unchanged into `examples/live/` (file named on each entry, read 20 October 2026). Where a tool has no saved output, the step is marked **needs a live check**. Most of this skill runs on the sourced references and the person's own data through `scripts/subgroup_check.py`; the library adds safety events for comparable AI devices, source checks and the record.

## regulatory-dh.search_safety_events (counted; A1 step 5, optional)

- Saved: `safety_events_aidoc_2026-10-19.json` (`{manufacturer: "Aidoc", limit: 10}`): no recalls; MAUDE counts by product code (QAS 0, QFM 0, QIH 10 with 2024: 2, 2025: 5, 2026: 3). Observation saved with it: the MAUDE rows carry no manufacturer, so the 10 QIH reports cannot be attributed to Aidoc.
- Saved: `safety_events_QIH_since2025_2026-10-19.json` (`{product_code: "QIH", jurisdiction: "US", since: "2025-01-01", limit: 5}`): five Class II recalls (Philips EPIQ Elite ultrasound, FUJIFILM Synapse PACS, three Intuitive da Vinci entries); none is filtered to product code QIH.
- Pitfalls: recalls are not filtered to the product code; MAUDE counts are reports, not confirmed events, and are never attributed to a company; `source_url` is the API endpoint, not the record (register C1 evidence). Keep a row only if its title or summary names the product or a comparable device the person named; count the rest as "returned, not about these devices". Describe each kept event only by what the record states; never judge its relevance to the person's model.
- Use: context for A1 harm mapping only ("events the records show for comparable devices"). An empty result is never read as evidence of safety or fairness.

## regulatory-dh.retrieve_guidance (counted; not relied on)

- Saved: `guidance_and_verify_2026-10-19.json`: "predetermined change control plan artificial intelligence" and "AI Act high-risk medical device" returned no passage; "PCCP" returned five passages with `source_url` "[GAP]" and `retrieved_at` null, worded as Health Canada guidance (register C6). No query for NIST AI RMF, Section 1557 or ONC DSI has a saved output: **needs a live check**. Rules in this skill come from `references/`, not from this tool.

## verify.qualify_source and verify.check_claim (counted; when the person brings a paper, a vendor document or a web page)

- Saved: `guidance_and_verify_2026-10-19.json`: `qualify_source {url: "https://www.fda.gov/media/166704/download"}` returned tier "inadmissible", "no provenance", publisher FDA, status current (register C1).
- Saved: `qualify_source_ecfr92.json` (`{url: "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-92", question: "Section 1557 language access and patient care decision support tools duties"}`): "inadmissible", "no provenance", title "45 CFR Part 92 -- Nondiscrimination in Health Programs or Activities", score 33 (authority 25, recency 0, relevance 5, provenance 0) (register C1).
- Pitfalls (register): `check_claim` decides on word overlap and can return "supported" for a claim and its negation (N3); it needs the full `qualify_source` object (C18). Accept a claim only with a passage read in the same direction. Regulator pages rated "inadmissible" are still the primary source: cite the research row, and say Verify could not rate it.
- No saved output for a fairness or bias paper: **needs a live check**.

## verify.build_record (counted; when an output leaves the conversation)

- Saved: `build_record_refusal.json` (`{clearances: [{cleared_by: {name: "Claude"}, scope: ...}], text: ...}`): "build_record refuses a record without a human cleared_by.name". Call it only when the person names who clears it.

## agent-pack (through `dh-technology` digital-health-expert)

- Saved: `jobs_experts_2026-10-19.json`: `list_experts {query: "governance"}` returned `ai-ml-governance-director` ("Director-level reviewer of manufacturer AI/ML systems ... model-risk files, GMLP-aligned change envelopes, training-set lineage, drift", department AI/ML & Data Science), the worker bound to this skill.

## Catalogue jobs

- `list_jobs_2026-10-19.json` lists no job for AI governance, bias testing or release controls. Every task's formula row says "Catalogue job: none".

## Not used here

- Every `watch_*` tool: never called.
- `analytics.*`: the subgroup arithmetic runs in `scripts/subgroup_check.py` on the person's file; no analytics tool computes subgroup metrics (proposed as a future tool in the build notes).
