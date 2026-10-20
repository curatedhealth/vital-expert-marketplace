# Worked example: A2 evidence read and B1 review (illustrative index)

Illustrative. `sample-data/evidence_index_illustrative.csv` was written for this example: a readmission risk model, release v3.0, used in an NHS trust in England and sold in Germany as CE-marked class IIa software (as the person states). It describes no real product. The script output is saved beside it (`read_output.txt`, `review_output.txt`, produced 20 October 2026). No library call was made: the connector was disconnected during this build.

**Request (illustrative):** "Read date 20 October 2026. Release v3.0. Our pass rule, written 2 September 2026: every applicable item present. Review the misses."

---

**Answer.** Your rule is not met: 5 items are missing or not assessable (R02, R06, R08, R10, R12), and all 5 would have to become present and assessable for v3.0 to meet it (computed from your index). Three of the five have an owner and a present-by date; one group, interpreter-assisted visits, was not seen at test time and is still not tested.

**Your rule.** "Every applicable item present", written 2 September 2026.

| Item | Why | Owner | Release waits | Present by |
|---|---|---|---|---|
| R02 Subgroup test on the release model | Evidence is on v2.4; release is v3.0 | Priya Nair | yes | 15 November 2026 |
| R06 DCB0160 deploying organization risk assessment | No evidence recorded | owner not named | not given | not given |
| R08 Bias test using the ethnicity attribute | Policy statement given in place of a test | data science lead | no | 1 October 2026 (earlier than the read date) |
| R10 Post-release monitoring plan by group | No evidence recorded | Priya Nair | no | 1 December 2026 |
| R12 Instructions state group performance | Applicability not given | owner not named | not given | not given |

**Not yet applicable.** R03, R04 and R11 (AI Act Articles 10, 14 and 12) apply from 2 August 2028 for MDR devices, as set by Regulation (EU) 2026/1744, 8 July 2026 (AI EU-19); whether v3.0 is high-risk is for `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control.

**Duties beside the decision (for your legal owner).** R06: NHS guidance says the deploying organization does its own clinical risk assessment and should not adopt technology that does not meet DCB0160 (NHS AI and Digital Regulations Service, read 19 October 2026, CP-UK-09, CP-UK-10). R08: special-category data for bias detection only under the Article 4a conditions (Regulation (EU) 2026/1744, DA-52), and a GDPR DPIA before high-risk processing (GDPR Article 35, EN-111).

**Also flagged.** R13 calibration evidence is dated 25 October 2026, after the read date; it does not belong to this read.

**For you to decide.** Release or hold while R02 waits; who owns R06 and R12; whether R08 and R10 may stay open at release (the old task said the model does not ship while a failed item is open); when the index is reread (not given).

**Calls made.** `python3 scripts/evidence_check.py read` and `review --pass-rule "all applicable" --rule-date "2 September 2026"` on the illustrative index. No library call (connector unavailable on 20 October 2026). Full version with every item on request.

**Record.** Governance review draft for the owner. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
