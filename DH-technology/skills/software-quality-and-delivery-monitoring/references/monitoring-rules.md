# Monitoring rules: what the sources say, row by row

Source: `engineering-interop-security-research.md` (EN rows, read 20 October 2026), `quality-systems-research.md` (QS, EU, ST and CH rows, read 19 October 2026), `product-lifecycle-research.md` (PL rows, read 20 October 2026) and `ai-ml-regulation-research.md` (cited as AI US-nn, read 19 October 2026). Interpretive reference for A1, A2 and B1. Every line carries its row. In answers, cite each fact by source name and date in plain words with the row id after it (`gap-rules.md`, "How to cite"). Rows marked [WF] were read through a summarizing fetch: say so when a fact rests on one. A fact not in a row is `[GAP]`.

**The rule that shapes this skill.** No source read for this skill sets a threshold for any measure it reads: no trace coverage figure, no acceptable count of cases run on an older build, no deploy frequency, change failure rate, rollback rate, recovery time, capacity margin, utilization ceiling, latency or uptime target, and no number of days a component may run past end of support. Industry benchmarks (for example published DevOps survey tiers) are not in the sources. The person's pass rules are the only rules; the model counts and reads against them and never supplies one.

## 1. V&V completeness (A1; old DH-04.03.2.2 and DH-04.03.4.2 tasks)

| Rule | As the source states it | Row |
|---|---|---|
| Requirements baseline | Validation cannot be completed without an established SRS | EN-006 |
| Verification and validation | Verification is phase output against phase input, including traceability analyses; validation is specifications against user needs and intended uses | PL21, PL22 |
| Effort follows hazard | The testing effort varies with the safety risk of the automated function | EN-005 |
| Any change re-opens validation | Validation status re-established after any change, with system-wide impact analysis | EN-008 |
| Regression | Unchanged but vulnerable portions shown not adversely affected | EN-009 |
| Inspection element | Design and development software validation is a minimum element in inspection model 2 (CP 7382.850, 2 February 2026) | QS33 |
| Risk drives the inspection | Investigators review risk management documentation throughout the inspection | QS31 |
| Risk files kept current | Reviewed and updated when unforeseen risks or new information emerge | QS22 |
| Unresolved anomalies | A list with each anomaly's impact on safety and effectiveness belongs in a US submission | PL20 |
| Version history | Tested versions with dates and change descriptions | PL20 |
| IEC 62304 scope | Lifecycle requirements, not validation and final release | ST6, PL105 |

