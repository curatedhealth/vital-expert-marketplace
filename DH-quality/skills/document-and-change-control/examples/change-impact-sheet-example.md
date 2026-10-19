# Change question sheet: CR-0142 (illustrative)

Device: Illustrative insulin dose calculator app, US 510(k) cleared (person's K number not given), EU MDR class IIb under a technical documentation assessment certificate (as the person states)
Change: Release 4.0: (a) code changes to support a new major iOS version, including how dose alerts are processed while the app runs in the background; (b) dose recommendations rounded to 0.5 unit instead of 1 unit.

## FDA software-change questions (final guidance, 25 October 2017; predates the QMSR, CH10)
Scope: 510(k)-cleared device or De Novo baseline; not PMA or 510(k)-exempt devices (QX10, QX33)

| # | Question | Answer | Basis given | What the source says about this answer | Row |
|---|---|---|---|---|---|
| PRE0 | Is the change made with the intent to significantly affect safety or effectiveness (e.g. to significantly improve clinical outcomes or mitigate a known risk)? | not answered [GAP] |  |  | QX35 |
| PRE1 | Has a risk-based assessment of whether the change could significantly affect safety or effectiveness been done? | yes | Risk assessment RA-0142 rev 1 |  | CH11 |
| PRE2 | Have unintended consequences of the change been considered, not only the intended effect? | unknown | Background-processing side effects not yet assessed |  | QX21 |
| PRE3 | Is the comparison made against the most recently cleared device (give its K or DEN number)? | no | Baseline K number not stated in the change request | The comparison baseline is the most recently cleared device (QX18, QX33). | QX18, QX33 |
| PRE4 | Has this change been assessed on its own and together with the other changes made since that clearance? | no | Releases 3.2 and 3.3 since the last clearance not reviewed together | Assess each change separately and in aggregate; cumulative changes can cross the threshold (QX12, QX13). | QX12, QX13 |
| Q1 | Is the change made solely to strengthen cybersecurity, with no other impact on the software or device? | no | Not a cybersecurity change | Go on to Q2. | CH12 |
| Q2 | Is the change made solely to return the system to the specification of the most recently cleared device? | no | New behavior, not a return to specification | Go on to Q3a. | CH13 |
| Q3a1 | Does the change create a new, or modify an existing, hazard, hazardous situation or cause in the risk management file? | yes | RMF hazard H-07 (dose miscalculation) cause list modified by rounding change |  | CH14 |
| Q3a2 | Is the harm of that hazard, situation or cause serious or worse, judged on the pre-mitigation risk score? | yes | H-07 severity: serious (pre-mitigation) |  | CH14, QX19 |
| Q3a3 | Is it not already effectively mitigated in the most recently cleared device? | unknown | Owner to confirm whether existing control C-07 covers 0.5 unit rounding |  | QX18 |
| Q3b | Does the change create or need a new or modified risk control for a hazardous situation that could result in significant harm? | unknown |  |  | CH15 |
| Q4 | Could the change significantly affect clinical functionality or performance specifications directly associated with the intended use? | yes | Dose output resolution is a performance specification tied to intended use (SRS-112) | Source: a new 510(k) is likely required (CH16). | CH16, QX17 |
| POST1 | Did verification or validation produce any unexpected result? | not answered [GAP] |  |  | QX15, QX16 |

- Q3a: not all three criteria answered; Q3a cannot be read.

## FDA PCCP (final guidance reissued 18 August 2025, AI US-01) and section 515C
Scope: AI-enabled devices through 510(k), De Novo or PMA (AI US-02)

| # | Question | Answer | Basis given | What the source says about this answer | Row |
|---|---|---|---|---|---|
| P1 | Was a PCCP authorized with this device's marketing authorization? | no | No PCCP in the authorization, per the person | No PCCP applies; walk the FDA software-change questions or the PMA route. | AI US-10 |
| P2 | Is this modification specified in the PCCP's Description of Modifications? | not applicable (P1 answered no) |  |  | AI US-04 |
| P3 | Was it implemented and verified per the Modification Protocol, meeting its acceptance criteria? | not applicable (P1 answered no) |  |  | AI US-05, AI US-12 |
| P4 | Does the device stay within its intended use? | not applicable (P1 answered no) |  |  | AI US-08 |
| P5 | Is there any deviation from the authorized PCCP? | not applicable (P1 answered no) |  |  | AI US-13 |

## MDR certified devices: Annex IX 4.10 and 2.4; MDCG 2025-6 on pre-determined AI changes
Scope: Devices under an MDR certificate issued by a notified body

| # | Question | Answer | Basis given | What the source says about this answer | Row |
|---|---|---|---|---|---|
| X1 | Is the device covered by an EU technical documentation assessment certificate? | yes | Certificate as stated by the person |  | QX30 |
| X2 | Could the change affect the safety and performance of the device or the conditions prescribed for use? | yes | Dose output changes the conditions of use of the dose recommendation | Source: changes of this kind require approval of the notified body that issued the certificate; the manufacturer informs it of the plan; the notified body decides between a new conformity assessment and a supplement (QX30, QX31). | QX30, QX31 |
| X3 | Is it a substantial change to the QMS or to the device range covered? | no | No QMS change |  | EU24 |
| X4 | For an AI-enabled device: was this change pre-determined and assessed at the initial conformity assessment, and documented under AI Act Annex IV point 2(f)? | no | Not an AI-enabled device, per the person |  | AI EU-30, AI EU-05 |

## Changes applied to devices already in use: corrections, removals, FSCA
Scope: US 21 CFR 806; EU MDR Article 2(68) and 87

| # | Question | Answer | Basis given | What the source says about this answer | Row |
|---|---|---|---|---|---|
| F1 | Will the change be applied to devices already in use (for example a pushed software update)? | yes | Pushed through the app stores to installed base | A correction includes modification or adjustment without physical removal (VG25). | VG25 |
| F2 | US: is it made to reduce a risk to health, or to remedy a violation that may present a risk to health? | no | Feature change, not made to reduce a risk to health | Source: improvements that do not reduce a risk to health are exempt from reporting (VG23); a record with a justification reviewed by a designated person is still kept (VG24). | VG22, VG23 |
| F3 | EU: is it taken for technical or medical reasons to prevent or reduce the risk of a serious incident? | no | Not taken to prevent a serious incident |  | VG3, VG8 |

Open questions: fda_sw:PRE0, fda_sw:PRE2, fda_sw:Q3a3, fda_sw:Q3b, fda_sw:POST1

Decision: for the owner. This sheet records answers and what the sources say; it does not decide whether a submission, notification or approval is needed.
