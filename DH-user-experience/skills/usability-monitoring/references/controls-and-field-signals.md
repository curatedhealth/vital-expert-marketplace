# Controls in the build and signals from the field

Used by A2. `UX-` rows are in `ux-usability-research.md`; `CS` rows in `implementation-research.md`.

## 1. Checking controls against the build

| Rule for the skill | Rows |
|---|---|
| Risk-control order of preference: inherent safety by design, then protective measures, then information for safety (labeling, training). The check records each control's type as designed and as shipped. | UX-US-33 |
| The user interface includes packaging, labeling, training materials, controls, displays, alarms and logic of operation, so a control may sit outside the screen. | UX-US-31 |
| Labeling or "additional training" as the fix for critical-task errors is not acceptable without data showing it works. A control that moved from design to training between mock-up and build is a change the check reports. | UX-US-42, CS79 |
| Training is valid but not preferred, because knowledge decays and labeling may not be at hand. | CS77, CS78 |
| The training customers receive should match the training used in validation. | CS80 |
| Lay-use devices let users verify, where appropriate, that the device works, and warn when no valid result was produced. | UX-EU-19 |

The old register rule holds: a control in the mock-up is not a control in the build. Each control is checked on the build version the person names, with their evidence (screenshot, build note, test record).

## 2. Signals after release

| Signal | Rule | Rows |
|---|---|---|
| User feedback on decision support | Certified modules let users give feedback on evidence-based interventions, exportable with intervention, action, feedback, user, date and location. If the product is certified health IT, this export is a monitoring source. | UX-US-55 |
| Expected usage profile | NICE ESF Standard 16: company and evaluator agree a plan to report usage against an expected usage profile agreed at commissioning, plus anonymized aggregate outcomes. | CS61 |
| Performance changes | NICE ESF Standard 16: for products that change over time, agree how and when performance changes are reported and to whom. | CS62 |
| Pilot-site statement | NICE ESF Standard 15: real-world pilot evidence may include a statement that the product was used as expected (who, how, for how long). | CS59 |
| Deploying site self-assessment | SAFER Guides (2025 set of eight; CMS measure text still says "all nine"). The site's own self-assessment, not the manufacturer's. | CS72, CS73, CS74 |
| Comparable field events | `regulatory-dh.search_safety_events`: recalls and MHRA alerts of comparable products. Prompts only. | `references/tools.md` |

## 3. What the field-event tool can and cannot do (observed 19 October 2026)

- Can: match a word in the product text in US recalls (`product: "insulin"` returned six recalls; `product: "display"` three), and return UK MHRA alerts with gov.uk URLs (`product: "software", jurisdiction: "UK"` returned eight).
- Cannot: filter by cause (no use-error field; `product: "use error"` returned nothing); link US recall records (API endpoint only, no recall number); state the basis of `event_date`; keep one recall as one row (two rows for the 27 February 2025 Tandem recall); explain the MAUDE blocks it attaches (NVI and PDT on `product: "decision support"` with no recalls). EU 0 and CH 0 events are loaded.
- Interface-related summaries seen: Omnipod 5 iOS App, Class II, 23 May 2025 (comma not recognized as decimal separator; "0.1 unit recognized as 1 unit"); t:slim X2 with the t:slim mobile app, Class II, 3 July 2025 (right-to-left language, graphical defects); Hologic Genius Review Station display, Class II, 23 March 2026 (operated outside the validated display configuration "due to user modification of the manufacturer-installed settings").

Describe each event only by what its record states. A recall of another product is never evidence of a use error, a cause or a design flaw, and absence of events is not evidence of safety.

## 4. Not in the sources

- Thresholds for feedback volume, override rates or usage drop-off that should trigger action. These are the person's.
- DCB0160 clause content (hazard log, safety case) `[GAP]`; the DCB0160 rows are [WF] (CS70, CS71).
- Post-market vigilance timelines: the Quality and Regulatory packs hold them.
