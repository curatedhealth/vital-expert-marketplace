# Evidence maturity: the named frameworks and the library's convention

Interpretive reference shared with `company-and-evidence-assessment` (this pack); used here by A1 (evidence measures), A2 (movement read) and B1 (evidence review). Pack rule 7: apply a named framework with its own limits stated; the level assigned is labeled "proposed" for the person; never write "clinically validated" beyond the framework's own words. Rows come from `diligence-research.md` (DL, read 20 October 2026), `clinical-study-and-rwe-research.md` (CV), `hta-submissions-research.md` (UK), `health-economics-methods-research.md` (HE-) and `customer-success-implementation-research.md` (CS), read 19 October 2026.

Rows marked [PAPER] are published methods. The DOI travels with the row id: in prose, once at the first row from that paper; in a table, in the Rows cell beside the row id.

| Rows | Paper | DOI |
|---|---|---|
| DL-107 to DL-115 | Silberman et al. 2023, Evidence DEFINED | 10.1038/s41746-023-00836-5 |
| DL-116 to DL-118 | Day et al. 2022, clinical robustness score | 10.2196/37677 |
| DL-119 | Marshall et al. 2023, letter criticizing the score | 10.2196/41715 |
| DL-120, DL-121 | Sedhom et al. 2021, Digital Health Scorecard | 10.1038/s41746-021-00476-7 |
| DL-122, DL-123 | Goldsack et al. 2025, DiMe evaluation framework | 10.1038/s41598-025-21996-2 |
| DL-124, DL-125 | Vinay et al. 2025, funding versus evidence | 10.1371/journal.pone.0323390 |
| CV155 to CV159 | Goldsack et al. 2020, V3 | 10.1038/s41746-020-0260-4 |

## 1. Pick the framework by what the product is

| Framework | Built for | What it gives | Its own limits | Rows |
|---|---|---|---|---|
| NICE Evidence Standards Framework (ESF, ECD7) | Digital health technologies in the UK health and care system | A tier by intended purpose: A (system impact), B (understanding and communicating), C (interventions); most regulated medical devices fall in tier C, whose four groups follow the IMDRF significance-of-information axis (UK12, HE-082 to HE-084). 21 standards in 5 groups (UK13, CS57); an early-deployment subset of 16 (CS67). | Voluntary for NHS commissioners, "not mandated" (HE-079). Excludes software in a medical device, professional training and research data-collection technologies (HE-081). The tier classifies the product's purpose; it is not a grade of the evidence. Last updated 9 August 2022 (CS56). | UK12, UK13, HE-079 to HE-084, CS56 to CS68 |
| Evidence DEFINED | Patient-facing digital health interventions that change behavior and whose value depends on health outcomes; intended users are payers, PBMs, health systems, pharma, trade bodies and societies, not investors (DL-108) | Four steps: screen for absolute requirements, apply an established method such as GRADE, apply the supplementary checklist, apply evidence-to-recommendation guidelines (DL-107). Levels 0 (adoption not recommended, DL-110), 1 to 3 (feasibility, small and large clinical pilots, DL-111), 4 (scale may be appropriate with two or more high-quality RCTs, DL-112). | Evidence is one domain among several; interrater reliability not yet quantified; updates planned every 6 to 12 months (DL-113). Authors employed by a health insurer, disclosed (DL-115). The checklist items (Supplementary Table 2) are not in this skill's sources `[GAP]`. Step 1 requirements are set by each organization (DL-109). | DL-107 to DL-115 |
| V3 | Biometric monitoring technologies: connected products that turn mobile-sensor data into behavioral or physiological measures (CV156) | Three components: verification (bench, sensor), analytical validation (algorithm, in people), clinical validation (meaningful clinical state in the context of use) (CV155, CV157 to CV159). | Applies to sensor-based measures only. Does not apply to a therapy app with no sensor-derived measure; say so rather than force it. | CV155 to CV159 |

Comparators that are not maturity frameworks, cited only as context: the clinical robustness score (DL-116: FDA filings plus registered trials, equally weighted; 44 percent of 224 venture-backed companies scored 0 and the score did not correlate with funding, DL-117; proxies only, selection bias, authors from the cohort's data firm, DL-118) and its critique (DL-119: too narrow for services not regulated by FDA). The Digital Health Scorecard (DL-120, one oncology setting, DL-121). The DiMe evaluation framework (DL-122: evidence, usability, privacy and security as top domains; industry body authors, senior-skewed experts, DL-123). Funding did not track evidence in one dementia-prevention sample (DL-124). The research file's own summary: none of these was designed for investors, and none has published interrater reliability (`diligence-research.md`, "Changes and conflicts" item 8).

## 2. The library's evidence maturity score is a convention, not a framework

`diligence-dh.get_evidence_maturity` returns a score under rubric v1 (7 October 2026): "score = round(100 x points earned / assessable maximum); a component whose source is not loaded is excluded from the maximum, not counted as zero". Components and their rules as returned on 19 October 2026: regulatory status (20 points if any authorization is loaded, 10 more if any is a De Novo grant, of 30); clinical evidence (product-linked completed interventional studies, randomization, results posted, of 40); active development (of 10); product breadth (of 10). Reimbursement and jurisdiction breadth were excluded. Its own limits: "a stated convention for comparing documented evidence, not a predictive model or a valuation"; "US sources only; absence of EU, UK or Swiss data lowers nothing and proves nothing" (`examples/live/evidence_maturity_K191716_somnio_2026-10-19.json`).

How to use it:
- Report the score with its formula, every component and input, and the excluded components. Compare two dated runs with `scripts/maturity_diff.py`; never restate a score from memory.
- It is close in shape to the clinical robustness score (registrations as proxies, DL-116, DL-118) and carries the same criticism (DL-119). Say so when the person treats it as a quality measure.
- It counts registered studies in the loaded registry only. A product with published trials can score 0 on clinical evidence: write "no registered study linked in the loaded sources", never "no evidence".
- It never becomes a framework level, a rating of the company, or an input to a decision weight unless the person puts it there.

## 3. How to propose a framework level

1. Name the framework and why it fits the product (section 1 table). If none fits, say so `[GAP]`.
2. NICE ESF: propose the tier from the intended purpose as the record or the person states it, cite UK12 and HE-084, and add "proposed; the tier classifies purpose, not evidence".
3. Evidence DEFINED: the level needs a GRADE assessment of the product's studies (DL-107 step 2). This skill does not grade studies. If the person brings a review, use its certainty rating as theirs; otherwise route to `dh-clinical-development` literature-and-real-world-evidence-review and write "level not assessable until the evidence is graded `[GAP]`". Never assign level 4 without two or more high-quality RCTs the person or the review has identified (DL-112).
4. V3: list each component and whether the person's material or a record shows it; components with nothing behind them are `[GAP]`.
5. Write every level as "proposed level X under FRAMEWORK, for the person to confirm", with the framework's limits beside it.
6. Words never used: "clinically validated" (except V3's own "clinical validation" component, CV159, for a BioMeT that has it), "proven", "evidence-based" as a verdict.
