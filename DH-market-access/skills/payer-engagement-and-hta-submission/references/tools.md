# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them (for example `literature_search_literature`). Every behavior noted was observed in live calls on 19 October 2026; the saved outputs are in `examples/live/`.

## market-access-dh.list_schemes (free)

- No arguments. Returns per scheme `listing_count`, `last_load`, `posture`, `posture_reason`, `clock_rule`.
- Use it once per run to know which schemes the library can show precedents for. On 19 October 2026: DE_DIGA 82 listings (partial; `ends_on` empty on all), FR_PECAN 2, FR_LATM 2, FR_LPPR 0 (gap), UK_NICE_EVA 15, UK_NICE_HTG 2, UK_NICE_NHAP 0, US_CMS_DMHT 3, US_CMS_RPM 4.
- Pitfall: the tool's own description still says LATM is empty; it holds 2 listings (register C7, lane E2).

## market-access-dh.find_scheme_precedents (counted)

- Required `scheme`. Optional `indication`, `product_category`, `limit` 1 to 25.
- Use it in A2 for comparable decisions on the route the person is taking.
- DE_DIGA: search by ICD-10-GM code or German term (`F51` returned somnio, HelloBetter Schlafen, somnovia; all permanent). English terms can return nothing (register C9). Deleted DiGA can have empty indications and drop out (register C9).
- Describe a precedent only by what its row states (indication, status, dates, price). Do not label it therapeutic or telemonitoring unless the row's indication or source says so. On 19 October 2026 FR_PECAN held ODYSIGHT (indication: chronic maculopathies, no type stated) and Continuum+ Connect (indication: télésurveillance médicale).
- Rows hold status, listing date and price. They do **not** hold the study behind a listing, the positive care effect claimed, or the registry link, although the DiGA directory publishes them (`DE30`). Comparable evidence is therefore `[GAP]` from the library; read it on the directory page in `source_url`.
- UK_NICE_EVA and UK_NICE_HTG rows are guidance documents, not products: `manufacturer` is NICE and product names are not stored. Renumbered guidance appears twice (HTE8 and HTG675; HTE9 and HTG676). Count guidance once.
- UK_NICE_HTG stores HTG778, titled "early-use assessment", as `permanent` / "recommended". Early use is conditional by definition (`UK6`). Read the title and say "check the guidance".

## market-access-dh.retrieve_guidance (counted)

- `query`, optional `namespace`, `limit`. "DiGA evaluation concept trial listing requirements" returned no passage (register C6). Use `references/` for requirements; call this once at most, and only for a rule the references lack.

## literature.search_literature (counted)

- `query`, optional `filters`, `limit`. A DOI or PMID in the query pins that paper first.
- Searching by product name ("somnio … randomized") returned dCBT-I trials that do not name the product in title or excerpt. A name match is not identity: ask the person for the DOI of each study they rely on.
- `trial_ids` was empty on every record returned, including RCTs. Registration (`DE14`) cannot be confirmed from the library: `[GAP]` until the person shows the registry entry.

## literature.get_record (counted)

- One of `doi`, `pmid`, `pmcid`, `openalex_id`. Returns identifiers, venue, year, design, retraction status, an open-access URL and an excerpt.
- The excerpt is the start of the abstract. For 10.1155/da/2171041 it held background and design but no result. Effect sizes are never in the record.

## literature.classify_study (counted)

- `record`. Returns design and the fields that decided it (publication type and title words). It reads metadata, not the methods section.

## literature.grade_evidence (counted)

- `record` or `records`, `question_type` (treatment default), `standard` (`cebm2011` default, or `grade` as draft).
- Returns a CEBM level from the design alone ("rct for a treatment question -> level 2"). It does not consider comparator, risk of bias, setting or size. Report it as "CEBM level from design", never as a quality verdict, and never as BfArM's, HAS's or NICE's view.

## verify.qualify_source then verify.check_claim (counted)

- `qualify_source` with `doi` returned tier gold, status current, for 10.1155/da/2171041. Call it first.
- `check_claim` with `claim` `{text}`, `passage` `{text, locator}` quoted verbatim from the paper, and the `source` object.
- **Critical pitfall.** `check_claim` decides on word overlap. With a passage that states only the study question, it returned "supported" for a design claim (61 percent overlap), for an efficacy claim (80 percent) and for the efficacy claim's negation (71 percent). A "supported" status therefore proves only that the words match. Before you accept it: (1) the passage must be the results or conclusion sentence that states the finding, with its numbers; (2) you read the passage and confirm it says what the claim says, including direction; (3) the output shows the passage beside the claim. A claim whose passage is not a result is "not checked", whatever the status.
- The returned citation drops `doi`, `pmid` and authors. Build the citation from `get_record`.
- Do not use `verify.verify_text` with bare DOIs: it returns "unverifiable" (register C18). Do not send register facts to Verify (register C1).

## verify.build_record (counted)

- `clearances` with a named human in `cleared_by`. Only when an output leaves the conversation. It refuses a model or tool name.

## Call budget

A typical A1 run is 1 free call plus 6 to 10 counted calls per study checked: `get_record`, `classify_study`, `grade_evidence`, `qualify_source`, and one `check_claim` per claim. Check the claims the narrative will rely on, not every sentence of the paper.
