# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them (for example `literature_get_record`). Counted calls draw on the library key's monthly allowance; free calls do not. Every behavior noted was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`.

## market-access-dh.list_schemes (free)

- No arguments. Use once in A1 to say which bodies the library holds decisions for (context for the monitoring skill), never as a rule source.
- 19 October 2026: UK_NICE_EVA 15 rows, UK_NICE_HTG 2, UK_NICE_NHAP 0, FR_LPPR 0, FR_PECAN 2, FR_LATM 2, DE_DIGA 82. The scheme records carry no economic method rules (perspective, discounting, thresholds). Those come from `body-economic-standards.md`.

## market-access-dh.retrieve_guidance (counted when it answers)

- `{query: "NICE evidence standards framework budget impact analysis cost-effectiveness standard 17 18"}` returned no passage ("no passage retrieved in this namespace"; register C6). Do not call it for economic methods; use the references.

## literature.search_literature (counted)

- `query`, optional `filters`, `limit`. A DOI in the query pins that paper first.
- Economic evaluations come back with a design label for the trial, not the analysis: "Guided Internet-Based Cognitive Behavioral Therapy for Insomnia: Health-Economic Evaluation ... Alongside a Randomized Controlled Trial" (DOI 10.2196/25609) was labeled `rct` 0.98 with an empty excerpt; a QALY secondary analysis (DOI 10.3399/bjgpo.2022.0090) `other` 0.3; a conference proceedings abstract `systematic_review` 0.78 (register N8). There is no filter for economic evaluations. Ask the person for the DOI of each study the model uses.

## literature.get_record (counted)

- One of `doi`, `pmid`, `pmcid`, `openalex_id`. Returns identifiers, venue, year, design, retraction status, open-access URL and an excerpt (the start of the abstract).
- For DOI 10.1016/j.lanepe.2026.101691 the excerpt stopped before the results and `trial_ids` was empty, although the abstract names NCT02558647 (register N8). Costs, QALYs and intervals are never in the record: take them from the paper. When the record carries a `pmcid` or `oa_url`, read the full text before writing `[GAP]`: for this DOI the Europe PMC full text (PMC13186012, `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13186012/fullTextXML`, read 19 October 2026) states the utility instrument and weights (Methods, Outcomes), "No discounting was performed" and the alternative perspectives (Methods, Cost-effectiveness analysis), all of which the abstract leaves silent.

## literature.classify_study and literature.grade_evidence (counted)

- `classify_study {record}` returned `rct` 0.78, decided by "title:randomized" only. `grade_evidence {record, question_type: "treatment"}` returned CEBM level 2 ("rct for a treatment question -> level 2").
- Report both as "design label and CEBM level from design only". Neither says anything about the economic analysis, its perspective or its inputs, and neither is a body's view.

## verify.qualify_source, verify.check_claim, verify.check_currency (counted)

- Working sequence: `qualify_source {doi}` (returned tier gold, status current, source score 72), then `check_claim {claim: {text}, passage: {text, locator}, source: <the full qualify_source object>}` with the passage quoted verbatim from the paper's results (register C18: a DOI alone returns "unverifiable").
- **Pitfall (register N3), measured on an economic result.** Passage: the Findings sentence reporting "-€278 [95% CI: -1413 to 858] lower costs and 0.025 QALYs gained [95% CI: 0.010 to 0.041]". The accurate claim returned "partial" (44 percent overlap); an overstated claim, "dCBT-I significantly reduces societal costs", also returned "partial" (40 percent) although the cost interval includes zero; only an overt reversal returned "unsupported" (29 percent). Verify cannot tell a significant from a non-significant cost difference. Read every passage yourself: direction, interval, horizon and comparator must match.
- The returned citation drops DOI, authors and year (register C18). Cite from `get_record`.
- `check_currency {doi}` returned not retracted, corrected, superseded or withdrawn, `current: true`. Use it for every study a model rests on.
- `check_currency {url: <NICE PMG36 page>}` returned `notices: ["not checked"]` with `current: false`. That means not checked, not out of date. Method currency is in the references' version rows (`HE-033`, `HE-057`, `HE-064`), never from this call.
- `qualify_source {url: <NICE PMG48 chapter 3>}` returned tier "inadmissible", "no provenance" (register C1). Do not send method pages to Verify; cite the HE row.

## analytics.budget-impact-model (counted when it answers)

- Returned HTTP 422 ("Nothing was counted") with `uptake_curve` as `[{year, value}]` and as a plain list `[0.05, 0.1, 0.15]` (register N5; earlier builds saw the same with other shapes). Use `analytics.scenario-modeler` or the arithmetic in the conversation instead, and say the calculator was not used.

## analytics.scenario-modeler (counted)

- Exposed and working on 19 October 2026 (register C12 had recorded it as not exposed).
- `parameters` (a number is constant, a list is one value per period), `formula` over those names and `t`, `periods`, `aggregate` (sum, cumulative, none).
- A budget impact as arithmetic: `{parameters: {population: 10000, uptake: [0.05, 0.1, 0.15], new_cost: 200, displaced_cost: 420}, formula: "population * uptake * (new_cost - displaced_cost)", periods: 3}` (illustrative inputs) returned -110,000, -220,000, -330,000, sum -660,000.
- Pitfalls: periods are numbered from `t: 0`, so label them year 1 to 3 yourself; the response note says "Public registers and published literature" although every number is the caller's. The output is a hypothesis on the person's inputs.

## analytics.risk-tornado (counted)

- Same `parameters`, `formula`, `periods`, plus `parameter_ranges` (low and high per name) or `variation_pct` (default 0.2).
- On the same illustrative inputs with ranges for `displaced_cost` (300 to 600) and `new_cost` (150 to 300) it returned swings of 900,000, 450,000 and, at plus or minus 20 percent, 264,000 for `population`.
- Pitfall: list parameters (here `uptake`) are skipped and reported only in `skipped_parameters`. Say so, or pass a constant.

## analytics.mcda and analytics.rice (counted)

- For B1 only, to rank gaps the person has scored. `mcda` needs every score (a missing one returns HTTP 400) and returns no robustness view (register C17); `rice` reads `confidence` as a percent (register N5). Not called in this build; behavior from the register.

## verify.build_record (counted)

- `{clearances: [{cleared_by: {name: "Claude"}}]}` returned "build_record refuses a record without a human cleared_by.name". Call it only with the name of the person who clears.

## Catalogue jobs

- `list_jobs` (19 October 2026), Evidence and Reimbursement suite: `evidence-table` available (literature tools plus Verify), `budget-impact` available ("buyer supplies inputs", but its calculator returns 422), `price-anchor` available (a price ceiling: not used here, pricing belongs to dh-market-access), `value-dossier` design partners, not startable.
- `find_job {query: "budget impact value dossier evidence"}` returned no match although three of those jobs exist (register C7 by analogy: search does not reach job names).
- `start_job` returns the method and tool names and runs nothing; the assistant makes the calls itself.

## Call budget

A typical A2 run: 4 to 6 counted calls per study the model rests on (`get_record`, `classify_study`, `grade_evidence`, `qualify_source`, `check_currency`, one `check_claim` per key result), plus 1 to 3 analytics calls. A1 needs only the free scheme list.

## Not used here

`watch_*` tools; `analytics.vba-price-anchor` (a price ceiling is a pricing position: dh-market-access); `commercial-dh.*`.
