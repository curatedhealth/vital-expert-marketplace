# Engagement read rules: usage, dropout and what they can and cannot show

Interpretive reference for A3 (folded in from DH-01.06.3.2 Engagement Effectiveness Assessment & Retention Quality Monitoring). Every rule cites its row in `safety-and-engagement-research.md` (SE). The sources define what to count and how to report it; none sets a benchmark, a retention target or a "good" completion rate (research file "Not sourced"). Definitions, thresholds and targets are the person's.

## 1. Engagement is a use link, never the outcome

| Rule | Rows |
|---|---|
| FDA's Digital Health Advisory Committee (6 November 2025, advisory, non-binding) said the relationship between engagement, adherence, symptoms and outcomes "may not be well understood and will be important to characterize". | SE26 |
| Higher baseline motivation may explain both engagement and outcomes; a usage-outcome correlation is not causal evidence. | SE82 (Perski 2017, DOI 10.1007/s13142-016-0453-1) |
| Usage correlates with behavioral outcomes, but the association is often not strong. | SE88 (Michie 2017, DOI 10.2196/jmir.7126) |
| The DiGAV asks for usage reporting without making usage a benefit. | SE70 to SE73; research file "Changes and conflicts" 5 |
| Users may use enjoyable features most while less popular features drive outcomes: the most-used feature is not shown to be the effective one. | SE84 (Perski 2017, DOI 10.1007/s13142-016-0453-1) |

The old task rule of the parent skill stays: use of the app is not proof of the outcome. In this skill engagement is the "used" link of the A1 plan; A2 reads the later links.

## 2. Usage or adherence: name it correctly

| Rule | Rows |
|---|---|
| Adherence needs three things: measurable usage, an operationalized intended use, and a justification of that intended use. | SE90 (Sieverink 2017, DOI 10.2196/jmir.8578) |
| Without a justified intended use, the measure is "actual usage", not adherence. | SE92 (Sieverink 2017, DOI 10.2196/jmir.8578) |
| The goal or assumed working mechanism should define intended use and adherence measures. | SE93 (Sieverink 2017, DOI 10.2196/jmir.8578) |
| Field practice: of 62 evaluations, 34 used "the more use, the better"; 28 set an intended-use threshold; 6 justified it. | SE91 (Sieverink 2017, DOI 10.2196/jmir.8578) |
| Sustained engagement is not always required; establish "effective engagement", sufficient engagement to achieve the intended outcomes, for each intervention. | SE86, SE87 (Michie 2017, DOI 10.2196/jmir.7126) |
| Optimal dose: a predefined engagement level at which a specific intervention is effective; it may vary by user. | SE83 (Perski 2017, DOI 10.1007/s13142-016-0453-1) |
| Receipt (understands and can perform the skill) differs from enactment (uses the skill). | SE85 (Perski 2017, DOI 10.1007/s13142-016-0453-1) |

So: a figure is called "adherence" only when the person has an intended use with a stated justification; otherwise it is "usage". Whether an engagement level is "effective engagement" is a hypothesis the A1 plan and A2 check test; this skill never calls a usage level effective.

## 3. Definitions the person picks

| Rule | Rows |
|---|---|
| Three measurement routes: self-report or qualitative, automated usage logs, physiological correlates. Name which one each figure comes from. | SE80 (Perski 2017, DOI 10.1007/s13142-016-0453-1) |
| Engagement varies within and across people over time; a single snapshot misleads. Report by week. | SE79 (Perski 2017, DOI 10.1007/s13142-016-0453-1) |
| Define how use and engagement were measured; report usage outcomes; state how attrition-related missing data were handled. | SE95 (CONSORT-EHEALTH, DOI 10.2196/jmir.1923) |
| An attrition diagram (login behavior per group over time as a survival curve) is "highly encouraged". | SE96 (CONSORT-EHEALTH, DOI 10.2196/jmir.1923) |
| Describe intended doses and timing and the usage instructions users received. | SE97 (CONSORT-EHEALTH, DOI 10.2196/jmir.1923) |
| State the version evaluated and whether content was frozen or changed during the period. | SE98 (CONSORT-EHEALTH, DOI 10.2196/jmir.1923) |
| Where nonuse or harms are observed, some qualitative analysis should be part of the report. | SE99 (CONSORT-EHEALTH, DOI 10.2196/jmir.1923) |

