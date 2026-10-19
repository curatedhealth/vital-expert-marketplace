# Study quality criteria

Interpretive reference for A1 (study quality check) and B1. It lists what a finished user research study can be checked against, each criterion with its row. Row ids: UX- from `ux-accessibility-usability-research.md`, PE- from `patient-engagement-equity-research.md`, UXR- from `user-research-additions.md`. No criterion carries a pass mark here: the person decides what is good enough.

## 1. Sample fit (did the participants match the question?)

| Criterion | What to check | Rows |
|---|---|---|
| Role matches the task | Each session's participant is the role the question named (patient task, clinician task). A session with the wrong role is noted, and findings from it are not generalized to the named role (register method). | UX-US-36 |
| Groups counted apart | Professionals and lay users, pediatric and adult users, are distinct populations; counts and findings are reported per group. | UX-US-36 |
| Planned vs held | Sessions per group against the study plan. A shortfall is a fact; whether it matters is the person's call. | Plan (A1 of the sibling) |
| Condition-related limits | Where the condition causes functional limits, whether people with a representative range of them took part. | UX-US-37 |
| Access needs | NHS guidance (not law): 1 person with access needs in every 5 research participants. Report the person's own share beside it, as context. | UX-UK-25 |
| Employees | Allowed in formative work with caution about bias; noted so no one reuses the sessions as validation. | UX-US-45, UX-US-38 |
| Sampling | Non-probability samples may not represent the target population; say how participants were found. | PE-06 |
| Rationale recorded | MHRA: the rationale for participant numbers should be documented. Check that one exists, not whether it is right. | UX-UK-17 |

## 2. Method fit (does the method support the claim made from it?)

| Claim made from the study | Method fit | Rows |
|---|---|---|
| "We learned where the design is weak" | Formative methods fit (walk-through, think-aloud, interviews, contextual inquiry). | UX-US-29, UXR-02, UXR-04, UXR-05 |
| "The final design is safe to use" or "validated" | Formative work cannot support it: results do not apply directly to the final design; think-aloud and employees are not acceptable in validation. Stops for the regulatory owner. | UXR-03, UX-US-40, UX-US-38, UX-US-34 |
| "Users find it easy to use" from SUS | The wording stops for the owner (governance stop rule); SUS results from formative work do not carry to the final design (UXR-03) and validation is qualitative (UX-US-43). Published means are context: 68, SD 12.5, as cited by Hyzy et al. (UX-M-08); 76.64 across 114 apps, 68.05 without physical-activity apps (UX-M-09); the authors conclude 68 is a suitable benchmark for digital health apps (UX-M-10). | Governance; UXR-03, UX-US-43; context UX-M-08 to UX-M-10 [PAPER], DOI 10.2196/37290 |
| "We reached saturation" | FDA sets no criteria for evaluating saturation; ask what new stops the last sessions added. | PE-09 |
| "The labeling fix solved it" | For a critical task, not without new data. | UX-US-42 |

## 3. Protocol completeness (formative)

The seven elements a formative protocol typically specifies (UXR-02): purpose, goals and priorities; portion of the UI; scenarios and tasks; participants; data collection methods; data analysis methods; how results will be used. Mark each present, partial or absent in the person's protocol. "How results will be used" absent is the element most tied to actionability.

## 4. Reporting patient involvement (GRIPP2 short form)

Where patients were involved as partners in the research (not only as participants), GRIPP2 is the international reporting guidance; the short form suits studies where involvement is a secondary focus, the long form (34 items) where it is the main focus (PE-89 to PE-91). The five short-form items (UXR-07 to UXR-11):

| Item | What the report should do |
|---|---|
| 1 Aim | Report the aim of PPI in the study |
| 2 Methods | Describe clearly the methods used for PPI |
| 3 Study results | Report the results of PPI, positive and negative |
| 4 Discussion and conclusions | Comment on how far PPI influenced the study, positive and negative effects |
| 5 Reflections | Comment critically on what went well and what did not |

GRIPP2 is a reporting checklist, not a quality score: mark each item reported or not, and never sum items into a grade. The UK Standards for Public Involvement (six standards, including Impact: identify and share the difference involvement makes) are a framework, not a mandated rule (PE-65, PE-68).

## 5. Ethics record

Whether the study file shows who made the ethics determination (IRB, ethics committee or named reviewer) and on what basis (UX-M-11, UX-M-12, UX-M-14, UXR-06), and for Great Britain whether consent was taken where practicable (UX-UK-19). The check is that a determination is recorded, never whether it was right.

## Gaps

- No sourced quality scale for formative user research; any score or level is the person's `[GAP]`.
- GRIPP2 long-form item text was not added to the rows (only its scope, PE-90) `[GAP]`.
- No sourced rule for how many sessions per group make a finding "generalizable" `[GAP]`.
