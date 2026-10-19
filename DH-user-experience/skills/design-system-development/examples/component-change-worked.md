# Worked example: A2 component change

Run on 19 October 2026. The inventory is an illustrative file written for this example (`sample-data/component_inventory.csv`); the company, products and teams are invented. The research rows are real. The safety-event call is a real library call (`live/safety_events.json`, first entry).

**Request:** "We're releasing Dose input 3.1.0. The plus and minus steppers grow to 24 by 24 CSS pixels, and the out-of-range error now shows as text under the field instead of a red border only. Inventory attached. Our regulatory lead Dana says the patient apps and the dosing calculator are device software. Who rechecks what? Our patient app runs alongside a Medtronic infusion programmer; is anything in the field about their screens?"

**Calls and runs**

1. `python3 scripts/ds_adoption.py sample-data/component_inventory.csv` (Dose input rows below).
2. `regulatory-dh.search_safety_events` `{manufacturer: "Medtronic", since: "2025-01-01", jurisdiction: "US", limit: 5}`: five Class II recalls of Medtronic Neuromodulation clinician programmer and patient apps.

Version map for Dose input, from the script: Patient app iOS and Patient app Android on 3.0.0 (owner: Patient app team; clinical yes; device UI yes; no modification; lifecycle "trial"; accessibility status "not tested since 3.0.0"); Dosing calculator on 2.0.0 (owner: Dosing team; clinical yes; device UI yes; modification "fork"; status "tested WCAG 2.1 AA March 2025").

## Answer (short mode)

**Recheck both patient apps; the dosing calculator will not receive this change.** Patient app iOS and Android use Dose input 3.0.0 and are device software per Dana. The dosing calculator runs a fork of 2.0.0, and a fork receives no updates from the system component (DSX-33), so the larger steppers and the text error will not reach it unless the Dosing team ports them.

**Criteria the change touches**

| Change | Criterion | Row |
|---|---|---|
| Steppers to 24 by 24 CSS pixels | 2.5.8 Target Size (Minimum), AA | UX-STD-11 |
| Error shown in text, not color only | 3.3.1 Error Identification, A; 1.4.1 Use of Color, A | UX-STD-19, DSX-02 |
| New error text | 4.1.3 Status Messages, AA, if announced without focus | DSX-07 |

**Recheck list:** Patient app iOS and Android (Patient app team): the steppers and the error state, with automated, manual and in-context tests (UX-UK-24, DSX-37, DSX-38); "not tested since 3.0.0" is your recorded status, so no earlier result covers these states. Clinical tasks depending on the error state: not named `[GAP]`. Which dosing tasks use the out-of-range state?

**Questions for Dana and your quality owner (device surfaces):** Was the change assessed for risk and impact before implementation (QS34)? It is a software modification, so a design change (CH9). It changes the user interface, which moves a modified device past HF Submission Category 1 (Decision Point B, UX-US-49); whether a critical task is new or impacted decides Category 2 or 3 (UX-US-50 to UX-US-52). These answers are theirs.

**Field events (Medtronic, as the records state):** five Class II recalls of programmer and patient apps from 9 January 2025 to 8 April 2026; for the A810 app, "in rare cases, the steps may be displayed out of order" (8 April 2026); for the A71100 app, "a Device Reset message displayed on the app was unable to be cleared" (20 November 2025). Source: openFDA enforcement reports; the library links the API, not the record. No cause is inferred, and they concern Medtronic's apps, not your component.

**Record:** Change note draft. Significance, HF category and release are your owners' decisions. Uncleared. AI-assisted.

The full version adds the per-product recheck table and the token check.

## What this example shows

- The fork is caught by the version map: the change would otherwise be assumed to reach a device product.
- Criteria come from rows tied to what changed, not a generic checklist.
- Device questions are put to the owners the person named, with rows, and none is answered.
- The field events are quoted, dated and kept separate from the person's component.
- Word count of the answer above, excluding the calls list and the table's row column: about 330.
