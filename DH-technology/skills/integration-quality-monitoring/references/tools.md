# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them. Counted calls draw on the library key's monthly allowance.

**How this file was built.** The connector was disconnected during this build (20 October 2026: `ToolSearch "+Vital_Digital_Health regulatory"` found no tool), so no call was made. Every behavior below comes from live outputs saved on 19 October 2026 by earlier builds, copied into `examples/live/` (file named on each entry, read 20 October 2026), and from those builds' `tools.md` files. Where a tool has no saved output, the step is marked **needs a live check**.

**What this means for the skill.** The library holds no interoperability content: no FHIR, US Core, SMART or USCDI records, no ONC certified product list (CHPL), and no EHR vendor data. This competency runs on the sourced references in this folder, the person's own sample exchanges, launch matrix, map review sample and workflow observations, and `scripts/integration_check.py`. The library has no standards change log, so the standards currency read (A2) compares the person's versions with the research rows as read, not with a library feed. The library is used only for sign-off and, where the person wants one, an expert download.

## verify.build_record (counted; every task, only when an output leaves the conversation)

- Saved: `verify_build_record_refusal_2026-10-19.json`: `{clearances: [{cleared_by: {name: "Claude"}, role: "model"}], text: "..."}` returned "build_record refuses a record without a human cleared_by.name" (retrieved 19 October 2026).
- Call it only when the person names who clears the output. Until then the output is an uncleared draft.

## verify.qualify_source (counted; not used for rule rows)

- Not saved for HL7, eCFR or Federal Register pages. The regulatory build observed on 19 October 2026 that `qualify_source` rated the FDA PCCP guidance URL "inadmissible", "no provenance" (`dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control, `references/tools.md`; register item C1). Whether HL7 or eCFR pages rate the same way: **needs a live check**. The rows in `references/` carry their own URL, quote and read date; do not spend calls checking them through Verify.

## agent-pack.list_experts and agent-pack.download_agent (counted; only when the person wants an expert)

- Saved: `list_experts_implementation_2026-10-19.json`: `{query: "implementation", limit: 10}` returned `security-engineer-digital-health`, `digital-clinical-trials-director`, `interoperability-integration-director` (called 19 October 2026).
- Saved: `catalogue_and_experts_clinical-informatics-lead_2026-10-19.json` (pair cv3 build, 19 October 2026): `{query: "clinical", limit: 20}` listed `clinical-informatics-lead` ("specifies how a digital health product reads and writes the care record ... Does not configure a live EHR"); `download_agent {expert: "clinical-informatics-lead"}` returned stop rules ("Live-EHR change ... stop for the accountable owner"; never "Treating FHIR conformance or a successful interface as clinical benefit") and a `plumbing` field with "trust the foreign key" and "[GAP] (persona_archetype)" (register C15).
- `fhir-integration-specialist` and `data-engineering-manager-health` (bound in the old tasks) have no saved list or download output: **needs a live check**.
- The download itself is run by `dh-technology` digital-health-expert.

## regulatory-dh.retrieve_guidance (counted; not used)

- No saved output for FHIR, ONC, USCDI, TEFCA or EHDS queries. Earlier builds saw the guidance store return nothing for most regulatory topics and passages without source URLs (register C6). **Needs a live check** before any use; never quote a passage without a source URL.

## regulatory-dh.search_safety_events (counted; optional, A2 or B1, only if the person asks about interface-related events)

- No saved output for interface, HL7 or EHR integration queries. Earlier builds observed that `product` matches the whole phrase (register C9). **Needs a live check.** Describe any event only by what its record states; never judge its relevance to the person's product.

## Catalogue jobs

- No saved `list_jobs` output covers interoperability; saved outputs from other builds list no interoperability job. Every task's formula row says "Catalogue job: none" (**needs a live check** to confirm).

## Not used here

- Every `watch_*` tool: never called.
- `analytics.*`: no ranking or modeling is part of this competency.
