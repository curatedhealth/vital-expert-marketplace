# Worked example: A1 lifecycle stage map with a named comparable product (live data, 20 October 2026)

**Request (illustrative product, real comparable):** "We are building a game-based attention therapy for children with ADHD. We have a working prototype and a draft intended use; no feasibility study yet. Our stages are Concept, Feasibility, Pivotal, Release, Post-market. Which stage are we in, what do we owe before Feasibility, and how did EndeavorRx move through FDA? Owner: Mia Chen, head of product."

---

**Answer.** You are in your Concept stage, which maps to the MRC/NIHR "development or identification of the intervention" phase (TM2; DOI 10.1136/bmj.n2061). The item that blocks Feasibility is a set of predefined progression criteria (TM14); without them a feasibility study has nothing to pass.

**What Concept owes (from what you shared)**

| Work product | Named by | Status |
|---|---|---|
| Intended use and definition statement (significance, situation, core functionality) | IMDRF N12 (PL58) | Draft held; version not given |
| Program theory: components, mechanisms, context | MRC/NIHR (TM6, TM7; DOI 10.1136/bmj.n2061) | [GAP] |
| Key uncertainties named | MRC/NIHR (TM4, DOI 10.1136/bmj.n2061) | [GAP] |
| Predefined progression criteria for feasibility | MRC/NIHR (TM14, DOI 10.1136/bmj.n2061) | Missing |
| Design and development plan in the design and development file | QMSR via ISO 13485 7.3.10 (PL9, QS24) | [GAP] |

**Blocks, by dependency.** Definition statement, then program theory, then progression criteria, then Feasibility entry. Repeat Concept rather than move on while these stay open (TM3).

**EndeavorRx, from the FDA records (retrieved 13 October 2026)**

| Date | Record | Pathway | Days submission to decision | Predicate as stored |
|---|---|---|---|---|
| 15 June 2020 | DEN200026 EndeavorRx | De Novo, class 2, product code QFT, regulation 882.5803 | 60 | none stated |
| 13 December 2023 | K231337 EndeavorRx | 510(k) | 219 | DEN200026 |
| 14 June 2024 | K233496 EndeavorOTC | 510(k) | 228 | DEN200026 |

MAUDE: 2 reports for QFT, both 2023; reports, not confirmed events. No recall or alert stored. Records only: they do not state why the later 510(k)s were filed, what changed, or the product's market status. Whether your product falls under 882.5803 is a question for `dh-regulatory-and-quality` regulatory-pathway-and-classification.

**Decisions for Mia Chen.** (1) Which progression criteria Feasibility must meet (TM14). (2) Whether Concept repeats until the program theory exists (TM3). (3) Who attends the Feasibility entry gate (PL1).

**Gaps and stops.** Device status not stated `[GAP]`. Clinical claims for the game mechanism stay hypotheses until tested; the evidence goes to `dh-clinical-development` study-protocol-and-endpoint-design.

**Record.** Lifecycle stage map draft for Mia Chen. AI-assisted. Clears it: Mia Chen, head of product. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

**Calls made (live, counted):** `regulatory-dh.get_authorization {reference: "DEN200026"}`; `regulatory-dh.search_devices {query: "Akili", jurisdiction: "US"}`; `regulatory-dh.search_safety_events {product: "EndeavorRx"}`. Outputs saved in `examples/live/regulatory_records_2026-10-20.json`; timeline built with `python3 scripts/lifecycle_timeline.py examples/live/regulatory_records_2026-10-20.json --product endeavor` (output in `examples/live/timeline_endeavorrx.md`). No unpublished product name was sent to the library.

---

Word count of the answer above (without the calls list and the table's source column), counted with `wc -w` during the build: under 450.
