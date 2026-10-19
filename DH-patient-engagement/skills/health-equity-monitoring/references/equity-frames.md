Copied from the design skill (health-equity-and-inclusive-design, DH-02.03.4.1) so this package stands alone.

# Equity frames: what each says and where it applies

Interpretive reference. Every point cites its row in `patient-engagement-equity-research.md` (PE rows) or `accessibility-pointer-rows.md` (UX rows). Rows were read on 19 October 2026. Which frame applies to the person's organization is their legal or compliance owner's call; this file lays out what each frame says.

A frame is a lens the person may choose for defining subgroups or duties. None of them sets a target for the person's product. National definitions and indices are context.

## 1. Section 1557 (45 CFR part 92), United States

Who is covered is not in this skill's sources: the definition of "covered entity" was not quoted in the research pass `[GAP]`. Ask the person whether their legal owner treats them, or the customer deploying the product, as a covered entity. Litigation stays on parts of the rule are also not sourced `[GAP]` (research "Not sourced").

| Duty | What the row says | Date | Rows |
|---|---|---|---|
| Effective date | Part 92 effective 5 July 2024, with later compliance dates for listed provisions | 5 July 2024 | PE-106 |
| Language access (92.201) | Reasonable steps to give meaningful access to each person with limited English proficiency; language help free of charge, accurate, timely, private | No separate date listed in the rows; the 5 July 2024 effective date is the one sourced | PE-107 |
| Machine translation (92.201) | Where text is critical to rights or access, accuracy is essential, or language is complex or technical, machine translation must be reviewed by a qualified human translator | as above | PE-108 |
| No own interpreter (92.201) | A person may not be required to bring or pay for their own interpreter | as above | PE-109 |
| Notice of language assistance (92.11) | In at least the 15 most common limited-English languages of the relevant State or States | Within one year of 5 July 2024 | PE-116, PE-117 |
| Notice of nondiscrimination (92.10) | Required | Within 120 days of 5 July 2024 | PE-116 |
| Written policies (92.8) | Required | Within one year of 5 July 2024 | PE-116 |
| Decision support tools (92.210) | No discrimination through patient care decision support tools; ongoing duty to make reasonable efforts to identify tools whose inputs measure race, color, national origin, sex, age or disability, and to mitigate the risk | 92.210(b) and (c): within 300 days of 5 July 2024 (1 May 2025 by calendar count; the rule states only the 300 days) | PE-113, PE-115 |
| Decision support tool, defined | Any automated or non-automated tool used by a covered entity to support clinical decision-making | | PE-114 |
| ICT accessibility (92.204) | Health programs through ICT must be accessible unless undue burden or fundamental alteration; recipients' websites and apps follow Section 504 as interpreted consistent with ADA Title II | No separate compliance date listed; 5 July 2024 applies | PE-110, PE-111, UX-US-21, UX-US-22 |

What this means for the work:

- A product step that only works in English, or that relies on unreviewed machine translation of clinical or rights-related text, is a step where a limited-English group may be left out (PE-107, PE-108). Whether the duty binds the person is their legal owner's call.
- A risk score, triage rule or eligibility algorithm used to support clinical decisions is a decision support tool in the rule's own definition (PE-114). If its inputs include race, color, national origin, sex, age or disability, the identify-and-mitigate duty is the relevant row (PE-113). The model lists the inputs the person names; it does not judge whether mitigation is adequate.
- Web and app accessibility conformance (92.204, HHS 504 WCAG 2.1 dates) is pointed to the dh-user-experience accessibility skills. The dates as the rows give them: HHS 504 recipients with 15 or more employees from 11 May 2027, fewer than 15 from 10 May 2028 (PE-112, UX-US-16, UX-US-17), moved by an HHS interim final rule effective 7 May 2026 from 11 May 2026 and 10 May 2027 (UX-US-18).

## 2. Diversity action plans (FDORA sections 3601 and 3602), United States

