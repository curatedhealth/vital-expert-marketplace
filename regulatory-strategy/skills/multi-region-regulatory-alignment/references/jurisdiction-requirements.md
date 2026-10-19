# Jurisdiction requirements for software medical devices

Interpretive reference. Every line cites the research row it comes from: `MR-`, `JX-` and `CHG-` rows are in `multi-region-sources.md`; `US-`, `EU-`, `UK-`, `IM-` and `CH-` rows are in `pathways-submissions-sources.md`. All rows were read on 19 October 2026. Where no row exists the line says `[GAP]`. Do not add a rule here that has no row.

Legal status words used throughout: **in force** (law or final guidance that applies now); **adopted, later date** (law with a future date of application); **draft** (a draft instrument or guidance); **proposal** (consulted on, not adopted); **exploratory** (stated intent, no mechanism).

## 1. How the same software is classified

| Jurisdiction | Rule for software | What it means for the same product | Rows |
|---|---|---|---|
| United States | Class I general controls; Class II special controls; Class III premarket approval. The class follows the device type and product code. Some software meets the device definition but sits under enforcement discretion; clinical decision support that meets all four statutory criteria is not a device (guidance of 29 January 2026). | Read the class from the product code or the predicate's record; check the CDS criteria before assuming a device. | US-01, US-02, US-03, US-17, US-18, US-19, US-20, US-23, US-68 |
| European Union | MDR Rule 11: decision software class IIa, IIb for serious deterioration or surgical intervention, III for death or irreversible deterioration; monitoring software IIa, IIb for vital parameters with immediate danger; all other software class I. Where several rules apply, the strictest applies. | Most decision software is at least class IIa. MDCG 2019-11 rev.1 (June 2025) maps IMDRF category IV to class III and category III to IIb; categories I and II fall to IIa. The table is illustrative. | EU-02, EU-03, EU-04, EU-05, EU-06, EU-07, EU-27, EU-31 |
| Switzerland | MedDO Art. 15 applies EU MDR Annex VIII for classification. Swissmedic notes Rule 11 strictly limits class I software. | Expect the EU class. | CH-01, CH-04, CH-05 |
| Great Britain | UK MDR 2002 applies MDD-era active-device rules: diagnostic devices allowing direct diagnosis or monitoring of vital processes are IIa (IIb where immediate danger); all other active devices class I. | The same software can be class I in GB and class IIa or higher in the EU and Switzerland. A new GB classification aligned to Rule 11 was consulted on; no made instrument was found `[GAP]`. | UK-14; conflicts note in `pathways-submissions-sources.md` |
| Canada | Classes I to IV under the Schedule 1 rules; Class IV highest. | A software-specific Canadian rule was not read `[GAP]`; classify with the person's regulatory owner against Schedule 1. | MR-01 |
| Australia | Schedule 2 rule 4.5 (diagnosis or screening: III, IIb or IIa by seriousness), 4.6 (monitoring: IIb, IIa or I), 4.7 (specifying or recommending treatment: III where death or severe deterioration may follow). Rules apply to new applications from 25 February 2021 and to devices already on the register from 1 November 2024, with exceptions. | Classify separately; do not assume the EU class carries over. | MR-14, MR-15, MR-16, MR-17, MR-18 |
| IMDRF (reference, not law) | N12 sets categories I to IV from seriousness of the situation and significance of the information; the highest category applies where several situations are covered. | A shared vocabulary for the argument, not a class in any jurisdiction. | JX-01, JX-02, JX-03, IM-02 |
| Brazil, Japan | Software classification rules were not read. | `[GAP]` | Not sourced |

## 2. Routes to market

