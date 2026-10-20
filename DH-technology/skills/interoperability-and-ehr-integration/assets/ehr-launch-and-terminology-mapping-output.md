# Output format: EHR launch and terminology mapping

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/fhir_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 70, scopes 100, launch 70, map 100, step 50, record 50.

1. **Answer** (two or three sentences): launch type and the scope findings; context fields present or missing in the sandbox token; map flags; the step that changes. No "integrated" or "ready" verdict.
2. **Scopes:** Scope · Finding · Rows (from `fhir_check.py scopes`; only scopes with a finding in short mode).
3. **Sandbox launch:** EHR · sandbox · context field · present or MISSING · scope requested.
4. **Map flags:** Line · Flag (K1 to K5) · Fact.
5. **Step:** before (actor, system, data retyped) and after (what goes away, or the step added).
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Launch and mapping draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Registration note for EHR (launch type, client id, redirect URI, launch endpoint, as given)
### Scopes
| Scope | Level | Resource | Permissions | Finding | Rows |
|---|---|---|---|---|---|
### Screen to FHIR map
| Screen | Resource | Interaction | Write-back | Note |
|---|---|---|---|---|
### Sandbox launch log
| Sandbox | Test user | Test patient | Context fields present | Context fields missing | Scopes granted |
|---|---|---|---|---|---|
### Code systems by element
| Element | Source system | Target system or uncoded | Licensing line | Rows |
|---|---|---|---|---|
### Map flags (labels are yours)
### Clinical step: before and after
### Gaps
### For you to decide
### Calls made
### One line offering anything not shown
### Record (the very last line)
Launch and mapping draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
