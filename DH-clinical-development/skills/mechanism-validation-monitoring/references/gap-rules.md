# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A research row states it | The fact plus the row id ("fidelity is delivery as intended, TM92") | None |
| Published method | [PAPER] row | "ORBIT milestones set a priori (TM57), DOI 10.1037/hea0000161" | Cite the DOI |
| Abstract only or [WF] | BCT Taxonomy v1, Bellg 2004, GRADE EtD Part 1 | "BCT Taxonomy v1, abstract only (TM51): technique list not read, label not checked" | Accept the person's label as theirs |
| Regulation about a named classification | TM119 to TM130 | "882.5801 requires ... (TM120); whether it applies to your product is a regulatory question `[GAP]`" | `dh-regulatory-and-quality` regulatory-pathway-and-classification |
| Not in the sources | Thresholds, effect sizes, mediation methods, minimal important differences, Bellg fidelity strategies, newer De Novo summaries | "Not in this skill's sources `[GAP]`" | Ask the person; methods go to `dh-clinical-development` study-protocol-and-endpoint-design |

## Library facts

| Situation | How to word it |
|---|---|
| `get_authorization` has no intended use | "Intended use not on the library record; taken from the decision summary (TM132)" or `[GAP]` |
| `search_devices` returns nothing | "Not found in the library store; absence is not evidence the device does not exist `[GAP]`" |
| `find_trial` finds no registration | "No ClinicalTrials.gov link found by the library; absence is not evidence the trial is unregistered" |
| Verify returns "supported" or "partial" | Reported as support only when the passage was read and says the same thing (N3) |
| Verify rates a regulator PDF inadmissible | "Not checkable through Verify (C1); quoted from row TMnn, read 20 October 2026" |

## The person's facts

| Situation | How to word it |
|---|---|
| Link with no measure | "Not measurable: no measure in the plan `[GAP]`"; not scored (old task rule) |
| Measure chosen after the data were read | "Not scored: measure not named in advance (TM57)"; may be reported as an exploratory observation, labeled |
| Threshold not set | Report the value; no met or missed verdict |
| Data missing for a link | Report the missing count; no imputation by the model |
| Version or data cut not given | "Version not given" or "data cut not given", and ask; never fill either with today's date or a date read off a file; comparisons across versions wait for it |
| A measure said to have "dropped", "risen" or "improved" with one time point in the file | "Change cannot be computed from this file: one time point"; the value is reported as a level, not a change |
| No owner named | "Owner not named"; ask. Never suggest a job title |
| Engagement definition or threshold not set, or set after the data were read | Report values without a verdict; "not compared: definitions not set before the data were read" |
| "Is our retention good?" | "No source in this skill sets an engagement benchmark or retention target; the threshold is yours" (`engagement-read-rules.md`) |
| "Is this event reportable?" | "The call of the owner you name for vigilance reporting, or owner not named"; lay out the rule text with rows (`signal-read-rules.md` section 3); route to `dh-regulatory-and-quality` audit-capa-and-complaints |
| Event category or seriousness not assigned | "Category not given" or "not assessed"; the model never assigns one |

## Never

- Never call a link proven, validated or evidence-based on a precedent or a Verify status alone.
- Never fill a threshold, a proxy or a missing value from memory.
- Never read engagement as the outcome (CS32).
- Never read silence as "not applicable".
