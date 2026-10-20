# Library tools used by the Healthcare UX Design competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `regulatory-dh_search_safety_events`). Counted calls draw on the library key's monthly allowance; free calls do not.

This is a method pack: there is no UX suite in the library. Knowledge sits in `references/`; the library adds comparable field events, two ranking calculators for what the person scored, a literature source check, and the record. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`. The same file sits in both skills of the pair (clinical-workflow-ux-design and usability-monitoring).

| Tool | Used in | Counted |
|---|---|---|
| `regulatory-dh.list_jurisdictions` | Before any safety-event search | Free |
| `regulatory-dh.search_safety_events` | Design A2 (optional); monitoring A2 | Yes |
| `analytics.mcda` | Design B1; monitoring B1 | Yes |
| `analytics.rice` | Monitoring B1, only if the person asks for RICE | Yes |
| `verify.qualify_source`, `verify.check_claim` | Monitoring A1, if a published benchmark is quoted outside the conversation | Yes |
| `verify.build_record` | Any output that leaves the conversation | Yes |
| `agent-pack.list_experts`, `agent-pack.download_agent` | Only if the person wants the role on their own assistant | Yes |

## regulatory-dh.list_jurisdictions (free)

- No arguments. Observed: US 892 safety events (openFDA recalls and MAUDE counts); UK 10 MHRA alerts; EU 0; CH 0 ("Swissmedic FSCA not loaded in this release [GAP]"); TW and CA 0.
- Use it once to know where events can come from. An EU or Swiss product has no field events in the library; say so.

## regulatory-dh.search_safety_events (counted)

- Arguments: at least one of `manufacturer`, `product`, `product_code`; optional `jurisdiction` (US, EU, UK, CH, all), `since` (YYYY-MM-DD), `limit` 1 to 25.
- What it covers (its own coverage line): "US: FDA enforcement recalls whose product text mentions software, algorithm, application, firmware or app; MAUDE counts by year" and "UK: MHRA medical safety alerts matched by whole-phrase manufacturer name or software terms".
- What the filter can do:
  - Match a word in the product text: `{product: "insulin", jurisdiction: "US", since: "2025-01-01"}` returned six recalls, two of them interface-related (Omnipod 5 decimal separator, 23 May 2025; t:slim app right-to-left language, 3 July 2025). `{product: "display", jurisdiction: "US", since: "2024-01-01"}` returned three recalls with "display" in the title.
  - Return UK alerts with a gov.uk record URL: `{product: "software", jurisdiction: "UK"}` returned eight alerts.
- What it cannot do:
  - Filter by cause. There is no use-error field. `{product: "use error"}` returned nothing and the gap "no stored safety events for this scope". Of the three "display" recalls, one describes user modification of settings (Hologic, 23 March 2026); the other two are device faults. Read every summary and sort it yourself, and say the sorting is yours.
  - Cite the US recall record: `source_url` is the API endpoint `https://api.fda.gov/device/enforcement.json`, with no recall number. Cite title and event date and say "openFDA enforcement report, record not linked" (register P1).
  - State what `event_date` means (initiation, classification or posting) `[GAP]` (register P1).
  - Keep one event as one row: the 27 February 2025 Tandem recall came back as two rows, one per product line (register P1).
  - Explain MAUDE blocks: `{product: "decision support"}` returned no recalls but MAUDE counts for product codes NVI and PDT with no reason given, and an empty gaps list, although the "use error" call with no results returned a gap line (register P1). MAUDE counts are reports, not confirmed events.
  - UK: `manufacturer` is null on most alerts; MDA/2019/024 is stored as "AI Medical AG" while its summary says "Manufactured by B. Braun Avitum AG" (register N1). Quote the summary.
- Rule for this pack: field events are prompts for which misreads to look for, never evidence of a use error, a root cause or a design flaw in another company's product. Absence of events is not evidence of safety.

## regulatory-dh.retrieve_guidance (counted; not used)

- `{query: "human factors validation critical tasks"}` returned no passage. `{query: "usability"}` returned five fragments (two journal articles, an NHS DTAC guide), each with `source_url` "[GAP]" and `retrieved_at` null (register C6). The sourced references in this skill replace the guidance store for human factors questions. Do not cite a passage without a source URL.

