# Worked run: A4 safety by design and A3 flags, with reSET and EndeavorRx as precedents

Request (illustrative product, real precedents): "We're building a contingency management app for stimulant use disorder with a prize wheel for negative urine screens, like reSET. What safety by design do we need, and what did FDA and the recall record say about reSET?"

Connector note: the VITAL connector was not available when A3 and A4 were added (DH-01.06 fold, 20 October 2026). This run reuses the live outputs saved on 20 October 2026 in `examples/live/connector_calls_2026-10-20.json` (`regulatory-dh.get_authorization {reference: "DEN160018"}`, `{reference: "DEN200026"}`, `regulatory-dh.search_safety_events {product_code: "PWE"}` and `{product_code: "QFT"}`). Recheck these calls live before relying on them (`references/tools.md`).

---

**Answer.** Your design creates at least four hazard sources the reSET record names, plus one from the reward logic itself. Mitigations, labeling wording, thresholds and the risk ratings are yours; none is set here. Whether 21 CFR 882.5801 applies to your product is `[GAP]`: `dh-regulatory-and-quality` regulatory-pathway-and-classification. Owner not named; who decides?

**Hazards (proposed from your description; yours to accept).**

| Hazard | Source in the design | Mitigation | Indicator and threshold | Rows |
|---|---|---|---|---|
| Wheel spin granted on a positive screen | Prize wheel (reward logic) | not given | not given; you set it before launch (SE63, not legally binding) | PWE recalls, 7 June 2021 |
| Software failure delays access to lessons or rewards | Lesson and reward delivery | not given | not given | SE11 |
| Use error | All screens | not given | not given | SE12, SE13 |
| App used in place of clinician sessions | Whole product | not given | not given | SE12; SE89 (Michie 2017, DOI 10.2196/jmir.7126) |
| Therapy not delivered as designed | A1 chain | not given | not given | TM139 |

**What the reSET records state.** De Novo DEN160018, granted 14 September 2017, 21 CFR 882.5801, product code PWE (`get_authorization`). FDA named "Device software failure, leading to delayed access", mitigated by software verification and validation (SE11), and use error, mitigated by labeling including a user guide with screenshots (SE12, SE13). The adjunct warning exists because these patients "typically have medical and psychiatric comorbidities that may be detected and addressed in face-to-face clinician therapy sessions" (SE12). In the trial, 13 percent had any adverse event; none in the reSET arm was adjudicated device-related (SE14). The summary states benefit without contingency management incentives was not evaluated (SE15). `search_safety_events {product_code: "PWE"}` returned two Class II recalls of 7 June 2021: patients "received access to a contingency management wheel spin for potential rewards regardless of the UDS results".

**Labeling elements 882.5801 names (context).** Hazard analysis; instructions with images; compatible devices; a warning that the device does not replace medication (SE1, TM122).

**A3 flags for the wheel.** Rewards of value outside the app: `dh-go-to-market` channel-and-partner-design. The reward is a mechanic tied to the abstinence link (TM135); its software logic is a hazard source above.

**Handoffs.** Risk file: `dh-regulatory-and-quality` design-controls-and-risk-management. Post-launch reading: mechanism-validation-monitoring A4.

Safety-by-design draft. AI-assisted. No severity, probability, acceptability or threshold set by the model; nothing called safe. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

Calls made: none live in this run; saved outputs of 20 October 2026 for `regulatory-dh.get_authorization {reference: "DEN160018"}` and `regulatory-dh.search_safety_events {product_code: "PWE"}`.

---

## A3 precedent note (EndeavorRx, saved records)

`get_authorization {reference: "DEN200026"}`: EndeavorRx, De Novo granted 15 June 2020, 21 CFR 882.5803, product code QFT. The decision summary describes a regimen enforced by lock-out and reminders (TM142) and a pivotal control that matched reward and engagement (TM143). Its risk table names "Treatment results in screen addiction" and "Treatment results in decreased sleep quality" (SE16). `search_safety_events {product_code: "QFT"}` returned no recalls and 2 MAUDE reports (2023), which are reports, not confirmed events. These are record facts for that product only, not targets or evidence for another product.
