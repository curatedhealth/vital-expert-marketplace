# Method standards (what the register is judged against)

Status rule as in the other skills of this plugin: VERIFIED-REOPENED = the primary or official text was opened, the wording appears in it, and the passage is registered in `verbatim-passages.json` (or in the due diligence plugin's register, by id); SUMMARY-ONLY = abstract or secondary report only, never used for a figure or rule; [CHECK] = not verified, with the reason. Access date for every row: 7 November 2026.

The rNPV structure and the separation of rate and probability come from the WIPO guide; the documentation duty for the rate from IVS 103; success-rate benchmarks are reused from the due diligence plugin.

| Id | Standard or source | Version / date | What it states (for this judgement) | Passage ids | Status | URL |
|---|---|---|---|---|---|---|
| N1 | WIPO, Intellectual Property Valuation in Biotechnology and Pharmaceuticals, chapter 3 | web publication read 7 Nov 2026; **a guide, not a standard** | rNPV applies success probabilities at each milestone (VP-V-001); it is a refinement of DCF with cash flows adjusted by probability (VP-V-002); cost of capital is separated from probability (VP-V-003); the rate should not reflect the drug's own risk (VP-V-004); adjusting only the rate hides the risk (VP-V-005); assumptions must be data-driven (VP-V-007); rNPV is the de facto method (VP-V-008) | VP-V-001 to VP-V-005, VP-V-007, VP-V-008 | VERIFIED (re-opened) | https://www.wipo.int/web-publications/intellectual-property-valuation-in-biotechnology-and-pharmaceuticals/en/3-the-income-approach.html |
| N2 | IVSC, IVS 103 and IVS 210 | standard (red-line copy; unchanged text) | document the rate and its evidence (VP-V-030); the risk behind the cash flows must be captured in the rate (VP-V-031); compensation for risk goes into the expected payoff through a cash-flow risk margin or the rate (VP-V-036); R&D assets may carry higher risk (VP-V-037) | VP-V-030, VP-V-031, VP-V-036, VP-V-037 | VERIFIED (re-opened) | https://icaew.com/-/media/corporate/files/technical/corporate-finance/valuation/ivs-effective-31-january-2025-redline-edition.ashx |
| N3 | BIO / Informa / QLS, Clinical Development Success Rates 2011-2020; Wong, Siah, Lo 2019 (reused by id) | industry report (not peer-reviewed); peer-reviewed | phase transition success is advanced over advanced plus suspended (VP-B-004); the two sources differ and are never mixed (VP-B-001, VP-B-060) | VP-B-001, VP-B-004, VP-B-060 | VERIFIED (re-opened) | https://go.bio.org/rs/490-EHZ-999/images/ClinicalDevelopmentSuccessRates2011_2020.pdf |
| N4 | A registered default or range for a biotech discount rate | not located | the one rate-magnitude source opened concerns capitalizing R&D outlays (VP-V-060, VP-V-061) and is out of scope for a deal rate | none | [CHECK] | n/a |

## Judgement rules
- Show the cascade first, then the rate, then the result.
- The probability is applied once; if the rate is argued to carry risk, say so and do not apply the probability twice.
- A probability above the benchmark stratum needs a stated reason (FV-01).
- Another market or currency is a GAP.