## analytics.mcda (counted)

- Arguments: `alternatives` (each `id` plus `scores`, criterion to number, 0 to 4) and `criteria_weights` (the person's, summing to 1).
- Returns "EVIDEM Multi-Criteria Decision Analysis (weighted-sum, 0-4 scale)": `value_estimate` = sum of weight times score divided by 4, times 100, with `contributions` per criterion. Checked by hand and by `scripts/mcda_swap.py` on the live call (`examples/live/mcda_alert_placement.json`): values match.
- Pitfalls: every criterion is treated as higher is better (`negative_criteria: []`, no input field to set it), so name criteria that way ("workflow interruption avoided", not "interruption"). `name` comes back null. No robustness view; the top two options in the live call differed by 1.25 points, and `scripts/mcda_swap.py` shows the weight at which they swap (register C17).

## analytics.rice (counted)

- Arguments: `initiatives`, each with `id`, `reach`, `impact` (0.25, 0.5, 1, 2 or 3), `confidence`, `effort`; the person supplies every number.
- Pitfall: confidence must be given in percent. With `confidence: 0.8` the tool echoed 0.008 and returned scores 100 times too small (0.96 instead of 96). With `confidence: 80` it returned 96. Ties are not flagged (two initiatives at 200).
- Limit for this pack: RICE has no severity term. In the live run a training update tied for first with a contrast fix and ranked above a dose-unit redesign, although FDA ranks training last among risk controls (UX-US-33, CS77). Use RICE only when the person asks for it, and say what it leaves out. For safety-related repairs prefer `analytics.mcda` with a severity criterion the person scores.

## verify.qualify_source and verify.check_claim (counted)

- `qualify_source {doi: "10.2196/37290", question: ...}` returned tier "gold", title "System Usability Scale Benchmarking for Digital Health Apps: Meta-analysis", JMIR mHealth and uHealth, 2022, PMID 35980732, retraction status none.
- `check_claim` works only when `source` carries the record `qualify_source` returned (source_id, tier, source_type, title, publisher, date, status, code). With a minimal `{source_id, doi}` it returned a 502 error four times ("Nothing was counted"); with no `source` it returned "unverifiable", "No admissible source was available".
- With the full record and the passage quoted from research row UX-M-09, it returned "supported", rationale "Strong overlap (70%) with context". The decision rests on word overlap (register N3): read the passage yourself and accept the claim only if the passage states the finding in the same direction.
- The returned citation has DOI, PMID, authors and year empty although `qualify_source` held them (register C18). Build the citation from the research row (author, DOI) instead.

## verify.build_record (counted)

- Needs `clearances` with a human `cleared_by.name`. With "Claude" it refused: "build_record refuses a record without a human cleared_by.name". Call it only when an output leaves the conversation and the person names who clears it.

## agent-pack.list_experts and download_agent

- `list_experts {query: "design"}` returned 25 of 31 matches, including the bound worker `service-design-director` ("Does not run usability studies and does not produce interface designs") and `ux-research-lead` ("Leads human-factors and usability research for regulated digital health").
- `download_agent {expert: "service-design-director"}` returned 69,631 characters, version 2026-10-16. Its stop rules are the source of `references/governance.md`. Offer it only when the person wants the role on their own assistant.

## Reliability

- Several calls on 19 October 2026 returned 503 or 502 ("Nothing was counted"); parallel calls failed more often than single calls. Retry once, one call at a time. If a call still fails, say which call failed and continue on the references.
- Do not call `watch_*` tools.

## Catalogue jobs (list_jobs, 19 October 2026)

`list_jobs` returned 29 jobs in four suites (Regulatory, Evidence and Reimbursement, Diligence, Commercial). None covers a task in this skill, so every task's formula table says "Catalogue job: none" and the direct calls in the steps stay the method. Not wired, by rule: `post-market-watch` (it sets a `watch_register` watch). Not wired, by scope: `partner-prioritization` runs `analytics.mcda` and `analytics.rice` but is scoped to partners and indications; call the calculator directly. `evidence-table` applies only where a task builds a literature evidence table; no task here does. No `start_job` run was made, because no job was wired.