Every definition (what counts as a session, an active week, discontinuation, completion; the window; the denominator) is the person's, written down before the data are read, as in A1. A definition chosen after the data were read is labeled so and its result is reported as exploratory, never compared with a threshold.

## 4. DiGAV § 23c definitions, where the product is a DiGA

Use these only where the person says the product is a DiGA (or asks for these definitions). Whether the DiGAV applies is `dh-regulatory-and-quality` regulatory-pathway-and-classification's question.

| Item | Definition as the DiGAV states it | Rows |
|---|---|---|
| What is reported | Usage volume, usage frequency, discontinuation; from first use to the end of the prescribed period, capped at 90 days for longer periods | SE70 |
| Usage volume | Average minutes of use per week; users who discontinued are included | SE71 |
| Usage frequency | Average number of sessions ("Nutzungsvorgänge") per week | SE71 |
| Discontinuation | Three consecutive weeks without use (period of 90 days or more), or 25 percent of the period without use (shorter periods); resuming later does not undo it | SE72 |
| Reporting items | Number and share discontinuing, weekly distribution of discontinuations, number and share completing, mean days to discontinuation | SE73 |
| Publication | BfArM publishes outcome-measurement results once a manufacturer first reports usage frequency data from at least 200 users in a calendar quarter | SE77 |
| Change status | Changes to the outcome-measurement results are not significant changes under § 18 | SE69 |
| Later items | Patient-reported health status near the end of the period and satisfaction near the midpoint, dropouts included; first such report due 15 April 2028; indication-specific questionnaires from 1 January 2028 | SE74 to SE76 |

The DiGAV discontinuation rule is a regulator-set definition, not a target (SE72). It does not say which day counts as the day of discontinuation; `scripts/engagement_read.py` counts the days from first use to the last use before the qualifying gap and says so in its output. The person confirms or replaces that reading.

## 5. Engagement-linked risks go to A4

| Fact | Rows |
|---|---|
| FDA's EndeavorRx risk table lists "screen addiction" and "decreased sleep quality" among risks to health, each mitigated by labeling and clinical performance testing. | SE16 |
| 882.5705 requires measuring any increase in disturbed sleep or sleepiness with a validated measure. | SE4 |
| DHAC 2025 (advisory): for children, safety measures could include monitoring and limiting screen time. | SE29 |
| Engagement mechanics can carry risks to health that go into the risk file, not only into growth metrics. | Research file "Changes and conflicts" 4 |

If the person's usage data show very high use where the design named an overuse or screen-time risk, A3 reports the figure as a level and hands it to A4 as a candidate signal. Whether it is a risk to health is not decided here.

## 6. Gamification evidence, as context only

| Fact | Rows |
|---|---|
| 19 papers: 59 percent positive, 41 percent mixed, mostly moderate or lower quality; many lacked a non-gamified comparator. | SE102, SE103 (Johnson 2016, DOI 10.1016/j.invent.2016.10.002) |
| Mental health apps: gamification is not driven by behavior change theory and is often a black box. | SE105 (Cheng 2019, DOI 10.2196/13717) |
| Physical activity: Hedges g 0.42 overall, 0.23 against an active non-gamified control; further rigorous trials needed. | SE106 to SE108 (Mazeas 2022, DOI 10.2196/26779) |

These describe published bodies of evidence. None is a benchmark for the person's product.

## Never

- State a benchmark, a "good" retention rate or a target (none is sourced).
- Call a usage level "effective", "adherent" or a mechanic "safe", "effective" or "compliant".
- Read engagement as the outcome, or a rise in engagement as evidence the product works.
- Impute missing usage, or drop discontinued users from usage means (SE71 includes them where the DiGAV applies; elsewhere the person's definition says).
