# Engagement rules

Interpretive reference for A3 (engagement mechanics design). Every rule cites its row in `safety-and-engagement-research.md` (SE) or `therapeutic-mechanism-research.md` (TM). The person decides which mechanics ship, what counts as effective engagement for their product, any intended-use threshold and any limit on a mechanic. This file lists what the sources name; it never sets a benchmark or a target.

No primary source in this skill sets an engagement benchmark, a retention target or a "good" completion rate (research file "Not sourced"). The DiGAV defines discontinuation and the items to report (SE72, SE73) without a target, and MDCG 2025-10 asks the manufacturer to set its own thresholds (SE63) without values. Any number of that kind is the person's.

## 1. Engagement is a proximal outcome, not the outcome

| Rule | Rows |
|---|---|
| Engagement and fatigue are proximal outcomes an adaptive intervention should track to prevent abandonment; they sit on the chain, before the change and the outcome. | TM87 (JITAI, DOI 10.1007/s12160-016-9830-8) |
| Engagement is shaped by the intervention (content and delivery), the context (setting and population) and the target behavior; engagement in turn moderates the intervention's effect on its mechanisms of action. | SE78 (Perski 2017, DOI 10.1007/s13142-016-0453-1) |
| An unmeasured third variable, such as higher baseline motivation, may explain both more engagement and better outcomes: a usage-outcome correlation is not causal evidence. | SE82 (Perski 2017, DOI 10.1007/s13142-016-0453-1) |
| Usage correlates with behavioral outcomes, but often not strongly. | SE88 (Michie 2017, DOI 10.2196/jmir.7126) |
| FDA's Digital Health Advisory Committee (November 2025) said the relationship between engagement, adherence, symptoms and outcomes may not be well understood and will be important to characterize. Committee advice, non-binding. | SE26 |
| The DiGAV requires usage to be reported (volume, frequency, discontinuation) without making usage a benefit. | SE70 to SE73; research file "Changes and conflicts" 5 |

Consequence for A3: every engagement metric is written as a proximal outcome on a named link. It is never written as the product's outcome, and a rise in usage is never written as evidence the product works (N3).

## 2. Tie each mechanic to a link

| Rule | Rows |
|---|---|
| The goal or the assumed working mechanism should lead when defining intended use and choosing adherence measures. | SE93 (Sieverink 2017, DOI 10.2196/jmir.8578) |
| Users may engage most with the features they enjoy, while less popular features carry the effect ("popular" versus "effective" features). | SE84 (Perski 2017, DOI 10.1007/s13142-016-0453-1) |
| Receipt (the user understands and can perform the skill) differs from enactment (the user uses the skill). | SE85 (Perski 2017, DOI 10.1007/s13142-016-0453-1) |
| Gamification in mental health apps is not driven by behavior change theory, and is often treated as a black box. | SE105 (Cheng 2019, DOI 10.2196/13717) |
| Each component is tied to one link of the mechanism; a component tied to no link is listed as left out or proposed for removal. | TM8, TM11 (MRC/NIHR, DOI 10.1136/bmj.n2061); A2 old task rule |

Consequence for A3: each mechanic (cue, reminder, streak, points, levels, reward, narrative, social feature, lock-out, unlock sequence) names the link it serves (most often the user action link) and the A2 component it supports. A mechanic tied to no link goes on the "not tied" list for the person to decide. Where the person names a mechanic as serving only usage, say so: it is a usage mechanic, not a therapy component.

## 3. Effective engagement versus usage

| Rule | Rows |
|---|---|
| Sustained engagement is not always required; for each intervention, establish "effective engagement", meaning sufficient engagement to achieve the intended outcomes. | SE86 (Michie 2017, DOI 10.2196/jmir.7126) |
| Specify and establish empirically what effective engagement is for each intervention. | SE87 (Michie 2017, DOI 10.2196/jmir.7126) |
| Optimal dose is a predefined level of engagement at which a specific intervention is effective; it may vary by user. | SE83 (Perski 2017, DOI 10.1007/s13142-016-0453-1) |
| Engagement is dynamic within and across individuals over time; one snapshot metric misleads. | SE79 (Perski 2017, DOI 10.1007/s13142-016-0453-1) |
| Three measurement routes: self-report or qualitative, automated usage logs, physiological correlates. | SE80 (Perski 2017, DOI 10.1007/s13142-016-0453-1) |
| Adherence needs three things: measurable usage, an operationalized intended use, and a justification of that intended use. | SE90 (Sieverink 2017, DOI 10.2196/jmir.8578) |
| Of 62 evaluations, 34 used "the more use, the better", 28 set a threshold and 6 justified it. | SE91 (Sieverink 2017, DOI 10.2196/jmir.8578) |
| Without a justified intended use, the measure is "actual usage", not adherence. | SE92 (Sieverink 2017, DOI 10.2196/jmir.8578) |
| Describe use parameters (intended doses and timing) and the usage instructions users received; define and measure use and engagement. | SE97, SE95 (CONSORT-EHEALTH, DOI 10.2196/jmir.1923) |

Consequence for A3: for each mechanic, write (a) the usage measure, (b) the intended use as the person operationalizes it, and (c) the person's justification. If (b) or (c) is missing, the column reads "usage, not adherence (SE92)" and the definition of effective engagement stays open for the person. The model never fills an intended-use threshold.

## 4. What gamification papers state (context, not a target)

