# Component adoption and drift

Inventory rows: 11; components: 7; component uses (component x product): 18; products: 6 (your product list).
Products in your list using no listed component: Help center.

## Adoption by component

| Component | Current version | Products using it | On current version | Versions in use | Which versions |
|---|---|---|---|---|---|
| Alert banner | 1.0.0 | 1 of 6 | 1 of 1 | 1 | 1.0.0 |
| Button | 4.2.0 | 4 of 6 | 4 of 4 | 1 | 4.2.0 |
| Date picker | 4.2.0 | 3 of 6 | 1 of 3 | 2 | 4.1.0, 4.2.0 |
| Dose input | 3.0.0 | 3 of 6 | 2 of 3 | 2 | 2.0.0, 3.0.0 |
| Input mask | 2.3.0 | 2 of 6 | 2 of 2 | 1 | 2.3.0 |
| Modal | 4.2.0 | 1 of 6 | 0 of 1 | 1 | 4.0.2 |
| Text input | 4.2.0 | 4 of 6 | 3 of 4 | 2 | 3.8.1, 4.2.0 |

## Drift: uses not on the current version

| Component | Product | In use | Current | Drift | Owner | Clinical surface | Device UI |
|---|---|---|---|---|---|---|---|
| Date picker | Patient app Android | 4.1.0 | 4.2.0 | behind: minor (1) | Patient app team | yes | yes |
| Date picker | Patient app iOS | 4.1.0 | 4.2.0 | behind: minor (1) | Patient app team | yes | yes |
| Dose input | Dosing calculator | 2.0.0 | 3.0.0 | behind: major (1) | Dosing team | yes | yes |
| Modal | Marketing site | 4.0.2 | 4.2.0 | behind: minor (2) | Growth team | no | no |
| Text input | Marketing site | 3.8.1 | 4.2.0 | behind: major (1) | Growth team | no | no |

## Behind current, by owner

| Owner | Uses | Behind current | of which clinical surface | of which device UI |
|---|---|---|---|---|
| Clinician portal team | 4 | 0 | 0 | 0 |
| Dosing team | 1 | 1 | 1 | 1 |
| Growth team | 3 | 2 | 0 | 0 |
| Patient app team | 4 | 2 | 2 | 2 |
| Platform team | 6 | 0 | 0 | 0 |

## Accessibility status, as you recorded it

| Component | Version | Status (your words) | Products | Clinical surfaces | Device UI |
|---|---|---|---|---|---|
| Alert banner | 1.0.0 | not tested | 1 | 1 | 0 |
| Button | 4.2.0 | tested WCAG 2.2 AA September 2026 | 4 | 3 | 3 |
| Date picker | 4.1.0 | 2 issues open (target size 2.5.8) | 2 | 2 | 2 |
| Date picker | 4.2.0 | tested WCAG 2.2 AA September 2026 | 1 | 1 | 0 |
| Dose input | 2.0.0 | tested WCAG 2.1 AA March 2025 | 1 | 1 | 1 |
| Dose input | 3.0.0 | not tested since 3.0.0 | 2 | 2 | 2 |
| Input mask | 2.3.0 | 1 issue open (error identification 3.3.1) | 2 | 2 | 2 |
| Modal | 4.0.2 | tested WCAG 2.1 AA March 2025 | 1 | 0 | 0 |
| Text input | 3.8.1 | tested WCAG 2.1 AA March 2025 | 1 | 0 | 0 |
| Text input | 4.2.0 | tested WCAG 2.2 AA September 2026 | 3 | 3 | 3 |

Uses by status: tested WCAG 2.2 AA September 2026: 8; tested WCAG 2.1 AA March 2025: 3; 2 issues open (target size 2.5.8): 2; not tested since 3.0.0: 2; 1 issue open (error identification 3.3.1): 2; not tested: 1.

## Local modification (drift from the system)

| Component | None | Override | Fork | Not recorded |
|---|---|---|---|---|
| Alert banner | 1 | 0 | 0 | 0 |
| Button | 4 | 0 | 0 | 0 |
| Date picker | 3 | 0 | 0 | 0 |
| Dose input | 2 | 0 | 1 | 0 |
| Input mask | 0 | 2 | 0 | 0 |
| Modal | 1 | 0 | 0 | 0 |
| Text input | 3 | 1 | 0 | 0 |

Forked uses receive no updates from the system component (research row DSX-33): Dose input in Dosing calculator.

## Lifecycle

Uses by lifecycle value: stable: 13; trial: 3; use with caution: 2.

In use with a flagged lifecycle value (deprecated; retired; use with caution):

| Component | Product | Version | Lifecycle | Owner | Clinical surface |
|---|---|---|---|---|---|
| Input mask | Clinician portal | 2.3.0 | use with caution | Clinician portal team | yes |
| Input mask | Dosing calculator | 2.3.0 | use with caution | Clinician portal team | yes |

No threshold, target or verdict is applied. Counts are on your inventory as supplied.