| Point | What the row says | Rows |
|---|---|---|
| Drugs | Sponsor of a phase 3 or other pivotal study of a new drug submits a DAP | PE-30 |
| Devices | DAP in the IDE application; where no IDE is needed, in the 510(k), De Novo or PMA submission | PE-34 |
| Content | Enrollment goals, rationale, how the sponsor will meet them | PE-31 |
| Goals disaggregated by | Age group, sex, racial and ethnic characteristics; may include geographic location and socioeconomic status | PE-37 |
| How goals are met | Outreach and enrollment strategies, site selection, inclusion and exclusion practices, diversity training | PE-38 |
| Trigger | Applies only to studies whose enrollment starts more than 180 days after FDA publishes the final guidance | PE-36 |
| Status | Draft guidance announced 28 June 2024 (89 FR 54010); on 19 October 2026 FDA still lists it as a draft, restored under a court order to its 29 January 2025 version | PE-40, PE-41 |

Reading recorded in the research file (not an FDA statement): while no final guidance exists, the statutory DAP requirement is not yet triggered (research "Changes and conflicts"). Say so with that label. Whether a given study needs a DAP, and its enrollment goals, belong to the person's regulatory owner; the model can lay out the subgroups the statute names (PE-37) as a starting frame and point to the clinical-validation and regulatory packs for the study itself.

## 3. CMS Framework for Health Equity 2022 to 2032

- Definition of health equity used by CMS (PE-118).
- Five priorities: standardized data; causes of disparities; capacity building; language access, health literacy and culturally tailored services; accessibility (PE-119).
- Standing: the PDF still downloads, but the CMS program page returned 404 on 19 October 2026; its current standing as CMS policy is not established (research "Changes and conflicts"). Cite it as a framework document, not current CMS policy.

## 4. NIH definitions

- Health disparity: a measurable difference in health between specific population groups (PE-124).
- NIH-designated populations with health disparities: low socioeconomic status, underserved rural populations, racial and/or ethnic minority populations, people with disabilities, sexual minority groups (PE-125). Earlier NIH wording used a broader category; only the current wording was read (research "Changes and conflicts").
- Individual low-SES indicators include income below 200 percent of the federal poverty threshold (PE-126).

Use: a ready list of dimensions the person can adopt or reject. Not a list the model imposes.

## 5. CDC/ATSDR Social Vulnerability Index (SVI), United States, area level

- Ranks census tracts on 16 ACS variables in four themes: socioeconomic status, household characteristics, racial and ethnic minority status, housing type and transportation (PE-120, PE-121).
- Percentile ranks from 0 to 1, higher meaning more vulnerable; tracts at or above the 90th percentile are flagged (PE-122).
- Use the U.S. database across states and the state database within one state; rankings differ (PE-123).
- It describes an area, not a person. A person living in a high-SVI tract is not thereby vulnerable; use it for grouping counts by area band, never to label an individual. The SVI file itself is not in the library (`[GAP]`; future slot B6).

## 6. NHS England Core20PLUS5 (England) [WF]

- Core20: the most deprived 20 percent of the national population by the Index of Multiple Deprivation (PE-127).
- PLUS: groups identified locally (PE-128).
- Five adult clinical areas, including hypertension case-finding and lipid management (PE-129).
- All three rows were read through a summarizing fetch tool, not raw text: say so when a point rests on them, and re-check the page before quoting it outside the conversation.

## 7. Representativeness in patient input

- FDA's patient preference information guidance (final, 30 March 2026) lists "representative study population" among recommended study qualities (PE-22, PE-27). Useful when the person's equity question concerns who took part in co-design or preference work.
- The UK Standards for Public Involvement include Inclusive Opportunities: involvement partnerships accessible and including a range of people (PE-65, PE-66). A framework, not a mandated rule (PE-65).
- NICE commits to engaging groups protected by equality legislation (PE-63).

## Not covered here (point elsewhere)

- WCAG, EN 301 549, Section 508, European Accessibility Act scope: dh-user-experience accessibility skills (UX rows; for example UX-STD-04 on W3C's advice to target WCAG 2.2, UX-EU-04 on health apps under the EAA).
- EU and UK equality law beyond the rows above: not sourced `[GAP]`.
