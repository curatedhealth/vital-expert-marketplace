# Participants, sample and ethics screen

Interpretive reference for A1 (study plan) and for the sample-fit check in the monitoring sibling. Row ids: UX- from `ux-accessibility-usability-research.md`, UXR- from `user-research-additions.md`, PE- from `patient-engagement-equity-research.md`.

## Who takes part

| Point | What the sources say | Rows |
|---|---|---|
| User groups | Professionals and lay users are distinct populations; so are pediatric and adult users. Plan and count each group separately. | UX-US-36 |
| Representativeness | Where the condition causes functional limits (the guidance's examples are diabetic retinopathy and neuropathy), people with a representative range of those limits should be considered in preliminary evaluations. | UX-US-37 |
| People with access needs | NHS guidance (not law): try to include 1 person with access needs in every 5 research participants; agencies can recruit people with different needs at no extra cost. GOV.UK services must include disabled people in user research (government policy). | UX-UK-25, UX-UK-26, UX-UK-08 |
| Employees | Allowed in formative work, with caution about bias. Not in validation, except rare cases. | UX-US-45, UX-US-38 |
| Residence | For validation supporting US use, participants should reside in the US. Formative work has no such row. | UX-US-39 |
| Patient input sampling | Probability sampling makes results more likely to reflect the target population; non-probability samples may not be representative, and the choice must be weighed when interpreting the data. | PE-06 |
| Patient experience data | Data collected by anyone (patients, caregivers, advocacy groups, researchers, manufacturers) about the experience of a disease, including impacts and preferences. | PE-04 |

Patients as co-design partners or on an advisory board are a Patient Engagement subject (`patient-research-and-co-design`); this skill covers task-based research with patients and clinicians.

## How many

No source sets a formative sample size. What the rows allow you to say:

- Formative evaluation may use varying sample sizes depending on the information needed, complexity and user variability (UX-M-04).
- FDA restates Faulkner (2003): 15 users found at least 90 percent and on average 97 percent of known problems; 20 users at least 95 and on average 98 percent; 30 users found on average under 2 percent more than 15 (UX-M-01, UX-M-02). Faulkner's paper itself was not read. These figures describe one study's software problems, not a rule.
- FDA states that a statistically "correct" sample size is extremely difficult to set, because published estimates assume fixed, uniform, independent problem probabilities (UX-M-03).
- MHRA sets no fixed number; the rationale for participant numbers should be documented (UX-UK-17).
- For interviews aimed at patient experience, FDA describes saturation (no new relevant information emerging) and says there are no set criteria for evaluating it (PE-09).
- FDA's 15-per-group minimum applies to validation testing (UX-US-35). Quoting it as a formative target is a category error; say so if the person does.

The number of participants per group is the person's decision. The model writes the rationale they give, and lists the rows above as context.

## Expertise

FDA recommends engaging early with patients and with qualitative researchers, survey methodologists, statisticians, psychometricians and preference researchers (PE-08, PFDD Guidance 2, February 2022). Where the person's study feeds patient-reported outcome or preference work, the PFDD series applies: Guidance 1 (June 2020) and 2 (February 2022) final, Guidance 3 final October 2025, Guidance 4 draft April 2023 (PE-01, PE-02, PE-07, PE-10, PE-17). That work belongs to the clinical or regulatory owner; this skill points there.

## Ethics screen (facts for the person's ethics reviewer, not a determination)

| Question | Facts | Rows |
|---|---|---|
| Does the Common Rule apply? | 45 CFR 46 applies to research conducted, supported or otherwise regulated by a federal department that adopted it. Privately funded usability work is not covered by that text unless an institution or agency makes it so. | UX-M-11 |
| Is it "research"? | Research is a systematic investigation designed to develop or contribute to generalizable knowledge. Product-specific testing may or may not meet this; the source leaves it to the facts. | UX-M-12 |
| Exemption for interviews, surveys, observation | 46.104(d)(2) applies if at least one criterion holds: identity cannot readily be ascertained; disclosure would not reasonably harm the subject; or identifiable recording with a limited IRB review. | UX-M-14, UXR-06 |
| Exemption for benign tasks | 46.104(d)(3): adults, benign behavioral interventions, prospective agreement, plus an identifiability or harm criterion. Benign means brief, harmless, painless, not invasive, no lasting impact, not offensive. Deception about the research voids it unless conditions are met. | UX-M-15, UX-M-16, UX-M-17 |
| Children | For research with children, (d)(2) applies only to educational tests or non-participant observation of public behavior; (d)(2)(iii) never applies; (d)(3) is not listed. | UX-M-18 |
| Secondary use of health records | 46.104(d)(4)(iii) covers secondary use of identifiable health information regulated by HIPAA as health care operations, research or public health. | UX-M-19 |
| Minimal risk | Harm no greater than in daily life or routine examinations or tests. | UX-M-13 |
| Great Britain, formative work | MHRA: risks and benefits to participants should be considered and documented, and participants should give informed consent where practicable, even in early formative testing. | UX-UK-19 |

Whether a study is research, exempt or needs review is decided by the person's IRB, ethics committee or named reviewer. The model lays out these facts and never states that a study is exempt.

## Data the study holds

- Use pseudonymous codes (for example P01) in every file the model reads or a script runs on. `scripts/research_log.py` refuses files with identifying columns or contact data.
- Recordings and consent forms stay with the person's research operations; never paste them into the conversation or a library call.
- Exemption (d)(2)(i) turns on whether identity can readily be ascertained (UXR-06); keeping identifiers out of analysis files is consistent with that criterion, but the determination is the reviewer's.

## Gaps

- Common Rule informed-consent elements (45 CFR 46.116) were not extracted `[GAP]`.
- Participant payment rules (for example inducement rules where participants are Medicare beneficiaries) are not in this skill's sources `[GAP]`; route payment questions to the owner the person names for this.
- EU and UK rules on ethics review for non-clinical user research are not in the sources `[GAP]`, apart from MHRA's advisory guidance (UX-UK-19).
- GDPR rules for research recordings are not in this skill's sources `[GAP]`.
- FDA's human-subject protection and IRB rules (21 CFR 50 and 56) for FDA-regulated clinical investigations were not read in this build `[GAP]`. When a US device company asks about IRB review, name them as a question for the reviewer, with no statement on whether they apply.
