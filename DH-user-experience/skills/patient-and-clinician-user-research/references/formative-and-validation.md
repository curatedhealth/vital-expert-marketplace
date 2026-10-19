# Formative user research and human factors validation

Interpretive reference for every task. It separates the research this competency runs (formative, exploratory) from human factors validation testing, which belongs to the person's regulatory or human factors owner. Every rule carries its row id; rows are in `ux-accessibility-usability-research.md` (UX-) and `user-research-additions.md` (UXR-).

## Two kinds of work

| | Formative user research (this skill) | Human factors validation testing (not this skill) |
|---|---|---|
| Purpose | Explore strengths, weaknesses and unanticipated use errors of a design in progress (UX-US-29); decide whether design changes are needed (UXR-03) | Assess user interactions with the final user interface to identify use errors that could cause serious harm (UX-US-30) |
| Design state | Design in progress; results do not apply directly to the final UI (UXR-03) | The UI must represent the final design (UX-US-34) |
| Methods | Varying formality: cognitive walk-through, observation, discussion, interview (UXR-02), contextual inquiry (UXR-04), interviews and focus groups (UXR-05) | Simulated use with all critical tasks performed under realistic conditions (UX-US-34) |
| Think-aloud | Acceptable (UX-US-40, UX-M-05) | Not acceptable, because it does not reflect actual use (UX-US-40) |
| Employees as participants | Allowed, with caution about bias (UX-US-45) | Should not take part, except in rare cases where all users are employees (UX-US-38) |
| Sample size | Varies with the information needed, complexity and user variability (UX-M-04); no formula gives a "correct" size (UX-M-03) | FDA: in general at least 15 participants, and at least 15 per distinct user population (UX-US-35) |
| Numbers | Counts and scores describe what happened | Primarily qualitative; no numerical acceptance criteria for error rates (UX-US-43) |
| Who decides it is enough | The person running the study | The regulatory or human factors owner, against FDA guidance (reissued 3 August 2026, UX-US-25) and MHRA guidance for Great Britain (UX-UK-13) |

FDA guidance is nonbinding: "should" means recommended unless a statute or regulation is cited (UX-US-26). MHRA's guidance is advisory (UX-UK-14).

## Rules that follow

1. **Name the kind of work before planning.** If the person calls a study "summative", "validation" or "for the submission", stop the plan at the boundary: the protocol, the critical-task list and the conclusions belong to the regulatory or human factors owner (governance). This skill can still lay out the sourced test-design facts (UX-US-34 to UX-US-41) as a draft for that owner.
2. **A formative study cannot be relabeled as validation afterward.** Formative results do not apply directly to the final design (UXR-03). If no formative work is done and flaws appear in validation, the validation test effectively becomes formative (UX-M-06).
3. **Distinct user populations are planned separately.** Pediatric and adult users are distinct; so are professionals and lay users (UX-US-36). In this skill, patients, caregivers and clinicians are separate user groups unless the person says otherwise; never pool their counts.
4. **Critical tasks are the regulatory owner's list.** FDA defines a critical task by the serious harm that incorrect performance or omission could cause, including compromised medical care (UX-US-28); MHRA selects critical tasks by severity of harm (UX-UK-18). The model never decides that a task is or is not critical; it uses the person's flag.
5. **A stop on a flagged critical task goes to the owner as recorded.** The model does not judge whether it is a use error (UX-US-27, UX-UK-15) or how severe it is. FDA gives severity of harm more weight than probability (UX-US-32), which is why the owner sees every such stop, whatever its count.
6. **Labeling or training is not a fix by assertion.** In a submission, claiming that changed instructions or more training mitigated a critical-task error is not acceptable without new data showing it worked (UX-US-42). In formative work, a proposed labeling fix is a design change to test again, not a closed finding.
7. **Risk-control order.** Inherent safety by design first, then protective measures, then information for safety (UX-US-33). A research action that proposes only wording for a critical-task stop says so.
8. **Known problems with similar products are inputs.** FDA suggests looking at use-related problems with similar devices, from MAUDE, recalls, complaint files and earlier studies (UXR-01). The library's safety events can seed scenarios; a record is described only by what it states.
9. **Records are kept even when not submitted.** FDA recommends keeping human factors information whether or not it is submitted (UX-US-53). Formative records feed the owner's file.

## Submission context (for orientation only)

FDA's final guidance on the content of human factors information in submissions (issued 29 May 2026, UX-US-47) sorts submissions into three HF Submission Categories using decision points A to D (UX-US-48 to UX-US-52). Which category applies is the regulatory owner's call (`dh-regulatory-strategy`). This skill does not choose a category.

## Gaps

- IEC 62366-1 clause text and IEC/TR 62366-2 sample-size advice are paywalled; only the public abstract is used (UX-STD-36, UX-STD-37) `[GAP]`.
- A primary methods paper on think-aloud was not found; think-aloud is described only from FDA guidance `[GAP]`.
- Changes between the 2016 and 2026 FDA guidance texts were not diffed `[GAP]`.
