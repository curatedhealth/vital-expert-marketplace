# Post-market expectations: changes, performance monitoring, safety events

Interpretive reference for task A2 and B1. Row prefixes: `AI` = `AI_ML_REGULATION.md`, `RP` = `REG_PATHWAYS_SUBMISSIONS.md`, `Q` = `QUALITY_SYSTEMS.md`. The model sorts and lays out; whether a change is covered, significant or reportable is the person's decision.

## 1. Changes made against an authorized PCCP (US)

| Situation | What the source says | Row |
|---|---|---|
| Change specified in the Description of Modifications and done per the Modification Protocol | No new marketing submission; implement per the protocol and document the change and analysis in the quality system | [AI US-12] |
| Change deviates from the authorized PCCP | Would generally make the device adulterated and misbranded | [AI US-13] |
| Change not in the PCCP at all | Back to the general software-change decision: FDA's "Deciding When to Submit a 510(k) for a Software Change to an Existing Device" (25 October 2017; predates the QMSR) | [Q CH9, CH10] |
| PMA device, change consistent with an approved PCCP | No PMA supplement | [AI US-15] |
| Later 510(k) for the device | Compare to the predicate as cleared before PCCP changes | [AI US-14] |

**The 2017 software-change questions (for changes outside a PCCP).** Start with a risk-based assessment [Q CH11]. A change solely to strengthen cybersecurity is in many cases not likely to need a new 510(k) [Q CH12]. A change that only restores the most recently cleared specification likely does not [Q CH13]. A new 510(k) is likely needed if the change creates or modifies a hazard with serious harm not already mitigated [Q CH14], needs new risk controls to prevent significant harm [Q CH15], or could significantly affect clinical functionality or performance tied to intended use [Q CH16]. The model lays out which question each change touches; the regulatory owner decides.

**Sorting each logged change.** For each change in the person's log, write one of: "in the PCCP as described: protocol steps documented? (person to confirm)"; "in the PCCP but a protocol step is not evidenced"; "outside the PCCP: 2017 questions apply, owner decides"; "not enough detail `[GAP]`". Never write "covered" or "compliant".

## 2. Changes in the EU

- Pre-determined changes assessed at the initial conformity assessment and in Annex IV point 2(f) are not a substantial modification under the AI Act and not a change to the certified device under MDR Annex IX 4.10 [AI EU-05, EU-30].
- Plans for substantial changes to the QMS or device range go to the notified body [Q EU24]. Design changes must be taken into account in a timely manner in the QMS [Q EU2].
- Legacy MDD devices: significant change tests in MDCG 2020-3 Rev.1; software chart C; bug fixes, latency improvements and security updates are non-significant examples only if the risk-benefit ratio is not negatively affected; algorithm changes that may alter diagnosis or therapy are significant examples [Q CH4 to CH8].
- AI Act legacy rule: a high-risk system placed on the market before the Chapter III date is caught once it undergoes significant design changes [AI EU-22].

## 3. Performance monitoring expectations

| Expectation | Status of the source | Row |
|---|---|---|
| FDA anticipates monitoring of safety (for example adverse events) and performance as PCCP changes are implemented; the Modification Protocol describes post-market surveillance plans | Final guidance, 18 August 2025 | [AI US-36] |
| A postmarket performance monitoring plan in the quality system; not generally required for 510(k) unless a special control; may be a PMA condition of approval | Draft guidance, 7 January 2025 | [AI US-37, US-38] |
| FDA's request for comment on measuring real-world performance and drift (docket FDA-2025-N-4203, comments closed 1 December 2025) | Not guidance | [AI US-39] |
| Deployed models are monitored for performance and retraining risk is managed (GMLP principle 10) | Joint principles, 2021 | [AI UK-10] |
| Mechanisms to detect and revert or stop a change that fails its performance criteria (PCCP principle 1) | Joint principles, October 2023 | [AI US-31] |
| AI Act post-market monitoring: active, systematic collection and analysis of performance data over the lifetime; may be integrated into the MDR PMS system | Regulation; date for Annex I devices unclear `[GAP]` | [AI EU-33, EU-34] |
| Commission guidance with a PMM plan template | Due by 2 September 2027 under Regulation (EU) 2026/1744 | [AI EU-35] |
| MDR and AI Act both require post-market monitoring of medical device AI | MDCG 2025-6 (not binding) | [AI EU-36] |
| MDR PMS feedback into risk management | Regulation | [Q EU14, EU15] |

Performance thresholds, drift metrics and alert limits are the person's. The model checks whether each expectation has a named plan, data and owner.

## 4. Safety events and incident clocks

Reportability is the person's decision; the model states the clocks as facts.

| Jurisdiction | Clock | Row |
|---|---|---|
| EU serious incident | Immediately once causality is established or reasonably possible, no later than 15 days after awareness; 10 days for death or unanticipated serious deterioration; 2 days for a serious public health threat | [Q VG4 to VG6] |
| EU counting | Calendar days; awareness day is day 0 | [Q VG12] |
| EU trend reporting | Statistically significant increases in non-serious incidents; method and observation period in the PMS plan | [Q VG9] |
| EU indirect harm | Harm from decisions based on incorrect device output is indirect harm and reportable when it meets serious incident criteria; a software error causing incorrect assessment is a malfunction example | [Q VG14, VG15] |
| US MDR | 30 calendar days; 5 work days when remedial action is needed to prevent unreasonable risk of substantial harm | [Q VG17, VG18] |
| US corrections and removals | Report within 10 working days of initiating [Q VG22]; a correction includes modification or adjustment without physical removal [Q VG25]; unreported corrections still need a record with a reviewed justification [Q VG24] | [Q VG22, VG24, VG25] |
| GB | 15, 10 and 2 days, same structure as the EU, in force since 16 June 2025 | [Q VG28; RP UK-08] |

## 5. What the library shows about safety events

`regulatory-dh.search_safety_events` returns FDA software-related recalls, MAUDE report counts by product code and year, and MHRA alerts. Observed limits on 19 October 2026 (`references/tools.md`): recalls are not filtered by product code; MAUDE counts are per product code and carry no manufacturer; recall rows link to the API endpoint, not the recall record; EU and Swiss events are not loaded. A count of reports is not a count of confirmed events, and an empty result is not evidence of safety.
