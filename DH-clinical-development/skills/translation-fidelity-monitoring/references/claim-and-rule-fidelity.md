# Claim and decision rule fidelity

Interpretive reference for tasks A1, A2 and B1. Rows from the copied research files; read dates there. Where a fact is not in a row, it is `[GAP]`.

## 1. Fail conditions for claims (proposed from the old method; the person confirms)

The old DH-01.01.4.2.1 method defines a fail as "a wider population, a stronger verb, or a missing caveat the source had", and DH-01.01.4.2.2 adds that a claim with no source is a fail. The sourced rows below show what each looks like in published decisions and labeling rules.

| Fail type | What the source shows | Rows |
|---|---|---|
| Wider population | STARS-ADHD, the pivotal trial behind EndeavorRx (TM144), enrolled "paediatric patients (aged 8-12 years, without disorder-related medications) with confirmed ADHD". A claim to "children with ADHD" is wider. | TM144; `examples/live/pubmed_abstracts_2026-10-20.txt` |
| Wider population (labeling rule) | Use in patients outside the approved population is FDA's example of a communication inconsistent with labeling (nonbinding guidance). | PC-US-27 |
| Stronger verb | STARS-ADHD concludes AKL-T01 "might be used to improve objectively measured inattention"; "clinically proven to improve attention" drops the hedge and the measure. Verify returned "supported" for the unhedged verb (N3). | Live calls 11 and 14 |
| Missing caveat | reSET labeling must warn it is not a standalone therapy (882.5801); the reSET summary states no benefit in primary opioid users; EndeavorRx "may not display benefits in typical behavioral symptoms, such as hyperactivity". | TM122, TM138, TM144 |
| Different regimen | CFL factors include the use regimen; 882.5804 labeling states frequency and duration of use. | PC-US-23, TM126 |
| Harm | A communication that increases the potential for harm relative to labeling is inconsistent with it. | PC-US-24 |
| Selective presentation | Unfavorable or inconsistent findings must be disclosed; disclosure does not cure a study inadequate for the claim. | PC-US-30, PC-US-31 |
| DiGA consistency | The claimed care effect must be consistent with intended purpose, functions, content and published statements. | TM148 |
| German advertising | Attributing efficacy a product does not have, or a false impression of certain success, is misleading; quotes from literature must be faithful. | PC-DE-03 to PC-DE-05 |

FDA guidance rows are nonbinding; HWG and DiGAV rows are German law. Whether any applies to the person's product is a question for the owner the person names for regulatory status, or owner not named.

## 2. Fail conditions for decision rules

| Check | Rows |
|---|---|
| The rule fires as specified: decision point, tailoring variable, option. | TM77 to TM82 |
| The rule behaves as specified when tailoring data are missing. | TM89 |
| The tailoring variable is measured as specified; unreliable measures make a rule little better than random, invalid ones may recommend counterproductive options. | TM88 |
| Engagement and fatigue proximal outcomes are tracked for adaptive rules. | TM87 |
| reSET's specified contingency management gave virtual rewards for lesson completion and for negative drug screens. | TM135 |
| FDA Class II recalls of the reSET and reSET-O mobile apps dated 7 June 2021 describe reward access "regardless of the UDS results"; "Positive UDS results should not have resulted in access to a wheel spin." | Live call 4 (`regulatory-dh.search_safety_events {product_code: "PWE"}`) |
| 882.5801 requires software verification, validation and hazard analysis and documentation that the device implements the therapy model. | TM121 |

## 3. Facts that bear on a repair (lay out; applicability is for the owner the person names for regulatory status, or owner not named)

| Fact | Rows |
|---|---|
| For a DiGA, a significant change materially affects safety, function, quality, data protection and security, or the care-effect evidence, including patient-group changes; minor editorial changes are bundled and notified up to four times a year. | PL95 |
| BfArM provides an electronic checklist (Prüfbogen) to decide whether a change is significant. | PL96 |
| A change that alters the SaMD definition statement re-opens categorization. | PL59 |
| Clinical performance may be re-confirmed per independent module; a combination that changes indications needs whole-product evaluation. | PL75 |
| FDA recommends review by qualified medical or scientific, legal and regulatory personnel before a CFL communication is disseminated (nonbinding). | PC-US-33 |

## 4. What Verify can and cannot do here

`check_claim` decides on word overlap (register N3). In the build it returned "unsupported" for a claim with new words (hyperactivity, teenagers; 33 percent) but "supported" for a negation (90 percent) and for a dropped hedge (89 percent). It can help find widened claims that add words; it cannot detect a stronger verb or a reversed meaning. FDA decision summaries are rated inadmissible (C1). `scripts/fidelity_sample.py claims` sets the words side by side so the person can mark them.
