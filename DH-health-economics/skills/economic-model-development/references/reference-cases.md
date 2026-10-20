# Reference cases by decision-maker

What each HTA body or payer framework states about perspective, discounting, outcome measure, time horizon, form of analysis, thresholds and budget impact. Every cell carries its row id in `health-economics-methods-research.md` (HE- rows, read 19 October 2026). A blank cell means the research file does not hold the rule: write `[GAP]` and name the body's text to read; never fill it from memory.

Use this file to frame a model (A1) and to check one (sibling skill). It states what a body has written. Which body's case applies, and whether a result is acceptable, is the person's and the decision-maker's call.

## England: NICE

| Element | Technology appraisal and HST manual (PMG36) | HealthTech program (PMG48), covers digital and AI | Evidence Standards Framework (ESF, voluntary for commissioners) |
|---|---|---|---|
| Status | Retitled "NICE technology appraisal and highly specialised technologies guidance: the manual"; published 31 January 2022, last updated 13 October 2026 (HE-033) | Published 14 July 2025, last updated 17 December 2025; combines the former diagnostics, interventional procedures and medtech programs (HE-064, HE-065) | Published 10 December 2018, updated 9 August 2022; not mandated (HE-078, HE-079) |
| Reference case required | Yes; non-reference-case analyses justified and kept separate (HE-035) | Early-use keeps the PMG36 section 4.2 reference case; deviations justified and discussed with NICE early (HE-070) | Not a reference case; evidence scaled to financial risk (HE-080) |
| Perspective | Health effects for patients and, when relevant, carers (HE-036); costs NHS and PSS (HE-037); productivity costs excluded, may be shown separately (HE-038) | As PMG36 (HE-070) | UK costs relating to NHS and PSS resources (HE-089) |
| Form of analysis | Cost-utility with fully incremental analysis, or cost-comparison (HE-039); cost-comparison when similar benefit at similar or lower cost than NICE-recommended comparators (HE-042) | Routine use: cost-utility and cost-comparison (HE-073). Early use: simplified models, reuse of existing models, or intermediate outcomes with threshold analyses (HE-069) | Standard 17 budget impact analysis for all tiers (HE-087); standard 18 cost-utility, or cost-consequences where QALYs are not possible, for higher financial risk (HE-090, HE-091) |
| Outcome and utilities | QALYs; EQ-5D preferred in adults (HE-043); patients report, carers if patients cannot (HE-044); mapping is a departure (HE-045). EQ-5D-5L: see PMG51 below | Same; PMG51 applies to HealthTech cost-utility (HE-059) | Health, cost and resource impacts versus current care (standard 13, HE-086) |
| Time horizon | Long enough for all important differences (HE-040) | As PMG36 (HE-070) | `[GAP]` |
| Discount rate | 3.5% a year for costs and effects (HE-047); 1.5% only if all three criteria are met (HE-048) | As PMG36 (HE-070) | `[GAP]` |
| Threshold as written | No precise maximum (HE-049); below £25,000 per QALY decision normally on the estimate (HE-050); £25,000 to £35,000 and above, stronger case (HE-051); net health benefit at £25,000 and £35,000 when modifiers apply (HE-052) | £20,000 per QALY "generally considered cost effective", stronger case between £20,000 and £30,000 (HE-074); cost-neutral or cost-saving generally considered cost effective under cost comparison (HE-076) | None stated |
| Severity modifier | Not applied initially to HealthTech appraisals (HE-053); weights in Table 6.1 (HE-054) | Not applied initially (HE-075) | n/a |
| Uncertainty | `[GAP]` beyond the sections cited | Switching values for rapidly iterating technologies (HE-077); early use names the uncertainties that drive the decision (HE-068); evidence uncertainties resolvable within 3 years (HE-072) | n/a |
| Budget impact | NHS England may ask for longer implementation above £40 million a year in any of the first 3 years (HE-055) | `[GAP]` | Standard 17 content for tiers B and C: population and uptake, technology and implementation costs (staffing, training, IT), comparator costs, relevant indirect costs (HE-088) |

### EQ-5D-5L (PMG51, interim methods statement of 27 August 2026)

- The UK 5L value set (Rowen et al. 2026, HE-127) derives all adult reference-case utilities (HE-058); required in HealthTech cost-utility (HE-059).
- 3L data are mapped to the UK 5L set with the DSU/EEPRU model (HE-060). No 3L utilities in sensitivity or scenario analyses (HE-061).
- Applies to new topics; for HealthTech, any topic launched after publication (HE-062). Topics started before keep mapping 5L to 3L (HE-063).
- The PMG36 web text at section 4.3.16 still says the opposite (HE-046). Follow PMG51 for new topics and say which applies.

## France: HAS (2020 guide)

| Element | Rule | Row |
|---|---|---|
| Version | 2020 edition, 27 recommendations; page updated 8 July 2026 | HE-102 |
| Perspective | Collective; a healthcare-system perspective must be justified | HE-103 |
| Form | Cost-utility when quality of life is an important consequence, otherwise cost-effectiveness on life years | HE-104 |
| Discounting | When the horizon exceeds 12 months; 2.5% at publication for horizons under 30 years, then falling to a floor of 1.5% | HE-105 |
| Utilities | EQ-5D-5L with the French value set in force (Andrade et al. 2020, HE-128); 3L transitional fallback, then mapping | HE-106 |
| Results | Efficiency frontier, ICER or net benefit; expenditure transfers between funders. No threshold in the passages read | HE-107 |
| When HAS requires an economic opinion for a device or digital product | `[GAP]` (research file "Not sourced") | |

