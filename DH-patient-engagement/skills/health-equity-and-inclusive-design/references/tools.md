# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `literature_search_literature`). Counted calls draw on the library key's monthly allowance.

This is a method pack: the work runs on the person's own aggregate counts and the sourced references. The library adds published evidence, the claim check, a ranking calculator for options the person scored, and the record. The person's counts never go into a library call. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`.

## literature.search_literature (counted)

- Arguments: `query`; optional `filters` (`date_from`, `date_to`, `designs[]`, `language`), `limit` 1 to 50.
- Observed: `{query: "digital health intervention engagement disparities race ethnicity income older adults", filters: {date_from: "2020-01-01"}, limit: 6}` returned 6 of 24 merged records from PubMed, Europe PMC, OpenAlex and Crossref.
- Pitfalls seen:
  - Two of six records were off topic (social engagement among older adults; forgone care in the pandemic). Read every title before using a record.
  - Design labels can be wrong: Katz et al. 2024 (doi:10.1001/jamanetworkopen.2023.56070), a systematic review and meta-analysis by its own title, came back as `design: "other"` (confidence 0.3); a scoping review came back as `systematic_review` (0.78).
  - `trial_ids` empty on every record.
- Use it in A1 only when the person wants published evidence on who a similar intervention left out. A paper about another population is context, not evidence about the person's product.

## verify.qualify_source then verify.check_claim (counted)

- Working sequence: `qualify_source {doi, question}` then `check_claim {claim: {text}, passage: {text, locator}, source: {source_id, doi, tier}}` with a passage you have read.
- Observed: `qualify_source {doi: "10.1001/jamanetworkopen.2023.56070"}` returned tier "gold", status current, score 78, not retracted.
- `check_claim` returned "supported" for the claim in the passage's direction (overlap 33%) and also "supported" for its negation ("showed no difference", overlap 18%) from the same passage. The status follows word overlap, not direction (register item N3). Accept a literature claim only when you have read the passage and it states the claim in the same direction; record the passage and locator in the output.
- The citation returned has title null, no authors, year null, Harvard "Unknown (n.d.)". Build the citation from the `qualify_source` record instead.
- `qualify_source {url: "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-92"}` returned tier "inadmissible", "no provenance", although the title was read correctly (register item C1). Do not run regulatory rows through Verify; the rows already carry URL, quote and read date.

## analytics.mcda (counted)

- Arguments: `alternatives` (each `id` plus `scores`, a map of criterion to number) and `criteria_weights` (the person's weights; should sum to 1).
- Method returned: "EVIDEM Multi-Criteria Decision Analysis (weighted-sum, 0-4 scale)". `value_estimate` is the weighted sum of scores divided by 4, times 100; `contributions` break it down.
- Observed (illustrative scores, three inclusive changes, four criteria, weights 0.35, 0.30, 0.20, 0.15): 77.5, 70, 58.75. `name` null on every result; `negative_criteria` empty.
- Pitfalls: every criterion is treated as higher-is-better and the schema offers no way to set a negative one, so name criteria as benefits ("effort avoided", not "effort"). No robustness view (register item C17): report which weight would change the order only if you compute it from the contributions, and say so.
- Use in B1 only on scores the person gave. Never fill a score.

## regulatory-dh.retrieve_guidance (counted)

- Observed: `{query: "Section 1557 language access", limit: 5}` and `{query: "diversity action plan", limit: 5}` both returned no passages ("no passage retrieved in this namespace"). The store does not hold these topics (register item C6). Use the sourced rows instead.

## agent-pack.list_experts and agent-pack.download_agent (counted)

- `list_experts {query: "equity"}` returned three experts; the Health Equity & Digital Access Lead (`health-equity-access-lead`) is the worker for this skill.
- `download_agent {expert: "health-equity-access-lead"}` returned 69,958 characters, 53 skills, among them the six register tasks of DH-02.03.4.1 and 4.2. Its stop rules are the source of `governance.md`. Offer it only when the person wants the role on their own assistant.
- Defects seen (register items C14, C15): the prompt lists six "bound competencies", none of them equity; it says "Tools you can operate (24)" while the file lists 31, including UniProt, ChEMBL, PubChem and DailyMed; work-product sections are titled "None"; "[GAP] (persona_archetype)" and "trust the foreign key" plumbing remain.

## verify.build_record (counted)

- Needs `clearances` with a human `cleared_by.name`. Observed: with "Claude" it refused ("build_record refuses a record without a human cleared_by.name").
- Call it only when an output leaves the conversation and the person names who clears it.

## find_job

- `{query: "health equity"}` returned no matches: there is no library job for this work; this skill is the method.

## Not used here

- `watch_*` tools.
- commercial-dh and diligence-dh: not needed for equity work on the person's own product.

## Local helper

- `scripts/equity_compare.py` (no connector): reads aggregate counts per subgroup (columns `dimension, subgroup, eligible, reached`, optional `outcome_n, outcome_met`), requires `--min-cell` (the person's small-cell rule), takes one `--reference "dimension=subgroup"` per dimension. Outputs rates with Wilson 95 percent intervals, differences in percentage points and ratios against the reference, shares of eligible and reached, and suppresses small counts and their complements. Refuses rates in place of counts, reached above eligible, and outcomes counted outside the reached. Tested on 19 October 2026 on `examples/sample-data/rpm_equity_illustrative.csv` (illustrative, not real data).
