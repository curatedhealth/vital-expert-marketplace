# Output format: clinical task and workflow fit

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** task, role, setting and moment in one line; the data shown first; the step the screen replaces and the step it adds.
2. **Frame:** users and population split, market, certified health IT or not.
3. **Data (compact):** Item · Shown / on request / withheld · Reason (the person's words).
4. **Before and after:** Old step · Screen · Added step (including training) · Rows. If the person asked for the whole service, give the blueprint instead: one line per step across patient, clinician and back-stage, with handoffs and `[GAP]` receivers marked; label it "method, not a sourced rule".
5. **Site checks:** the SAFER Guide touched, silent mode if the product adapts locally, NHS DCB0160 [WF] if in England.
6. **Open questions (at most three):** the old step first if unknown.
7. **Record:** "Task fit draft. No time or outcome claim. Uncleared until a named person clears it through verify.build_record. AI-assisted." or the clearer's name.
8. One line offering the full version.

## Full mode

### Answer

### Frame
| Item | Value |
|---|---|
| Task | |
| Role (person's words) | |
| Setting and moment | |
| Users and populations | |
| Market | |
| Certified health IT | |

### Data shown and withheld
| Data item | Shown / on request / withheld | Reason | Core or site-variable | Rows |
|---|---|---|---|---|

### Before and after
| Old step | Replaced by | Step added | Interface elements outside the screen (labeling, training, alarms) | Rows |
|---|---|---|---|---|

### Decision support placement and feedback
Where the intervention appears in the task; where feedback is given; time-critical note if any.

### Environment
| Factor | Fact for this setting | Row |
|---|---|---|

### Service blueprint (only if asked; method, not a sourced rule)
| Step | Patient | Clinician (role) | Back-stage | Handoff (from, to) | Data and system | Support | Rows |
|---|---|---|---|---|---|---|---|

### What the deploying site will check
| Check | Applies because | Row |
|---|---|---|

### Gaps

### Record
Task fit draft. No claim of time saved or errors reduced. AI-assisted. Cleared by NAME through verify.build_record, or "uncleared draft" until a named person clears it.
