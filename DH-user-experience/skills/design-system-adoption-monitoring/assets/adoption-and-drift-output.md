# Output format: adoption and drift

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** clinical and device uses behind current, with owners; then the largest drift (forks, most versions in use, flagged lifecycle).
2. **Basis:** as-of date; inventory rows and products counted; where "current" comes from (declared by you, or highest in the inventory).
3. **Behind current by owner (compact):** Owner · Uses · Behind · of which clinical · of which device UI.
4. **Drift worth your attention:** forks, overrides, flagged lifecycle, component versions with your status "not tested" or open issues, quoted in your words.
5. **Against your rules:** met or missed per rule, or "no rule set".
6. **What it means (two lines at most, with rows).**
7. **Record:** "Counts on your inventory as supplied. No threshold applied unless yours. Clears: the person you name. Record built with verify.build_record once they clear it; until then, uncleared draft. AI-assisted."
8. One line offering the full version.

## Full mode

### Answer

### Basis
| Item | Value |
|---|---|
| As-of date | |
| Inventory rows, components, uses | |
| Products (your list, or named in the inventory) | |
| Current version source | declared / highest in inventory (labeled) |

### Adoption by component
| Component | Current | Products using it | On current | Versions in use |
|---|---|---|---|---|

### Uses not on current
| Component | Product | In use | Current | Drift | Owner | Clinical | Device UI |
|---|---|---|---|---|---|---|---|

### Behind current by owner
| Owner | Uses | Behind | Clinical | Device UI |
|---|---|---|---|---|

### Accessibility status as you recorded it
| Component | Version | Status (your words) | Products | Clinical | Device UI |
|---|---|---|---|---|---|

### Local modification and lifecycle
| Component | Override | Fork | Flagged lifecycle uses |
|---|---|---|---|

### Against your rules
| Rule (your words) | Number | Met / missed / no rule |
|---|---|---|

### Gaps
Columns missing, products not listed, current versions not declared.

### Calls and runs

### Record
Counts on your inventory. No conformance statement. AI-assisted. Clears: NAME (the person you name). The record is built with `verify.build_record` once NAME clears it; until then it reads "uncleared draft".
