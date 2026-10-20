# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them (for example `market-access-dh_find_scheme_precedents`). Counted calls draw on the library key's monthly allowance; free calls do not. Every behavior noted was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`.

## market-access-dh.list_schemes (free)

- No arguments. Use once per run to know which decisions the library can show.
- 19 October 2026: UK_NICE_EVA 15 rows (posture partial, "NICE_API_KEY is empty. Not a refreshed licensed pull"), UK_NICE_HTG 2, UK_NICE_NHAP 0, FR_PECAN 2, FR_LATM 2, FR_LPPR 0, DE_DIGA 82 (`ends_on` empty on all), BE_MHEALTH 33, IE_HSE_CGM 12; AU_MSAC, CH_BAG, ES_REDETS, FI_DIGIHTA and SE_TLV 0 with a stated reason.

## market-access-dh.find_scheme_precedents (counted)

- Required `scheme`; optional `indication`, `product_category`, `limit` 1 to 25.
- `{scheme: "UK_NICE_EVA", limit: 25}` returned 15 rows, all status "conditional", status_raw "early value assessment", `manufacturer` "National Institute for Health and Care Excellence". `{scheme: "UK_NICE_HTG", limit: 10}` returned HTG778 and HTG624, both "permanent", "recommended".
- **The `evidence_passage` is the page header**, for example "... Overview 1 Recommendations 2 The technology 3 Committee discussion 4 Further evidence". It holds no recommendation text, no committee reasoning, no economic result and no evidence-generation outcome. Read the guidance page at `source_url` (or the person's copy) for every decision you describe (register N7 and N6).
- Renumbered guidance appears twice: HTE8 and HTG675, HTE9 and HTG676. The HTE rows' passages say "We have moved health technology evaluation 8 to become HealthTech guidance 675 ... The guidance itself has not changed." Count each guidance once (register N6). `scripts/decision_evidence_log.py` merges them.
- HTG778, titled "Digital technologies to support self-management of asthma: early-use assessment", is stored as permanent / recommended. Early use is conditional by definition (`HE-071`). Read the title and the guidance (register N6).
- `listed_on` is the publication date; "Last updated" dates appear only inside the passage text (HTG660 "Last updated: 07 September 2026"; HTG712 "30 April 2026").
- For DiGA, search by ICD-10-GM code or German term; English terms can miss rows (register C9). DiGA rows hold no claimed or struck effects (register N7).

## market-access-dh.get_status_history (counted)

- `{reference: "HTG660", scheme: "UK_NICE_EVA"}` returned one entry, changed_on 8 February 2023, note "day-zero snapshot 2026-10-15", `days_to_stated_end: null`, and a gap line "only a day-zero snapshot is stored", although the page says it was last updated 7 September 2026 (register C11). History cannot show whether an early-use recommendation changed; read the guidance's update information.

## market-access-dh.retrieve_guidance (counted when it answers)

- `{query: "NICE evidence standards framework budget impact analysis cost-effectiveness standard 17 18"}` returned no passage (register C6). Do not call it for methods; use the references.

## literature.get_record and verify.check_currency (counted)

- For A2, to check that the studies a model rests on are still current. `check_currency {doi: "10.1016/j.lanepe.2026.101691"}` returned not retracted, corrected, superseded or withdrawn, `current: true`.
- `check_currency {url: <NICE PMG36 page>}` returned `notices: ["not checked"]` and `current: false`. That is "not checked", never "out of date". Methods currency comes from `methods-changes.md`.
- `get_record` returned `trial_ids` empty for a trial whose abstract names NCT02558647 (register N8). Take the registry id from the paper with its locator. When the record carries a `pmcid` or `oa_url`, read the open-access full text (Europe PMC `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC<id>/fullTextXML`) before marking any field `[GAP]` from the abstract.

## verify.qualify_source and verify.check_claim (counted)

- Use only when the person wants a claim about a study checked (for example a committee statement that cites a trial result). Working sequence and pitfalls: qualify the DOI first, pass the full source object, quote the results passage; `check_claim` decides on word overlap and rated an accurate and an overstated cost claim both "partial" (register N3, measured in the support skill's build; see `examples/live/` in `reimbursement-evidence-support`).
- `qualify_source {url: <NICE PMG48 page>}` returned "inadmissible", "no provenance" (register C1). Do not send NICE pages to Verify; quote them with URL and read date.

## verify.build_record (counted)

- Refuses a model or tool name: `{cleared_by: {name: "Claude"}}` returned "build_record refuses a record without a human cleared_by.name". Only with the person who clears.

## Catalogue jobs

- `scheme-precedents` (available, "single-tenant watch") lists `find_scheme_precedents` and `watch_scheme`. Use the precedent call only; never set a watch (watches are not separated by customer key, register N2).
- `reimbursement-matrix` (available) gives status per scheme; status is dh-access-and-value's subject.
- No job reads decision documents. `value-dossier` is design-partner only.

## Call budget

A typical A1 run: 1 free call, 1 to 3 precedent calls, 0 to 2 status histories, plus reading 2 to 4 guidance pages (not library calls). A2: 1 `check_currency` per study the model rests on.

## Not used here

`watch_*` tools; analytics calculators (the person's formula in B1 is simple arithmetic; `scripts/decision_evidence_log.py` does it); pricing tools.
