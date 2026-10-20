# Usability test results: what the sources say about reading them

Used by A1. `UX-` rows are in `ux-usability-research.md`; `CS` rows in `implementation-research.md`. FDA guidance quoted is the 3 August 2026 reissue (UX-US-25); it is recommended, not required (UX-US-26).

## 1. Which kind of test produced the log

| Kind | What it is for | Rows |
|---|---|---|
| Formative | Explores design strengths, weaknesses and unanticipated use errors. Sizes vary with need, complexity and user variability. Employees may take part, with caution. Think-aloud is acceptable. | UX-US-29, UX-M-04, UX-US-45, UX-US-40 |
| Validation (summative) | End of development: identifies use errors that could cause serious harm and tests risk controls. FDA notes "summative" is sometimes defined more narrowly. | UX-US-30 |

A1 asks which kind the person ran. The same log reads differently: a formative log feeds design; a validation log is read against the validation conditions below.

## 2. Validation conditions to check the log against

| Condition | Rule | Row |
|---|---|---|
| Representative users | Participants represent the intended users. | UX-US-34 |
| All critical tasks | Every critical task is performed in the test. | UX-US-34 |
| Final UI | The user interface is the final design. | UX-US-34 |
| Realistic conditions | Test conditions represent actual use. | UX-US-34 |
| Sample | At least 15 participants per distinct user population; professionals and lay users, and pediatric and adult users, are distinct. | UX-US-35, UX-US-36 |
| Functional limits | A representative range of condition-related limits is included where the condition causes them. | UX-US-37 |
| Employees | Not validation participants except where all users are employees. | UX-US-38 |
| US residence | For US use, participants should reside in the US; exceptions need a rationale. | UX-US-39 |
| Think-aloud | Not acceptable in validation. | UX-US-40 |
| Training | Not immediately before testing; training in the test matches real training. | UX-US-41, CS80 |
| Rationale for numbers | MHRA sets no fixed number; the rationale is documented. | UX-UK-17 |

FDA restates Faulkner (2003): 15 users found at least 90 percent and on average 97 percent of known problems; 30 users found on average under 2 percent more than 15 (UX-M-01, UX-M-02). FDA also says a statistically "correct" sample size is extremely difficult to set (UX-M-03). Faulkner's paper itself was not read.

## 3. How results are read

| Rule | Row |
|---|---|
| Validation testing is primarily qualitative; FDA sets no numerical acceptance criteria for error rates. Counts describe; they do not pass or fail a device. | UX-US-43 |
| Use error has FDA's three-part definition; a result caused solely by device failure is not a use error. Users may not know a use error happened (MHRA), so observation, not self-report, finds them. | UX-US-27, UX-UK-15 |
| If no formative work was done and flaws appear in validation, that test effectively becomes formative. | UX-M-06 |
| A statement of compliance with IEC 62366 is not enough without supporting evidence (MHRA). | UX-UK-16 |

## 4. SUS, if the person collected it

| Rule | Row |
|---|---|
| Scoring as restated by Hyzy et al. 2022 (DOI 10.2196/37290): odd items minus 1, 5 minus even items, sum times 2.5, range 0 to 100. Brooke's original was not read. | UX-M-07 [PAPER] |
| General benchmark cited by the paper: mean 68 (SD 12.5), attributed to Sauro and Lewis (not read). | UX-M-08 [PAPER] |
| Digital health apps: 117 SUS scores for 114 apps (2011 to 2021), mean 76.64 (SD 15.12); physical-activity apps averaged 83.28; excluding them, 68.05 (SD 14.05). | UX-M-09 [PAPER] |
| The authors conclude 68 (SD 12.5) is suitable for digital health apps; one meta-analysis with its own limits. | UX-M-10 [PAPER] |

Benchmarks are context, never targets. Adjective bands for SUS are not sourced `[GAP]`. SUS does not measure use error or safety.

## 5. Participants and ethics

| Rule | Row |
|---|---|
| Consent where practicable, and participant risks and benefits considered even in early formative testing (MHRA). | UX-UK-19 |
| The Common Rule applies to research conducted, supported or regulated by a federal department that adopted it; privately funded usability work is not covered by that text unless an institution or agency makes it so. Whether product testing is "research" depends on the facts. | UX-M-11, UX-M-12 |
| Exemptions for surveys, interviews and observation (d)(2), benign behavioral interventions (d)(3), with limits for children and deception. The person's institution decides. | UX-M-14 to UX-M-18 |

## 6. Not in the sources

- A pass rate, an error-rate threshold, a task-success target or a SUS target. These are the person's acceptance rules.
- A severity scale. The person's risk file sets it.
- Brooke, Bangor and Sauro and Lewis originals; SUS adjective bands.
