# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `analytics_rice`). Counted calls draw on the library key's monthly allowance; free calls do not.

This is a method pack. The library has no accessibility suite and no accessibility job (`find_job {query: "accessibility"}` returned no matches; `list_jobs` lists none). The skill runs on its sourced references and the person's own facts. The person's issue log and test records never go into a library call. The library adds a ranking calculator for repairs the person scored, Verify for a sourced date or rule that leaves the conversation, and the record. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`. Several calls first returned HTTP 503 or 502 ("Nothing was counted. Try again"); a retry minutes later worked.

## regulatory-dh.retrieve_guidance (counted)

- Arguments: `query`; optional `namespace`, `limit`.
- Observed: "WCAG" returned five passages, all `source_url` "[GAP]" and `retrieved_at` null (a stroke-survivor paper and a WHO telehealth accessibility document). "accessibility" returned five, four without a source URL and three off-topic (algorithmic bias, a GDPR recital, a WHO strategy); one is NICE PMG36 5.3.8 on submission accessibility. A multi-word question on Section 504 dates returned nothing.
- Do not use it for accessibility law or WCAG. The rows in `references/` replace it. Do not cite a passage without a source URL.

## verify.qualify_source then verify.check_claim (counted)

- `qualify_source {url: "https://www.w3.org/TR/WCAG22/"}` returned tier "inadmissible", "no provenance". W3C text cannot be verified through Verify today; cite the row (URL, quote, read date) instead.
- `qualify_source {url: "https://www.govinfo.gov/content/pkg/FR-2026-05-11/pdf/2026-09266.pdf"}` (the HHS 504 extension) returned tier "bronze", publisher "Federal Register", date "2026-05-09" (the document is in the Federal Register of 11 May 2026), title null.
- `check_claim` needs the `source` object as `qualify_source` returned it (`source_id`, `tier` and so on). With `source: {url}` alone it returned "unverifiable".
- **Pitfall.** With the qualified source and the extension rule's own sentence as the passage, the current date ("11 May 2027") and the superseded date ("11 May 2026") both returned "partial", rationale "source tier bronze". Verify does not tell a moved date from its replacement. Read the passage yourself and confirm direction (register N3); the status alone proves nothing about which date is current.
- The citation it returns has `title` null and the Chicago form gives the 9 May date. Build the citation from the row instead.

## analytics.rice (counted)

- Arguments: `initiatives`, each with `id`, `reach`, `impact` (0.25, 0.5, 1, 2 or 3), `confidence`, `effort`. The person supplies every number.
- **Pitfall.** `confidence` is read as a percent and divided by 100. Passing 80 gives 0.8 (score 3,360 for reach 4,200, impact 3, effort 3). Passing 0.8 is silently divided again (score 33.6). The order stays the same, the scores do not. Always pass confidence as a percent (0 to 100), and say so when asking the person.
- Use it in B1 only to rank repairs the person scored. Never fill a score. The live calls are saved in `examples/live/rice_barrier_fixes.json`.

## analytics.mcda (counted)

- Not called in this build. Behavior measured in sibling builds (register C17): weighted sum on a 0 to 4 scale; every criterion is treated as higher-is-better; no robustness view. If the person prefers weighted criteria to RICE, phrase criteria so higher is better ("users reached", "effort avoided").

## agent-pack.list_experts and agent-pack.download_agent

- `list_experts {query: "access"}` returned nine experts, including the Health Equity & Digital Access Lead (`health-equity-access-lead`), the worker for this skill, and the UX Research Lead and UX/UI Designer.
- `download_agent {expert: "health-equity-access-lead"}` returned 69,958 characters, 53 bound skills including the six old accessibility tasks (Access requirement, Barrier fix, Assistive check, Conformance sample, Open barrier age, Access release decision). Its stop rule is the source of `references/governance.md`. Offer it only when the person wants the role on their own assistant.

## verify.build_record (counted)

- Needs `clearances` with a human `cleared_by.name`. With "Claude" it refused: "build_record refuses a record without a human cleared_by.name".
- Call it only when an output leaves the conversation and the person names who clears it.

## Local helper

- `scripts/a11y_issue_log.py` (no connector): summarizes the person's issue log against their target WCAG version and level, using `references/data/wcag_criteria.csv`. Tested on 19 October 2026 on `examples/sample-data/issue_log_illustrative.csv` (illustrative) for targets 2.2 AA, 2.1 AA and 2.0 AA; outputs saved beside it. The criteria counts it reports (55, 50 and 38 at AA) match rows WX1, WX2 and WX5.

## Not used here

- `regulatory-dh.search_safety_events`: use-error events belong to the UX 4.x usability skills.
- Literature tools: no task here rests on a published study.
- `watch_*` tools.

## Catalogue jobs (list_jobs, 19 October 2026)

`list_jobs` returned 29 jobs in four suites (Regulatory, Evidence and Reimbursement, Diligence, Commercial). None covers a task in this skill, so every task's formula table says "Catalogue job: none" and the direct calls in the steps stay the method. Not wired, by rule: `post-market-watch` (it sets a `watch_register` watch). Not wired, by scope: `partner-prioritization` runs `analytics.mcda` and `analytics.rice` but is scoped to partners and indications; call the calculator directly. `evidence-table` applies only where a task builds a literature evidence table; no task here does. No `start_job` run was made, because no job was wired.