Old task rules kept as checks: every hazard points to at least one verification or validation case, and a hazard with no case is an open gap; a unit test that does not exercise the hazard does not count (the script flags hazards covered only by unit-level cases for the person to judge); cases are compared with the release candidate build and cases run on an older build are listed for repeat or explicit waiver; a pass is not carried across a build that changed the hazardous function; the class statement is read against the current hazard (an item the person marks as able to influence a clinical action, with a class the person's own procedure treats as lowest, is listed for the person; the model never reclassifies); a class never tied to a hazard is flagged; a plan is opened and checked to name this product, and a template not filled for this product is not counted.

**Not sourced.** IEC 62304 class definitions and class-by-class plan lists are paywalled (EN research file, "Not sourced"): the plan list checked is the one the person's procedure states.

## 2. Delivery and pipeline (A2; old DH-04.03.3.2 tasks)

| Rule | As the source states it | Row |
|---|---|---|
| No CI/CD-specific regulator text | No FDA or EU source found that addresses pipelines or continuous deployment of device software directly | EN research file, "Not sourced" |
| Change control area | Changes evaluated for risk and impact before implementation; software changes are an element (ISO 13485 4.1.6, 7.5.6, 7.6) | QS34 |
| Digital records | System logs and audit trails are recommended assurance evidence for production and QMS software | EN-022 |
| CSA record | Who tested and when, issues found, conclusion, approval where appropriate | EN-020 |
| PCCP changes | A change consistent with the authorized PCCP needs no new submission but is documented in the quality system; deviation generally makes the device adulterated and misbranded; detect-and-revert mechanisms | AI US-12, AI US-13, AI US-31 |

Old task rules kept as checks: deploys and rollbacks counted over a period the person states; a failed health check kept apart from a reverted clinical defect; the stage that caught each failure named, or "caught in production"; a green dashboard is not reported as zero failures; releases compared with the required stage list; hotfix exceptions listed and whether each was recorded at the time; an unrecorded skip is not treated as a hotfix.

## 3. Platform capacity, first failure and residency (A2; old DH-04.03.1.2 and DH-01.06.4.2.1)

| Rule | As the source states it | Row |
|---|---|---|
| Offshore storage [WF] | Storage outside the US is permitted with a BAA; location can raise risk the risk analysis must address | EN-034 |
| Cloud provider is a business associate [WF] | Even without a decryption key; Security Rule standards apply | EN-032, EN-033 |
| Activity review | Regular review of audit logs, access reports and incident tracking (HIPAA, required) | EN-101 |
| Contingency | Backup, disaster recovery and emergency mode plans required; testing addressable | EN-102 |
| EU reliability | Repeatability, reliability and performance in line with intended use (MDR Annex I 17.1) | EU20 |
| CSA continuous monitoring | Continuous performance and data monitoring are accepted assurance methods for production and QMS software | EN-016 |

Old task rules kept as checks: a scale claim is compared with the latest load result or production peak for the same unit, with its date and environment; a cloud quota is not a load test; errors and saturation are read on the component the design said would fail first, and saturation on another component is shown, never hidden; the live store region is compared with the placement table; a replica or backup that leaves the region is flagged; a backup is never assumed to stay in the primary region. **Not sourced:** any capacity margin, utilization ceiling, uptime or recovery figure, and GDPR international transfer rules (`[GAP]`; transfers route to `cybersecurity-and-privacy-by-design`, this pack).

## 4. Components, SBOM and known vulnerabilities (A2)

| Rule | As the source states it | Row |
|---|---|---|
| SBOM support fields | Level of support (maintained, no longer maintained, abandoned) and end-of-support date per component | EN-054 |
| SBOM in a cyber device submission | Commercial, open-source and off-the-shelf components (524B(b)(3)) | EN-045 |
| KEV designed out | Vulnerabilities in CISA's Known Exploited Vulnerabilities Catalog should be designed out of the device | EN-052 |
| KEV as input [WF] | CISA says use KEV as an input to vulnerability management prioritization; an entry needs a CVE id, evidence of active exploitation and a clear remediation action | EN-080, EN-081 |
| Patch cadence (statute) | Known unacceptable vulnerabilities on a justified regular cycle; critical vulnerabilities that could cause uncontrolled risks out of cycle as soon as possible | EN-044 |
| Uncontrolled risk clocks (enforcement policy) | Communicate within 30 days, fix within 60 days to benefit from FDA's 806 enforcement policy; not a statutory deadline | EN-066, EN-067 |
| Controlled versus uncontrolled risk | Defined by residual risk of patient harm | EN-063, EN-064 |
| Routine patches | Patches for controlled risk generally need no 806 report | EN-065 |
| EU products outside MDR | CRA support period at least five years unless expected use is shorter; MDR devices excluded | EN-091, EN-086 |

The script matches the person's SBOM against a KEV list only when the person supplies one (CVE ids); the skill names vulnerabilities by their public identifiers only and never describes how to exploit them. Whether a vulnerability is controlled or uncontrolled, and the patch priority, are the person's: route to `security-and-privacy-operations-monitoring` (this pack).

## 5. Public signals: recalls of comparable software (A2)

FDA recall records and MHRA alerts in the library are read as their records state them (`tools.md`). A recall of another firm's software is a signal the person may weigh for their own hazards (risk files are updated with new information, QS22); the skill never judges relevance and never treats an empty search as evidence of safety. Reportability, corrections and removals route to `dh-regulatory-and-quality` audit-capa-and-complaints.

## 6. Release gate and miss owners (B1; old DH-04.03.2.2.3, DH-04.03.4.2.3, DH-04.03.3.2.3, DH-01.06.4.2.2, DH-01.06.4.2.3)

No source sets a release criterion (`medical-software-lifecycle-and-delivery`, this pack, delivery rules section 5). Old task rules kept as steps, with the person's words in each slot: the pass rule is written before any unit is scored (elements that count, pass or fail per element, the element that blocks release); a validation miss states whether it blocks release, who accepted it and what the user is told, or the owner of the fix; a miss is never closed by editing the expected result after the run; the gate decision is recorded against the build id with a named acceptor ("Do not ship class C on an informal chat approval" is the old rule's wording, kept as a record requirement, not a class judgment); the pipeline stage that fails or is skipped gets a named owner and a named next release that should show the change ("Do not assign the whole platform team"); a failed architecture element gets the owner and recheck date the person sets, or "stopped", and is not closed because an earlier assessment described it.
