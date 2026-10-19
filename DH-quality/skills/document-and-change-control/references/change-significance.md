# Change significance: the decision logic of each framework

Interpretive reference for tasks A2 and B1. Each step cites its row: QS, EU, VG and CH rows in `QUALITY_SYSTEMS.md`; US, EU and UK rows of the AI file in `AI_ML_REGULATION.md` (cited as AI US-12 and so on); QX rows in `supplementary-rows.md`. Read on 19 October 2026.

The model lays out each question, the answer the person gave, and what the source says that answer points to. The person's regulatory owner decides. Every "points toward" below is the source's own hedge ("likely required", "likely not required"); none is a determination.

## 0. Which frameworks apply

| The device | Framework to walk | Rows |
|---|---|---|
| US, cleared by 510(k) (or authorized by De Novo, used as the comparison baseline) | FDA software-change questions (section 1) | CH9, QX10, QX33, QX35 to QX37 |
| US, with an authorized PCCP | Check the PCCP first (section 2); then section 1 for anything outside it | AI US-10, AI US-12 |
| US, PMA | Section 515C for PCCP changes (AI US-15). Other PMA change rules are `[GAP]` here: the 2017 guidance does not address PMA devices (QX10) | QX10, AI US-15 |
| US, 510(k)-exempt | Not addressed by the 2017 guidance (QX10); rules `[GAP]` here | QX10 |
| EU, legacy device under an MDD or AIMDD certificate or declaration | MDCG 2020-3 Rev.1 (section 3) | CH1 to CH8, QX22 to QX29, QX34, QX38 |
| EU, MDR certificate after technical documentation assessment | Annex IX 4.10 (section 4) | QX30, QX31 |
| EU, MDR QMS or device range change | Annex IX 2.4 (section 4) | EU24 |
| EU, AI-enabled device with pre-determined changes | MDCG 2025-6 and AI Act Article 43(4) (section 4) | AI EU-30, AI EU-05 |
| UK | No UK change-significance rule is sourced here: `[GAP]`. MHRA stated it will issue PCCP draft guidance for comment (government response published 6 October 2026) | AI UK-04 |
| Any market, a fix to devices already in use | Corrections, removals and field safety corrective actions (section 5) | VG22 to VG25, VG3, VG8 |

Always, whatever the market: the change goes through the QMS change process and is "adequately evaluated for risk and impact on products and processes prior to implementation" (QS34), and the risk file is reviewed when new information emerges (QS22, EU15).

## 1. FDA: Deciding When to Submit a 510(k) for a Software Change (25 October 2017, final)

Status: final guidance issued 25 October 2017 (CH9). FDA notes it predates the QMSR and asks manufacturers to check the current QMSR (CH10). Its own QS citations (820.30 and others) are to the retired regulation.

**Before the questions**
- Ask what the change is meant to do. If the intent is to significantly affect safety or effectiveness (for example, to significantly improve clinical outcomes or to mitigate a known risk), the guidance treats it as a change that could, and says a new 510(k) is "likely required" regardless of the questions (QX35). Whether the intended effect is significant is the owner's answer.
- Start with a risk-based assessment of whether the change could significantly affect safety or effectiveness, positively or negatively (CH11).
- Consider unintended consequences, not only the intended effect (QX21).
- Assess each change separately and in aggregate (QX12); compare with the most recently cleared device (QX18, QX33); cumulative changes that cross the threshold call for a new 510(k) (QX13).
- Non-software changes, such as labeling, go to the general change guidance, whose content is `[GAP]` here (QX11).

**The questions**

| # | Question (source wording, shortened) | If the answer is yes, the source says | Row |
|---|---|---|---|
| 1 | Made solely to strengthen cybersecurity, with no other impact? | "In many cases" a new 510(k) is not likely required | CH12 |
| 2 | Made solely to return the system to the specification of the most recently cleared device? | A new 510(k) is "likely not required"; the impact must still be evaluated | CH13 |
| 3a | Does it create or modify a hazard, hazardous situation or cause; is the harm serious or worse (pre-mitigation); and is it not already effectively mitigated in the most recently cleared device? | If all three hold, a new 510(k) is "likely required" | CH14, QX18, QX19 |
| 3b | Does it create or need a new or changed risk control to prevent significant harm? | "Likely required"; redundant or enhanced controls generally not | CH15 |
| 4 | Could it significantly affect clinical functionality or performance specifications tied to intended use? | "Likely required". Indications or intended-use changes are outside this question | CH16, QX17 |

"Significant harm" means a risk level of serious or worse, for example injury needing professional medical intervention (QX19).

**After the questions**
- If the conclusion is no new 510(k), document the basis (QX14) and the change (QX13). The records must be available to an FDA investigator on request (QX20).
- Unexpected verification or validation results reopen the decision (QX15). Passing V&V does not override a finding that the change could significantly affect safety or effectiveness (QX16).

**Change types (Section VI)**: infrastructure changes (compilers, languages, drivers, libraries, so a runtime or library upgrade belongs here) are weighed by complexity, and large V&V script changes are a signal (QX36); architecture changes, such as porting to a new OS or new middleware, may impact overall performance or extend the operating environment (QX37); core algorithm changes go through the questions, and a complete rewrite may need a new 510(k) even with unchanged claims (QX37). FDA invites discussion of these "gray areas" with the reviewing Office and Division (QX36).

## 2. PCCP (AI-enabled devices, final guidance reissued 18 August 2025)

