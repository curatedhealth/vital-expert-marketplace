# Output format: component change note

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** the products to recheck (clinical and device first), the criteria the change touches, and whether a device change-control question is open.
2. **Change:** component, old and new version, what changed (your words), breaking or not (your call).
3. **Recheck list (compact):** Product · Version now · Owner · Clinical / device · What to recheck · Test type.
4. **Clinical tasks depending on a changed state:** as you named them, or `[GAP]`.
5. **Device questions for your owners:** only for device surfaces, each with its row; none answered here.
6. **Field events (if called):** as the records state, with the calls listed.
7. **Record:** "Change note draft. Significance, HF category, submissions and release are your owners' decisions. Clears: the person you name. Record built with verify.build_record once they clear it; until then, uncleared draft. AI-assisted."
8. One line offering the full version.

## Full mode

### Answer

### The change
| Item | Value |
|---|---|
| Component | |
| Old version, new version | |
| What changed (your words) | |
| States added, removed, altered | |
| Tokens changed | |
| Breaking (your call, your version rule) | |

### Version map for this component
| Product | Version in use | Owner | Clinical | Device UI | Modification (fork gets no update) |
|---|---|---|---|---|---|

### Criteria touched
| Change element | Criterion (number, name) | Row | Recheck |
|---|---|---|---|

### Recheck list
| Product | What to recheck | Test type (automated, manual, with people) | Clinical tasks depending on changed state | Owner |
|---|---|---|---|---|

### Device change-control questions (device surfaces only)
| Question for your owner | Row | Answer (your owner's) |
|---|---|---|

### Field events (optional)
| Title (as recorded) | Event date | Class | Summary (quoted) | Source |
|---|---|---|---|---|

### Gaps

### Calls made

### Record
Change note draft. No statement that the change is minor, safe, non-significant or compliant. AI-assisted. Clears: NAME (the person you name). The record is built with `verify.build_record` once NAME clears it; until then it reads "uncleared draft".
