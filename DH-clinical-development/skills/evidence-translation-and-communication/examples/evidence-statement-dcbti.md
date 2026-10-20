# Worked example: A1 evidence statement, short mode (live library data, 19 October 2026)

**Request (test; the clearer is a fictional name):** "What did the Schuffelen trial show for depression? One paragraph for our evidence file. Our medical director Dr. Lena Vogt will clear it."

**Calls made:** `literature.list_sources` (free); `literature.get_record {pmid: "40458292"}`; `literature.check_retraction {doi: "10.1155/da/2171041"}`; `verify.qualify_source {doi, question}`; `verify.check_claim` (statement below, results passage, full source object); `literature.grade_evidence {standard: "grade"}`; `literature.build_evidence_table`; `literature.build_citation`. Outputs: `examples/live/`.

---

**Answer.** In one pragmatic randomized trial of 140 adults with comorbid insomnia and depression, digital CBT-I added to care as usual reduced depressive symptoms compared with a waiting list at 12 and 24 weeks, as the authors report ("-3.34 and -2.83; ps <0.001; ds = 0.66-0.78"; primary outcome PHQ-9). Whether these figures are differences between arms is not stated in the passage read `[GAP]`: confirm in the full text before quoting them as such. Certainty not rated `[GAP]`.

| Outcome | Statement | Passage | Same direction? | Certainty | Source |
|---|---|---|---|---|---|
| Depressive symptoms (PHQ-9), 12 and 24 weeks | Reduced versus waiting list | Abstract, PMID 40458292: "Large treatment effects at 12- and 24 weeks showed significant reductions in depressive symptoms (-3.34 and -2.83; ps <0.001; ds = 0.66-0.78) in the dCBT-I group." | Yes: population, comparator and time points match | Not rated `[GAP]` | Schuffelen, Maurer, Gieselmann, Depression and Anxiety (2025), DOI 10.1155/da/2171041 |

**Checks.** Design: randomized, pragmatic (publication types and abstract). Registry: DRKS00030919, read from the abstract; the library's `trial_ids` field was empty. Retraction: none (Crossref checked). Verify returned "supported" (62 percent overlap) once the instrument name was left out of the claim; with "PHQ-9" in the claim it returned "partial", because the passage does not contain it. The statement names PHQ-9 only as the primary outcome, from the abstract's methods sentence, read by hand.

**What this does not say.** One trial, waiting-list comparator, abstract-level reading: results passage from the abstract, full text not read here. 120 of 140 participants were women. The authors' "robustness across diverse patient groups" is their conclusion, not a subgroup result, and is not repeated.

**Gaps.**
- Certainty: no rating from a person or body. The library's GRADE output, "high", is the starting level for a randomized design with every factor empty; it is not a rating (ES-90, ES-94).
- Comparator is a waiting list: no statement about active comparators can be made from this trial.
- A full search was not run; the library does not reach Cochrane or Embase. For a review, use DH-01.02.4.1.

**Record.** AI-assisted draft. Clears it: Dr. Lena Vogt (medical director, as named). The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

---

Word count of the answer above (without the calls list and the source column): checked by script (whitespace tokens), 350 words.