## Germany: IQWiG General Methods 8.0

| Element | Rule | Row |
|---|---|---|
| Version | 8.0 of 19 December 2025; English since 1 July 2026 | HE-108 |
| Role | Health economic evaluation supports price negotiation (section 35b SGB V, mainly drugs); not a price recommendation | HE-109, HE-113 |
| Perspective | SHI-insured community; wider perspectives separately | HE-110 |
| Discounting | 3% after year 1; sensitivity at 0% and 5%, optionally 3% costs and 1.5% benefits | HE-111 |
| Budget impact | Mandatory with the evaluation; at least 3 years; without and with the product | HE-112 |
| Utilities | German 5L value set exists (Ludwig et al. 2018, HE-128); whether IQWiG requires it: `[GAP]` | |
| DiGA economics or pricing | Not in General Methods 8.0; BfArM and GKV-Spitzenverband documents not read `[GAP]`; DiGA pricing belongs to dh-market-access (coding-pricing-and-payer-contracting) | |

## United States: ICER and AMCP

| Element | ICER Value Assessment Framework 2023 | ICER-PHTI framework for digital health technologies | AMCP Format 6.0 (public-comment draft rows only) |
|---|---|---|---|
| Status | 2023 framework, period 2023 to 2026 (HE-114); reference case current as of 23 October 2025 (HE-120) | Published September 2023; used for DHT reviews from 2024 (HE-115, HE-121) | Advisory (HE-130); 6.0 released October 2026, only the March 2026 draft read (HE-131) |
| Perspective | Health care system base case, modified societal analysis, co-base where conditions are met (HE-116) | Two BIA perspectives: the DHT user, and the payer or plan sponsor (the main one) (HE-123) | Payer (HCDM) primary, societal supplementary (HE-136, draft) |
| Primary economic measure | Cost-effectiveness | Budget impact is the primary measure of comparative value (HE-115, HE-121) | CEA and BIA |
| Discounting | 3% for costs and outcomes (HE-117) | `[GAP]` | Typically 3% (HE-136, draft) |
| Outcome | QALY and evLY; EQ-5D-5L preferred if available; lifetime horizon default (HE-118, HE-120) | Other benefits such as productivity captured but kept out of the primary BIA (HE-121) | QALY or evLY; supplementary measures add to QALYs (HE-137, draft) |
| Horizon | Lifetime default (HE-120) | BIA 1 year; 2 to 5 year scenarios where offsets accrue later; one cohort followed from inception (HE-122) | BIA typically 1 to 3 years, dynamic population; PMPM and total (HE-138, draft) |
| Threshold or benchmark as written | Health Benefit Price Benchmark range $100,000 to $150,000 per evLY and per QALY; results shown at $50,000, $100,000, $150,000 and $200,000 (HE-118) | Threshold price giving 15% savings versus usual care; for very high-cost populations a 3:1 ROI price; otherwise the cost-neutral price; ICER calls these payer-suggested starting points (HE-124) | No absolute PMPM affordability threshold (HE-138, draft) |
| Budget impact threshold | $821 million for prescription drugs, 2025-2026; not for DHTs (HE-119) | n/a | n/a |
| Model access | `[GAP]` | `[GAP]` | Modifiable electronic BIA with unlocked inputs (HE-139, draft) |
| Evidence tiers | n/a | Tiers 1, 2, 3a, 3b (HE-125) | Digital therapeutics subsection 2.1.1B, no new content (HE-135) |

## European Union: HTA Regulation (EU) 2021/2282

Economic evaluation is a non-clinical domain outside joint clinical assessment; pricing, reimbursement and value conclusions stay national (HE-093, HE-094, HE-095). Device JCA covers selected class IIb and III devices with an expert-panel opinion (HE-096); AI or ML software is a selection criterion (HE-097); the first selection of 6 October 2026 held no digital-only product (HE-101). An EU JCA does not supply a reference case for an economic model.

## Open conflicts to state, never resolve

1. **NICE threshold.** PMG36 states £25,000 to £35,000 per QALY (HE-050, HE-051); PMG48, which covers digital HealthTech, still states £20,000 and £20,000 to £30,000 (HE-074). For a digital product assessed in the HealthTech program, both written ranges are shown; the research file treats this as an open conflict until NICE updates PMG48. The person chooses which to report against, and the output says the conflict exists. Note: the research file's conflict note dates the PMG36 range to March 2026 while HE-033 gives a last update of 13 October 2026; cite HE-050 and HE-051 for the range and HE-033 for the version.
2. **NICE EQ-5D.** PMG51 replaces PMG36 section 4.3.16 for new topics (HE-046, HE-057 to HE-063).
3. **NICE early value assessment.** Now "early-use HealthTech guidance" (HE-067); the old interim statement applies only to early-use topics started before 14 July 2025 (HE-066).
4. **ESF manual name.** The ESF cites the old manual title; the methods now sit in PMG36 and PMG48 (research file "Changes and conflicts", item 3).
5. **AMCP.** Final 6.0 wording not read; rows HE-133 to HE-139 are draft text.

## What the research file does not hold

Listed in its "Not sourced" section: the ISPOR task force full texts (abstract-level only), the CHEERS 2022 Explanation and Elaboration report, the Second Panel's recommendations, HAS device doctrine, DiGA economics, ICER's individual DHT reports, NICE DSU TSD 22 and 23, UKHSA cost-consequences advice, and EU HTACG device guidance. Any rule from these is `[GAP]`.
