# VITAL Expert plugins for Cowork

Add the marketplace `curatedhealth/vital-expert-marketplace`. In Claude it shows as **from vital-expert** (Vital.Expert). Cowork does not render custom plugin icons yet; packs that ship an icon keep `icon.png` for directory use only. Do not paste a file link.

If you previously added `curatedhealth/vital-expert-plugins`, remove that marketplace and add `curatedhealth/vital-expert-marketplace`, then install the packs below.

## Foundational (no library key)

- **VITAL TRUSTED** (`vital-trusted`). Nineteen skills for daily life-sciences work against TRUSTED (Tangible, Rule-compliant, Unbiased, Safe, True, Ethical, Defensible). No connector required. Prove skills use VITAL Verify when that connector is installed.
- **VITAL Verify** (`vital-verify`). Connector plus check skills. Paste a `vvfy_` key when you have one. URL `https://mcp.vital.expert/api/mcp/verify`.

## Digital Health (seven packs)

Each Digital Health pack asks for the same `vlib_` key and uses `https://mcp.vital.expert/api/mcp/library`. Do not add a second connector. Legacy one-core packs are retired from this marketplace; install only these seven.

| Pack | Plugin id | Folds in |
|---|---|---|
| Regulatory and quality | `dh-regulatory-and-quality` | Regulatory Strategy, Quality |
| Access and value | `dh-access-and-value` | Market Access, Health Economics |
| Clinical development | `dh-clinical-development` | Clinical Product Development, Clinical Validation (plus DTx safety and engagement) |
| Go to market | `dh-go-to-market` | Commercial, Customer Success |
| Patient and user experience | `dh-patient-and-user-experience` | Patient Engagement, User Experience |
| Strategy and portfolio | `dh-strategy-and-portfolio` | Diligence, Digital Health Strategy, Innovation, Cross-Functional Leadership (governance and portfolio) |
| Technology | `dh-technology` | Data Science, Advanced Analytics, Decision Support, Analytics Product, Interoperability, Cybersecurity, Software Engineering, and DTx design (.1 and .4) |

Choose one heading, then one job. The job holds its tasks as sections. A missing fact stays a gap.

Former one-core Digital Health packs are not listed here; they are superseded by the seven packs above.

## Navigator

- **Navigator AI investment** (`navigator-ai-investment`). Facilitated AI investment decisions on the VITAL Ontology Navigator. Uses the Ontology Navigator connector already on the account. No key is in this pack. Do not add a second connector.
