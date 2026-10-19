# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names are the library's; your assistant may prefix them (for example `commercial-dh_audit_claims`). Counted calls draw on the library key's monthly allowance. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`.

This is a method pack: the knowledge sits in `references/`. The library adds a claim label check against the authorization record, literature search and Verify for any published figure the program material uses, a ranking calculator for options the person scored, and the record. Several calls on 19 October 2026 first returned 503 or 502 ("Nothing was counted"); a retry worked. Retry once, then say the library did not answer.

## commercial-dh.audit_claims (counted; A1, optional)

- Arguments: `reference` (exact regulatory identifier, scheme identifier or normalized name), `claims` (up to 20 strings), optional `intended_use` (audited as a claim).
- Returns per claim a label (`matches_record`, `exceeds_record`, `no_authorization_on_file`), findings (F1 for therapeutic or diagnostic wording with no authorization), an evidence-maturity block and the regulatory blocks it read.
- Pitfalls seen:
  - By product name it reported no authorization while its own search block in the same response found one: `reference: "somnio"` gave `authorization_on_file: false` beside an EU MDR Class IIa record "On the EU market"; `reference: "Somryst"` gave `false` beside 510(k) K191716 "Substantially Equivalent". Pass the exact identifier (for example `K191716`).
  - With `K191716` the authorization was found, but `intended_purpose_from_record` was `[GAP]`, so every claim, including a neutral community statement, was labeled `exceeds_record` and no F1 was raised for "Clinically proven to cure insomnia". A label without an intended purpose on record cannot be read as a finding.
  - Program offers ("Free smartphone loan for patients who cannot afford a device") are labeled like product claims. The tool does not see inducement questions; those are B1.
  - `intended_use` is added to the claim list and labeled with them.
- Use: optional prompt list for the owner's review in A1 Step 5. Report labels only with these limits stated. Never present a label as clearance or as a regulatory opinion (the tool says "Preparation for expert review, not a regulatory opinion").

## literature.search_literature (counted; A1 or A2, optional)

- Arguments: `query`, optional `limit`, `filters` (`date_from`, `designs`, ...).
- Observed: "patient organisation industry funding disclosure transparency" returned a 2020 BMJ systematic review with meta-analysis (doi 10.1136/bmj.l6925) and related studies, plus one off-topic AI ethics review. `trial_ids` empty on every record; design labels carry low confidence on several rows (0.3). Read the paper before using any figure.

## verify.qualify_source then verify.check_claim (counted)

- `qualify_source {doi, question}` rated doi 10.1136/bmj.l6925 tier "gold", status current.
- `check_claim` with `source` given as `{doi, source_id}` only returned 502 twice; passing the object returned by `qualify_source` as `source` worked.
- Direction is not judged (register N3): from the passage "27% ... disclosed this information on their websites" it returned "supported" both for "about a quarter (27%) disclosed it" (83 percent overlap) and for "Most ... disclosed it" (89 percent overlap). Accept a literature claim only when you have read the passage and it states the claim in the same direction.
- The returned citation had DOI, PMID, authors and year empty and Harvard "BMJ (n.d.)" (register C18). Build the citation from the paper.

## analytics.mcda (counted; B1)

- Arguments: `alternatives` (id and scores, 0 to 4) and `criteria_weights` (the person's, summing to 1).
- Value = sum of weight times score / 4, times 100. Every criterion is treated as higher-is-better (`negative_criteria` returned empty; no input to set it). Name criteria so that higher is better ("inducement exposure avoided", not "inducement exposure").
- No robustness view; run `scripts/mcda_swap.py` on the saved call (it checks the connector's values and prints swap weights).

## agent-pack.list_experts and agent-pack.download_agent (free listing, counted download)

- `list_experts {query: "advocacy"}` returned no expert. `{query: "marketing"}` returned the Digital Marketing Manager (`digital-marketing-manager`), the worker for this skill, plus a department-head variant and a partnerships manager.
- The download (71,217 characters, 53 bound skills) carries the six old program tasks and the stop rules used in `governance.md`. Its mandate says it "Does not structure partner deals"; partnership terms in A2 are therefore drafts for the person's owner.

## verify.build_record (counted)

- With `cleared_by.name` "Claude" it refused: "build_record refuses a record without a human cleared_by.name". Call it only when the person names who clears an output that leaves the conversation.

## Not used

- `analytics.rice`: measured for the monitoring skill; RICE fits program changes, not support options.
- `watch_*` tools.
