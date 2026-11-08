# Intake

Ask for all missing items in one message. For each item, what happens if it is missing is stated.

| # | Input | If missing |
|---|---|---|
| 1 | Buyer mode: business development (fit and deal terms) or investor (value inflection and capital) | ask; do not start |
| 2 | Unit: single asset, or company (list the pipeline assets to run; each gets its own register, then a roll-up) | ask; do not start |
| 3 | Markets in scope: US, EU, or both | ask; another market is a [GAP], never a guess |
| 4 | Asset: INN or code, indication as worded in the (expected) label, modality, mechanism class, development phase, whether patients are selected by a biomarker | ask; do not assume a product, indication or phase |
| 5 | Documents provided, each with its type (regulatory review document, journal paper, registry entry, clinical study report, protocol and analysis plan, investor deck, press release, conference abstract) and date | ask; with no documents the register has no rows |
| 6 | Whether a data room index exists and which listed items are not yet provided | record "not yet set"; listed-but-missing items become gaps |
| 7 | The mechanism register from assess-scientific-validity-and-moa, if it exists | record "not yet set"; any row whose mechanism rationale is a GAP stays a GAP and the register says so |

Explicit don'ts: never assume the product, indication, phase or market; never treat a press release or conference abstract as the regulatory record; never choose an estimand strategy the documents do not state (record it as GAP).
If the only documents are press releases or abstracts, say so at the top of the register and carry the regulatory-record gap. If no clinical data exist (preclinical asset), write one gap row and stop; skill B can still chain a benchmark from phase.
