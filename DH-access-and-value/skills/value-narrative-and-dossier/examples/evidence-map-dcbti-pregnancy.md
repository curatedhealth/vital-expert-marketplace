# Worked example: A1 Evidence and audience map, short mode

Live run on 19 October 2026. The request is a test request; the person, the product and the owner are illustrative. The study, the passages and every tool result are real (`examples/live/`).

**Request (illustrative):** "Our app delivers the digital CBT-I tested in Felder et al. 2020 (DOI 10.1001/jamapsychiatry.2019.4491). It is FDA-cleared for insomnia in adults. We want to tell US health plan P&T committees and an NHS commissioner three things: it improves insomnia severity in pregnancy, it improves sleep duration, and it works for adults with insomnia generally. Quick view please. Regulatory owner: Maya Chen."

---

**Answer.** One of the three claims can be carried: in pregnant women with insomnia symptoms, digital CBT-I improved Insomnia Severity Index scores more than standard treatment from baseline to postintervention (10 weeks). The sleep duration claim is contradicted by the paper's own results, and the "adults generally" claim widens the trial's population, so both are held. Certainty has not been rated by anyone yet `[GAP]`. The cleared indication you gave (insomnia in adults) and the trial population (pregnant women) are close but not identical: Maya Chen decides whether the pregnancy result relates to the cleared indication for payors (PC-US-37).

**Claim register**

| # | Claim | Passage (locator) | Verify | Same direction? | Certainty | May enter? |
|---|---|---|---|---|---|---|
| C1 | ISI improvement vs standard treatment, pregnant women, postintervention | "Women randomized to receive digital CBT-I experienced statistically significantly greater improvements in insomnia symptom severity ... (difference = -0.36; 95% CI, -0.48 to -0.23 ...)" (Abstract, Results) | supported, 67% | Yes | `[GAP]` | Yes |
| C2 | Sleep duration improved | "... all secondary outcomes, with the exception of sleep duration, were statistically significant." | unsupported, 17% | No: states the opposite | n/a | No |
| C3 | Works for adults with insomnia | same passage as C1 | supported, 77% | No: population widened | n/a | No |

The tool scored C3 higher than C1 and did not call C2 contradicted (register N3); the readings above, not the scores, decide.

**Audience fit**

- US health plan P&T committees: payor audience (PC-US-34). C1 can be HCEI only if it relates to the cleared indication, rests on competent and reliable evidence and carries the context (PC-US-04, PC-US-40); not for prescribers or a public website (PC-US-35). 2018 final guidance, June 2026 revised draft (PC-US-47).
- NHS commissioner: ESF is voluntary (HE-079); a budget impact analysis is expected for every tier (HE-087). None supplied `[GAP]`.

**Gaps**

- Certainty for ISI: not yet rated by a person `[GAP]` (per outcome, ES-96).
- Trial registration: library record empty; the abstract names NCT02805998.
- Budget impact for the NHS: not supplied `[GAP]`.

**Record.** Draft for the owner. AI-assisted. Clears it: Maya Chen. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

---

Calls made (19 October 2026): `literature.get_record {doi}`; Europe PMC abstract read for the Results passage (the record excerpt stopped at the design); `literature.check_retraction {doi}` (none, Crossref); `verify.qualify_source {doi, question}` (gold, 67); `verify.check_claim` three times. `scripts/claim_register.py examples/live/verify_dcbti_pregnancy.json` reproduces the register.

Word count of the output between the rules, counted by script during the build: 380 words, including the passage column.
