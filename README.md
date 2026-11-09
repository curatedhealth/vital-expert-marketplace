# VITAL Expert plugins for Cowork

Add the marketplace `curatedhealth/vital-expert-marketplace`. In Claude it shows as **from vital-expert** (Vital.Expert). Cowork does not render custom plugin icons yet; packs that ship an icon keep `icon.png` for directory use only. Do not paste a file link.

If you previously added `curatedhealth/vital-expert-plugins`, remove that marketplace and add `curatedhealth/vital-expert-marketplace`, then install the packs below.

## Foundational (no library key)

- **VITAL TRUSTED** (`vital-trusted`) — **0.3.4 Pilot** (branch `trusted-0.3.4`, not Released). Do not treat as Released until the owner publishes. The former `vital-verify` plugin remains retired.

## Digital Health (seven packs)

Each Digital Health pack asks for the same `vlib_` key and uses `https://mcp.vital.expert/api/mcp/library`. Do not add a second connector. Legacy one-core packs are retired from this marketplace; install only these seven.

| Pack | Plugin id | Folds in |
|---|---|---|
| Regulatory & Quality (DH) | `dh-regulatory-and-quality` | Regulatory Strategy, Quality |
| Access & Value (DH) | `dh-access-and-value` | Market Access, Health Economics |
| Clinical Development (DH) | `dh-clinical-development` | Clinical Product Development, Clinical Validation (plus DTx safety and engagement) |
| Go-to-Market (DH) | `dh-go-to-market` | Commercial, Customer Success |
| Patient & User Experience (DH) | `dh-patient-and-user-experience` | Patient Engagement, User Experience |
| Strategy & Portfolio (DH) | `dh-strategy-and-portfolio` | Diligence, Digital Health Strategy, Innovation, Cross-Functional Leadership (governance and portfolio) |
| Technology (DH) | `dh-technology` | Data Science, Advanced Analytics, Decision Support, Analytics Product, Interoperability, Cybersecurity, Software Engineering, and DTx design (.1 and .4) |

Choose one heading, then one job. The job holds its tasks as sections. A missing fact stays a gap.

Former one-core Digital Health packs are not listed here; they are superseded by the seven packs above.

## Navigator

## Enterprise Strategy (live-test)

- **Target Evaluation & Due Diligence** (`vital-es-target-evaluation-due-diligence`). CF-01.02.06. Draft `0.1.1-live-test`. Standard KA Pass; not Marketplace Done.
- **Financial Modeling & Valuation** (`vital-es-financial-modeling-and-valuation`). CF-01.02.02. Draft `0.1.1-live-test`. Standard KA Pass; ranges only — no fairness opinion or recommended price; not Marketplace Done.

- **Navigator AI investment** (`navigator-ai-investment`). Facilitated AI investment decisions on the VITAL Ontology Navigator. Uses the Ontology Navigator connector already on the account. No key is in this pack. Do not add a second connector.
