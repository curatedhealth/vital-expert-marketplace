# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them (for example `mcp__Vital_Digital_Health__verify_check_claim`). Counted calls draw on the library key's monthly allowance.

Behavior below was observed in live calls on 19 October 2026. Saved outputs are in `examples/`.

## What the library does not hold

- No outcome-contract or risk-share data: no stored DiGA outcome components, no ACCESS participant results, no published model clauses. `market-access-dh.retrieve_guidance` returned no passage for "erfolgsabhängige Preisbestandteile DiGA outcome-based price component" or for "outcomes-based contract risk-sharing agreement digital health" (both: `results: []`, `gaps: ["[GAP]", "no passage retrieved in this namespace"]`).
- `find_job` for "outcomes contract risk share value-based" returned no job.
- So the method facts come from `references/`, and the contract facts come from the person.

## market-access-dh.list_schemes (free)

- No arguments. Returns each scheme's authority, clock rule, listing count, last load and posture.
- The DE_DIGA `clock_rule` names GKV-Spitzenverband negotiation after year one but says nothing about the 20 percent outcome-linked component. Do not read the scheme rule as the full price rule; use `risk-share-models.md`.

## market-access-dh.find_scheme_precedents (counted)

- Required: `scheme`. Optional: `indication` (use ICD codes or German terms for DiGA, for example "F32"), `limit` 1 to 25.
- Use in A1 or A2 to show comparables in the same indication: their status and the `price` field as recorded.
- Pitfalls: the `price` field does not say whether it is the negotiated amount or the manufacturer's first-year price, and it does not show any outcome-linked component. Quote it as "price recorded in the directory copy, retrieved DATE", never as the comparator's contract terms. `manufacturer_country` can be wrong (SOFY GmbH, Österreich, stored as DE).

## analytics.budget-impact-model (counted when it answers)

- Required: `eligible_population`, `current_mix` (name, share, annual_cost_per_patient; shares sum to 1), `new_treatment_annual_cost_per_patient`, `uptake_curve` ("uptake by year, each value from 0 to 1").
- Observed: five calls with valid inputs and four different `uptake_curve` shapes (`{year, share}`, `{year, uptake}`, `{year, value}`, plain numbers) all returned "could not answer this call (422). Nothing was counted." The job card (`start_job budget-impact`) gives no item schema.
- Until fixed: do the arithmetic by hand on the person's inputs (yearly patients = population x uptake; net = patients x (new cost minus weighted current cost)), show every input, and label the result "hypothesis on your inputs". Never call it a forecast or a price.

## literature.search_literature and literature.get_record (counted)

- Use only when the person asks for validated instruments or evidence for a measure.
- `search_literature {query: "PHQ-9 minimal clinically important difference validation", limit: 5}` returned Löwe et al. 2004 (Medical Care, PMID 15550799) first, plus off-topic records (an esketamine cohort, a Chinese student survey). Read titles before using any record.
- `search_literature` returned an empty `excerpt` for Löwe 2004; `get_record {pmid: "15550799"}` returned the abstract opening. The excerpt does not contain the MCID value itself, so the value cannot be checked from it `[GAP]`.

## verify.qualify_source then verify.check_claim (counted)

The working sequence for a literature claim:

1. `verify.qualify_source {doi: "10.1097/00005650-200412000-00006"}` returned `tier: "gold"`, `source_id` equal to the DOI.
2. `verify.check_claim` with `claim {text}`, `passage {text, locator}` quoted from the abstract, and `source` carrying the qualify result: `{source_id, tier, source_type, doi, official_url}`. Returned `status: "supported"` with the deciding passage.

Pitfalls observed:

- Passing `source: {doi: "..."}` alone returned `unverifiable`, "No admissible source was available", for the same claim and passage. Pass the qualified source object.
- The returned `citation` had empty title, authors and year although the record holds them. Build the citation from `literature.get_record`.
- Official documents are rated inadmissible: `qualify_source {url: "https://www.cms.gov/priorities/innovation/files/access-payments-amts-perf-targets.pdf"}` returned `tier: "inadmissible"`, "no provenance", and `check_claim` on an ACCESS target then returned `unverifiable`. Cite regulator and statute facts to their row in `references/` (URL, quote, read date) instead.

## verify.build_record (counted)

- Needs a named human in `cleared_by`; refuses a missing name or a tool or model name. Use only when an output leaves the conversation.

## Not used here

- `watch_*` tools.
- Any call with the person's confidential contract terms, prices or patient data.
