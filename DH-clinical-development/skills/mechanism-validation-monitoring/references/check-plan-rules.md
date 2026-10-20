# Check plan rules: what counts as evidence that a link happened

Interpretive reference for A1 and A2. Every rule cites its row in `therapeutic-mechanism-research.md` (TM) or `implementation-research.md` (CS). The sources define what to measure and insist on prespecification; none sets a threshold. Thresholds are the person's.

## 1. Read the chain in order: delivery, use, change, outcome

| Link | What counts as evidence it happened | Rows |
|---|---|---|
| Delivered | Fidelity: delivered as intended. Dose: quantity implemented. Reach: whether and how the intended audience came into contact with it. | TM92, TM94 (Moore, DOI 10.1136/bmj.h1258); CS37 (Proctor, DOI 10.1007/s10488-010-0319-7) |
| Delivered (software) | For a software component, fidelity includes the software implementing the component as specified. A recall record is quoted as it states (precedents: PWE recalls of 7 June 2021); its bearing on the person's product is not judged. | TM121, TM139; `precedents.md` |
| Used | Engagement proximal outcomes; at the individual level, RE-AIM implementation is the patients' use of the intervention. | TM87 (JITAI, DOI 10.1007/s12160-016-9830-8); CS25 |
| Changed (mediator) | A proximal outcome on the causal pathway, measured shortly after the intervention option or at the time point the plan names. | TM84 (JITAI, DOI 10.1007/s12160-016-9830-8) |
| Outcome | The distal outcome the product is for. | TM83 (JITAI, DOI 10.1007/s12160-016-9830-8) |
| Context | Barriers or facilitators external to the intervention; effects can differ by context even with identical implementation. | TM96 (Moore, DOI 10.1136/bmj.h1258) |

The old task rule stays: do not treat use of the app as proof of the outcome. Implementation outcomes are preconditions for clinical outcomes, and a failed deployment must be told apart from an ineffective product (CS32). Engagement is one link; it is never the last.

## 2. Measures and their denominators

| Rule | Rows |
|---|---|
| Fidelity is measured as adherence: content, frequency, duration and coverage (dose), in Carroll's framework; quality of delivery and participant responsiveness are moderators there. | TM102, TM103 (Carroll, DOI 10.1186/1748-5908-2-40) |
| Fidelity may be met by delivering only the essential components; name them first (from the design skill's fixed functions). | TM105 (Carroll, DOI 10.1186/1748-5908-2-40), TM117 (StaRI, DOI 10.1136/bmj.i6795) |
| Reach is computed on a valid denominator of eligible people, not volunteers. | CS27 |
| Penetration published calculations: eligible users who use the service over all eligible; providers delivering over providers expected to deliver. | CS39 (Proctor, DOI 10.1007/s10488-010-0319-7) |
| RE-AIM implementation measures include percent of "perfect" delivery completed, adaptations made, cost, and consistency across staff, time and settings. | CS29 |
| Bellg 2004 names five fidelity areas (design, training, delivery, receipt, enactment). Abstract only: the strategies per area were not read. Say so if used. | TM99 (abstract only, DOI 10.1037/0278-6133.23.5.443) |
| Frameworks disagree on the parts of fidelity (Moore: no consensus; Carroll: adherence plus moderators; Bellg: five areas). Name the framework the plan uses. | TM94 (Moore, DOI 10.1136/bmj.h1258), TM101, TM102 (Carroll, DOI 10.1186/1748-5908-2-40), TM99 (Bellg, abstract only, DOI 10.1037/0278-6133.23.5.443); research file "Changes and conflicts" 3 |
| For an adaptive rule, plan how missing tailoring data are handled; a rule fed by unreliable data is little better than random. | TM88, TM89 (JITAI, DOI 10.1007/s12160-016-9830-8) |

## 3. Set it in advance

| Rule | Rows |
|---|---|
| Milestones are specified a priori and on clinical significance, which prevents moving the target after the data are in. | TM57 (ORBIT, DOI 10.1037/hea0000161) |
| Outcomes of the strategy and the intervention are pre-specified, with any pre-determined targets documented. | TM118 (StaRI, DOI 10.1136/bmj.i6795) |
| Process evaluations test hypothesized causal pathways quantitatively, and use qualitative methods for unexpected mechanisms. | TM95 (Moore, DOI 10.1136/bmj.h1258) |
| Integrate process data with outcomes to see whether effects differ by implementation or prespecified moderators, and test hypothesized mediators. | TM97 (Moore, DOI 10.1136/bmj.h1258) |
| A feasibility-stage process evaluation does not replace one alongside the full trial. | TM98 (Moore, DOI 10.1136/bmj.h1258) |
| Old task rule kept: do not fill a gap with a proxy not named in advance. A proxy is allowed only if the plan names it, and it is reported as a proxy. | TM57 (ORBIT, DOI 10.1037/hea0000161) |

## 4. What a link check can and cannot show

- A met link in one cohort and version supports that link there; it does not show the next link (TM8, TM84).
- A mediator moving with the outcome is consistent with the mechanism; whether it mediates is a statistical question for whoever the person names for the analysis, or owner not named (`dh-clinical-development` study-protocol-and-endpoint-design). Quote a published mediation result only from a passage read in the same direction (N3).
- An effect can differ by context with identical delivery (TM96). Report the cohort's context.
- Count met links over measurable links; never over all links, and never as a score (old task rule: do not score a `[GAP]` link).
