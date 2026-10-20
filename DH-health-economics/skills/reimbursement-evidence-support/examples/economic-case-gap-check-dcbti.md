# Worked example: A2 economic case gap check, digital CBT-I, NICE and HAS

Live library calls on 19 October 2026. Trimmed outputs in `examples/live/`. The study is a real published trial-based economic evaluation, used as the person's named evidence for this example; nothing here says which product it tested or whether a body would accept it.

**Request:** "Our fully automated digital CBT-I app's economic evidence is the 2-year trial-based analysis in DOI 10.1016/j.lanepe.2026.101691. We have no budget impact analysis yet. Is it enough for NICE HealthTech and for HAS, and can we say the app significantly lowers costs? Test it at 20,000 and 30,000 per QALY."

**Calls made**

1. `literature.search_literature` (economic evaluations of dCBT-I, limit 6): the study came first, labeled `rct` 0.78; a health-economic evaluation alongside an RCT (DOI 10.2196/25609) was labeled `rct` 0.98 with an empty excerpt. Saved: `live/literature_verify_vethe_2026-10-19.json`.
2. `literature.get_record {doi: "10.1016/j.lanepe.2026.101691"}`: PMID 42164344, PMCID PMC13186012, 2026, retraction none, `trial_ids` empty; the excerpt stops before the results.
3. `literature.classify_study`: `rct` 0.78, decided by "title:randomized".
4. `literature.grade_evidence {question_type: "treatment"}`: CEBM level 2 from design only.
5. `verify.check_currency {doi}`: not retracted, corrected, superseded or withdrawn.
6. `verify.qualify_source {doi}`: tier gold, current, score 72.
7. `verify.check_claim` three times on the Findings sentence of the abstract (read at Europe PMC): the accurate claim "partial" (44 percent overlap); "dCBT-I significantly reduces societal costs" "partial" (40 percent); an overt reversal "unsupported" (29 percent).
8. Open-access full text read, because `get_record` returned PMCID PMC13186012: Europe PMC `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13186012/fullTextXML`, Methods (Outcomes; Cost-effectiveness analysis), read 19 October 2026. It settles fields the abstract leaves open: "Short Form-6D (SF-6D; derived from the SF-12) with UK general population utility weights applied" (Methods, Outcomes); "No discounting was performed since costs and outcomes, reported at 6-months and 2-years, could not be separated by year" (Methods, Cost-effectiveness analysis); "We supplemented the base case analysis by estimating ICERs from patient, employer, and healthcare perspectives" (same section, Appendix B pp 8).
9. `scripts/model_check.py --spec live/model_spec_vethe_2026-10-19.json --body NICE_ROUTINE --body ESF --body HAS --body CHEERS --thresholds 20000 30000`. Output: `live/model_check_vethe_output.txt`. The model description was written from the abstract and the full text; a field both leave silent is null.

## Answer (short mode)

**On the sourced rules, the economic case is not yet shown for NICE or HAS, and "significantly lowers costs" is not supported.** The study is a cost-utility analysis, which both bodies use (`HE-073`, `HE-104`). For NICE, its societal cost perspective is a departure from the NHS and PSS reference case (`HE-037`), and there is no budget impact analysis for ESF standard 17 (`HE-087`). The full text adds three departures: SF-6D, not EQ-5D (`HE-045`); no discounting; the comparator is online patient education. Rules read 19 October 2026.

| Item | NICE | HAS | Row |
|---|---|---|---|
| Evaluation type | Shown (cost-utility) | Shown | `HE-073`, `HE-104` |
| Perspective | Departure: societal base case, not NHS and PSS; healthcare-perspective scenario in Appendix B | `[GAP]`: societal stated; whether it is the collective perspective is for the owner to confirm | `HE-037`, `HE-103` |
| Utilities and value set | Departure: SF-6D with UK weights, a mapping departure whatever the weights | Departure: French 5L expected | `HE-045`, `HE-058`, `HE-106` |
| Discounting | Departure: none (3.5% in the rule) | Departure: none (2.5% in the rule) | `HE-047`, `HE-105` |
| Comparator | `[GAP]`: online patient education; whether it is current NHS care is for the owner to confirm (no NICE comparator row in the references) | | |
| Follow-up | 587 of 1,720 (34.1%) at final follow-up; authors: "long-term certainty is limited by attrition" (abstract) | | |
| Results | ICER shown; net health benefit not shown | Frontier not shown | `HE-041`, `HE-107` |
| BIA (ESF 17) | Not shown | | `HE-087` |
| UK costs (ESF 17) | Not shown: 2019 euros, Norwegian setting | | `HE-089` |

**The cost claim.** The paper reports "-€278 [95% CI: -1413 to 858] lower costs and 0.025 QALYs gained [95% CI: 0.010 to 0.041]" (abstract, Findings). The cost interval includes zero, so "significantly lowers costs" is not checked. Verify rated it "partial", the same as the accurate claim, because it matches words. A claim you can source: lower mean cost and 0.025 QALYs gained over 2 years against online patient education, with the intervals.

**Arithmetic on your thresholds (hypotheses).** The paper's own ratio is -€10,973 per QALY with a 94% probability of cost-effectiveness at €0 (the authors' conclusion, not this check). At your 20,000 and 30,000, net monetary benefit is €778 and €1,028 per patient on the point estimates, in 2019 euros. NICE's written ranges are in pounds and conflict: £20,000 to £30,000 in PMG48 (`HE-074`), £25,000 to £35,000 in PMG36 (`HE-050`, `HE-051`). NICE decides.

**Design grade.** RCT, CEBM level 2 from design only. Registration: NCT02558647 (abstract, Methods); the library record's `trial_ids` is empty.

**Record:** Calls of 19 October 2026. Perspective and claim wording are decisions for the accountable owner. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. Next step offered: B1 gap plan.

## What this example shows

- The library labels a trial-based economic evaluation by its trial; the economic items come from the paper, not the record.
- When a paper is open access, the full text settles fields the abstract leaves silent. Here it turned three `[GAP]` items into departures.
- Verify cannot separate a significant from a non-significant cost difference; the interval decides, read by hand.
- A ratio sits beside both NICE ranges and the currency mismatch is stated; nothing says "cost-effective" in the skill's voice.
