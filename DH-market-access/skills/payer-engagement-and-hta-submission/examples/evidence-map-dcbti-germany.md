# Worked example: A1 evidence requirement map, digital CBT-I, Germany

Live library calls on 19 October 2026. Raw outputs saved in `examples/live/`. The study is a real published trial used as the person's named study for this example; nothing here says which product it tested.

**Request:** "Our digital CBT-I app is for adults with insomnia and depression, class I. Our pragmatic RCT is DOI 10.1155/da/2171041. Is it enough for a permanent DiGA listing, and can we claim it improves depressive symptoms?"

**Calls made**

1. `market-access-dh.list_schemes` (free): DE_DIGA 82 listings, last load 15 October 2026, posture partial. Saved: `live/list_schemes_2026-10-19.json`.
2. `literature.get_record` `{doi: "10.1155/da/2171041"}`: PMID 40458292, *Depression and Anxiety* 2025, publication types "Randomized Controlled Trial", "Pragmatic Clinical Trial", retraction status none, `trial_ids` empty. The excerpt states background and design, no result.
3. `literature.classify_study` on that record: rct, confidence 0.98, decided by publication type and the title word "randomized".
4. `literature.grade_evidence` `{question_type: "treatment"}`: CEBM 2011 level 2, rule "rct for a treatment question -> level 2".
5. `verify.qualify_source` `{doi: "10.1155/da/2171041"}`: tier gold, status current.
6. `verify.check_claim` three times with the same abstract passage (the design sentence): a design claim, the efficacy claim, and the efficacy claim's negation. All three came back "supported" (overlap 61, 80 and 71 percent). Saved: `live/literature_verify_2026-10-19.json`.
7. `market-access-dh.find_scheme_precedents` `{scheme: "DE_DIGA", indication: "F51", limit: 10}`: somnio (00508), HelloBetter Schlafen (01772), somnovia (02097), all permanent. Saved: `live/de_diga_F51_2026-10-19.json`.
8. `scripts/diga_study_rules.py --record live/literature_verify_2026-10-19.json` gave the rule table below (no facts file yet).

## Answer (short mode)

**Not yet shown on the sourced rules, and the depression claim is not checked.** The trial is a randomized comparison of digital CBT-I added to care as usual against a waiting group, which fits the DiGA requirement for a comparative study against non-use (`DE10`, `DE11`). The library record cannot show the other study rules, so six of them stay `[GAP]` until you show the paper sections. Rules read 19 October 2026 (DiGAV as amended 27 January 2026).

| Rule | Status | What would close it |
|---|---|---|
| Comparative study, use beats non-use (`DE10`) | Design shown (RCT); result not shown | Results section |
| Comparator reflects real care (`DE11`) | `[GAP]`; the excerpt names a waiting group and care as usual | Methods section |
| Run in Germany or transferable (`DE12`, `DE13`) | `[GAP]` | Methods: sites |
| Registered in an ICTRP registry (`DE14`) | `[GAP]`; the record carries no trial id | Registry entry |
| Published within 12 months of completion (`DE14`) | `[GAP]`; published 2025 | Completion date |
| Use duration and frequency collected (`DE15`) | `[GAP]` | Methods; ask the accountable owner whether the 2026 rule applies to this study |
| Patient group as ICD-10-GM codes (`DE9`) | `[GAP]` | Your intended codes (for example F51, F32/F33) |

**Effect type is your decision.** Depressive symptoms would be a medical-benefit claim (health status, `DE6`). Class I also allows a structure and process claim (`DE7`). Either way it needs a results passage.

**The claim "improves depressive symptoms" is not checked.** The record holds only the study question. Verify returned "supported" for the claim and for its opposite from that same sentence, because it matches words, not findings. Send the results sentence with its numbers and the check will be repeated and read.

**Design grade.** RCT, CEBM level 2 from design only. It does not judge comparator, bias or setting, and it is not BfArM's view.

**Comparables.** Three insomnia DiGA are permanently listed: somnio (since 22 October 2020), HelloBetter Schlafen (since 18 December 2022), somnovia (since 28 October 2024). Library copy retrieved 15 October 2026. This shows the route exists for the indication, not that your study would qualify. The evidence behind each listing is on its directory page, not in the library.

**Record:** Uncleared draft, AI-assisted. Effect type, comparator and the claim wording are decisions for the accountable owner (owner not named). Next step offered: submission readiness for a DiGA permanent application.

## What this example shows

- The literature record answers design and identity, not the DiGA study rules. A rule the record cannot answer is `[GAP]`, never met.
- Verify's "supported" must be read: the same passage "supported" a claim and its negation. The skill accepts a claim only with a results passage that states the finding.
- Comparables in the register's codes (`F51`) work; an English term may not.
