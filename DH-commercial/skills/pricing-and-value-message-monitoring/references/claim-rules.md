# Claim rules: what a claim can cross, and what a safer draft keeps

Interpretive reference for tasks A2 and B1. Every rule cites its row in `promotion-and-claims-research.md` (PC-) or `channels-partners-research.md` (CP-). Read on 19 October 2026; not owner-reviewed. Rows marked [INDUSTRY] are self-regulatory codes, not law; rows marked [WF] were read through a summarizing tool and must be re-checked before reliance. A flag is a reason for the owner to look, never a finding that a law was broken.

## First question for every claim: what is the anchor?

A claim is judged against the intended use the product holds in that market, as the person states it from the label, the instructions for use or the authorization. Marketing copy is itself evidence of intended use (PC-US-17, PC-US-20, PC-EU-03, PC-UK-01), so a claim beyond the intended use is both a promotion problem and a regulatory-status problem. If the intended use is not known, every flag is provisional and the audit says so.

## Claim types

| # | Claim type | Example wording | Rows it can cross | What a safer draft for the owner keeps or drops |
|---|---|---|---|---|
| 1 | Cure, treat or prevent a disease | "cures insomnia", "prevents relapse" | PC-EU-10, PC-UK-07, PC-DE-03; [INDUSTRY] PC-UK-13; for a product sold as wellness, PC-US-15, PC-US-60, PC-US-63 | Keep the intended purpose as stated on the label; replace the verb with the measured outcome, population, comparator and time point, with its source; drop "cure" |
| 2 | Certain success or no harm | "guaranteed", "no side effects", "completely safe" | PC-DE-04; [INDUSTRY] PC-UK-13; PC-US-03 (omission) | Drop the guarantee; give safety information only as the labeling or a sourced passage states it |
| 3 | Efficacy and "clinically proven" | "clinically proven", "works in 6 weeks" | PC-US-28 to PC-US-31 (CFL evidence and disclosure), PC-US-72, PC-US-73 [WF], PC-DE-05 (study citation), PC-UK-04 (device-indicating words); [INDUSTRY] PC-UK-10 | State the study, its design, population and result as the passage reads; disclose material limitations; name author, date and source in Germany |
| 4 | Approval, certification or endorsement | "FDA-cleared", "CE-certified", "DiGA-listed", "doctor-recommended" | PC-EU-11, PC-UK-08; PC-US-63 (no clinical-grade or equivalence claims for wellness); PC-UK-03 and PC-DE-11 (testimonials) | State the authorization exactly as the record holds it (route, class, identifier) and only for the use it covers; testimonials only if accurate and representative, as the owner decides |
| 5 | Comparative | "better than sleeping pills", "beats competitor X" | PC-US-26 (head-to-head in the same indication can be consistent), PC-US-27, PC-EU-02, PC-DE-03, PC-US-72 [WF] | Keep only a comparison the passage reports for the same indication and population; name the comparator as the study did; describe a competitor only by its record |
| 6 | Population or use beyond the intended use | "for teens", "also helps anxiety" | PC-US-22, PC-US-27, PC-EU-02 (d), PC-US-07 | Drop for clinicians and consumers; for US payors only under 502(gg) with its statements (PC-US-08, PC-US-45, PC-US-46) |
| 7 | Diagnosis or self-test implied | "take the test", "find your ADHD type", color-coded readings | [INDUSTRY] PC-UK-12, PC-UK-14, PC-UK-16; PC-US-63; EU: PC-EU-02 (use outside the assessed intended purpose) | Remove the diagnostic implication unless the product holds that intended use |
| 8 | Coverage or price | "covered by your insurance", "free with your fund", a price | PC-EU-07 (misleading action, includes price), PC-US-03, PC-EU-08 (omission); CP-DE-01 (two DiGA routes); CP-DE-03 (patient pays above the amount) | State the route and who it applies to, as the record and rows support; never imply coverage proves effect; price wording goes to the pricing owner |
| 9 | Numbers | "45 minutes more sleep", "70 percent improve" | US: PC-US-31 (disclose unfavorable findings), PC-US-40 (payor context). Germany: PC-DE-05 (faithful reproduction). EU: PC-EU-07 (results to be expected). Cite only the rows for the market audited. | Keep only a figure read in a passage in the same direction, with its denominator, comparator and time point |
| 10 | Disclaimers used as a fix | "not a medical device", "for information only" | PC-UK-02, PC-US-74 [WF], PC-US-30; EU: PC-EU-07 (overall presentation deceives) | A disclaimer does not rescue a medical claim; fix the claim |
| 11 | German public advertising | Health fear or benefit, disease lists, children | PC-DE-09 to PC-DE-13 | Outside Fachkreise: no suggestion that health improves with use or suffers without it; no listed diseases; nothing aimed mainly at children under 14 |
| 12 | DiGA specifics | In-app ads, data used for advertising, auto-renewal | PC-DE-15 to PC-DE-17 | Remove advertising from the DiGA; no auto-renewing or time-limited offers |
| 13 | Payor material | Budget impact, cost offsets, value dossiers | PC-US-04 to PC-US-07, PC-US-34 to PC-US-40 | Tie to the cleared indication; present design, limits and sensitivity; state material differences from labeling; keep off public websites (PC-US-35) |
| 14 | Health data in marketing | Sharing app data with ad platforms | PC-US-80 to PC-US-84 (HBNR), PC-US-85 to PC-US-87 (HIPAA marketing), PC-DE-16 | Flag for the compliance or privacy owner; not a wording fix |

## Evidence behind a claim

- A claim with a number or an efficacy statement needs a passage the person supplies or the library returns. Check it with `verify.qualify_source` then `verify.check_claim`, and accept "supported" only after reading the passage yourself in the same direction, for the same population and comparator (register N3).
- A listing, a code, a price or uptake is never evidence that a product works.
- FDA's evidence bar for CFL communications depends on the claim, not on the approval standard (PC-US-29); the FTC expects randomized, controlled human testing for most health benefit claims [WF] (PC-US-73). Say which bar the audience and market bring.

## The library's claim labels

`commercial-dh.audit_claims` labels claims `matches_record`, `exceeds_record` or `no_authorization_on_file`. On 19 October 2026 the store held no intended purpose for the records tried (`intended_purpose_from_record: "[GAP]"`), so every claim, including the device's own classification wording, came back `exceeds_record`; for somnio it reported no authorization while its own inner search returned an EU MDR Class IIa record (`examples/live/audit_claims_summary.json`). Use the call for one fact only, whether an authorization record was matched, and confirm that against the inner search block. Never report its label as a finding.
