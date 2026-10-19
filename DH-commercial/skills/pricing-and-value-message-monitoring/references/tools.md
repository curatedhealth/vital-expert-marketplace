# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them (for example `commercial-dh_audit_claims`). Counted calls draw on the library key's monthly allowance; free calls do not.

Behavior below was observed in live calls on 19 October 2026. Trimmed outputs: `examples/live/`.

## verify.extract_claims (counted)

- `text` up to 20,000 characters; `granularity` "sentence".
- Splits by sentence, not by claim: "Doctor-recommended and CE-certified." came back as one claim holding two claims. Every sentence is marked `checkable: true`. Split compound sentences yourself before mapping rules.
- Live: a five-sentence ad returned c1 to c5 with offsets, kinds "numeric" or "factual", and empty `cited_refs`.

## commercial-dh.audit_claims (counted)

- `reference` (exact regulatory identifier, scheme identifier or normalized name), `claims` (up to 20), optional `intended_use` (audited as an extra claim, placed first).
- Returns per claim a label (`matches_record`, `exceeds_record`, `no_authorization_on_file`), `intended_purpose_from_record`, `authorization_on_file`, findings (F1 when therapeutic or diagnostic wording meets no authorization), an evidence maturity block from Diligence, and the regulatory blocks it read.
- Defect (proposed register item, see build notes): with `intended_purpose_from_record` "[GAP]", every claim is labeled `exceeds_record`. For `DEN160018` (reSET) all seven claims, including the caller's intended use and a sentence matching the record's own classification ("Computerized Behavioral Therapy Device For Substance Use Disorders"), were `exceeds_record`.
- Defect: for `somnio` the response set `authorization_on_file: false` and labeled all four claims `no_authorization_on_file`, while its own `search_devices` block returned somnio as EU MDR Class IIa, CE mark, "On the EU market" (Basic UDI-DI PP12257SOMNIO57), and its evidence block counted 3 authorizations. The lookup uses `get_authorization`, which matches identifiers, not names.
- Use: call it once with the exact identifier (K, DEN or P number, or Basic UDI-DI) to see which authorization record exists; read the inner `get_authorization` and `search_devices` blocks yourself. Do not report the labels or the evidence maturity score as findings. The claim judgment comes from `references/claim-rules.md` and the intended use the person states.

## regulatory-dh.get_authorization (counted)

- `reference`: K, DEN or P number, Basic UDI-DI, or "<SRN> <trade name>". Returns route, class, decision date, product code, regulation number, source URL. No intended-use text is stored (register P5).
- Live: `DEN160018` returned reSet, Pear Therapeutics, De Novo, class 2, `status: "DENG"` (FDA's raw code, register C3), decided 14 September 2017, product code PWE, regulation 882.5801.

## verify.qualify_source and verify.check_claim (counted)

- Working sequence for a passage behind a claim: `qualify_source` (DOI, PMID or URL), then `check_claim` with the claim, the verbatim passage (`text`, `locator`) and the returned source object.
- `qualify_source {url: "https://www.fda.gov/media/102575/download"}` returned tier "silver", publisher FDA, status current (an earlier attempt returned HTTP 503).
- Pitfall (register N3): decided on overlap. Same-direction claim: "supported" (69 percent). Negated claim on the same passage: "partial" (58 percent), not "contradicted". Accept "supported" only after reading the passage yourself.
- Pitfall (register C18): the citation returned by `check_claim` has `title` and `year` null; cite from `qualify_source`.
- Do not send register facts (listings, prices, authorizations) to Verify: register pages rate "no provenance" (register C1).

## verify.build_record (counted)

- Needs a named human in `cleared_by`; a model name is refused ("build_record refuses a record without a human cleared_by.name"). A record of an audit is not a clearance of the claims audited; say so in the record text.

## literature.search_literature (counted when it answers)

- HTTP 503 twice on 19 October 2026. Ask the person for the DOI or document behind a claim and qualify that.

## Not used here

- `watch_*` tools; change tracking of competitors' claims is not offered.
- `commercial-dh.get_pricing_corridor`: corridor evidence is the sibling skill's (and register N4 applies).
