# Claim map rules

Interpretive reference for task A1 and B1. Every rule cites the row it comes from in the copied research files. Rows are dated in those files (TM and PL rows read 20 October 2026; PC- and ES- rows 19 October 2026). Where a fact is not in a row, it is `[GAP]`.

## 1. What a claim sets

| Rule | Rows |
|---|---|
| Intended use is the firm's objective intent, shown by labeling claims, advertising, statements, design or distribution. What the product says sets what it is for. | PC-US-17, PC-US-20 |
| A German DiGA's claimed positive care effect must be consistent with its intended purpose under device law and with its functions, content and the manufacturer's published statements. | TM148, PL92 |
| A positive care effect under DiGAV is either a medical benefit (health status, disease duration, survival, quality of life) or a patient-relevant structure and process improvement in nine named areas. | TM145 to TM147 |
| A DiGA application states, in plain language, aim, mode of action, content and use, and the sources of its medical content (guidelines, textbooks, studies). | TM149 |

## 2. What counts as support

| Rule | Rows |
|---|---|
| A claim is supported only by a passage that states the result in the same direction, for the same population and outcome. Verify's `check_claim` decides on word overlap: in this build a negation of the source's conclusion returned "supported" (90 percent overlap) and a claim with the hedge removed returned "supported" (89 percent). Read the passage every time. | Register N3; `examples/live/connector_calls_2026-10-20.json` calls 13 and 14 |
| For SaMD, clinical evaluation has three parts: valid clinical association (scientific validity), analytical validation and clinical validation. Analytical and clinical validation are necessary for any SaMD. | PL63 to PL65 |
| Evidence for valid clinical association can come from literature, professional guidelines, proof-of-concept studies or the manufacturer's own investigations; clinical performance is tested in the target population for the intended use. | PL70, PL72 |
| Where no measurable patient outcome benefit is claimed, MDCG 2020-1 says clinical relevance is shown through predictable, reliable use and usability. | PL73 |
| The three parts are not a strict stepwise sequence. | PL74 |

## 3. Certainty

| Rule | Rows |
|---|---|
| GRADE certainty has four levels: high, moderate, low, very low. | ES-89 |
| Certainty is rated per outcome, not per study or product. | ES-96 |
| Randomized evidence starts high and non-randomized starts low; rating down for risk of bias, inconsistency, indirectness, imprecision, publication bias. | ES-90, ES-91 |
| GRADE is not a quantitative score. | ES-94 |
| Statement wording can follow size and certainty: "results in" (high), "likely results in" (moderate), "may result in" (low) (Santesso, abstract only, DOI 10.1016/j.jclinepi.2019.10.014). | ES-201 |
| `literature.grade_evidence` returns a CEBM level from the design tag only. It is a library label, not GRADE certainty, and never replaces a rating by the person or a review. | Register N8; live call 7 |

The certainty of each claim is the person's or a review's. If none exists, the claim map says `[GAP]` and points to `dh-clinical-development` literature-and-real-world-evidence-review.

## 4. Consistency rules for claims beyond a label (lay out; never decide)

| Rule | Rows |
|---|---|
| For PMA and De Novo products, FDA asks whether a communication changes the indication, patient population, use limitations or directions, or use regimen; failing any factor makes it inconsistent with labeling. Nonbinding guidance. | PC-US-23 |
| Also inconsistent: increasing the potential for harm relative to labeling, or directions that would not enable safe and effective use under the represented conditions. | PC-US-24 |
| Use in patients outside the approved population is FDA's example of inconsistent information. | PC-US-27 |
| Disclosing a weak study's limitations does not correct a misleading message; unfavorable or inconsistent findings must be disclosed. | PC-US-30, PC-US-31 |
| For 510(k) and exempt devices, a claim that would need a new 510(k) is inconsistent with labeling. | PC-US-22 |
| German advertising law bans attributing efficacy a product does not have and false impressions that success is certain; cited studies must state author, date and source and quotes must be faithful. | PC-DE-03 to PC-DE-05 |

## 5. Mechanism claims

| Rule | Rows |
|---|---|
| Mechanisms are the causal links between components and outcomes. A mechanism statement is part of the program theory and stays a hypothesis until a passage states it. | TM6 to TM8 |
| Several FDA special controls require a validated model of therapy and clinical data validating it "as implemented by the device" (882.5801, 876.5960, 880.5735, 890.5800). Others (882.5803, 882.5705, 886.5500) instead require clinical performance with validated measures and a full software description. | TM120, TM121, TM123, TM127 to TM129; research file "Changes and conflicts" item 7 |
| In reSET's De Novo summary, FDA's mitigation for "ineffective treatment" combined a validated therapy method, clinical data in the intended use population, software V&V showing the model was correctly implemented, and labeling. | TM139 |

## 6. Named products as precedents

Describe a named product only by its registry record, decision summary or publication. The `regulatory-dh.get_authorization` record carries dates, product code and regulation number, not indications or limitations (live calls 1 and 2). Indication and limitation wording for reSET and EndeavorRx is in TM132, TM138 and TM144. For other products, the decision summary was not read (research file "Not sourced"): `[GAP]`.
