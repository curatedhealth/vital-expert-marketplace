# Worked example: A2 and B1 on live library data (digital CBT for insomnia)

Run on 19 October 2026 against the VITAL Digital Health Library. The question is a realistic one for a digital therapeutic: app-based or digital CBT for insomnia (dCBT-I) versus health education, sham or waitlist, in people with insomnia disorder; outcomes insomnia remission and new-onset depression. The review is a Cochrane-style review (reviewer rule: Cochrane). Trimmed live outputs: `examples/live/`. The screening log and evidence table are illustrative files built around the live records and labeled as such; their counts are not a real review's.

## The request

"We have screened our dCBT-I search. Here is our screening log and our draft evidence table. Check the flow and the table, tell us what is wrong, and set up the certainty assessment."

## Calls made (13 counted for this example; 22 counted in the whole build)

1. `literature.list_sources()` (free): CENTRAL, Embase, PROSPERO not queried by the library.
2. `literature.search_literature(query="digital cognitive behavioral therapy for insomnia app randomized controlled trial", limit=8)`: 29 merged records; 3 of 8 shown were off topic.
3. `literature.get_record(pmcid="PMC13671329")`: DOI and PMID added; `record_id` differs from the search record.
4. `literature.deduplicate(records=[4 records], identifiers=["39836656", "10.1371/journal.pmed.1004510"])`: 6 inputs to 4; secondary analysis not linked to its parent trial.
5. to 7. `literature.classify_study` on three records: the conference abstract labeled `meta_analysis` "by title"; the secondary analysis `other`; the preliminary RCT `rct` from the title word.
8. `literature.grade_evidence(records=[4], question_type="treatment")`: conference abstract CEBM level 1 (not provisional); RCT level 2.
9. `literature.find_trial(record=<Chen 2025>)`: NCT04069247.
10. `literature.check_retraction(doi="10.1371/journal.pmed.1004510")`: none (Crossref).
11. `literature.build_evidence_table(...)`: results sentence put in the population field; duplicate kept.
12. `verify.qualify_source(doi="10.1371/journal.pmed.1004510")`: gold, current.
13. `verify.check_claim(...)` with the exact results sentence: "unsupported" (29% overlap) for a correct same-direction claim.

Results passage read from Europe PMC (abstract of PMID 39836656): `examples/live/passages_2026-10-19.json`.

## Script runs

- `python3 scripts/prisma_flow.py examples/screening-log-illustrative.csv --rule cochrane` (output: `examples/prisma-flow-output.txt`): 27 records identified; 4 duplicates, 2 removed by automation, 1 removed for another reason; 20 screened; 9 excluded; 11 reports sought; 1 not retrieved; 10 assessed; 4 excluded with reasons; 4 studies in 6 reports. All seven reconciliation lines hold.
- `python3 scripts/check_evidence_table.py examples/evidence-table-illustrative.csv` (output: `examples/evidence-table-check-output.txt`): one result counted twice (Chen 2025, new-onset MDD at 12 months, entered once by DOI and once by PMID); two designs resting on library labels; risk-of-bias judgments missing on every row; two rows without effect data.

## The answer (short mode)

**Answer.** Four studies in six reports pass full text. The flow reconciles. The evidence table is not ready: one result is entered twice, two designs rest on library labels, and no risk-of-bias judgment is recorded yet, so certainty cannot be set up. Next decision for your reviewers: merge the duplicate Chen rows and confirm the designs of Knutzen 2026 and the Lee 2025 abstract from the papers.

**Flow (PRISMA 2020, ES-20 [PAPER] doi 10.1136/bmj.n160).** Identified 27; removed before screening 7 (duplicates 4, automation 2, other 1; report the automation count separately, ES-21); screened 20; excluded 9; sought 11; not retrieved 1; assessed 10; excluded 4 with reasons; included 4 studies, 6 reports.

**Evidence table problems (script).**

| Problem | Rows | Rule |
|---|---|---|
| Same result twice: Chen 2025, new-onset MDD, 12 months | 2, 3 | ES-56 |
| Design from library label only | Knutzen 2026; Lee 2025 abstract | register N8 |
| Risk-of-bias judgment missing | all | ES-10 |
| Conference abstract in a primary-study table | Lee 2025 | note |

**Design check.** The library labeled the Lee 2025 conference abstract `meta_analysis` "by title" and gave it CEBM level 1, above the RCT. The paper is a conference abstract of a pooled analysis of two trials; your log excludes it at full text (record O03), yet it is in the evidence table: the reviewers decide whether to remove it or record why it stays. The RESiLIENT insomnia paper is a secondary analysis of a randomized trial (title), labeled `other`; it is grouped under study S-RESILIENT with the main report.

**Certainty set-up (GRADE, ES-89 to ES-96).** Not yet possible: risk of bias is the first domain and has no judgments. The library's GRADE output rated single records "high" with every factor empty; it is not an outcome's certainty.

**Finding checked.** "App-based CBT-I lowered new-onset MDD over 12 months versus health education (HR 0.58)": the passage (abstract, Methods and findings) states it in the same direction; accepted on reading. Verify returned "unsupported" on word overlap (register N3).

**Record.** AI-assisted (screening suggestions in 16 log rows; automation removed 2 records). Clears it: owner not named. The record is built with verify.build_record once that named person clears it; until then, uncleared draft.

Full version available: adds the risk-of-bias layout per result with passages, the Summary of Findings frame and the AI-use table.

## What the run showed about the tools

- Design labels decided by title words lifted a conference abstract to CEBM level 1 (register N8).
- `record_id` changes between search and get_record; key logs on DOI or PMID.
- `build_evidence_table` misplaced a results sentence and did not catch a duplicate study.
- `check_claim` rejected a correct same-direction claim and did not mark the reversed claim "contradicted" (register N3).
