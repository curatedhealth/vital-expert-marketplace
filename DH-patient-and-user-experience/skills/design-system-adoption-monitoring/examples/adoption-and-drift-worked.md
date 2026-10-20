# Worked example: A1 adoption and drift

Run on 19 October 2026. The inventory is an illustrative file written for this example (`sample-data/component_inventory.csv`); the company, products and teams are invented. The script output is saved as `sample-data/component_inventory_run.md`. No library call is needed for A1.

**Request:** "Attached is our component inventory as of today. Our product list: Patient app iOS, Patient app Android, Clinician portal, Marketing site, Dosing calculator, Help center. Our rule: no clinical surface behind the current version. Where do we stand?"

**Runs**

1. `python3 scripts/ds_adoption.py sample-data/component_inventory.csv --products "Patient app iOS;Patient app Android;Clinician portal;Marketing site;Dosing calculator;Help center"`

## Answer (short mode)

**Your rule is missed: 3 clinical uses are behind current, all on device surfaces.** Patient app iOS and Android run Date picker 4.1.0 (current 4.2.0, Patient app team), and the Dosing calculator runs a fork of Dose input 2.0.0 (current 3.0.0, Dosing team). The fork receives no updates from the system component (DSX-33), so it will not get later fixes unless the Dosing team ports them.

| Owner | Uses | Behind current | Clinical | Device UI |
|---|---|---|---|---|
| Patient app team | 4 | 2 | 2 | 2 |
| Dosing team | 1 | 1 | 1 | 1 |
| Growth team | 3 | 2 | 0 | 0 |
| Clinician portal team | 4 | 0 | 0 | 0 |
| Platform team | 6 | 0 | 0 | 0 |

**Drift worth your attention (your words quoted):**

- Date picker 4.1.0 on both patient apps carries your status "2 issues open (target size 2.5.8)"; 4.2.0 carries "tested WCAG 2.2 AA September 2026".
- Input mask 2.3.0 is marked by you "use with caution" and is in use on the Clinician portal and the Dosing calculator, both clinical, with "1 issue open (error identification 3.3.1)" and overrides on both.
- Dose input 3.0.0 on the patient apps is "not tested since 3.0.0" and in trial status.
- Help center uses no listed component.

**Against your rule:** "no clinical surface behind the current version": missed, 3 uses. No rule set for forks, lifecycle or test status, so no verdict on those.

**What it means:** the counts show which version each product runs, not whether the product is accessible: finding the system's code in a product does not show the implementation is usable or accessible (DSX-41). A contract check on the patient apps' date picker (A2) would show whether the open target-size issues are on the surface. Under USWDS's scheme a "use with caution" component fails accessibility, usability or development requirements (DSX-28); your status may mean something else.

**Record:** Counts on your inventory as supplied, as of 19 October 2026. Uncleared. AI-assisted.

The full version adds adoption per component, the version spread and the modification table.

## What this example shows

- Clinical and device uses lead the answer and are not folded into totals.
- The fork is named for what it means (no updates), with its row.
- Status words stay the person's; nothing is translated into "conformant".
- Only the person's rule gets a verdict.
- Word count of the answer above, excluding the table: about 290.
