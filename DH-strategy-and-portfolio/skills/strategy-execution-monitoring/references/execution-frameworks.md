# Execution frameworks: what the sources say, row by row

Source: `strategy-and-portfolio-research.md` (SP rows SP-001 to SP-176, read 20 October 2026) and `diligence-research.md` (DL rows, read 20 October 2026). Interpretive reference for A1, A2 and B1. Every line carries its row. Rows marked [WF] were read through a summarizing fetch; rows marked [PAPER] carry their DOI; rows marked "(inference)" are labeled "(inference)" every time they are cited. In answers, cite each fact by source name and date in plain words with the row id after it (`gap-rules.md`, "How to cite"). A fact not in a row is `[GAP]`.

Most of these rows are UK public-sector guidance (HM Treasury and UK project delivery bodies). Used for a company, label each "UK public-sector guidance, applied here as a checklist" (pack rule 5). They describe how to plan and review; they set no target for anyone.

## 1. From strategy to objectives (A1)

| Term | As the source states it | Row |
|---|---|---|
| ROAMEF | Rationale, objectives, appraisal, monitoring, evaluation, feedback | SP-091 |
| SMART objective | Specific, measurable, achievable, realistic, time-limited | SP-092 |
| Business as usual | The outcome expected if current arrangements continue: the baseline a benefit is measured against | SP-093 |
| Appraisal and evaluation | Appraisal before approval; evaluation after implementation (Magenta Book); plan evaluation from the outset | SP-090 |
| Optimism bias | Increase estimated costs and timeframes, decrease estimated benefits; bounds below | SP-096, SP-170 to SP-176 |
| Management case | Plans for monitoring costs and realizing benefits (Teal Book) | SP-097, SP-098 |
| Integrated strategy and costed plan | WHO: digital health initiatives follow an integrated strategy that is the basis for a costed action plan, led through strong governance (public-health context) | SP-061 |

### Optimism bias: the published bounds (UK public-sector guidance)

The supplementary guidance gives upper and lower bounds by project type (HM Treasury Green Book supplementary guidance: optimism bias, Table 1, SP-172, UK public-sector guidance). Quote the bounds for the project type the person names, and the instruction to start at the upper bound and reduce only with evidence, as context; the uplift applied is the person's number. The Green Book 2026 still points to these generic values where a body has no historical evidence of its own (SP-171); the guidance is not withdrawn, but the PDF dates from 2003 and rests on a 2002 Mott MacDonald review (SP-170): say so.

| Project type | Works duration, upper | Works duration, lower | Capital expenditure, upper | Capital expenditure, lower |
|---|---|---|---|---|
| Standard buildings | 4 | 1 | 24 | 2 |
| Non-standard buildings | 39 | 2 | 51 | 4 |
| Standard civil engineering | 20 | 1 | 44 | 3 |
| Non-standard civil engineering | 25 | 3 | 66 | 6 |
| Equipment/development | 54 | 10 | 200 | 10 |
| Outsourcing | n/a | n/a | 41 (operating expenditure) | 0 (operating expenditure) |

- Software, systems and ICT development projects are "equipment/development" (SP-173): a remote monitoring or digital therapeutic build starts at 54% on duration and 200% on capital expenditure. A service run by a contractor may be "outsourcing" (41% on operating expenditure). Which type fits is the person's call.
- Upper bounds are average historic bias at outline business case stage; earlier stages may need more; they are indicative starting values (SP-174).
- Method: start at the upper bound; reduce by a mitigation factor from 0.0 to 1.0 per contributory factor managed; aim for the lower bound by contract award (SP-175).
- No sound bounds exist for operating costs (other than outsourcing) or for benefits shortfall: test benefits with sensitivity analysis and switching values instead (SP-176), for example `analytics.risk-tornado` on the person's own ranges.
- Keep the person's unadjusted and adjusted figures side by side, both labeled theirs.

## 2. Benefits management (A1 and A2)

| Point | As the source states it | Row |
|---|---|---|
| Document and owner | Assurance of Benefits Realisation in Major Projects v2.1, August 2026, produced by the National Infrastructure and Service Transformation Authority | SP-099 |
| Five stages | Identification, valuation, planning, realization, review | SP-100 |
| Review-stage slogans | Define success; identify benefits; value and appraise; plan to realize; work to realize; review performance; Gate 0 links benefits to strategy | SP-101 |
| Plan to realize | By full business case: select the benefits to concentrate on, allocate responsibility for each, choose the metric for tracking | SP-102 |
| Outcomes first | A project that fails to deliver what was planned is not a success, however cheap or fast | SP-103 |
| Benefits register | Each benefit with description, linked objective, benefit owner, beneficiaries, baseline, target and measurement method (Benefits Measurement Guidance Note, May 2021, written for commercial benefits) | SP-104 |
| Benefits report and review | Reports compare baseline, target and actuals; first benefits review at 12 months of contract delivery and at least every 12 months after, "comply or explain" (same note) | SP-105 |
| New collection [WF] | Government Project Delivery benefits management collection published 30 July 2026: quick guide, workbook, templates aligned to the Teal Book | SP-106 |

