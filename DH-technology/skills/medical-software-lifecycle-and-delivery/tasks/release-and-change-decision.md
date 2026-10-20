# B1 Release and change decision

Framework task: DH-04.03.4.1, Part B, task B1. Carries the old task "DH-04.03.4.1.3 Problem resolution record" as step 3, and prepares the decision that the old monitoring task "DH-04.03.4.2.3 Release gate for the class" later reads.

## What this task delivers

For one release candidate or one planned change: what the change re-opens (validation, regression scope, risk file, documentation), the regulatory questions it raises laid out beside the person's facts, the problem resolution records with their status, and a release decision pack with every open item listed. The person decides go or no-go, who accepts each open problem, and, with the regulatory owner, whether a new submission is needed. It answers "what does this release or change put back on the table, and what must we decide before it ships?"

Why it matters: FDA treats any software modification as a design change (CH9), validation status must be re-established after any change (EN-008), and deviating from an authorized PCCP generally makes the device adulterated and misbranded (AI US-13). A release record that closes a problem on a hazardous function without a change or an accepted rationale, or that says "no new 510(k) needed" without the owner, says more than the team decided.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `clinical-algorithm-validator` (old DH-04.03.4.1.3). Work as a release engineer who assembles facts for the person's decision |
| Skill | DH-04.03.4.1 Part B, Release and change decision |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/delivery-and-change-rules.md` sections 3 to 5; `references/governance.md` |
| Tools | `regulatory-dh.search_devices` and `regulatory-dh.get_authorization` (step 1); `scripts/lifecycle_check.py problems`; `verify.build_record` on sign-off |
| Prompt | This guide |
| Template | `assets/release-and-change-decision-output.md` |
| Input | The request and its context: the change description in the person's words, the release candidate build id, the most recently cleared or certified version and its number, the risk file entries the change touches, the problem log (CSV columns in `scripts/lifecycle_check.py`), the cases rerun and their builds, whether a PCCP is authorized, the owners and the decision date the person sets |
| Governance | `references/governance.md`; go or no-go and the submission answer are the person's |
| Catalogue job | none known (needs a live check) |

## Read the request

- **Change and candidate.** Needed: the change in the person's words and the candidate build id. If either is missing, ask once; write "not given" until then.
- **Baseline.** The most recently cleared or certified version and its number. If not given, ask; never infer it from a library search on the product name.
- **The question asked.** "Can we ship?" and "does it need a new 510(k)?" are both answered with the facts and the open decisions, never with yes or no.
- **Short or full.** A direct question is short mode. "Prepare our release decision pack" is full mode.

## The rule that shapes this task: people decide

The model lays out the questions the sources ask, the facts the person gave against each, and what each answer depends on. It never says the change does or does not need a new submission, never closes a problem, never accepts a residual risk and never calls a release go. Where the person's facts allow two readings, it shows both and writes "your call".

## Workflow

### Step 1. Fix the baseline

Ask for the most recently cleared or certified version (CH13 compares to it). If the person gives a clearance number, read it: `regulatory-dh.get_authorization {reference: "K..."}` (or `search_devices {query: "<manufacturer>", jurisdiction: "US"}` first, since full product names can miss; `references/tools.md`). Quote product, pathway, decision date and product code as the record states them. The record does not hold the cleared software version or specification; ask the person for it. A PCCP's existence is not stored; ask.

### Step 2. What the change re-opens

One table, one line per item the person's change description touches: validation re-established with impact analysis (EN-008); regression scope over unchanged but vulnerable parts (EN-009), scope set by the person; risk file entries to review (QS22); document register elements touched (PL15, PL20: version history and unresolved anomalies always move); other functions affected (PL29); pipeline tool changes that need their own assurance (EN-011, EN-016).

### Step 3. Problem resolution records (old 4.1.3)

Run `python3 scripts/lifecycle_check.py problems --log FILE`. Each record: id, item, version found, effect on the hazardous function, change that fixed it or "open" (P1 to P5 flags). Old rule: a problem on a function the person's risk file ties to harm is not closed without a change or an accepted rationale, and a rationale names who accepted it (P4). The unresolved anomalies list in a US submission carries each anomaly's impact on safety and effectiveness (PL20).

### Step 4. The regulatory questions, laid out

US 510(k) devices: the questions of FDA's software change guidance in order (CH11 to CH16), each with the person's fact against it or "not given". Cybersecurity-only change: CH12; a change to authentication, encryption, connectivity or the update mechanism may bring 524B documentation (EN-060). AI model change: inside or outside the authorized PCCP (AI US-12, AI US-13), routed to `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control. EU legacy devices under Article 120: MDCG 2020-3 chart C and its examples, valid only if benefit-risk is not negatively affected (CH5 to CH8); for MDR-certified devices the notified body's change rules were not read (`[GAP]`). Every answer column reads "for the regulatory owner"; route to `dh-regulatory-and-quality` document-and-change-control.

### Step 5. Release decision pack

List, for the person: open problems on hazardous functions (P5), cases run on a build other than the candidate (from the person's test records, or `software-quality-and-delivery-monitoring`, this pack, task A1), document elements missing or in draft, change questions open, pipeline evidence missing (A2). Then the decision lines: go or no-go, who accepts each open item, notification or submission decision, decision date. Each is the person's: "not given" until they set it. Old monitoring rule carried forward as a fact, not a gate: "Do not ship class C on an informal chat approval" means the record names the acceptor and the build id.

## Build the output

Follow `assets/release-and-change-decision-output.md`. Answer first: what the change re-opens, how many problems are open on hazardous functions, which regulatory questions are open and for whom, and the decisions the person must make. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/lifecycle_check.py words ANSWER.md`; without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- No "new submission needed" or "not needed"; every regulatory answer is "for the regulatory owner".
- No release called go; no problem closed; no residual risk accepted by the model.
- The baseline record is quoted as the library states it, with its retrieval date.
- The pack is labeled "release decision draft for the owner".
- `python3 scripts/lifecycle_check.py words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Change records and the change procedure: `dh-regulatory-and-quality` document-and-change-control.
- AI changes and PCCPs: `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control.
- Corrections, removals and CAPA after release: `dh-regulatory-and-quality` audit-capa-and-complaints.
- Reading release gates and miss owners across releases: `software-quality-and-delivery-monitoring` (this pack).
