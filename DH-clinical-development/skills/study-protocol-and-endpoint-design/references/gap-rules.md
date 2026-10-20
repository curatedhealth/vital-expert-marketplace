# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A research row states it | The fact plus the row id ("visit modality fixed in the protocol, CV67") | None |
| Published method | The row is [PAPER] | "SPIRIT 2025 item 16 (SP-16), DOI 10.1136/bmj-2024-081477" | Cite the DOI |
| Nonbinding guidance | FDA guidance, EU recommendation paper | "FDA recommends (nonbinding guidance, CV42)" | Do not present as law |
| Draft | PFDD Guidance 4, diversity action plan guidance | "Draft, for comment only (PE-17)" | Do not plan on it as in force |
| Not yet effective | ICH E6(R3) Annex 2 in the EU before 15 January 2027 | "Adopted, effective in the EU on 15 January 2027 (CV2)" | Plan for it; say when it applies |
| Superseded parent | SPIRIT-AI and CONSORT-AI item numbers | "SPIRIT-AI numbering refers to SPIRIT 2013 (CV122)" | Map by content, not number |
| Not in the sources | Sample size method, margins, multiplicity, ISO 14155, MDR investigation rules, instrument cut-offs | "Not in this skill's sources `[GAP]`; the owner the person names for statistics or regulatory status supplies it, or owner not named" | Ask the named owner |

## Library and registry facts

| Situation | How to word it |
|---|---|
| `trial_ids` empty on a record | "Registry id not on the library record `[GAP]`; checked with find_trial" |
| `find_trial` returns no registration | "No ClinicalTrials.gov link found by the library; other registries not searched `[GAP]`. Absence is not evidence the trial is unregistered." |
| Registry record read directly | "Registry wording, as registered (ClinicalTrials.gov, read 19 October 2026)" |
| Registry and paper word the primary outcome differently | Quote both; "differs in wording; whether it changed is for the monitoring check (SP-16, CV114)" |
| Verify returns "supported" | Only reported as support when the passage was read and says the same thing (N3) |
| Design label from the library | "Library label `rct` (from metadata); design confirmed from the paper: yes/no" |
| Field missing from an abstract | If the source is open access, read the full text before marking the field `[GAP]`; mark `[GAP]` from an abstract only when the full text is not open, and say "abstract only" |

## The person's facts

| Situation | How to word it |
|---|---|
| Intended use, claim or indication not stated | "Intended use not stated `[GAP]`"; endpoints cannot be tied to a claim until it is |
| Device status unknown | "Device status not stated `[GAP]`; the owner the person names for regulatory status, or owner not named"; V&V still applies either way (CV46) |
| No comparator chosen | "Comparator not chosen `[GAP]`"; SP-9b stays open |
| No owner named for statistics | "Owner not named"; ask. Never suggest a job title |
| Assumption without a source | Record it as the person's assumption, labeled; never fill it |

## Never

- Never fill an effect size, standard deviation, dropout rate, margin, threshold or sample size from memory.
- Never treat a missing registry link as "not registered", or a library design label as the design.
- Never call a protocol complete, compliant or acceptable to a regulator.
