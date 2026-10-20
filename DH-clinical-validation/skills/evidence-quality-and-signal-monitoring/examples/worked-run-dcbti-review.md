# Worked example: A1, A2 and B1 on a published review (live library data)

Run on 19 October 2026 against the VITAL Digital Health Library and the Europe PMC full text. The review: Hwang et al., "Systematic review and meta-analysis on fully automated digital cognitive behavioral therapy for insomnia", npj Digital Medicine 2025, doi 10.1038/s41746-025-01514-4, first published 12 March 2025. Trimmed outputs: `examples/live/`; passages with locators: `examples/live/passages_2026-10-19.json`; script output: `examples/review-check-output.txt`. The AMSTAR 2 ratings file is illustrative (an appraiser's ratings, written to show the script); it is not a rating of this review.

## The request

"We want to cite the 2025 npj Digital Medicine meta-analysis on fully automated dCBT-I in our EU JCA dossier, planned for 15 January 2027. Is it current, how good is it, and should we rely on it?"

## Calls made (7 counted)

1. `literature.get_record(doi="10.1038/s41746-025-01514-4")`: PMID 40075149, PMCID PMC11903857, abstract with results.
2. `verify.check_currency(doi="10.1038/s41746-025-01514-4")`: `current: true` (publication status in Crossref only).
3. `literature.find_related(record=<review>, direction="cited_by", limit=8)`: a 2026 RCT, a 2026 pilot trial, two 2026 reviews, off-topic items.
4. `literature.search_literature(query="digital cognitive behavioral therapy for insomnia systematic review meta-analysis", filters={"designs": ["systematic_review","meta_analysis"], "date_from": "2020-01-01"}, limit=6)`: newer reviews, including a 2026 review in older adults.
5. `literature.check_retraction(doi="10.1371/journal.pmed.1004510")`: none in Crossref (a 2025 RCT among the candidates).
6. `literature.grade_evidence(records=[...])`: the review CEBM level 1, provisional; not used as a quality rating.
7. `verify.check_currency(doi="10.1016/S0140-6736(97)11096-0")`: control case, retracted.

Full text read from Europe PMC (not a library call): search to 31 March 2024; PROSPERO CRD42024526617; two independent screeners and extractors; RoB 2 (3 low, 19 some concerns, 7 high); random effects, I-squared 91% for insomnia severity; Egger's test p = 0.19; no GRADE or certainty statement, grey literature or excluded-studies list found by text search.

## The answer (short mode)

**Answer.** The review cannot serve as the dossier's literature search: its search ended 31 March 2024, and a JCA dossier needs its own information retrieval with a cut-off at most 3 months before submission, so on or after 15 October 2026 for a 15 January 2027 submission (ES-156, ES-168). It can still inform your own search as a seed. The library found 2025 and 2026 trials and reviews after its search date, not yet screened. Your appraisers have not rated it; the passages for the seven AMSTAR 2 critical domains are below. Next decision for you: rerun under the JCA rules, using this review as a seed, or not.

**Rule checks (`review_check.py`).**

| Body | Rule | Result |
|---|---|---|
| Cochrane, at its own publication | Search within 12 months before publication, preferably six (ES-52) | Within 12, outside six |
| EU JCA, your 15 January 2027 submission | Cut-off at most 3 months before (ES-156) | Outside |

**Publication status.** Not retracted, corrected, superseded or withdrawn in Crossref on 19 October 2026. This is not search currency.

**Candidate new studies after 31 March 2024 (not screened).** Knutzen 2026 preliminary RCT (10.1016/j.invent.2026.101007); Chen 2025 RCT (10.1371/journal.pmed.1004510); Schuffelen 2025 RCT (10.1159/000547436); Sleep Ninja 2026 pilot (non-randomized, draft label). Reviews: older adults 2026; wearable digital therapeutics 2026.

**AMSTAR 2 critical domains: passages (ratings are your appraisers').**

| Item | Passage found |
|---|---|
| 2 Protocol registered | PROSPERO CRD42024526617 (Methods) |
| 4 Search | PubMed, CENTRAL, Embase, PsycINFO to 31 March 2024; no grey literature found |
| 7 Exclusions justified | No list with reasons found |
| 9 Risk of bias | RoB 2; 3 low, 19 some concerns, 7 high |
| 11 Meta-analysis | Random effects; I-squared 91% |
| 13 Bias in interpretation | No certainty assessment found |
| 15 Publication bias | Funnel plot and Egger's test |

**Record.** AI-assisted. Clears it: owner not named. The record is built with verify.build_record once that named person clears it; until then, uncleared draft. Wording for the HTA body stops for the owner the person names (owner not named).

Full version available: adds the B1 options table and the AI-use table for a JCA rerun.

## Script demonstration (illustrative ratings)

With an illustrative ratings file (item 7 "No", item 10 "No", item 4 "Partial yes"), `review_check.py amstar2` returns: one critical flaw (item 7), one non-critical weakness (item 10), item 4 left to the appraisers, overall "Low: one critical flaw (ES-107)", and no score (ES-108).

## What the run showed about the tools

- `verify.check_currency` "current: true" is publication status only; the review's search ended more than 30 months before this run.
- `find_related` returns no total, empty authors and off-topic items; it is a signal source, not a search.
- The library's CEBM level 1 for the review says nothing about how well it was done (register N8 for the label basis).
