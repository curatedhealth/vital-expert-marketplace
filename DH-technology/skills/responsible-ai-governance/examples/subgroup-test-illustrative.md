# Worked example: A2 subgroup test and B1 release controls (illustrative data)

Illustrative. The scored file `sample-data/deterioration_scores_illustrative.csv` was generated for this example (700 cases, seeded random data) and describes no real model, site or patient. The script output it rests on is saved beside it (`groups_output.txt`, `rule_output.txt`, produced 20 October 2026). No library call was made: the connector was disconnected during this build.

**Request (illustrative):** "Model v2.1, holdout-2026Q2, threshold 0.3, compare language groups against English. Our rule, written 1 October 2026: sensitivity in any language group may sit at most 0.05 below English. Interpreter-assisted visits are not flagged in the data. US hospital, HHS-funded."

---

**Answer.** Against your rule, Spanish does not meet it: sensitivity 0.312 (10 of 32; 95% CI 0.180 to 0.486) against English 0.714 (35 of 49), a gap of 0.402; 12 more detected cases of 32 would bring it within 0.05 (computed on your data, not a target). Other language meets it (8 of 9), interpreter-assisted visits are not tested `[GAP]`, and outcome rates differ by group, so calibration and equal error rates cannot both hold.

**The test (yours).** Model v2.1; dataset holdout-2026Q2 (data cut not given); threshold 0.3; reference English; subset: not given (internal or external testing).

**Against your rule (written 1 October 2026).**

| Group | Value (count) | Reference | Your rule | Change that would meet it (computed) |
|---|---|---|---|---|
| Spanish | 0.312 (10/32) | 0.714 | not met | 12 more of 32 (22/32 = 0.688) |
| Other language | 0.889 (8/9; CI 0.565 to 0.980) | 0.714 | met | none needed |
| Group not recorded (20 cases) | 0.600 (3/5) | 0.714 | not compared | |
| Interpreter-assisted visits | [GAP]: not visible in this data | | not tested | |

**Criteria in conflict.** Outcome rates run from 0.113 (Other language) to 0.160 (Spanish). For any single threshold, a well-calibrated model will never have the same sensitivity and specificity for two groups with different outcome rates (Paulus and Kent, npj Digit Med 2020, DOI 10.1038/s41746-020-0304-9, DA-119). Your rule uses equal sensitivity (equal opportunity, Rajkomar et al. 2018, DOI 10.7326/M18-1990, DA-114); whether that criterion fits the decision is yours (DA-116).

**Acceptance.** Spanish: acceptor owner not named; written reason not given; release waits: not given. Beside it, for your legal owner: a Section 1557 covered entity must make reasonable efforts to mitigate the risk of discrimination from a patient care decision support tool (45 CFR 92.210, eCFR read 19 October 2026, PE-113).

**Controls (US).** Override and automation-bias training: not given in your material (FDA CDS guidance, 29 January 2026, UX-US-72). Post-release monitoring by language group: not given; NIST MEASURE 3.1 asks for tracking intended against actual performance (NIST AI RMF 1.0, January 2023, DA-14, voluntary).

**For you to decide.** Release, hold, or accept the Spanish gap with a named acceptor and a written reason; how interpreter-assisted visits get flagged so they can be tested.

**Calls made.** `python3 scripts/subgroup_check.py groups ...` and `rule --rule sensitivity:0.05 --rule-date "1 October 2026"` on the illustrative file. No library call (connector unavailable on 20 October 2026). Full version with every metric and the differences table on request.

**Record.** Release control draft for the owner. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
