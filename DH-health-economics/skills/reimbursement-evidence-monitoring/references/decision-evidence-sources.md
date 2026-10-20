# Where bodies show how they treated the evidence, and what the library holds

Interpretive reference for A1 and B1. Rows cited `HE-` are in `health-economics-methods-research.md`, `ES-` in `evidence-synthesis-research.md`, and `EN-`, `DE-`, `FR-` in `access-monitoring-sources.md`. All read 19 October 2026, not owner-reviewed. Rows marked [WF] were read through a summarizer: re-check before reuse.

## What a decision can tell you about the evidence

| Body | Where the reasoning on evidence sits | What it can say | Rows |
|---|---|---|---|
| NICE (HealthTech, early use) | The guidance's recommendations, "Committee discussion" and evidence-generation sections on nice.org.uk | Recommendation category (use while evidence is generated, more research needed, should not be used); the uncertainties the committee named; the outcomes prioritized for evidence generation; whether the economic analysis suggested value for money | `HE-071`, `HE-072`, `EN-1` to `EN-3` |
| NICE (routine use) | Recommendations, "Evidence" and "Committee discussion" sections | Whether the committee accepted the model's structure and inputs, which inputs drove the result, the conditions of a recommendation, further research asked | `HE-073`, `HE-076` |
| NICE early use, afterwards | Withdrawal or change of a recommendation; re-evaluation for routine use | NICE may withdraw a recommendation on listed grounds, including a company not engaging in evidence generation or evidence generation not resolving the essential uncertainties; companies may submit evidence early at monitoring touchpoints | `EN-2`, `EN-3`; `HE-072` |
| BfArM (DiGA) | The directory entry: claimed positive care effects, with unconfirmed ones struck after a trial | Which claimed effects a trial study did not confirm | `DE-24`; `DE-2` |
| GKV-Spitzenverband | Annual report on trial outcomes | Aggregate trial outcomes and the payer's stated reason for removals; no list of narrowed listings | `DE-1` to `DE-3` |
| HAS (CNEDiMTS) | Published opinions | Favorable or unfavorable opinion, and any real-world follow-up study required | `FR-5`, `FR-6` |
| EU JCA | JCA reports | Relative effects and the degree of certainty, with no value judgment; no economic content | `ES-149`, `HE-094`, `HE-095` |
| ICER-PHTI | Individual digital health assessment reports | `[GAP]`: no individual report was read (research file, "Not sourced") | |
| IQWiG | Health economic evaluations under § 35b SGB V, mainly drugs | `[GAP]` for digital products: none read | `HE-109` |

## What the library holds (measured 19 October 2026)

| Scheme | Rows | What a row holds | What it does not hold | Source |
|---|---|---|---|---|
| UK_NICE_EVA | 15 | Guidance title, reference, publication date, status "conditional", source URL, and an `evidence_passage` that is the page header and section list | The recommendations, committee discussion, uncertainties, economic results or evidence-generation outcomes | `tools.md`; `examples/live/nice_eva_precedents_2026-10-19.json` |
| UK_NICE_HTG | 2 | Same fields, status "permanent" and status_raw "recommended" | Same; HTG778, titled "early-use assessment", is stored as permanent | `examples/live/nice_htg_precedents_2026-10-19.json` |
| UK_NICE_NHAP | 0 | | Everything | `tools.md` |
| FR_PECAN, FR_LATM | 2 each | Listing status and dates | CNEDiMTS opinions and their reasoning (register N7) | `tools.md` |
| FR_LPPR | 0 | | Everything | `tools.md` |
| DE_DIGA | 82 | Listing status, dates, price | Claimed and struck positive care effects, study links (register N7) | `tools.md` |

Saved decision text (read 19 October 2026 by curl, under `examples/live/nice_pages/`): HTG624 chapters 1 (Recommendations), 3 (Evidence) and 4 (Committee discussion); HTG660 chapters 1 and 4 (Evidence generation recommendations); HTG675 chapters 1 (Recommendations), 3 (Committee discussion) and 4 (Further evidence), and its evidence generation plan chapter 3 (`htg675_egp_chapter_3.txt`). These are the run's reading, not library holdings.

Saved decision text (read 20 October 2026 by curl, dated files `*_2026-10-20.txt`, each starting with its URL and retrieval date): HTG624 overview, chapters 1, 2 (The technology), 3, 4, update information and history; HTG562 (Zio XT for detecting cardiac arrhythmias) overview, chapters 1 to 4, update information and history.