| Jurisdiction | Routes for software | Rows |
|---|---|---|
| United States | 510(k) against a predicate, at least 90 days before distribution; De Novo for novel class I or II devices without a predicate (directly or after a not-substantially-equivalent decision); PMA for class III. 510(k) and De Novo go through eSTAR. | US-04, US-05, US-06, US-07, US-09, US-10, US-14, US-36, US-37, US-38 |
| European Union | Class III: Annex IX, or Annex X with XI. Class IIb and IIa: Annex IX Chapters I and III with technical documentation sampling (IIa may use Annex II/III plus Annex XI). Class I: self-declaration. One notified body at a time per procedure. | EU-08, EU-09, EU-10, EU-11, EU-12 |
| Great Britain | Class I self-declared; other UKCA classes need a UK approved body (UK-15). CE marking is accepted for a transition period (section 4). UKCA is not recognized in the EU, EEA or Northern Ireland (UK-07). | UK-15, UK-07 |
| Switzerland | A declaration of conformity under Swiss or EU law. | MR-19 |
| Canada | A medical device license for Class II, III and IV; Class I needs no device license. A Class II application includes a QMS certificate to CAN/CSA-ISO 13485. | MR-02, MR-03 |
| Australia | Inclusion in the register; evidence from comparable overseas regulators can be used (section 3). | MR-07, MR-09 |

## 3. Reliance and recognition routes, with legal status

| Into | Relies on | What is accepted | Legal status | Rows |
|---|---|---|---|---|
| Australia (TGA) | EU notified bodies, MDSAP auditing organizations, Health Canada, Singapore HSA, Japan MHLW and PMDA, US FDA, UK approved bodies, IAF-accredited bodies | For example FDA 510(k), De Novo and PMA decisions, Health Canada licenses, MDSAP certificates. The device must have the same design, intended purpose and user. Some applications must be audited; any may be selected. UK approved bodies added in the compilation in force 1 December 2025; guidance updated 11 May 2026. | in force | MR-07, MR-08, MR-09, MR-10, MR-11, MR-12, MR-13 |
| Switzerland | EU/EEA notified body certificates | Deemed equivalent to Swiss certificates if equivalence of procedure and qualification is credibly demonstrated (MedDO Art. 25(4)). The EU treats Switzerland as a third country for devices; the MRA chapter is not updated. | in force | MR-20, CH-02, CH-03 |
| Switzerland | US FDA authorizations | Motion 20.3211; Federal Council guidelines of 30 April 2025; ordinance changes still being drafted. Envisaged conditions: Swiss data protection and QMS, a post-market surveillance plan, possibly clinical evidence. | draft policy; no in-force date | MR-21, MR-22 |
| Great Britain | CE marking (EU MDR, MDD) | MDR devices until 30 June 2030; MDD devices until the sooner of certificate expiry or 30 June 2028; up-classified self-declared MDD devices until 30 June 2028. | in force | UK-02, UK-03, UK-04, MR-23 |
| Great Britain | CE marking, indefinitely | Consultation 16 February to 10 April 2026; feedback being analyzed, no outcome published. | proposal | UK-05, UK-06, MR-24 |
| Great Britain | TGA, Health Canada, FDA | Reliance route including "specific software" meeting GB equivalence criteria, to come by a 2026 statutory instrument; published in draft. | draft | MR-25, MR-26, MR-27 |
| Great Britain | (2023 policy) | The 2023 statement that would have excluded SaMD and AIaMD from recognition is marked superseded. Do not cite it as current. | superseded | MR-28 |
| Great Britain and United States | Each other | Announced 2 April 2026: exploring future mutual recognition mechanisms. No mechanism exists. | exploratory | MR-29 |
| Brazil (ANVISA) | Health Canada, FDA, MHLW/PMDA, TGA | Optimized review for Class III and IV registration based on their approval documents (RDC 741/2022, IN 290/2024). The page does not mention software. | in force; software scope `[GAP]` | MR-30 |
| Japan | (reliance route for software) | No official English page stating one was found. | `[GAP]` | Not sourced |

IMDRF N89 (2 February 2026) defines reliance as one regulator using another's assessment or decision to reach its own decision (MR-31). Each regulator still decides.

