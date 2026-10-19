# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `regulatory-dh_retrieve_guidance`). Counted calls draw on the library key's monthly allowance; `list_jurisdictions` is free. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`.

## regulatory-dh.list_jurisdictions (free)

- No arguments. Returns per jurisdiction: authorization and safety-event counts, last load, sources, scope.
- 19 October 2026: US 1,226 authorizations (last load 19 October 2026); EU 3,142 with the decision date empty on all 3,142; UK no authorizations (MHRA PARD not loaded), 10 safety alerts; CH nothing loaded; TW 32; CA 227. JP, CN, AU, KR and others are closed gaps.
- Use it once per run to say what the library can and cannot show.

## regulatory-dh.retrieve_guidance (counted)

- Required `query`; optional `namespace` (guidance or ontology-navigation), `limit` 1 to 25.
- Lexical match on stored chunks, not a semantic search (the tool says so).
- Measured: "content of premarket submissions for device software functions documentation level" and "MDR Annex II technical documentation clinical evaluation report software" returned no passage. "eSTAR" returned NICE PMG36 medicines passages and an MHRA clinical-trials passage with no source URL. "clinical evaluation" returned five EMA vaccine and medicines passages. "Pre-Submission" returned FDA accessory and CADe passages with `source_url` "[GAP]", one citing the superseded Pre-Sub guidance address, and an Australian PBS medicines passage. Every passage had `retrieved_at` null.
- Rule: call it once with a short query in the source's words; use a passage only if it is device guidance, carries a source URL, and agrees with the reference rows. Otherwise say the store holds no passage for the question and work from `references/`. Never cite a passage without a URL.

## regulatory-dh.generate_report (counted)

- `reference` (K, DEN or P number, or a trade name) or `product_code`; `template` memo, identity, regulatory, precedents or safety; optional `since` (YYYY-MM-DD) for a Changes section on a memo.
- Measured with `reference=K191716, template=regulatory`: device identity, pathway, class, decision date, the predicate chain from the 510(k) summary (K191716 named DEN160018; the De Novo names none), prior decisions in the product code, gaps.
- Pitfall: `market_status.authorized.EU` came back `false` for that device although EUDAMED rows in the library carry no decision dates and the tool's own note says a missing record is not evidence of no authorization. Report EU status as "not found in the library's EUDAMED copy", never "not authorized".
- Use in B1 only to describe a predicate or comparable the person named, by what its record states.

## literature.search_literature (counted)

- Required `query`; optional `filters`, `limit`, `sources`.
- Measured: "digital cognitive behavioral therapy for insomnia randomized controlled trial app", limit 5: 18 merged records from PubMed, Europe PMC, OpenAlex, Crossref and bioRxiv; most records came back with an empty `excerpt`; one medRxiv preprint; one conference abstract labeled `meta_analysis`.
- It is a candidate finder for the person's systematic review, not the review itself.

## literature.get_record (counted)

- One of `doi`, `pmid`, `pmcid`, `openalex_id`. Measured with PMID 39836656: merged identifiers and an abstract excerpt that ended after the methods sentence, before any result. `trial_ids` was empty for this RCT (register N8). Semantic Scholar timed out (warning shown).
- To check a finding you need the results passage from the paper itself; ask the person for it or read the open-access text they point you to.

## literature.classify_study (counted)

- Required `record`. Measured: a conference abstract titled "pooled analysis of two randomized ... trials" came back `meta_analysis`, confidence 0.78, decided by title text. Check `publication_type_raw` (here "conference-abstract") before using the label.

## literature.grade_evidence (counted)

- `record` or `records`, `question_type`, `standard` (cebm2011 default, or grade, always draft).
- Measured: the RCT got CEBM level 2 and the conference abstract level 1 ("meta_analysis of randomized trials"). The level follows the design label only (register N8). Present levels as a draft for the person's appraisal, with the label's basis.

## verify.qualify_source then verify.check_claim (counted)

- `qualify_source(doi=...)` rated the PLOS Medicine RCT "gold", status current.
- `check_claim(claim, passage{text, locator}, source)` returned "supported" ("Strong overlap (86%) with context") for "App-based CBT-I reduced the onset of major depressive disorder" from a passage that stated only the trial's aim and design. The returned citation had no title, authors or year ("Unknown (n.d.)").
- Rule: pass only a results passage you have read, quoted exactly, with its locator; accept "supported" only if that passage states the finding in the same direction as the claim. Otherwise report "not checked: no results passage" (register N3).
- `verify.verify_text` with bare DOIs returns unverifiable (register C18); do not use it for literature. Register pages are rated "no provenance" (register C1); cite register facts to the register page instead.

## verify.build_record (counted)

- Needs a named human in `cleared_by`. Call it only when an output leaves the conversation and the person names who clears it.

## Not used here

- `watch_register` and other watch tools: described only.
- `classify_product`, `find_predicates`, `compare_authorizations`: classification and predicate strategy belong to DH-03.03.3; this skill only records what the person's regulatory owner decided.
