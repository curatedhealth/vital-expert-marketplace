# Method standards (Q1)

| Id | Standard | Version / date | What it requires (for this judgement) | Status | URL |
|---|---|---|---|---|---|
| C1 | Report counts and plain notes; never a verdict | TR-H3, `trusted-capability-map` | Owner decision, product concept v0.4, 20 October 2026 |
| C2 | A check that did not run is reported as not checked; no companion result is described unless the companion returned it | TR-H4 | Owner decision, 20 October 2026 |
| C3 | Work stays an uncleared draft unless the person names who cleared it | TR-H5 | Owner decision, 20 October 2026 |
| C4 | Depth follows the reader: light, short, full | TR-H12 | Owner decision, 20 October 2026 |
| C5 | Name the kind of internal process the work goes to next; never replace or name a company's SOP | TR-H11 | Owner decision, 20 October 2026 |
| C6 | Plain language for the person; codes and skill names only on request | TR-H13 | Owner decision, 20 October 2026 |
| C7 | Every summary ends with the closing statement, unchanged | TR-H10 | Owner decision, 20 October 2026 |
| C8 | Letters the person turned off are shown as "off by choice" and not run; hard rules still run | Concept §6.3, `trusted-capability-map/tasks/choose-letters.md` step 6 | Owner decision, 20 October 2026 |
| C9 | Prove skills run whenever VERIFY is connected, including when True is off | Concept §6.3 and §17 | Owner decision, 20 October 2026 |
| V1 | A support status is word overlap with a supplied passage, not a verdict that the sentence is true in the world | VERIFY server instructions | Read 20 October 2026. `[CHECK]` against VERIFY documentation |
| V2 | Status names: supported, partial, unsupported, contradicted, unverifiable, out_of_scope | VERIFY server instructions | Read 20 October 2026. `[CHECK]`: the `check_claim` schema says only "returns a status" |
| V3 | Confidence (faithfulness) percent = (supported + 0.5 × partial) ÷ (supported + partial + unsupported + contradicted + unverifiable), whole percent, out_of_scope excluded | VERIFY server instructions | Read 20 October 2026. Computed by `confidence-scoring`, not here. `[CHECK]` |

Rows above are migrated from prior `rules.md` citations. Status vocabulary: VERIFIED / PARTIAL / UNVERIFIED / [CHECK] / [GAP]. Re-verify against primary PDFs before Released.

| WC-IFPMA-4.2 | Promo accurate, balanced, fair, complete; no distortion/exaggeration/omission | IFPMA Code of Practice Art. 4.2 | VERIFIED (digest 8 Nov 2026) | https://www.ifpma.org/wp-content/uploads/2018/09/IFPMA_Code_of_Practice_2019_EN.pdf |
| WC-IFPMA-4.3 | Claims substantiable via labeling or scientific evidence; evidence to HCPs on request | IFPMA Art. 4.3 | VERIFIED (digest 8 Nov 2026) | same PDF |
| WC-ABPI-6.1 | Claims accurate, balanced, fair, objective; relative risk with absolute risk | ABPI Code 2024 Cl. 6.1 | VERIFIED (digest 8 Nov 2026) | https://www.pmcpa.org.uk/the-code/2024-interactive-abpi-code-of-practice/clause-6-information-claims-comparisons-and-disparagement/ |
| WC-ABPI-6.2 | Every claim/comparison capable of substantiation; provide on request | ABPI Cl. 6.2 | VERIFIED (digest 8 Nov 2026) | https://pmcpa.org.uk/media/r0anf5ya/2024-abpi-code.pdf |
| WC-FDA-BadAd | Common failures: omit risk, overstate benefit, unsupported claims | FDA Bad Ad Program | VERIFIED (digest 8 Nov 2026) | https://www.fda.gov/drugs/prescription-drug-advertising-and-promotional-labeling/bad-ad-program |

Rows WC-* accessed 8 November 2026 via WORLD_CLASS_PRACTICES_DIGEST.
