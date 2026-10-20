# Worked run: A1 claim map and B1 limits for an ADHD game therapy, on live library data

Run on 20 October 2026. The request: "Our game-based ADHD therapy, FocusPlay, is modeled on EndeavorRx and rests on the STARS-ADHD trial. Here is our store copy. Map our claims to the evidence and tell us where we go too far." FocusPlay and its copy are illustrative, written for this example; EndeavorRx, STARS-ADHD and STARS-Adjunct are real and were read live. Calls and outputs: `examples/live/connector_calls_2026-10-20.json`; abstracts in `examples/live/pubmed_abstracts_2026-10-20.txt`.

Calls in order: `verify.extract_claims` (store copy), `literature.search_literature`, `literature.find_trial`, `literature.classify_study`, `literature.grade_evidence`, `regulatory-dh.get_authorization {reference: "DEN200026"}`, `verify.qualify_source` (STARS-ADHD DOI; the De Novo PDF URL), `verify.check_claim` (four claims against one passage).

---

## Short mode output (as handed to the person)

**Answer.** Five sentences in your copy. One is sourced, two are narrower in the source than in your copy, one is [GAP], and one is refused by the authorized label you cite. Proposed claim the product will not make: anything about hyperactivity. You decide; owner not named.

| Claim (verbatim) | Status | Passage (locator) | Source | Rows |
|---|---|---|---|---|
| "Play 25 minutes a day, 5 days a week." | Sourced (dose) | "25 min per day, 5 days per week for 4 weeks" (abstract, Background) | DOI 10.1016/s2589-7500(20)30017-0; NCT02674633 | TM142 |
| "FocusPlay is a game-based therapy for children with ADHD." | Narrower in source | "aged 8-12 years, without disorder-related medications" (abstract, Methods) | same | TM144 |
| "Clinically proven to improve attention in 4 weeks." | Narrower in source | "might be used to improve objectively measured inattention" (abstract, Interpretation) | same | ES-201 |
| "Not a replacement for medication." | [GAP] | No passage read | none | |
| "Helps kids with hyperactivity and impulsivity." | Refused | "may not display benefits in typical behavioral symptoms, such as hyperactivity" (Indications for use) | DEN200026 | TM144 |

**Words that differ.** Your copy drops the source's hedge ("might be used to") and its measure ("objectively measured inattention"), and widens "aged 8-12, without medications" to "children". Verify returned "supported" both for the source sentence and for its negation, and for your unhedged verb (N3), so these were read by hand.

**Certainty.** Not rated [GAP]. The library labels STARS-ADHD CEBM level 2 from its design tag (N8); that is not certainty. STARS-Adjunct (DOI 10.1038/s41746-021-00429-0) is open-label in children on stimulants; the library could not classify it.

**Rules that apply.** Your product is not EndeavorRx: its label does not transfer. If FocusPlay is a US device, claims beyond its own labeling are tested on indication, population, limitations and regimen (PC-US-23, nonbinding guidance). Device status: owner not named [GAP].

**Limits (proposed, B1).** Hyperactivity: stated as a limitation (TM144); messages about it stay off. Ages outside 8 to 12 and medicated children: not studied in the pivotal trial; an open-label study exists. Standalone use: the cited label is adjunctive (TM123). Who may reopen each: owner not named.

**Not checked.** The De Novo summary: Verify rated it inadmissible (C1); quoted from TM144.

**Record.** Evidence claim map draft. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

**Calls made.** Listed above.

---

Word count of the short mode output above, without the table's source column and the calls list: 367 (counted by script on 20 October 2026).