## 4. MDSAP: who uses it and how

Members: TGA, ANVISA, Health Canada, Japan MHLW/PMDA, US FDA. Observers: EU, Singapore HSA, UK MHRA, WHO IVD prequalification. Documents moved to a TGA-managed site (FDA update of 18 December 2025). Each regulator uses MDSAP outputs differently and keeps its own authorization power (MR-32, MR-33, MR-34, MR-35).

| Regulator | Use | Rows |
|---|---|---|
| Health Canada | MDSAP certification required for Class II, III and IV licenses, as the MDSAP site states. The regulation itself requires a certificate from a registrar recognized by the Minister and does not name MDSAP. | MR-03, MR-05, MR-06 |
| TGA | Reports and certificates used as evidence, if Australian requirements were covered in the audit. | MR-36, MR-42 |
| ANVISA | May replace its premarket inspection for the GMP certificate (Class III and IV) and its renewal every four years. | MR-37 |
| Japan MHLW/PMDA | May exempt a site from on-site inspection or replace much of the inspection documents; PMDA may still inspect. | MR-38 |
| US FDA | Substitute for routine inspections; not for-cause or follow-up inspections, not PMA pre-approval or post-approval inspections. | MR-39, MR-40, MR-43 |
| Singapore HSA, Korea MFDS (not members) | HSA accepts MDSAP certificates as QMS evidence; MFDS can replace on-site GMP audits with document review. | MR-41 |
| EU notified bodies | MDSAP audit reports can be taken into account in MDR surveillance audits (MDCG 2020-14). This passage came from the library's guidance store without a source URL; confirm on the MDCG page before citing. | `[GAP]` for a sourced row; see `tools.md` |

## 5. Registration duties once authorized

| Jurisdiction | Duty | Rows |
|---|---|---|
| United States | Register within 30 days of starting operation and list devices; annual registration and listing confirmation 1 October to 31 December; changes within 30 days; lapse gives "failed to register" or "failed to list" status. Annual registration fee USD 13,785 (FY 2027 rate, from 1 October 2026). | JX-28, JX-29, JX-30, JX-31, JX-32, US-55 |
| Canada | Annual signed license statement before 1 November; the Minister may cancel the license if it is not filed. New or modified QMS certificates to Health Canada within 30 days of issue; certificates valid at most three years. | JX-33, JX-34, JX-35, MR-04 |
| European Union | EUDAMED actor, UDI/device, certificate and market surveillance modules mandatory since 28 May 2026. A device first placed before that date with units still being placed is registered in the UDI/device module by 28 November 2026; a device first placed on or after it is registered before the first unit. Vigilance and clinical investigation modules become mandatory on release with no voluntary period. | JX-36, JX-37, JX-38, JX-39, JX-40, JX-41 |
| Great Britain | Devices must be registered with the MHRA. Renewal cycle `[GAP]`. | UK-01 |
| Switzerland | Product registration with Swissmedic from July 2026, with a six-month transitional period. Exact end date `[GAP]`. | JX-42, CH-08 |
| Australia, Brazil, Japan | Registration and renewal duties were not read. | `[GAP]` |

The monitoring skill (DH-03.03.2.2) turns these into a dated obligations table.

## 6. Where the regions disagree (use in every map)

- **GB versus EU class.** Much stand-alone software is class I in GB and class IIa or higher in the EU and Switzerland (UK-14, EU-02).
- **Legacy and current EU certificates can coexist in the register.** A product can show MDD-era records and MDR records with different classes; describe each record by its regime and identifier, never infer why the class differs.
- **UK reliance is not available yet.** It sits in a draft statutory instrument (MR-26, MR-27). CE acceptance dates are law (MR-23).
- **Swiss FDA route is not available yet** (MR-21).
- **Health Canada's MDSAP requirement** is a recognition policy stated on the MDSAP site, not text in the regulation (MR-05, conflicts note).
