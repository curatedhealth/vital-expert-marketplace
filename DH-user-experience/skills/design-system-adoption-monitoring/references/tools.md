# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `regulatory-dh_search_safety_events`). Counted calls draw on the library key's monthly allowance; free calls do not.

This is a method pack: the library has no design-system suite and no catalogue job for this work (`find_job {query: "design system component accessibility"}` returned no match on 19 October 2026). The skill runs on the person's own component list and the sourced references. The library adds field safety events as context for device surfaces, the ranking calculator for follow-ups the person scored, and the record. The person's inventory, product names and issue logs never go into a library call. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`. Several calls returned 503 ("could not answer this call (503). Nothing was counted.") and succeeded when retried after a short wait.

## regulatory-dh.search_safety_events (counted)

- Arguments: at least one of `manufacturer`, `product`, `product_code`; optional `jurisdiction` (US, EU, UK, CH, all), `since` (YYYY-MM-DD), `limit` 1 to 25.
- Coverage as returned: US FDA enforcement recalls whose product text mentions software, algorithm, application, firmware or app, plus MAUDE counts; UK MHRA alerts; CH not loaded.
- `product` matches words in the recall title, not the problem described. `{product: "display", since: "2025-01-01"}` returned two hardware display recalls (a review-station monitor, a surgical console viewer). `{product: "user interface", since: "2024-01-01"}` returned two image-processing recalls whose title says "primary user interface" and whose problem is a calculation error. There is no use-error or user-interface field `[GAP]`.
- A manufacturer query works better for the person's own products: `{manufacturer: "Medtronic", since: "2025-01-01", jurisdiction: "US", limit: 5}` returned five Class II recalls of clinician programmer and patient apps, including one whose summary says infusion "steps may be displayed out of order" (event date 8 April 2026) and one where "a Device Reset message displayed on the app was unable to be cleared" (20 November 2025). It also attached MAUDE counts for product codes QIH and QQC without saying why.
- Recall `source_url` is the openFDA API endpoint, not the record; no recall number. Cite title and event date and say "openFDA enforcement report, record not linked". The `event_date` basis is not stated `[GAP]`.
- Use in B1 only, and only for components on a medical device user interface: to show what the person's own or a named partner's field events state about screens and displays. Quote the summary. Never infer a root cause, a use error or a design flaw from a recall, never count events as an indicator of the design system, and never read "no events" as evidence of safety.

## analytics.rice (counted)

- Arguments: `initiatives`, each with `id`, `reach`, `impact` (0.25, 0.5, 1, 2 or 3), `confidence`, `effort`. Every number is the person's.
- Pitfall measured: `confidence` is read as a percent. Given `0.8`, the tool divided it by 100 and returned confidence 0.008 and scores 100 times too small (`examples/live/rice_fraction_confidence.json`). Given `80`, it returned 0.8 and the expected scores (`rice_percent_confidence.json`). The order did not change in the test, but every score was wrong by a factor of 100. Always pass confidence as a whole percent (80, not 0.8), and check that each returned `score` equals reach x impact x (confidence / 100) / effort.
- Returns `score` per initiative and the method line "RICE Prioritization (Reach x Impact x Confidence / Effort)", citing Intercom (2016), a vendor article, so the method is not a sourced rule here; it is a calculator the person chooses.
- `name` comes back null.
- Use in B1 to rank follow-ups (migrations, fixes, contract changes) the person scored.

## analytics.mcda (counted)

- Arguments: `alternatives` (each `id` and `scores`, a map of criterion to number) and `criteria_weights` (the person's weights; should sum to 1).
- Behavior from sibling builds (DH-03.02.3.1, register C17): a weighted sum on a 0 to 4 scale; every criterion is treated as higher-is-better; no robustness view. Name criteria so a higher score is better ("migration effort avoided", not "migration effort"). Not called in this build.
- Use in B1 when the person prefers weighted criteria to RICE (for example choosing whether to fix a breach in the contract or the surface).

## regulatory-dh.retrieve_guidance (counted)

- `{query: "WCAG accessibility", limit: 5}` returned no passage. `{query: "human factors", limit: 5}` returned five passages, all with `source_url` "[GAP]" and `retrieved_at` null, from a journal perspective, a reference list and what reads as FDA off-the-shelf software guidance. Do not cite a passage without a source URL. The sourced references in this skill replace the guidance store for this work.

## verify.qualify_source (counted)

- `{url: "https://www.w3.org/TR/WCAG22/"}` returned tier "inadmissible", "no provenance", publisher null, although the title and status "current" were read. A standards body's own page is rated like a register page (register item C1). The rows in `references/` carry the quote and URL instead; do not use Verify to qualify WCAG, GOV.UK, NHS or USWDS pages.

## verify.build_record (counted)

- Needs `clearances` with a human `cleared_by.name`. With the name "Claude" it refused: "build_record refuses a record without a human cleared_by.name". Call it only when an output leaves the conversation and the person names who clears it.

## agent-pack.list_experts and agent-pack.download_agent

- `list_experts {function: "Digital Product", limit: 30}` returned eight experts, including the UX/UI Designer, Digital Health (`ux-ui-designer-digital-health`) and the Service Design Director (`service-design-director`). Both downloads list all six old design-system tasks (Component contract, Component change, Adoption of the component, Contract check, Behind-version count, System follow-up). The Service Design Director's own prompt says it never produces "interface designs, interaction specs or UI copy" and routes "interface questions" to the UX designer, so this skill works as the UX/UI Designer.
- `download_agent {expert: "ux-ui-designer-digital-health"}` returned 66,915 characters (59 skills). Its stop rules are the source of `references/governance.md`. Offer it only when the person wants the role on their own assistant.

## literature.search_literature (counted)

- `{query: "design system component library adoption user interface consistency health software", limit: 5}` returned five records, none measuring design-system adoption, drift or effectiveness. Not used in the tasks. If a published usability or accessibility finding is ever cited, use `verify.qualify_source(doi)` then `verify.check_claim` with a passage that states the finding in the same direction (register item N3).

## Not used here

- `watch_*` tools.

## Local helper

- `scripts/ds_adoption.py` (no connector) reads the person's inventory CSV (component, version, products, accessibility status; optional current version, owner, clinical, device UI, modification, lifecycle) and prints the version map, drift by owner, accessibility status as recorded, local modifications and flagged lifecycle values. It sets no threshold. Tested on 19 October 2026 on `examples/sample-data/component_inventory.csv` (illustrative; output saved as `component_inventory_run.md`) and on edge cases (no current version, non-numeric versions, missing columns). The same script ships in the development skill, where it builds the version map for change notes and adoption plans.

## Catalogue jobs (list_jobs, 19 October 2026)

`list_jobs` returned 29 jobs in four suites (Regulatory, Evidence and Reimbursement, Diligence, Commercial). None covers a task in this skill, so every task's formula table says "Catalogue job: none" and the direct calls in the steps stay the method. Not wired, by rule: `post-market-watch` (it sets a `watch_register` watch). Not wired, by scope: `partner-prioritization` runs `analytics.mcda` and `analytics.rice` but is scoped to partners and indications; call the calculator directly. `evidence-table` applies only where a task builds a literature evidence table; no task here does. No `start_job` run was made, because no job was wired.
