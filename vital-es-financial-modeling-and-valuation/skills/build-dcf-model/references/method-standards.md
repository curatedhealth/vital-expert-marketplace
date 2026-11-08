# Method standards (what the register is judged against)

Status rule as in the other skills of this plugin: VERIFIED-REOPENED = the primary or official text was opened, the wording appears in it, and the passage is registered in `verbatim-passages.json` (or in the due diligence plugin's register, by id); SUMMARY-ONLY = abstract or secondary report only, never used for a figure or rule; [CHECK] = not verified, with the reason. Access date for every row: 7 November 2026.

No published standard prescribes the cash-flow construction for a development-stage asset; the discount-rate duty and consistency come from IVS 103 and the rNPV structure from the WIPO guide.

| Id | Standard or source | Version / date | What it states (for this judgement) | Passage ids | Status | URL |
|---|---|---|---|---|---|---|
| D1 | WIPO, Intellectual Property Valuation in Biotechnology and Pharmaceuticals, chapter 3 (income approach) | web publication read 7 Nov 2026; **a guide, not a standard** | rNPV and DCF structure; sales grow from a low base, peak and decline (VP-V-009); post-market cash flows run to patent expiry or peak sales (VP-V-010); the rate combines several factors (VP-V-013); choosing the rate is difficult (VP-V-006) | VP-V-006, VP-V-009, VP-V-010, VP-V-013 | VERIFIED (re-opened) | https://www.wipo.int/web-publications/intellectual-property-valuation-in-biotechnology-and-pharmaceuticals/en/3-the-income-approach.html |
| D2 | IVSC, International Valuation Standards effective 31 January 2025 (red-line edition; unchanged text also in the 2022 edition), IVS 103 Valuation Approaches | standard | the valuer must document the method for the discount rate and give evidence for its derivation (VP-V-030); evaluate whether the risk behind the cash-flow assumptions is captured in it (VP-V-031); the rate must be consistent with the type of cash flow (VP-V-032); the terminal value is discounted with the same rate (VP-V-033) | VP-V-030 to VP-V-033 | VERIFIED (re-opened) | https://icaew.com/-/media/corporate/files/technical/corporate-finance/valuation/ivs-effective-31-january-2025-redline-edition.ashx |
| D3 | Kossmeier et al.; Cha, Rifai, Sarraf (McKinsey): forecast optimism (registered by the commercial viability skill) | peer-reviewed study; consulting article | published sales forecasts have run high; context only, no correction applied | VP-H-001, VP-H-002, VP-H-010 | VERIFIED (re-opened) | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8414520/fullTextXML |
| D4 | Terminal-value share threshold | not located | no opened source sets a threshold for how much of a value may come from the terminal value; the share is reported only | none | [CHECK] | n/a |

## Judgement rules
- State the cash flows first, then the rate, then the result; name the rule id beside every figure.
- The present value is a range over scenarios and rates; the rate is a human choice.
- A value after the last explicit year exists only through a terminal assumption the team supplied with a source.
- Another currency or market is a GAP, not a conversion.
