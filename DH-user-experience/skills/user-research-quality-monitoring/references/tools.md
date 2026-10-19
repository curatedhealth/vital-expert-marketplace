# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `analytics_mcda`). This is a method pack: it runs mainly on the person's own logs and `scripts/research_log.py`. The library adds a literature check, ranking calculators for repairs the person scored, and the record. The person's research data never goes into a library call. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`.

## verify.qualify_source and verify.check_claim (A1, when a study report cites a paper)

- `verify.qualify_source {doi, question}` rated Hyzy et al. 2022 (doi 10.2196/37290) and GRIPP2 (doi 10.1136/bmj.j3453) tier "gold", status current.
- `verify.check_claim {claim: {text}, passage: {text, locator}, source}`:
  - With `source: {doi: "..."}` every claim came back "unverifiable, no admissible source". Pass the whole object `qualify_source` returned.
  - A negated claim ("the 68 benchmark is not suitable for evaluating digital health apps") against the passage stating it is suitable came back "supported" ("Strong overlap (60%) with context"). The tool does not check direction (register N3). Read the passage yourself; accept a claim only if the passage states it in the same direction.
  - A claim carrying two facts from different sentences came back "partial, the passage does not state the figure" though the figure was in the passage. Check one fact per claim.
  - The returned citation has authors empty and year null (register C18); take the reference from `literature.get_record`.
- Use: when a study report cites a published figure (for example a SUS benchmark), check that the report's wording matches what the paper states. `examples/live/verify_sus.json`.

## literature.get_record (counted)

- `{doi: "10.2196/37290"}` returned the merged record (PMID 35980732, PMC9437782), design meta-analysis (confidence 0.98), retraction none, `trial_ids` empty.

## analytics.rice (counted), B1 step 5, optional

- Arguments: `initiatives`, each with `id`, `reach`, `impact` (0.25, 0.5, 1, 2 or 3), `confidence`, `effort`, all from the person.
- `confidence` must be a percent (80, not 0.8). Given 0.8 the tool divided by 100 again and returned scores 100 times too small (9.6 became 0.096), with no warning (`examples/live/rice.json`).
- `name` is null on every row; keep your own map. The method citation returned is a vendor blog (Intercom, 2016), not a sourced standard.

## analytics.mcda (counted), B1 step 5, alternative

- For repairs scored by the person on their own criteria (0 to 4, higher is better) with weights summing to 1. Measured in the Quality build (`qms-design-and-governance`): weighted-sum EVIDEM method, every criterion treated as higher-is-better, no robustness view (register C17). Name criteria so higher is better ("effort avoided", not "effort").

## agent-pack.list_experts and agent-pack.download_agent

- `list_experts {query: "patient experience"}` returned the Patient Experience Designer (`patient-experience-designer`), the worker named for this competency; its download carries the three old task names of this competency (Action trace, Sample fit, Unactioned stop). Its remit says it does not produce human factors protocols or usability-test reports.
- `list_experts {query: "human factors"}` returned the Usability Test Specialist (`usability-test-specialist`), not bound to this competency in its download.

## regulatory-dh.retrieve_guidance: not used

- Queries "human factors validation testing participants", "usability" and "IEC 62366" returned no passage or passages with `source_url` "[GAP]" (register C6). The copied research files replace it.

## verify.build_record (counted)

- Refused a clearance named "Claude": "build_record refuses a record without a human cleared_by.name".

## Not used

- `regulatory-dh.search_safety_events`: field events say nothing about whether research was sound or acted on. The execution sibling uses it to seed scenarios.
- `watch_*` tools.

## Local helper

`scripts/research_log.py` (no connector, same file as the sibling's): `trace` follows insights to decisions and shipped changes as of a date; `stops` counts participants per stop and user group (sample fit); `sus` scores SUS by round. Refuses identifiable data. Tested on 19 October 2026 on the illustrative files in `examples/sample-data/`.

## Catalogue jobs (list_jobs, 19 October 2026)

`list_jobs` returned 29 jobs in four suites (Regulatory, Evidence and Reimbursement, Diligence, Commercial). None covers a task in this skill, so every task's formula table says "Catalogue job: none" and the direct calls in the steps stay the method. Not wired, by rule: `post-market-watch` (it sets a `watch_register` watch). Not wired, by scope: `partner-prioritization` runs `analytics.mcda` and `analytics.rice` but is scoped to partners and indications; call the calculator directly. `evidence-table` applies only where a task builds a literature evidence table; no task here does. No `start_job` run was made, because no job was wired.
