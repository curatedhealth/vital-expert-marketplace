# Tools: calls this skill uses, as measured on 19 October 2026

Every call below was made live on the VITAL Digital Health Library connector during the build; trimmed outputs are in `examples/live/connector_calls_2026-10-19.json`. Counted calls in the build: 13 (search 1, find_trial 4, classify_study 1, qualify_source 1, check_claim 2, retrieve_guidance 1, list_experts 3); `list_jobs` and `literature.list_sources` are free.

## literature.search_literature

- **Call:** `{query: "digital cognitive behavioral therapy insomnia randomized controlled trial app", limit: 6, filters: {designs: ["rct"]}}`.
- **Returns:** merged records (23 merged, 5 shown) from PubMed, Europe PMC, OpenAlex, Crossref and bioRxiv, each with DOI, PMID, PMCID where known, `design`, `design_confidence`, `retraction_status`, `trial_ids`, `excerpt`, per-source provenance and retrieval time.
- **Pitfalls:**
  - `trial_ids` was empty on every record, including RCTs that are registered (register item N8). Use `find_trial` to get the registration.
  - `excerpt` was empty on all five records; a results or methods passage for Verify must come from the full text (Europe PMC) or the person.
  - A conference abstract (`openalex:conference-abstract`) was labeled `rct` 0.78. Read the record type before treating it as a trial report (N8).
  - Off-topic records appear (a 2015 "single-shot" acute insomnia trial; a depression app trial). The model screens by the person's PICO; it never counts search hits as comparables.
  - bioRxiv has no keyword search ("no preprint in the last 30 days matched").

## literature.find_trial

- **Call A:** `{record: {doi, pmid, pmcid, title}}` for the paper. Returned NCT04069247 with `status` COMPLETED, `phases` ["NA"], `sponsor`, `match_via` "pubmed_secondary_id", and a warning that one other registration cites the paper as background only.
- **Call B:** `{nct_id: "NCT04069247"}`. Returned the same registration and the linked publication.
- **Call C:** a JAMA Network Open dCBT-I trial returned NCT04779372.
- **Call D:** a Nature Medicine app trial (RESiLIENT) returned "no linked registration found".
- **What it does not return:** registered outcomes, enrollment, masking, registration date, start or completion dates. Registry content therefore comes from the registry record itself (below). Absence of a link is not evidence the trial is unregistered: the connector reads ClinicalTrials.gov only, and other WHO primary registers are not reached (CV134).

## ClinicalTrials.gov record (direct read, outside the connector)

- **Read:** `https://clinicaltrials.gov/api/v2/studies/<NCT id>` returned the full record (status, dates, design, masking, enrollment, primary and secondary outcomes with time frames). Saved as `examples/live/nct04069247.json` and `nct04779372.json`.
- **Not readable:** the record history endpoint returned 403, so changes over time cannot be read by script; read the "History of Changes" on the registry page.
- **Use:** `scripts/registry_check.py --registry FILE.json --facts FACTS.json --as-of YYYY-MM-DD` sets the record beside the person's protocol or paper facts and computes the registration, results and update clocks (`examples/registry_check_nct04069247.md`). Registry text is the sponsor's own wording; quote it, do not correct it.
- **Measured difference:** NCT04069247 registers "Number of Participants With Major Depressive Disorder" ("Up to 12-month follow-up"); its paper (PMC11750088, section 2.4) states "time to onset of MDD". The library returns neither text; only the registry and the paper show it.

## literature.classify_study

- **Call:** `{record: {doi, publication_type_raw: ["Journal Article", "Randomized Controlled Trial", ...]}}` returned `rct` 0.98, decided by the publication type and the word "randomized" in the title. It reads labels, not the methods (N8). Confirm design from the paper.

## verify.qualify_source then verify.check_claim

- **qualify_source:** `{doi: "10.1371/journal.pmed.1004510", question: "..."}` returned tier gold, status current, score 61, retraction status none.
- **check_claim:** pass `claim {text}`, `passage {text, locator}` quoted from the paper, and the full object `qualify_source` returned (register C18: a bare DOI fails). The correct claim about the primary outcome returned "supported" (61 percent overlap). A claim stating the opposite metric ("number of participants ... not time to onset") from the same passage also returned "supported" (36 percent overlap). Verify decides on word overlap (register N3). Accept support only when you have read the passage and it says the same thing, in the same direction.
- **Citation returned:** identifiers null, authors empty, year null (C18). Build the citation from `qualify_source` or the record instead.

## regulatory-dh.retrieve_guidance

- **Call:** `{query: "digital health technologies remote data acquisition clinical investigations verification validation endpoint", limit: 5}` returned no passages and "[GAP] no passage retrieved in this namespace". The connector's guidance store does not hold the FDA DHT, DCT or ICH texts; this skill's references do.

## agent-pack.list_experts

- `{query: "clinical"}` lists `clinical-informatics-lead` (the bound worker; remit: "specifies how a digital health product reads and writes the care record, where decision support may sit, and how remote and decentralized capture stays integer. Does not configure a live EHR or sign a clinical evaluation.") and `clinical-validation-director` (remit: "endpoint and COA strategy, protocol robustness for software-generated evidence ..."). `{query: "statist"}` returned none: no statistics expert exists in the catalogue, so statistical questions in a review always go to the owner the person names for statistics, or owner not named.

## verify.build_record

Not called in this build. The tool refuses a record whose `cleared_by.name` is missing or is a tool or model name (tool description). Call it only with the name of the person who clears the output.

## Catalogue jobs

`list_jobs` (19 October 2026): no job checks a protocol or a registration. `evidence-table` (available) uses `find_trial` but grades studies; it does not compare registry and protocol. Every task in this skill names "none" as its catalogue job.
