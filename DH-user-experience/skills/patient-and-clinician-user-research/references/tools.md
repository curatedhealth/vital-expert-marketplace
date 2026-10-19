# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `regulatory-dh_search_safety_events`). This is a method pack: it runs mainly on the person's own study material and `scripts/research_log.py`. The library adds known problems with similar products, a literature check, a ranking calculator and the record. The person's participant data never goes into a library call. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`.

## regulatory-dh.search_safety_events (counted), A1 step 4, optional

- Arguments: at least one of `manufacturer`, `product`, `product_code`; optional `jurisdiction` (US, EU, UK, CH, all), `since` (YYYY-MM-DD), `limit` 1 to 25.
- Observed: `{product: "insulin", jurisdiction: "US", since: "2025-01-01", limit: 5}` returned five FDA software-related recalls (Tandem, Insulet), each with title, event date, recall class, manufacturer and summary, plus a MAUDE count block for product code QRX (`examples/live/safety_events_insulin.json`).
- Coverage as returned: US recalls whose product text mentions software, algorithm, application, firmware or app, and MAUDE counts; UK MHRA alerts; Swissmedic not loaded.
- Pitfalls seen:
  - No row carries a use-error field. Recalls describe software defects; two summaries describe interface conditions (a phone set to a right-to-left language; a comma not recognized as a decimal separator in manual entry). Quote the summary; never relabel a defect as a use error.
  - `source_url` is the openFDA API endpoint, not the recall record; no recall number. Cite title and event date and say "openFDA enforcement report, record not linked" (register P1).
  - MAUDE counts attach to a product query without a stated reason (code QRX here); counts are reports, not confirmed events.
  - Product matches the whole phrase; use one short term ("insulin", not "insulin dosing app") (register C9).
- Use: FDA suggests looking at use-related problems with similar devices, naming MAUDE and recalls among sources (UXR-01). Use events to propose scenarios for the study, labeled "proposed". Absence of events is not evidence of safety.

## literature.get_record and verify (A2 or B1, when a published claim is used)

- `literature.get_record {doi: "10.2196/37290"}` resolved Hyzy et al. 2022 (JMIR mHealth and uHealth, PMID 35980732, PMC9437782), design meta-analysis, retraction status none, `trial_ids` empty.
- `verify.qualify_source {doi, question}` rated Hyzy 2022 and GRIPP2 (doi 10.1136/bmj.j3453) tier "gold", status current.
- `verify.check_claim {claim: {text}, passage: {text, locator}, source}`:
  - With `source: {doi: "..."}` it returned "unverifiable, no admissible source" for every claim. Pass the whole object `qualify_source` returned as `source`.
  - With the full source object, a negated claim ("the 68 benchmark is not suitable for digital health apps") against the passage stating it is suitable returned "supported" ("Strong overlap (60%) with context"). Direction is not checked (register N3). Read the passage yourself and accept only a claim it states in the same direction.
  - A claim whose figure (76.64) is in the passage returned "partial, the passage does not state the figure", because the claim also carried a count (117) from another sentence. Check one fact per claim.
  - The citation returned has authors empty and year null (register C18). Build the reference from `get_record`.
- The SUS rows in this skill were read from the paper's full text in the research pass (UX-M-07 to UX-M-10); a Verify call is needed only when the person brings a new paper.

## analytics.rice (counted), B1 step 5, optional

- Arguments: `initiatives`, each with `id`, `reach`, `impact` (0.25, 0.5, 1, 2 or 3), `confidence`, `effort`. Every number comes from the person.
- Observed: `confidence` must be a percent (80, not 0.8). Given 0.8 it divided by 100 again and returned scores 100 times too small (9.6 became 0.096). Score = reach x impact x (confidence / 100) / effort; the live check matched by hand (`examples/live/rice.json`).
- `name` is null on every row; keep your own id-to-action map.
- The method citation returned is a vendor blog (Intercom, 2016); RICE is a prioritization convention, not a sourced standard. Say so if asked.
- Never fill a reach, impact, confidence or effort value for the person. If any is missing, no ranking.

## regulatory-dh.retrieve_guidance (counted): not used

- `{query: "human factors validation testing participants"}` returned no passages. `{query: "usability"}` returned five passages, all with `source_url` "[GAP]" (reference-list fragments and NHS DTAC text). `{query: "IEC 62366"}` returned two Health Canada passages without URLs (`examples/live/guidance_and_record.json`).
- Do not cite a passage without a source URL. The copied research files replace the guidance store for this competency (register C6).

## agent-pack.list_experts and agent-pack.download_agent

- `list_experts {query: "patient experience"}` returned the Patient Experience Designer (`patient-experience-designer`), the worker named for this competency. Its remit says it "Does not produce interface mockups, human-factors protocols, or usability-test reports". Its download carries the six old task names of DH-02.04.3.1 and 3.2.
- `list_experts {query: "human factors"}` returned the Usability Test Specialist (`usability-test-specialist`), who "Executes usability and human-factors tests against an existing protocol"; it is not bound to this competency in its download.
- Offer a download only when the person wants the role on their own assistant.

## verify.build_record (counted)

- Needs `clearances` with a human `cleared_by.name`. With "Claude" it refused: "build_record refuses a record without a human cleared_by.name".

## Not used

- `find_job {query: "user research usability"}` returned no jobs. `watch_*` tools are never called.

## Local helper

`scripts/research_log.py` (no connector): `sus` scores SUS from the person's file; `stops` counts participants per stop and user group from a session log; `trace` follows insights to decisions and shipped changes (used mostly by the monitoring sibling). Every subcommand refuses files with identifying columns or contact data. Tested on 19 October 2026 on the illustrative files in `examples/sample-data/`.

## Catalogue jobs (list_jobs, 19 October 2026)

`list_jobs` returned 29 jobs in four suites (Regulatory, Evidence and Reimbursement, Diligence, Commercial). None covers a task in this skill, so every task's formula table says "Catalogue job: none" and the direct calls in the steps stay the method. Not wired, by rule: `post-market-watch` (it sets a `watch_register` watch). Not wired, by scope: `partner-prioritization` runs `analytics.mcda` and `analytics.rice` but is scoped to partners and indications; call the calculator directly. `evidence-table` applies only where a task builds a literature evidence table; no task here does. No `start_job` run was made, because no job was wired.
