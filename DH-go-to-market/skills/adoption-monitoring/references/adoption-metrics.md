# Adoption metrics: definitions, denominators and what the script computes

Interpretive reference for DH-02.02.4.2 (A1 and A2). Definitions come from Proctor et al. (DOI 10.1007/s10488-010-0319-7, [PAPER]; the research row calls it 2011, the library record gives 2010, cite by DOI), the official RE-AIM site (re-aim.org) and the RE-AIM 1999 abstract (DOI 10.2105/ajph.89.9.1322, [PAPER, abstract]). Every row is in `customer-success-research.md` unless marked UX-. Not owner-reviewed.

Frameworks give definitions, not thresholds. No row sets a target adoption share, window or penetration level. Those are the person's.

## 1. The core rule from the register

Adoption is the trained task done in production, not attendance at a session, a login or session time (register CF-12.02.02.4.2.1; expert stop in `examples/live/agent_pack_digital-adoption-lead.json`). A rate is never reported without its denominator (register CF-12.02.02.4.2.2).

## 2. Definitions

| Outcome | Definition | Level | Row |
|---|---|---|---|
| Adoption (Proctor) | The intention, initial decision, or action to try or employ an innovation; also called uptake. | Provider or organization | CS34 |
| Adoption (RE-AIM) | Absolute number, proportion and representativeness of settings and delivery staff willing to initiate a program. | Setting and staff | CS24 |
| Adoption measures (RE-AIM) | Percent of settings approached that participate (valid denominator); percent of staff invited that participate. | Setting and staff | CS28 |
| Penetration (Proctor) | Integration of a practice within a setting. Two calculations: eligible persons who use the service divided by all eligible; providers who deliver divided by providers trained in or expected to deliver. | Setting | CS39 |
| Reach (RE-AIM) | Number, proportion and representativeness of individuals willing to participate, on a valid denominator of eligible people, not volunteers. | Individual (patients) | CS22, CS27 |
| Implementation (RE-AIM) | Staff fidelity and consistency at setting level; at individual level, clients' use of the intervention. | Both | CS25, CS29 |
| Fidelity (Proctor) | Degree to which the intervention was implemented as intended. | Provider | CS37 |
| Acceptability, appropriateness, feasibility (Proctor) | Agreeable or satisfactory; perceived fit; can be carried out in the setting. Kept distinct. | Stakeholder | CS33, CS35, CS36 |
| Sustainability (Proctor) | Maintained or institutionalized within ongoing operations. | Setting | CS40 |
| Maintenance (RE-AIM) | Institutionalized at setting level (program still running 6 or more months after support ends); at individual level, effects 6 or more months after the last contact. | Both | CS26, CS30 |

Conflicts the research names: Proctor's penetration is similar to RE-AIM reach; adoption is defined in both frameworks differently; sustainability maps to maintenance. **Pick one definition per metric and name it** ("Changes and conflicts" in `customer-success-research.md`).

## 3. Why these come before outcomes

Implementation outcomes are preconditions for clinical or service outcomes; a failed deployment must be kept apart from an ineffective product (CS32). Adoption and penetration are never evidence of clinical benefit, and never reimbursement proof (expert stop). Outcomes the customer agreed to see belong to DH-02.02.3.x; payment that depends on outcomes belongs to Market Access (outcomes-contract-monitoring).

## 4. Usage profile and feedback

| Rule | Row |
|---|---|
| NICE ESF Standard 16: company and evaluator agree a plan to report ongoing usage against an expected usage profile agreed at commissioning, plus anonymized aggregate outcomes. For NHS buyers the adoption rule should be that profile. | CS61 |
| ESF Standard 16: for products that change over time, agree how and when performance changes are reported and to whom. | CS62 |
| Audit and feedback: summarize performance data over a specified period and give it to clinicians and administrators to monitor, evaluate and modify behavior. A2 output is the audit; the feedback goes through the person's owner. | CS44 |
| Relay data as close to real time as possible on key process or outcome measures. | CS49 |
| ESF Standard 15: a pilot-site statement may confirm the product was used in line with expectation (who, how, for how long). | CS59 |

## 5. Decay after training

Training knowledge "can decay over time" (CS78); retention of training decays, which is why FDA does not test immediately after training (UX-US-41). The script's after-training activity table shows whether adopters keep doing the task month by month. It measures usage, not knowledge; never present it as a measure of retention of training.

## 6. Acceptability instrument (optional)

If the person wants an acceptability or usability reading beside usage, the System Usability Scale scoring as restated by Hyzy et al. 2022 (DOI 10.2196/37290): odd items minus 1, 5 minus even items, sum times 2.5, range 0 to 100 (UX-M-07). Context only: a general mean of 68 (SD 12.5) cited from Sauro and Lewis, not read (UX-M-08); across 117 SUS scores for 114 digital health apps the mean was 76.64 (SD 15.12) (UX-M-09). One meta-analysis with its own limits (UX-M-10). A benchmark is context, never the person's target. Usability evidence for a device belongs to the UX pack.

## 7. What `scripts/adoption_over_time.py` computes

| Column | Numerator / denominator | Definition used |
|---|---|---|
| Adoption (adopted/trained) | trained users with at least one task event on or after training, up to period end / users trained by period end | Proctor adoption as action (CS34). RE-AIM's staff-level denominator is "staff invited" (CS28); using trained users as that denominator is this skill's reading, not the row's wording. Say so in the output. |
| Penetration (active/eligible) | eligible users with a task event in the period / users on the person's eligible list | Proctor second calculation, "expected to deliver" (CS39) |
| Active/trained | users with a task event in the period / users trained by period end | Proctor second calculation, "trained in" (CS39) |
| Old step users | users with an old-step event in the period (count) | Register CF-12.02.02.4.2.2 ("note the old step if it is still in use") |
| Window adoption | trained users with a task event within W days of training / trained users whose W days have elapsed | The person's window and share (register CF-12.02.02.4.2.1) |
| After-training activity | adopters with a task event in month k after training / adopters observed for a full month k | Descriptive; section 5 |
| Maintenance | adopters trained at least M months ago with a task event in the last 30 days / those adopters | The person's M; RE-AIM's 6 months (CS26) is for outcomes after last contact, so say the script's measure is usage |
| Eligible but not trained | count | Feeds the sibling skill's session record |

The 30-day look-back in the maintenance line is the script's convention, stated in its output; change it only if the person sets another.

## Not sourced here

- Any target adoption share, window, penetration level, "active user" frequency, or engagement benchmark for clinicians or patients.
- Customer health score, renewal, churn, expansion, NPS (research "Not sourced"; the person's).
- Patient engagement retention benchmarks (for example attrition) belong to the patient engagement pack.
