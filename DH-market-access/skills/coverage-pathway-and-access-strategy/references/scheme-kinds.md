# What a status means, by kind of scheme

Source: the library's own scheme records (`market-access-dh.list_schemes`), read 19 October 2026, with each scheme's stated source URL. Only rules a record states are written here. Where a rule is needed but no record states it, the line says `[GAP]`. Re-check against the authority before relying on any rule; schemes change.

## The six kinds

| Kind (`pathway_kind`) | What a positive status means | What it does not mean |
|---|---|---|
| `listing`, `durable_listing` | The named product is on the payer's list. | Not proof of clinical benefit. Not a permanent price. |
| `anticipatory_coverage` | Temporary funding while evidence is completed. | Not durable coverage. A clock is running. |
| `durable_telemonitoring_listing` | A telemonitoring activity is on the common-law list. | Not a product-level price on its own. |
| `code_based_coverage` | A billing code exists that pays for a service. | The product is not "listed"; the code is what is covered. |
| `healthtech_guidance`, `early_value_assessment` | An HTA body has issued guidance or an early assessment. | Not funding. Not a purchase decision. |
| `national_funding_appraisal` | An appraisal or advice step toward funding. | Advice is not itself a coverage decision. |
| `validation_pyramid` | A validation level as the source names it. | The link from level to reimbursement is `[GAP]` in this reference. |

## Scheme by scheme

| Scheme | Country | Kind | Rule the record states | Source |
|---|---|---|---|---|
| DE_DIGA | DE | listing | Provisional trial up to 12 months (exceptionally 24); permanent listing after that. Listed DiGAs are covered for statutory health insurance patients (§ 33a SGB V). From month 13 the price is negotiated between the GKV-Spitzenverband and the manufacturer (§ 134 SGB V); the library's scheme record says "G-BA", which is not what the statute states. Detail and sources: `requirements/germany-diga.md`. | https://diga.bfarm.de/de/verzeichnis |
| FR_PECAN | FR | anticipatory_coverage | One year, non-renewable; LPPR dossier within 6 months or LATM within 9 months of start. Status date is the Journal officiel publication date. | https://www.has-sante.fr/ |
| FR_LPPR | FR | durable_listing | Common-law listing after or instead of PECAN for therapeutic digital medical devices. | https://www.ameli.fr/ |
| FR_LATM | FR | durable_telemonitoring_listing | Common-law telemonitoring listing. | https://www.has-sante.fr/ |
| BE_MHEALTH | BE | validation_pyramid | Levels M1 to M3 as the source names them, kept in `status_raw`. | https://www.mhealthbelgium.be/ |
| UK_NICE_EVA | UK | early_value_assessment | Evidence-generation period as stated in the guidance. Never merge with HTG or NHAP. | https://www.nice.org.uk/guidance |
| UK_NICE_HTG | UK | healthtech_guidance | Routine-use guidance. Guidance, not a device registration. | https://www.nice.org.uk/guidance |
| UK_NICE_NHAP | UK | national_funding_appraisal | Programme process; Secretary of State referral for technology appraisal. | https://www.nice.org.uk/process/pmg46/chapter/annex-a-national-healthtech-access-programme |
| US_CMS_RPM | US | code_based_coverage | Not a product listing; the decision reference is the CPT/HCPCS code. | https://www.cms.gov/files/document/mln901705-telehealth-remote-monitoring.pdf |
| US_CMS_DMHT | US | code_based_coverage | Digital mental health treatment codes G0552 to G0554; the decision reference is the code. | https://www.cms.gov/files/document/mln1986542-medicare-mental-health-coverage.pdf |
| IE_HSE_CGM | IE | durable_listing | Prior approval for patients initiating CGM from 1 December 2023; named list of CGM sensors for type 1 diabetes. No price on the source. | https://assets.hse.ie/media/documents/Frequently_Asked_Questions_CGM_for_Healthcare_professionals.pdf |
| CH_BAG | CH | durable_listing | MiGeL position 40.01.01.00.1 (from 1 July 2026) is a reimbursed class for interactive CBT digital applications in depression; it names no product; in evaluation until 31 December 2026; paid once for at most 90 days. | https://www.bag.admin.ch/de/mittel-und-gegenstaendeliste-migel |
| AU_MSAC | AU | national_funding_appraisal | MSAC advises the minister; funding is a separate government act. | https://www.msac.gov.au/applications |
| SE_TLV | SE | healthtech_guidance | TLV does not decide whether regions purchase; a later MTP-rådet recommendation is a separate act. | https://www.tlv.se/medicinteknikforetag/halsoekonomiska-bedomningar-och-rapporter-medicintekniska-produkter.html |
| FI_DIGIHTA | FI | early_value_assessment | Suitability opinion valid three years; not a reimbursement decision. | https://fincchta.fi/en/digi-hta-eng/arvioinnit-eng/ |
| ES_REDETS | ES | healthtech_guidance | Evaluations inform financing; not a reimbursement list. | https://redets.sanidad.gob.es/ |

## How much of each scheme the library holds

This changes with every load. Always take it from `list_schemes` at run time, never from this file.