Dates on the HTG624 pages (read 20 October 2026): overview "Last reviewed: 20 May 2022"; update information "December 2025: Medical technologies guidance 70 has been migrated to HealthTech guidance 624. The recommendations and accompanying content remain unchanged." The history page lists development documents only (scope 24 November 2020, draft guidance 1 November 2021, guidance documents 20 May 2022) and shows no "Last updated" date. The day of the December 2025 migration is not stated: `[GAP]`. HTG562: overview "Last reviewed: 1 December 2020"; update information "December 2025: Medical technologies guidance 52 has been migrated to HealthTech guidance 562."

So the library tells you **which** decisions exist and when; the decision document tells you **how** the evidence was treated. Read the page at `source_url`, or ask the person for the document, and quote it.

## What is not published or not sourced

- Product-level re-evaluation outcomes for early-use guidance: none published for HTG675 at the read date (`EN-6`).
- Which DiGA were narrowed after trial: the GKV report gives no list (`DE-2`).
- Individual ICER-PHTI reports, IQWiG evaluations of digital products, HAS rules on when an economic opinion is required for devices: `[GAP]` (HE research file, "Not sourced").
- NICE evidence generation plans are separate documents linked from the guidance; their content is read per guidance, not held in the references.

## Conflicts

- HTG675 evidence generation plan, section 3.5 (https://www.nice.org.uk/guidance/htg675/resources/evidence-generation-plan-for-digitally-enabled-therapies-for-adults-with-depression-13254224365/chapter/3-Approach-to-evidence-generation, page last updated 14 December 2023, read 19 October 2026): "This will be 3 years to allow for setting up, implementation, data collection, analysis and reporting." The guidance itself says "This guidance will be reviewed within 4 years" (`EN-6`). The plan does not state the date the 3 years start from: `[GAP]`. Show both; NICE decides. Saved text: `examples/live/nice_pages/htg675_egp_chapter_3.txt`.

## Reading a NICE decision for the evidence (checklist for A1)

1. Recommendation category and its wording, verbatim, with section number (`HE-071`).
2. For early use: the outcomes the committee prioritized for evidence generation (usually a list in the recommendations or an evidence-generation section) and the stated period or review point. Where the guidance states its own period (for example review within 4 years for HTG675, `EN-6`; 2 years for HTG768, `EN-5`), it governs over the 3-year default in PMG48 (`HE-072`).
3. Economic evidence: what the guidance says about cost-effectiveness or cost saving, the price or uptake it rested on if stated, the section 3 model result for each price and scenario, and the limitations the committee named, verbatim. Tie each limitation to the price, model or scenario it was raised against. Where a guidance tested several prices or scenarios, a doubt raised on one is not a doubt on the others. Worked mappings, checked against the saved pages:
   - HTG624 (Sleepio). Population-based price: cost incurring at 1 and 3 years; uptake drove the result (4.14). £66.11 tiered price: "cost incurring by £16.59 per user at the end of year 1 but cost saving by £68.97 per user at 3 years"; the 3-year extrapolation was not accepted (4.14). £45 per user (accepted): "cost saving by £4.52 per person" at 1 year and "the results do not depend on the uptake of the technology" (3.9); limits "dependence on the Sampson et al. (2021) study and the lack of remission outcomes" (4.15). All prices: comparator definition (3.4), no head-to-head evidence (4.5), drop-out bias (4.6), model variables and no data linkage (4.13), equivalence on indirect evidence (4.16).
   - HTG562 (Zio XT). Original price (£310, 2.8): after EAC revisions cost incurring in all three models (3.13). EAC base case: assumed an outpatient appointment after every test, which the committee said does not fully reflect practice (4.9). £265 in scenarios 3 and 5: cardiology saving in both; stroke model incurring in both; downstream stroke saving in scenario 3, incurring in scenario 5 (3.15). Long-term benefits not captured: stroke and cardiology models (diagnosis costs only), downstream stroke model beyond year 1, no cardiology downstream model (4.10). All prices: follow-up and repeat-test assumptions (4.11, 4.12, 3.14, 3.17), resource use and long-term consequences (4.12, data collection in 1.1).
4. Uncertainties and further research: what the committee said was missing.
5. Dates on the page: "Last reviewed" on the overview and the entries under update information (migration, changes), against the library's stored history (the store may hold only a day-zero snapshot, `tools.md`). The history page lists development documents, not a last-updated date.

Never turn a committee statement into a stronger one. "Could be cost effective based on current prices and evidence" is not "cost-effective".
