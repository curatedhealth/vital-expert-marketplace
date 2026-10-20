# Data integrity controls: the rules and where they come from

Interpretive reference for task B1. CV rows are in `clinical-study-and-rwe-research.md`; CVB rows in `gcp-quality-rows.md`.

## The frame: quality by design, set by the sponsor

- Quality is built into design and conduct; quality means fitness for purpose; critical-to-quality factors are identified prospectively. CV5, CV6; ICH E8(R1) CV28, CV29
- Where relevant, the sponsor sets pre-specified acceptable ranges (for example quality tolerance limits) for critical-to-quality factors; when exceeded, an evaluation checks for a systemic issue and whether action is needed. CVB3
- Processes are proportionate to risk to participants and importance of the data. CV7

This is why every pass rule in B1 is the person's: the sources require that limits exist and are set in advance; they do not set the limits.

## Control checklist (each line is a requirement element, not a threshold)

| # | Control | What the source asks | Row |
|---|---|---|---|
| 1 | Computerized systems fit for purpose | Fit for purpose, for example through risk-based validation. | CV9 |
| 2 | Validation owner and basis | The responsible party owns validation status over the life cycle; the approach rests on a risk assessment of intended use, data importance and potential impact. | CV11 |
| 3 | Validated before use; change control | Validated before use; later changes validated based on risk, considering old and new data. | CV12 |
| 4 | What is validated | Standard functions and protocol-specific configurations, automated checks and calculations; interfaces defined and validated; design through change control. | CV13 |
| 5 | Audit trails | Not disabled; modified only rarely with a logged justification; interpretable; unambiguous timestamps (for example UTC). | CV14 |
| 6 | Data flow overview | All parties see the data flow; tools validated for intended use; data and metadata move together. | CV102 |
| 7 | Source location | First durable electronic repository is the source for DHT data (FDA). | CV60 |
| 8 | Linkage | If sources are linked, the protocol prespecifies it, including how inconsistencies are resolved. | CV24 |
| 9 | RWD inside the trial | Fitness for purpose by reliability (accuracy, completeness, provenance, traceability) and relevance (key data elements). | CV23 |
| 10 | Centralized monitoring | Risk-based and centralized monitoring for missing, inconsistent and outlying data and potential deviations; trends within and across sites. | CV71, CVB5, CVB6 |
| 11 | Important deviation criteria | The sponsor sets trial-specific criteria for important deviations. | CVB2 |
| 12 | Contingency | Contingency plan for digital tool malfunction for critical-to-quality elements. | CV99 |
| 13 | Participant-entered endpoints | Erroneous entry on primary, key secondary or safety endpoints minimized. | CV103 |
| 14 | Same method across arms | One collection method in all arms. | CV58 |

## Reliability wording differs by source

ICH E6(R3) Annex 2: reliability = accuracy, completeness, provenance, traceability (CV23). FDA EHR and claims guidance (drugs): accuracy, completeness, traceability (CV79). FDA CDRH device guidance: accrual, quality, integrity; relevance = availability, timeliness, generalizability (CV91, CV92). Name the one you apply for the person's jurisdiction and product.

## What "met" means in a review

A control is "met" only on evidence the person shows (a validation summary, an audit-trail setting, a data flow diagram, a monitoring plan section). A vendor statement or a checklist tick without the document is "stated, evidence not seen". The model never writes that a system is validated or that the trial is inspection-ready.