| What the paper states | Rows |
|---|---|
| Gamification: "the use of game design elements in non-game contexts". | SE101 (Johnson 2016, DOI 10.1016/j.invent.2016.10.002) |
| 19 papers: 59 percent positive, 41 percent mixed, mostly moderate or lower quality; many lacked a non-gamified comparator. | SE102, SE103 (Johnson 2016, DOI 10.1016/j.invent.2016.10.002) |
| In 50 mental health apps, the most common elements were levels or progress feedback, points, rewards, narrative, personalization and customization. | SE104 (Cheng 2019, DOI 10.2196/13717) |
| Physical activity, 16 RCTs: Hedges g 0.42 overall; 0.23 against an active non-gamified control; the authors call for further rigorous trials. | SE106 to SE108 (Mazeas 2022, DOI 10.2196/26779) |

These describe the populations and behaviors the papers studied. They are never transferred to the person's product, and never used as a target.

## 5. Precedent mechanics (record facts only)

| What the record states | Rows |
|---|---|
| EndeavorRx: regimen about 25 minutes per day, 5 days per week, enforced in software by lock-out and reminders. | TM142 |
| EndeavorRx: the pivotal control matched reward and engagement but had different stimuli and no adaptive algorithms. | TM143 |
| EndeavorRx risk table: "Treatment results in screen addiction" and "decreased sleep quality", each mitigated by labeling and clinical performance testing. | SE16 |
| reSET: virtual rewards for lesson completion and negative drug screens; clinics may convert them to tangible rewards. | TM135 |
| reSET-O and reSET recalls of 7 June 2021 (Class II): access to the contingency management wheel spin "regardless of the UDS results". | `examples/live/connector_calls_2026-10-20.json` (`search_safety_events {product_code: "PWE"}`) |

## 6. Limits on mechanics: dark patterns and incentives

Which law applies to the person's product is a legal question for the owner the person names for consumer-protection law, or owner not named. The model lists what each source says and flags the mechanics that match its words. It never says a mechanic is compliant.

| What the source says | Rows | Status |
|---|---|---|
| FTC staff report (September 2022): dark patterns are "design practices that trick or manipulate users into making choices they would not otherwise have made and that may cause harm". | SE109, SE110 | [WF]; staff report, not a rule |
| FTC report: firms answer for the net impression of design elements, not only the words. | SE112 | [WF] |
| FTC report appendix: nagging ("asking repeatedly and disruptively") and confirmshaming ("using shame to steer users away from certain choices"); children's apps named as a setting. | SE113 | [WF] |
| ROSCA (15 U.S.C. 8403): an online subscription must disclose material terms before billing details, get express informed consent, and give simple mechanisms to stop recurring charges. | SE114 | statute |
| The 2024 Negative Option Rule amendments were vacated; the pre-2024 text is back from 12 February 2026; an advance notice opened 13 March 2026. | SE115, SE116 | Federal Register |
| FTC v. Cerebral (telehealth, April 2024): a complex multi-step cancellation was charged under ROSCA; the order requires an easy method to cancel. | SE117 | [WF] |
| FTC Epic Games order (14 March 2023): bars charging through dark patterns or without affirmative consent. | SE118 | [WF] |
| UCPD guidance (2021/C 526/01): no legal definition of "dark pattern", but the UCPD applies to them and no intention is required. | SE126 | Commission guidance |
| UCPD guidance: capturing attention that results in continued use (scrolling, clicking) can be a transactional decision. | SE127 | Commission guidance |
| UCPD guidance: continuous A/B testing and personalized persuasion, together with opacity, distinguish manipulation from strong persuasion. | SE128 | Commission guidance |
| UCPD guidance: vulnerability is dynamic and situational; exploiting it can be undue influence. | SE129 | Commission guidance |
| UCPD guidance: traders should ensure interface design does not distort decisions; confirmshaming could be an aggressive practice. | SE130 | Commission guidance |
| DSA Art. 25: online platforms must not design interfaces that deceive or manipulate; named practices include unequal prominence, repeated requests after a choice, and harder termination than subscription. Binds online platforms only, excludes micro and small enterprises and defers to the UCPD and GDPR. | SE119 to SE125 | regulation |
| AI Act Art. 5(1)(a) and (b): prohibited AI that uses purposefully manipulative or deceptive techniques, or exploits vulnerabilities due to age, disability or social or economic situation, to distort behavior with significant harm. Whether the 2026 omnibus amended Art. 5 was not checked. | SE131, SE132 | regulation |
| Digital interventions can harm through interactions that undermine the desired behavior, inappropriate data sharing, or use instead of more effective interventions. | SE89 (Michie 2017, DOI 10.2196/jmir.7126) | [PAPER] |

Incentives with value outside the app (cash, gift cards, devices, waived fees) to patients covered by public programs: `dh-go-to-market` channel-and-partner-design owns beneficiary-inducement rules; this skill does not hold those rows. A reward's own software logic is a component and a hazard source (section 5; A4).

How to apply: for each mechanic, record whether it uses repeated prompts, shame wording, unequal prominence of choices, a cancellation path harder than sign-up, attention capture designed to extend use, A/B-tested or personalized persuasion, or targeting of a vulnerable group (children, people in crisis). Each match is a flag with its row, for the person and their named owner. A flag is not a finding of unlawfulness; no flag is not a finding of compliance.