Status: final guidance first issued 4 December 2024, reissued 18 August 2025 (AI US-01); applies to AI-enabled devices through 510(k), De Novo and PMA (AI US-02). Its quality-system citations predate the QMSR (AI file, conflicts note 2).

| # | Question | What the source says | Row |
|---|---|---|---|
| P1 | Was a PCCP authorized with this device's marketing authorization? | A PCCP is authorized as part of the marketing authorization, never in a Pre-Submission | AI US-10 |
| P2 | Is the modification specified in the Description of Modifications? | The Description sets the specifications of the planned changes | AI US-04 |
| P3 | Was it implemented and verified per the Modification Protocol, meeting its acceptance criteria? | If consistent with the PCCP, no new submission is needed; document the modification and analysis in the quality system | AI US-05, AI US-12 |
| P4 | Does it keep the device within its intended use? | Modifications in a PCCP must maintain the intended use | AI US-08 |
| P5 | Any deviation from the authorized PCCP? | Deviations "would generally cause the device to be adulterated and misbranded" | AI US-13 |

If P1 is no, or any of P2 to P4 is no, the change goes through section 1 (or the PMA route). The library's authorization records do not show whether a PCCP was authorized (`references/tools.md`); ask the person and cite their authorization letter.

## 3. EU legacy devices: MDCG 2020-3 Rev.1 (May 2023)

Scope: legacy devices kept on the market under Article 120 until 31 December 2027 or 31 December 2028 by class (CH1), on conditions that include "no significant changes in the design and intended purpose" and an MDR QMS in place by 26 May 2024 (CH2). The guidance clarifies that condition (CH3).

- Two cumulative tests: there is a change in design or intended purpose, and it is significant (CH4). The manufacturer justifies, case by case, and documents the outcome for the competent authority (QX22).
- Administrative and manufacturing-process changes are generally not design changes (QX28).
- Main chart order: change related to corrective actions first, then A intended purpose, B design, C software, D substance or material, E sterilization (QX24).
- Software is assessed primarily with Chart C; a major software change that alters the control mechanism or operating principle goes to Chart B (CH5).
- Chart C asks C1 new or major OS or component change; C2 new or modified architecture or database structure, or an algorithm change; C3 user input replaced by a closed loop; C4 new user interface, medical feature, interoperability channel or data presentation; C5 negative effect on the benefit-risk ratio (QX23). The branch arrows did not survive text extraction; the significant and non-significant examples in the body text are the guide to reading each answer.
- Non-significant examples: bug fix back to original specification, latency improvements, security updates, non-medical features (CH6), an algorithm change impacting device control "without alteration of diagnosis or treatment" (QX38), third-party OS updates, UI appearance changes without new functions (QX25), valid only if the benefit-risk ratio is not negatively affected (CH7).
- Significant examples: OS change requiring software modification (QX26), new architecture, a "change of an algorithm which impact the operating principles or impact the control of the device and may alter the diagnosis or therapy delivered", closed loop replacing user input, new medical features, new interoperability channels (CH8), a change in how data is read such that treatment may be altered (QX27).
- Consequence: a non-significant change may be implemented without MDR certification during the transition (QX29); for devices under a notified body certificate, changes are verified by the notified body in surveillance or on prior-approval submission (QX34).

## 4. EU MDR certified devices

- **Annex IX 4.10:** changes to a device under an EU technical documentation assessment certificate need that notified body's approval where they "could affect the safety and performance of the device or the conditions prescribed for use"; where the manufacturer plans a change of that kind it informs the notified body ("any of the above-mentioned changes", QX30). Whether the change could so affect is the owner's assessment, recorded with its basis; do not state that every change must be notified, or that none need be. The notified body, not the manufacturer, decides whether a new conformity assessment or a certificate supplement is needed (QX31).
- **Annex IX 2.4:** plans for substantial changes to the QMS or the device range go to the notified body that approved the QMS (EU24).
- **Annex X 5.2:** for type-examination certificates, the equivalent approval rule (QX32).
- **AI-enabled devices:** changes pre-determined and assessed at initial conformity assessment are not a substantial modification and not a change under Annex IX 4.10 (AI EU-30; AI Act Article 43(4), AI EU-05). EU PCCP guidance is under development at IMDRF level (AI EU-31).
- No MDCG guidance on what counts as a change that "could affect the safety and performance" for MDR-certified devices is sourced here: `[GAP]`. MDCG 2020-3 is written for legacy devices; using its charts for an MDR-certified device is the owner's call and must be labeled as an analogy.

## 5. When the change fixes devices already in the field

| Market | Rule | Row |
|---|---|---|
| US | A correction includes modification or adjustment without physical removal | VG25 |
| US | Corrections or removals to reduce a risk to health are reported within 10 working days of initiation | VG22 |
| US | Improvements that do not reduce a risk to health are exempt from reporting | VG23 |
| US | Unreported corrections still need a record with a justification reviewed by a designated person | VG24 |
| EU | A field safety corrective action is corrective action for technical or medical reasons to prevent or reduce the risk of a serious incident | VG3 |
| EU | Except in urgency, an FSCA is reported before it is undertaken | VG8 |

Whether a fix is a reportable correction or an FSCA is the owner's decision; lay out the definitions and the facts.

## 6. Context from public safety data (library)

Recalls of released software versions show what a change can do once in the field, for example a Class I recall of a CGM app version that "can cause the app to terminate unexpectedly" (library, `search_safety_events`, event date 28 August 2025, saved in `examples/live/`). Use such rows as context for the risk questions, described only by what the row states. They are never evidence about the person's change.
