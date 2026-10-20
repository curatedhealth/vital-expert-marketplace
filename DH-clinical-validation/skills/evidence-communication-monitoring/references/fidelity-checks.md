# Fidelity checks: how a communication drifts from its evidence

Interpretive reference for A2 and B1. Rows: CV (`clinical-study-and-rwe-research.md`), ES (`evidence-synthesis-research.md`), PC (`promotion-and-claims-research.md`), read 19 October 2026 (ES section 15 read 20 October 2026). The comparison is always statement against passage and rating; the passage is read by a person or by you, never accepted from a tool status alone (register N3).

## Drift types

| # | Drift | What to compare | Rows it touches | Level | A faithful wording keeps |
|---|---|---|---|---|---|
| 1 | Comparator changed or dropped | Comparator in the statement versus the trial's | PC-US-03 (omission); PC-US-23 (US De Novo or PMA, cleared indication factors) | Review | The trial's comparator, named |
| 2 | Population widened | Population in the statement versus the studied and the cleared one | PC-US-23, PC-US-27; PC-EU-02; for prediction models TRIPOD+AI item 3b (CV125, [PAPER] DOI 10.1136/bmj-2023-078378) | Stop if beyond the intended use, else Review | The studied population, and the cleared one where they differ |
| 3 | Outcome switched or secondary presented as primary | Outcome and time point in the statement versus the prespecified ones | CONSORT 2025 items 10 and 14 (CV113, CV114, [PAPER] DOI 10.1136/bmj-2024-081123) | Review | The prespecified outcome and time point; others labeled secondary or not prespecified |
| 4 | Effect restated | Measure, size, direction and time point versus the passage (within-arm shown as between-arm, standardized effect shown as points, a p-value as "proven") | `certainty-wording.md` rule 3 | Review | The effect as the passage reports it |
| 5 | Certainty inflated | Certainty word or verb versus the person's or a body's rating (an unhedged "reduces" needs high, "likely" or "probably" moderate, "may" low, "the evidence is very uncertain" very low: Cochrane Handbook Table 15.6.b); a wide interval including no effect stated as "no effect"; a library starting level printed as certainty; certainty pooled across outcomes | ES-89, ES-90, ES-94, ES-96, ES-99, ES-195 to ES-198, ES-203 to ES-207 | Review | The rating, its rater and date, per outcome, with the Table 15.6.b verb for that rating |
| 6 | Unfavorable findings or harms dropped | Harms, null secondary outcomes, limitations, funding and conflicts (CONSORT 2025 item 5, CV111 [PAPER] DOI 10.1136/bmj-2024-081123) in the source versus the communication; where only the abstract was read, funding and conflicts not checked `[GAP]` | PC-US-31 (US clinician material); PC-US-40 (US payor); CONSORT 2025 item 15 harms (CV112, [PAPER] DOI 10.1136/bmj-2024-081123) | Review | Unfavorable findings and the material limitation |
| 7 | Proof, cure or guarantee language | Words such as proven, cure, guaranteed, no side effects | PC-EU-10; PC-DE-03, PC-DE-04; PC-UK-04, PC-UK-07; PC-UK-13 [INDUSTRY] | Stop | Factual result wording |
| 8 | Weak study carried by a disclaimer | A claim larger than the study, with a limitation line added | PC-US-30 (US clinician material); PC-US-53 (uncleared uses) | Stop | A claim the study can carry |
| 9 | Retracted, corrected or superseded source | Currency check of each cited DOI | ES-119, ES-121, ES-123 | Stop if retracted; Review if corrected | The current version, or the statement removed |
| 10 | Study not identified (Germany, advertising) | Whether the study concerns the product itself, author, date, source; figures reproduced faithfully | PC-DE-05 | Note, or Review if a figure is altered | Full citation and faithful figures |
| 11 | Wrong audience | US payor material on a public website or given to prescribers | PC-US-35 | Review | Separate versions per audience |
| 12 | Uncleared use to clinicians or consumers | Use or population outside clearance | PC-US-27; PC-US-50 to PC-US-56 (SIUU final January 2025, not for current implementation, PC-US-56) | Stop | Not drafted; scientific exchange routed to the owner |
| 13 | Single study as a body of evidence | "The evidence shows", "studies show" for one trial | `certainty-wording.md` rule 6 | Review | "In one randomized trial of N participants" |
| 14 | Registry details wrong or missing | Registry name, id and date in the paper versus the registry | CONSORT 2025 item 2 (CV111, [PAPER] DOI 10.1136/bmj-2024-081123) | Note | The registry, id with URL and date |
| 15 | Number with no passage | Any figure not found in a supplied passage | register N3 (Verify returned "partial" when a claim held a figure the passage lacked); check every figure by hand | Review | The figure from the passage, or removed |

Levels: **Stop** means the statement crosses a prohibited form, goes beyond the intended use, or rests on a retracted source; it stays out until the owner decides. **Review** means the statement differs from its passage or rating, or lacks a required statement; the owner decides on the faithful wording. **Note** means presentation or citation detail.

## Reviews and third parties citing the trial

`literature.find_related {direction: "cited_by"}` lists papers that cite a trial (via Semantic Scholar, no total count, no citation intent; `examples/live/find_related_cited_by.json`). A third party's restatement is described only by what its text says; drift there is reported to the person as a fact about that publication, never as the third party's error or intent. Correcting the published record is the authors' and the journal's process; the skill does not draft letters to editors.

## Impact measures

Reach, downloads, citations, questions received, recall or prescribing intent are not sourced here. They are the person's measures, from the person's data. A citation count is not evidence that a message landed as intended, and no impact measure is evidence of clinical effect.