The register columns in `scripts/execution_check.py` follow SP-104 (baseline, target, owner, measure, linked objective) plus dates. The review cadence in SP-105 is a UK contract-management convention; the person's own reread dates govern.

## 3. Scorecards (A1, if the person uses one)

| Point | Row |
|---|---|
| Healthcare balanced scorecard studies focus on design more than use or review; no agreement on which perspectives to use in healthcare; leadership, culture and communication enable implementation | SP-107 [PAPER], DOI 10.3390/ijerph191610291 |
| Of 20 studies, positive outcomes for patient satisfaction and financial performance, mild for staff satisfaction; many at high risk of bias | SP-108 [PAPER], DOI 10.1186/s12913-021-07452-7 |

The scorecard perspectives, measures and targets are the person's. OKRs are not sourced (research file, "Not sourced"): `[GAP]`.

## 4. Option tests and experiments (A2)

| Point | As the source states it | Row |
|---|---|---|
| Purposeful even when small | Early feasibility studies are not designed to give statistically valid results but should have specified purposes, appropriate subjects and meaningful endpoints (FDA wording for device EFS; borrowed here as a checklist for any test) | SP-115 |
| What early studies are for | Identify device or procedure changes, refine the intended use population, refine nonclinical tests | SP-113 |
| When an EFS fits | Device changes expected; the information cannot practically come from nonclinical tests | SP-111 |
| Plan evidence early | Plan evidence that supports the intended purpose and value proposition; one study can show safe use and capture time savings (NHS AI and Digital Regulations Service, England) | SP-127, SP-128 |

A test that had no endpoint, no success criterion or no decision rule before it started cannot be read against a rule. That is a fact about the test, not about the option.

## 5. Partners and licensors named in the strategy (A2 step 4)

| Point | Row |
|---|---|
| A listed partner discloses a material definitive agreement on 8-K Item 1.01 within four business days | DL-019 to DL-021 |
| Material contracts, including licenses the business depends on, are filed as exhibits with the period's 10-Q or 10-K; terms may be redacted | SP-130 to SP-133 |
| The library change log began 12 October 2026; "no change recorded" is a statement about the log, not the company (`diligence_get_deltas_BigHealth_Akili.json`) | tools.md |
| Company status comes only from the company's own filings or register: 8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15; Companies House; German insolvency notices. Form 25 concerns the listing only (DL-144); Form 15 is not dissolution (DL-149, inference) | DL-135 to DL-168 |

A press report about a partner is not a signal until the primary record is read. Label it "from you (press claim, not checked)", then answer it from the record where a row covers the company, and correct its date if the filings date it differently.

### Company status for the companies the research pass read

The research pass of 20 October 2026 read the primary record for four companies that appear in saved library outputs. For these, quote the status below with the filing name and date and the row id after it; do not write "[GAP]: not read". Every SEC row here is [WF] (read through a summarizing fetch): say so. For any other company, run the status step and write "Company status [GAP]: not read" with the filings to open. Status is as of the read date, 20 October 2026; a later filing can change it.

