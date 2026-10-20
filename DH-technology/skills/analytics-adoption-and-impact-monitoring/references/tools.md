# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them. Counted calls draw on the library key's monthly allowance; a call that returns an error says "Nothing was counted".

**How this file was built.** The connector was not connected during this build (checked 20 October 2026: no `Vital_Digital_Health` tools were available), so no call was made. Every behavior below comes from live outputs saved on 19 October 2026 by earlier builds, copied into `examples/live/` (file named on each entry, read 20 October 2026). Where a tool has no saved output for this skill's use, the step is marked **needs a live check**. This skill runs mainly on the person's own files through `scripts/adoption_check.py`; the library is used to read a paper behind a rule, to rank follow-ups the person scored, and for the record.

## literature.get_record (counted; A1 and A2, only for a [PAPER] row the answer leans on)

- Saved: `literature_get_record_proctor.json` (`{doi: "10.1007/s10488-010-0319-7"}`, 19 October 2026): PMID 20957426, PMC3068522, year 2010, retraction status "none", `trial_ids` empty, `design` "other" (confidence 0.3). The research row labels the paper Proctor 2011 (journal issue year); cite by DOI and say the library gives 2010.
- Pitfall (register N8): design labels are not reliable; never grade a methods paper from the label.
- ERIC (DOI 10.1186/s13012-015-0209-1), CFIR 2009 (DOI 10.1186/1748-5908-4-50), DECIDE-AI (DOI 10.1136/bmj-2022-070904), Davis 2017 (DOI 10.1093/jamia/ocx030): **needs a live check** (no saved output).

## verify.qualify_source and verify.check_claim (counted; only when a claim about a paper leaves the conversation)

- Saved: `verify_proctor.json` (19 October 2026): `qualify_source {doi: "10.1007/s10488-010-0319-7", question: ...}` returned tier "gold", source score 50; `check_claim` with the CS39 passage returned "supported" (100 percent overlap) for the penetration formula and also "supported" (38 percent overlap) for a distorted claim that penetration is logins divided by licenses sold. Accept a claim only with a passage read in the same direction (register N3). The citation block came back with title null and "Unknown (n.d.)" (register C18).
- The same file shows the NICE Evidence Standards Framework page rated "inadmissible", "no provenance" (register C1). Research rows already carry URL, verbatim quote and read date: cite them directly.

## analytics.mcda and analytics.rice (counted; B1, only to rank follow-ups the person scored)

- Saved: `mcda_enablement_options.json` (19 October 2026, illustrative inputs typed for the measurement): three enablement follow-ups scored on four criteria returned 80, 60 and 55 ("EVIDEM Multi-Criteria Decision Analysis (weighted-sum, 0-4 scale)"); every criterion is read as higher-is-better and no robustness view is returned (register C17). `rice_percent_confidence.json` (19 October 2026): confidence must be a whole percent.
- Use only if the person scores follow-up options and asks for a rank. The rank is arithmetic on the person's scores, never the follow-up decision. Sibling skill `analytics-products-and-decision-support` (this pack) carries `scripts/metric_check.py rank` to reproduce both and print tie points.

## verify.build_record (counted)

- Saved: `verify_build_record_refusal.json` (19 October 2026): `{cleared_by: {name: "Claude"}}` returned "build_record refuses a record without a human cleared_by.name". Call it only when the output leaves the conversation and the person names who clears it.

## Catalogue jobs

- `list_jobs_2026-10-19.json` (19 October 2026) lists no job for analytics adoption, report cadence or decision outcome monitoring. Every task's formula row says "Catalogue job: none".

## Not used here

- `analytics.scenario-modeler` and `analytics.risk-tornado`: not needed for reads; the saved file `analytics_calls_2026-10-19.json` is kept for the sibling skill's value-case arithmetic.
- Every `watch_*` tool: never called. Monitoring is by dated reruns of `scripts/adoption_check.py` on the person's files.
- `regulatory-dh.*`: device post-market duties are `dh-regulatory-and-quality` ai-ml-readiness-monitoring.
