# Program purpose, activities and material: what the sources say

Interpretive reference for task A1. Rows: PE- (`patient-engagement-research.md`), PC- (`promotion-and-claims-research.md`), CP- (`channels-partners-research.md`). Read on 19 October 2026; not owner-reviewed. These rows let the model flag wording for the person's regulatory, legal or promotional review owner. They never clear wording.

## 1. Purpose types and the sourced input routes they map to

The person names the purpose. Where it is to bring patient input into development, regulation or HTA, the route below has its own sourced rules.

| Purpose the person states | Route | What the source says | Rows |
|---|---|---|---|
| Collect patient experience data | FDA PFDD | Patient experience data may be collected by patients, caregivers, advocacy organizations, researchers or manufacturers; registries, focus group or meeting reports and surveys count | PE-04, PE-05 |
| Make the input representative | FDA PFDD Guidance 1 | Probability sampling makes results more likely to reflect the target population; non-probability samples may not | PE-06 |
| Find what matters to patients | FDA PFDD Guidance 2 (final February 2022) | Engage early with patients and method experts; saturation has no set criteria | PE-07 to PE-09 |
| Patient preference information for a device | FDA PPI guidance, final 30 March 2026 | Voluntary; most useful when decisions are preference sensitive; recommended study qualities listed | PE-22 to PE-27 |
| Input to an EU joint clinical assessment or consultation | Regulation (EU) 2021/2282 | Patient input in scoping, on draft reports and in consultations; conflict of interest rules | PE-53 to PE-57 |
| Input to EMA | EMA framework (20 January 2022) | Three modes of participation; declarations for individual experts | PE-42 to PE-46 |
| Input to NICE | NICE policy | Comment through organizations, submit evidence; at least two lay members per committee | PE-61, PE-64 |
| Involve the public in research | UK Standards for Public Involvement (a framework, not a rule) | Six standards | PE-65 to PE-68 |
| Education or awareness | No input route | Material rules in section 3 apply in full | PC rows below |

Old method rule kept: do not make advocacy recruitment the purpose of an education program (old task "Programme purpose", CF-12.02.03.2.1.1).

## 2. The action the program will not ask for

The person names it. The rows supply candidates the person may adopt, each labeled "proposed":

- Asking a patient organization to promote a prescription medicine (PE-70) [INDUSTRY].
- Using a patient engagement tool to market other reimbursable items or to recruit patients (CP-US-28).
- Asking patients for testimonials for use in product literature: MHRA treats repeated testimonials as manufacturer claims (PC-UK-03); German public device advertising bars third-party statements used in a misleading way (PC-DE-11).

## 3. What program material may say

Program material addressed to patients is labeling or advertising when it concerns the product. The rows below decide what a model flags for the owner.

| Rule | What to flag | Rows |
|---|---|---|
| Intended use is shown by labeling claims, advertising and oral or written statements | Any program text that describes what the product does for a condition sets or widens intended use | PC-US-17, PC-US-20, PC-EU-03, PC-UK-01 |
| Misleading labeling or advertising, including omission | Benefits stated without material facts | PC-US-01, PC-US-03, PC-US-70 |
| FTC: reasonable basis before dissemination; health benefit claims generally need randomized controlled human testing [WF] | Any benefit claim without its evidence | PC-US-72, PC-US-73 |
| Disclaimers cannot contradict a claim [WF] | "Not medical advice" next to a treatment claim | PC-US-74, PC-UK-02 |
| General wellness products: no disease, diagnostic threshold or clinical-grade wording; disease reference only as "may help reduce the risk of" or "may help living well with" | Program wording for a wellness app that names a disease | PC-US-61, PC-US-63, PC-US-65 |
| MDR Article 7: no misleading claims about intended purpose, safety or performance | Functions the device lacks, uses outside the intended purpose | PC-EU-01, PC-EU-02 |
| UCPD: practices aimed at a vulnerable group are judged from that group's average member; false cure claims and false approval claims are always unfair | Patient-facing material in the EU | PC-EU-06, PC-EU-10, PC-EU-11 |
| UK DMCCA: false prevent, treat or restore claims and false approval claims are always unfair (in force 6 April 2025) | Patient-facing material in the UK | PC-UK-07, PC-UK-08 |
| Germany HWG, public device advertising | Health improvement or fear claims, disguised advertising, testimonials, material aimed at children under 14, listed diseases | PC-DE-03 (efficacy a product does not have), PC-DE-09 to PC-DE-13 |
| Germany DiGA | The DiGA must be free of advertising; DiGA data may not be used for advertising | PC-DE-15, PC-DE-16 |
| CAP Code [INDUSTRY] | Medical claims only for a device with the applicable conformity marking; do not discourage essential treatment | PC-UK-10, PC-UK-11 |

Old method rule kept: an activity may use only the claims or content on its allowed list, and the person's owner approves that list (old task "Programme activity", CF-12.02.03.2.1.2).

## 4. Data the program collects

| Situation, as the person states it | Rule | Rows |
|---|---|---|
| The company is a HIPAA covered entity or business associate and uses PHI to send program communications about a product | Marketing needs individual authorization, except face-to-face or nominal gifts; treatment and operations exceptions are lost when a third party pays for the communication | PC-US-85 to PC-US-87 |
| A consumer app or program outside HIPAA holds identifiable health data | FTC Health Breach Notification Rule: unauthorized disclosure is a breach; notice within 60 calendar days; effective as amended 29 July 2024 | PC-US-79 to PC-US-84, CP-US-54 to CP-US-56 |
| A partner processes the data for the company in the EU | GDPR Article 28 contract terms | CP-EU-01 to CP-EU-07 |
| DiGA in Germany | Data only with consent and for listed purposes; advertising excluded | PC-DE-16 |

Whether the company is a covered entity, business associate, PHR vendor or controller is the person's privacy owner's call. The model lays out the rule for each case.

## 5. Library check for claims (optional)

`commercial-dh.audit_claims` labels claims against the authorization record. Read `tools.md` first: by product name it reported no authorization for two products that its own search block found, and with an FDA number it labeled every claim "exceeds_record" because the record held no intended purpose. Treat its labels as prompts for the owner's review, never as a verdict.