| Company | What the record states (cite in plain words, row after) | What it does not mean | Rows |
|---|---|---|---|
| Akili, Inc. (EDGAR CIK 1850266; formerly the SPAC Social Capital Suvretta Holdings Corp. I; Akili Interactive Labs, Inc. is its wholly owned subsidiary, not a former name) | Akili 8-K, 29 May 2024: Item 1.01 merger agreement with Virtual Therapeutics Corporation, cash tender offer at $0.4340 per share, Akili to survive as a wholly owned subsidiary. Akili 8-K, 2 July 2024: Item 2.01 offer completed 2 July 2024; Item 5.01 change in control, Akili became a wholly owned subsidiary of Virtual Therapeutics Corporation; Item 3.01 Nasdaq asked to file Form 25, Form 15 to follow. Form 25-NSE filed by Nasdaq, 2 July 2024 (body not readable). Form 15-12G, 12 July 2024. After it, only third-party SC 13G/A filings (last 13 November 2024) | The 29 May 2024 8-K is signing, not closing (DL-138). Form 25 concerns the exchange listing only (DL-144); after a merger it signals the old shares were converted, not that the business failed (DL-142, inference). Form 15 means SEC reporting stopped, not that the company ceased to exist (DL-149, inference). No later Akili filing will show a license or deal: it no longer reports | SP-148, SP-150 to SP-154 |
| Pear Therapeutics, Inc. (EDGAR CIK 1835567; formerly Thimble Point Acquisition Corp.) | Pear 8-K, 7 April 2023 (report date 5 April 2023): Item 1.03 chapter 11 filed 7 April 2023, US Bankruptcy Court for the District of Delaware, case 23-10429; Item 2.05 about 170 employees (92% of full-time staff) terminated; Item 7.01 a section 363 sale process, equity holders told to expect little or no recovery. Pear 8-K, 10 April 2023: Item 3.01 Nasdaq delisting notice, trading suspended 19 April 2023, no appeal. Form 25-NSE, 2 May 2023, is the last filing; no Form 15 and no 8-K after 10 April 2023 | No Item 1.03(b) plan confirmation appears, so the case outcome is open on EDGAR (DL-137, inference). No Pear filing names a buyer of Somryst, reSET or reSET-O; the court sale orders were not read | SP-155 to SP-161 |
| Big Health Inc | Not an SEC filer: EDGAR name lookup and Form D full-text search returned no entity (SP-162 [WF]). FDA establishment registration 3024442350 (Newport Beach), active, registration year 2026; listings SleepioRx (K233577) and DaylightRx (K233872) | An active FDA registration is not corporate status. No SEC forms exist to read; corporate status needs the state register for its legal entity: "Company status [GAP]: not read" for that register; ask the legal entity | SP-162, SP-163 |
| Aidoc Medical Ltd. | Not an SEC filer (SP-162 [WF]). FDA establishment registration 3014938447 (Tel Aviv-Yafo, Israel), active, registration year 2026, 25 device listings (mostly BriefCase triage and quantification, and aiOS) | As above: FDA registration is not corporate status; the Israeli company register was not read: "Company status [GAP]: not read" | SP-162, SP-164 |
| Virtual Therapeutics Corporation (Akili's acquirer) | No row | "Company status [GAP]: not read"; ask the legal entity and its register | none |

### Authorization holder and listing holder are different facts

The 510(k) or De Novo record names the applicant at clearance; the FDA registration and listing record shows who lists the device now. State both, each with its source, and never treat the listing holder as the buyer, licensor or rights holder: that is a contract or court-record question for the person's legal owner.

| Product | Authorized to (applicant at clearance) | Current FDA listing holder | Rows |
|---|---|---|---|
| EndeavorRx | De Novo DEN200026: akili interactive labs, inc. (Boston) | "AKILIINTERACTIVE Labs, Inc. C/O Virtual Therapeutics" (registration 3013341423, Kirkland, WA), registration year 2026; a second listing cites K231337 (created 25 June 2024) | SP-166, SP-168 |
| Somryst | 510(k) K191716: Pear Therapeutics, Inc., decision 23 March 2020 | Nox Medical (registration 3007389703, Reykjavik, Iceland), listing created 18 December 2024 | SP-165, SP-167 |
| reSET, reSET-O | De Novo DEN160018 and 510(k) K173681: applicant not in this skill's rows | Harvest Bio LLC (registration 3033280591, Middletown, CT), listings created 14 November 2024 | SP-169 |

Library profiles can carry a different CIK from the listed parent: the saved profile for "Akili Interactive Labs, Inc." carries CIK 0001741200 with two Form D rows (library, retrieved 19 October 2026), while the listed company whose 8-Ks are above is Akili, Inc., CIK 1850266 (SP-148 [WF]). Say which entity each fact belongs to.

A partner's change of control or delisting does not fail a milestone by itself: a milestone fails only on the elements of the person's pass rule. What the change means for the agreement (assignment, change-of-control clauses, the counterparty's legal name) is for the owner the person names for legal matters, or owner not named. If a partner's products on record do not match what the person says it supplies (for example a licensor named for a triage algorithm whose record lists only ADHD treatment products), say so as a fact and ask the person to confirm the counterparty's legal name on the contract.

## 6. Benchmarks

No source gives a benchmark for realization rates, milestone hit rates or experiment success rates in digital health (research file, "Not sourced"). A development success rate (SP-082 to SP-087) is drug-program context with its counting method, never a target or a threshold for the person's milestones.
