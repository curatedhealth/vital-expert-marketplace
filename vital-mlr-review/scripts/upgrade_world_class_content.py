#!/usr/bin/env python3
"""Rewrite READY skill goods + offline docs until world_class_meter PASSes.

Hybrid B: offline CLIs first; MCP optional. Never approve. Pilot only.
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
TOOLS = ROOT / "tools"
STAMP = "tools/stamp_ready_line.py"
LIABILITY = (
    "This prepares material for human MLR review. "
    "It is not medical, legal, or regulatory approval."
)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Unique good drafts (synthetic teaching artefacts; never live inputs)
# ---------------------------------------------------------------------------

GOODS: dict[str, str] = {
    "mlr-intake": f"""# Good sourced draft — mlr-intake

## Synthetic context (teaching only — MLR-H2)
- Person named markets: Germany (DE), Switzerland (CH). United States was never offered.
- Audience: HCP. Channel: promotional (person-declared after channel gate elsewhere).
- Artefact: leave-behind PDF v0.9-draft, sha256 teaching-hash-intk-01.
- Authorized-use (DE, pasted Fachinformation excerpt): "Zur Behandlung von Erwachsenen mit Typ-2-Diabetes mellitus…"
- Authorized-use (CH, pasted Swissmedic label excerpt): "Indiziert zur Behandlung von Erwachsenen mit Typ-2-Diabetes…"
- Missing: full current Fachinformation PDF → tagged [GAP] on DE label basis, not invented.

## Output cards

### Intake card
| Field | Value |
|---|---|
| Markets | DE, CH (explicit; no US default) |
| Audience / channel | HCP / promotional |
| Artefact | leave-behind v0.9-draft |
| Label basis DE | Fachinformation excerpt provided; full SmPC PDF [GAP] |
| Label basis CH | Swissmedic excerpt provided |
| Ruleset coverage (offline list) | DE=full (rulesets/de_amg.json), CH=stub |
| Status | findings_only |
| Tool mode | READY-local · not tool-checked |

### What this card refuses
- Inventing a US market because "most packs start there."
- Treating ruleset stub for CH as full coverage.
- Filling the missing DE Fachinformation from memory or web scrape without the person pasting text.
- Any status other than findings_only / revise / human_gate_required / prep_complete.

### Deterministic checks run
1. `scripts/check_jurisdictions.py` → markets present, non-empty, no silent US inject.
2. `tools/mlr_intake_offline.py` → packet skeleton with gaps array.
3. `tools/mlr_list_rulesets_offline.py` → coverage map DE=full CH=stub.
4. `{STAMP} --skill mlr-intake --status findings_only`

### Why this is good
Markets stay person-supplied. Gaps are named, not filled. Chairs are not blended. Offline path is complete without a `vmlr_` key.

### Liability
{LIABILITY}

### Stamp
READY-local / mlr-intake: not tool-checked · findings_only · not metered · 2026-11-08

### Cross-links
Next: mlr-channel-intent (if channel ambiguous) → chairs → mlr-compile → mlr-board-prep.
""",
    "mlr-capability-map": f"""# Good sourced draft — mlr-capability-map

## Synthetic context (teaching only — MLR-H2)
Operator asks: "What can this pack do for a DE+CH HCP leave-behind before the board?"
No artefact body yet — map skills and refuse approval language.

## Output cards

### Capability map card
| Skill | Job | Not for |
|---|---|---|
| mlr-intake | Markets, channel, label excerpts, ruleset coverage | Approving copy |
| mlr-channel-intent | Promo vs scientific-exchange gate | Medical accuracy |
| mlr-claims-matrix | Claim ↔ evidence locator grid | Legal misleadingness alone |
| mlr-fair-balance-isi | ISI / fair-balance presence & placement notes | Writing new ISI text as approved |
| mlr-medical-chair | Label / clinical accuracy findings | Legal privacy / comparative ads |
| mlr-legal-chair | Misleadingness, comparative, privacy | Clinical dose accuracy |
| mlr-regulatory-chair | Format, ISI process, pre-approval ceremony | Medical efficacy judgment |
| mlr-compile | Align + validate packet shape | Board ownership |
| mlr-verify-handoff | Passage / source proof via VERIFY when keyed | Standing in for chairs |
| mlr-board-prep | Named-human prep record | AI as cleared_by |

### Routing note
Eleven skills, one funnel. Ask which market and channel first; never default United States. Host reasoner selects skill; this map only orients.

### Offline checks
- `tools/mlr_list_rulesets_offline.py` — show which markets have full vs stub rulesets before promising depth.
- `{STAMP} --skill mlr-capability-map --status findings_only`

### Why this is good
Names every skill's job and its hard boundary. No "we can clear this for you." No marketplace publish claim (Pilot).

### Liability
{LIABILITY}

### Stamp
READY-local / mlr-capability-map: not tool-checked · findings_only · not metered · 2026-11-08

### Cross-links
Operator picks mlr-intake when markets are known; otherwise stay on the map until jurisdictions are explicit.
""",
    "mlr-channel-intent": f"""# Good sourced draft — mlr-channel-intent

## Synthetic context (teaching only — MLR-H2)
- Markets: DE, US (person listed both; US not defaulted).
- Draft claim: "Product X reduces HbA1c in adults with type 2 diabetes."
- Person initially said "scientific exchange" but supplied no unsolicited-request record and the piece is a branded leave-behind with ISI footer.

## Output cards

### Channel intent card
| Gate | Result |
|---|---|
| Declared channel | scientific exchange (person) |
| Artefact signals | branded leave-behind + ISI footer + efficacy claim |
| Unsolicited request on file | No → [GAP] |
| Recommended posture | Treat as **promotional** until person supplies exchange record OR revises channel |
| Status | human_gate_required |

### Decision narrative (findings, not approval)
Scientific-exchange framing cannot ride on a branded efficacy leave-behind without an unsolicited medical-information request trail. The gate does not rewrite the piece; it forces a human choice: (a) reclassify as promo and continue chairs, or (b) supply the MI request record and strip branding/claims that break exchange rules.

### Offline checks
- Channel enum from intake skeleton (`promo` | `scientific_exchange` | `mixed` | `unknown`).
- `{STAMP} --skill mlr-channel-intent --status human_gate_required`

### Why this is good
Surfaces channel conflict instead of silently accepting the person's label. Does not invent FDA/EMA channel law text. Hands Medical/Legal/Regulatory their own cards.

### Liability
{LIABILITY}

### Stamp
READY-local / mlr-channel-intent: not tool-checked · human_gate_required · not metered · 2026-11-08

### Cross-links
After human resolves channel → mlr-claims-matrix + chairs. If still unknown → stay gated.
""",
    "mlr-claims-matrix": f"""# Good sourced draft — mlr-claims-matrix

## Synthetic context (teaching only — MLR-H2)
- Markets: DE, CH.
- Claims extracted from leave-behind (person-highlighted):
  1. "Lowers HbA1c by 1.2% at week 24"
  2. "Better GI tolerability than Product Y"
  3. "Once-daily oral dosing"

## Output cards

### Claims matrix card
| # | Claim text | Evidence locator | Market notes | Status |
|---|---|---|---|---|
| C1 | Lowers HbA1c by 1.2% at week 24 | Study NCT-TEACH-001 CSR §3.2 page 41 [person paste pending] | DE/CH: need label-consistent endpoint language | revise — locator [GAP] |
| C2 | Better GI tolerability than Product Y | Head-to-head not in supplied label excerpts | Comparative → Legal chair + Medical | human_gate_required |
| C3 | Once-daily oral dosing | Matches DE Fachinformation posology excerpt line 12 | OK structurally vs pasted label | findings_only |

### Align note
Structural alignment only against pasted authorized-use text and person-supplied locators. No efficacy clearance. Comparative claim C2 cannot be "supported" by inventing a trial.

### Offline checks
1. `tools/mlr_claims_matrix_offline.py` on claims JSON → rows with gap flags.
2. `tools/mlr_align_claims_offline.py` against authorized-use excerpts.
3. `{STAMP} --skill mlr-claims-matrix --status revise`

### Why this is good
Every claim has a locator or an explicit [GAP]. Comparative ads route to Legal. Numbers are not invented to fill CSR gaps.

### Liability
{LIABILITY}

### Stamp
READY-local / mlr-claims-matrix: not tool-checked · revise · not metered · 2026-11-08

### Cross-links
Medical chair owns C1 clinical fit; Legal owns C2; Regulatory owns ISI adjacency for claim blocks.
""",
    "mlr-fair-balance-isi": f"""# Good sourced draft — mlr-fair-balance-isi

## Synthetic context (teaching only — MLR-H2)
- Markets: US, DE (person listed both).
- Artefact: 2-page HCP leave-behind. Page 1 efficacy bullets; page 2 dense ISI block in 7pt.
- Person asks: "Is fair balance OK?"

## Output cards

### Fair-balance / ISI card
| Check | Observation | Status |
|---|---|---|
| ISI present | Yes — page 2 block titled Important Safety Information | findings_only |
| Prominence vs claims | Efficacy on p1 in 12pt bold; ISI 7pt on p2 only | revise — prominence imbalance flagged for human Regulatory |
| Contraindications reflected | US boxed-warning theme mentioned; DE contraindications not mirrored in DE-facing panel | [GAP] DE fair-balance panel |
| Fair-balance standards ref | See `references/standards-by-market.md` (US 21 CFR 202.1 themes; DE HWG / Fachinfo balance) | findings_only |
| New ISI drafted by model | None — pack refuses to author approved ISI | N/A |

### Narrative
Presence ≠ balance. The skill records placement and type-size contrast; a named Regulatory reviewer decides whether revision is enough or the piece stays gated. No "fair-balanced / cleared" stamp.

### Offline checks
- Manual score against standards-by-market rows for US and DE.
- `{STAMP} --skill mlr-fair-balance-isi --status revise`

### Why this is good
Separates presence from prominence. Keeps DE and US distinct. Does not generate substitute ISI copy presented as final.

### Liability
{LIABILITY}

### Stamp
READY-local / mlr-fair-balance-isi: not tool-checked · revise · not metered · 2026-11-08

### Cross-links
Regulatory chair for process/format; Medical for safety statement accuracy vs label; Legal if omission could mislead.
""",
    "mlr-medical-chair": f"""# Good sourced draft — mlr-medical-chair

## Synthetic context (teaching only — MLR-H2)
- Markets: DE, CH.
- Claim under review: "Product X is indicated for adults and adolescents ≥12 years with type 2 diabetes."
- Pasted DE Fachinformation indication: adults only. CH excerpt: adults only.
- Adolescent extension not in supplied labels.

## Output cards

### Medical finding card
| Field | Value |
|---|---|
| Finding id | MED-001 |
| Topic | Indication population over-claim |
| Observation | Artefact includes adolescents ≥12; pasted DE/CH authorized-use text is adults only |
| Evidence | Person paste DE FI §4.1; CH Swissmedic excerpt §Indications |
| Gap | Adolescent indication not in supplied label → do not invent PIP/study support |
| Chair | Medical only (Legal/Regulatory not blended) |
| Status | revise |
| Suggested human action | Strike adolescent claim or supply label/variation text that includes ≥12 |

### Second finding (dose)
| Field | Value |
|---|---|
| Finding id | MED-002 |
| Topic | Dose frequency |
| Observation | "Twice daily" in body vs "once daily" in DE posology excerpt |
| Status | revise |
| Evidence | Fachinformation §4.2 line pasted by person |

### Offline checks
- Finding shape: `scripts/check_finding_shape.py`
- Forbidden approval phrases: `scripts/check_forbidden_phrases.py`
- `{STAMP} --skill mlr-medical-chair --status revise`

### Why this is good
Each finding cites pasted label lines. Population expansion is blocked without label support. No "medically accurate / approved" language.

### Liability
{LIABILITY}

### Stamp
READY-local / mlr-medical-chair: not tool-checked · revise · not metered · 2026-11-08

### Cross-links
Claims matrix rows C* for locator hygiene; Regulatory if variation procedure is the path; never Legal privacy topics here.
""",
    "mlr-legal-chair": f"""# Good sourced draft — mlr-legal-chair

## Synthetic context (teaching only — MLR-H2)
- Markets: DE, US.
- Artefact line: "The #1 prescribed T2D therapy among endocrinologists — better tolerated than Product Y."
- No IMS/IQVIA citation supplied. No head-to-head CSR. Footer collects email "for updates" without privacy notice link on DE panel.

## Output cards

### Legal finding card
| id | Theme | Observation | Status |
|---|---|---|---|
| LEG-001 | Comparative superiority | "Better tolerated than Product Y" without supplied H2H evidence | human_gate_required |
| LEG-002 | Ranking / #1 claim | "#1 prescribed" with no auditable data source on packet | revise — [GAP] source |
| LEG-003 | Privacy / notice | DE email capture without visible privacy notice / lawful-basis cue | revise |
| LEG-004 | Misleading omission risk | Efficacy bullets without adjacent risk cue on same panel (cross-ref fair-balance) | findings_only → hand Regulatory |

### Chair isolation
Medical owns whether tolerability language matches label; Legal owns comparative and ranking substantiation + privacy presentation. This card does not score HbA1c numerics.

### Offline checks
- `scripts/check_finding_shape.py` on findings JSON
- `scripts/check_forbidden_phrases.py`
- `{STAMP} --skill mlr-legal-chair --status human_gate_required`

### Why this is good
Comparative and ranking claims stay gated without invented market-share data. Privacy gap named for DE. No "legally cleared" wording.

### Liability
{LIABILITY}

### Stamp
READY-local / mlr-legal-chair: not tool-checked · human_gate_required · not metered · 2026-11-08

### Cross-links
Medical for clinical truth of tolerability; Regulatory for ISI placement; claims-matrix for locator rows.
""",
    "mlr-regulatory-chair": f"""# Good sourced draft — mlr-regulatory-chair

## Synthetic context (teaching only — MLR-H2)
- Markets: US, DE.
- Artefact: pre-approval congress booth panel mentioning Product X by trade name with efficacy chart.
- Person says "we will submit 2253 later" but Form 2253 workflow is **deferred** in this Pilot pack (owner lock 8 November 2026).

## Output cards

### Regulatory finding card
| id | Theme | Observation | Status |
|---|---|---|---|
| REG-001 | Pre-approval promo risk | Trade-name efficacy chart before person confirms approval status per market | human_gate_required |
| REG-002 | ISI / fair-balance process | US panel lacks adequate ISI adjacency notes (see fair-balance skill) | revise |
| REG-003 | DE HWG / format | Absoluteness of "safe and effective for all adults" on DE face | revise |
| REG-004 | Form 2253 | Out of scope this Pilot — record [DEFERRED]; do not simulate filing | findings_only |

### Process note
Regulatory chair records ceremony gaps (approval status unknown, ISI process, market-specific advertising rules). It does not file anything and does not treat deferred 2253 as optional forever — it surfaces the deferral as an explicit [DEFERRED] gap for the board pack.

### Offline checks
- Jurisdiction list via intake skeleton
- Forbidden phrases scan
- `{STAMP} --skill mlr-regulatory-chair --status human_gate_required`

### Why this is good
Pre-approval risk is gated, not soft-pedaled. 2253 deferral is honest. Format/ISI process stays out of Medical efficacy scoring.

### Liability
{LIABILITY}

### Stamp
READY-local / mlr-regulatory-chair: not tool-checked · human_gate_required · not metered · 2026-11-08

### Cross-links
Fair-balance-isi for prominence detail; board-prep for named human; intake for market list.
""",
    "mlr-compile": f"""# Good sourced draft — mlr-compile

## Synthetic context (teaching only — MLR-H2)
Inputs present: intake skeleton (DE, CH), channel=promo, claims matrix with 1 [GAP], medical findings MED-001/002, legal none for CH-only path, regulatory stub coverage CH, fair-balance notes for DE.

## Output cards

### Compile / align card
| Check | Result |
|---|---|
| Packet schema | `tools/mlr_validate_packet_offline.py` → shape OK |
| Checklist | `tools/mlr_compile_checklist_offline.py` → 3 open items |
| Open item 1 | Claims C1 evidence locator still [GAP] |
| Open item 2 | CH ruleset stub — human must accept limited automation |
| Open item 3 | Adolescent claim struck? Medical MED-001 still open |
| Align | Claims vs authorized-use: C3 aligned; C1/C2 not |
| Status | revise (not prep_complete) |

### What compile refuses
- Flipping status to prep_complete while gaps remain.
- Merging Medical+Legal+Regulatory into one "overall approve" score.
- Dropping CH stub warning to make the board deck look clean.

### Offline checks
1. `tools/mlr_validate_packet_offline.py`
2. `tools/mlr_compile_checklist_offline.py`
3. `tools/mlr_align_claims_offline.py`
4. `{STAMP} --skill mlr-compile --status revise`

### Why this is good
Compile is a gate of honesty: open items stay visible. Schema-valid ≠ board-ready.

### Liability
{LIABILITY}

### Stamp
READY-local / mlr-compile: not tool-checked · revise · not metered · 2026-11-08

### Cross-links
Return to chairs for open findings; mlr-board-prep only when human accepts residual gaps or they close.
""",
    "mlr-verify-handoff": f"""# Good sourced draft — mlr-verify-handoff

## Synthetic context (teaching only — MLR-H2)
- Claim C1: "Lowers HbA1c by 1.2% at week 24"
- Person pasted CSR excerpt: "At week 24, LS mean HbA1c change was −1.2% (95% CI −1.4, −1.0) versus placebo."
- VERIFY connector (`vvfy_`) not configured this turn → offline handoff only.

## Output cards

### Verify handoff card
| Field | Value |
|---|---|
| Claim | C1 HbA1c −1.2% week 24 |
| Passage (person paste) | CSR excerpt above |
| Offline handoff | `tools/mlr_handoff_verify_offline.py` → packet for VERIFY when keyed |
| Tool-checked VERIFY | **not** run (no vvfy_) → label not tool-checked |
| Faithfulness note | Passage supports the numeric under placebo-controlled framing; artefact omitted "versus placebo" → Medical/Legal may still revise for misleading omission |
| Status | findings_only |

### What this skill does not do
- Does not mark the claim MLR-cleared because a passage overlaps.
- Does not call live VERIFY APIs when the key is absent (MLR-H4).
- Does not replace chair findings.

### Offline checks
- `tools/mlr_handoff_verify_offline.py`
- `{STAMP} --skill mlr-verify-handoff --status findings_only`

### Why this is good
Honest about missing VERIFY key. Surfaces omission ("versus placebo") for chairs. Keeps passage text as person-supplied.

### Liability
{LIABILITY}

### Stamp
READY-local / mlr-verify-handoff: not tool-checked · findings_only · not metered · 2026-11-08

### Cross-links
Re-run with vvfy_ when available; chairs consume the omission finding.
""",
    "mlr-board-prep": f"""# Good sourced draft — mlr-board-prep

## Synthetic context (teaching only — MLR-H2)
- Packet after compile: DE+CH promo leave-behind; open items accepted by human reviewer **Jordan Lee** (named).
- Residual: CH ruleset stub acknowledged; C1 locator now filled; MED-001 adolescent claim struck in v0.9.1.

## Output cards

### Prep record card
| Field | Value |
|---|---|
| cleared_by | Jordan Lee (human) |
| Role | MLR coordinator |
| Markets | DE, CH |
| Artefact version | v0.9.1 |
| Status | prep_complete |
| Residual risks listed | CH automation stub; US not in scope |
| AI / model as cleared_by | **Rejected** (MLR-H5) |

### Offline build
`tools/mlr_build_prep_record_offline.py` with JSON:
`{{"cleared_by":"Jordan Lee","status":"prep_complete","markets":["DE","CH"],"artefact":"v0.9.1"}}`

Refusal demo (teaching): same tool with `"cleared_by":"ChatGPT"` → hard fail.

### Stamp
`{STAMP} --skill mlr-board-prep --status prep_complete`

READY-local / mlr-board-prep: not tool-checked · prep_complete · not metered · 2026-11-08

### Why this is good
Named human only. prep_complete means "ready for the human board," never "approved for use." Residuals stay on the record.

### Liability
{LIABILITY}

### Cross-links
Board meeting is outside this pack. No marketplace Released transition from this card.
""",
}


# ---------------------------------------------------------------------------
# Offline-first tools.md per skill
# ---------------------------------------------------------------------------

TOOL_MAP: dict[str, list[tuple[str, str, str, str]]] = {
    # (cli, path, use_for, never_for)
    "mlr-intake": [
        ("mlr_intake_offline.py", "tools/mlr_intake_offline.py", "Build intake skeleton + gaps", "Approving copy; inventing markets"),
        ("mlr_list_rulesets_offline.py", "tools/mlr_list_rulesets_offline.py", "Coverage map full/stub/missing", "Treating stub as full"),
        ("mlr_get_ruleset_offline.py", "tools/mlr_get_ruleset_offline.py", "Load one ruleset JSON", "Live network fetch"),
        ("check_jurisdictions.py", "scripts/check_jurisdictions.py", "Reject empty/US-default inject", "Medical judgment"),
        ("stamp_ready_line.py", STAMP, "Closing stamp line", "Approval language"),
    ],
    "mlr-capability-map": [
        ("mlr_list_rulesets_offline.py", "tools/mlr_list_rulesets_offline.py", "Show which markets have depth", "Promising unbuilt markets"),
        ("stamp_ready_line.py", STAMP, "Closing stamp line", "Approval language"),
    ],
    "mlr-channel-intent": [
        ("mlr_intake_offline.py", "tools/mlr_intake_offline.py", "Read channel field from skeleton", "Rewriting channel without human"),
        ("stamp_ready_line.py", STAMP, "Closing stamp line", "Approval language"),
    ],
    "mlr-claims-matrix": [
        ("mlr_claims_matrix_offline.py", "tools/mlr_claims_matrix_offline.py", "Claim rows + gap flags", "Inventing evidence locators"),
        ("mlr_align_claims_offline.py", "tools/mlr_align_claims_offline.py", "Structural align vs authorized-use", "Medical clearance"),
        ("stamp_ready_line.py", STAMP, "Closing stamp line", "Approval language"),
    ],
    "mlr-fair-balance-isi": [
        ("stamp_ready_line.py", STAMP, "Closing stamp line", "Approval language"),
        ("check_forbidden_phrases.py", "scripts/check_forbidden_phrases.py", "Block cleared/approved ISI phrasing", "Writing final ISI"),
    ],
    "mlr-medical-chair": [
        ("check_finding_shape.py", "scripts/check_finding_shape.py", "Finding object shape", "Legal themes"),
        ("check_forbidden_phrases.py", "scripts/check_forbidden_phrases.py", "Never-approve phrases", "Approving"),
        ("stamp_ready_line.py", STAMP, "Closing stamp line", "Approval language"),
    ],
    "mlr-legal-chair": [
        ("check_finding_shape.py", "scripts/check_finding_shape.py", "Finding object shape", "Clinical dose calls"),
        ("check_forbidden_phrases.py", "scripts/check_forbidden_phrases.py", "Never-approve phrases", "Approving"),
        ("stamp_ready_line.py", STAMP, "Closing stamp line", "Approval language"),
    ],
    "mlr-regulatory-chair": [
        ("check_finding_shape.py", "scripts/check_finding_shape.py", "Finding object shape", "Medical efficacy"),
        ("check_jurisdictions.py", "scripts/check_jurisdictions.py", "Market list hygiene", "Filing 2253"),
        ("stamp_ready_line.py", STAMP, "Closing stamp line", "Approval language"),
    ],
    "mlr-compile": [
        ("mlr_validate_packet_offline.py", "tools/mlr_validate_packet_offline.py", "Packet schema", "Board ownership"),
        ("mlr_compile_checklist_offline.py", "tools/mlr_compile_checklist_offline.py", "Open-item checklist", "Hiding gaps"),
        ("mlr_align_claims_offline.py", "tools/mlr_align_claims_offline.py", "Align pass", "Clearance"),
        ("mlr_get_packet_schema_offline.py", "tools/mlr_get_packet_schema_offline.py", "Schema dump", "Live MCP require"),
        ("stamp_ready_line.py", STAMP, "Closing stamp line", "Approval language"),
    ],
    "mlr-verify-handoff": [
        ("mlr_handoff_verify_offline.py", "tools/mlr_handoff_verify_offline.py", "Build VERIFY handoff packet", "Fake tool-checked VERIFY"),
        ("stamp_ready_line.py", STAMP, "Closing stamp line", "Approval language"),
    ],
    "mlr-board-prep": [
        ("mlr_build_prep_record_offline.py", "tools/mlr_build_prep_record_offline.py", "Named-human prep record", "AI as cleared_by"),
        ("stamp_ready_line.py", STAMP, "Closing stamp line", "Approval language"),
    ],
}


def tools_md(skill: str) -> str:
    rows = TOOL_MAP[skill]
    lines = [
        f"# Tools: {skill}",
        "",
        "## Offline first",
        "Hybrid B default: run local CLIs under `plugin/vital-mlr-review/tools/` and `scripts/`.",
        "Exit 0 = pass; 1 = hard rule error. Soft issues → flags / [CHECK] / [GAP].",
        "Label **not tool-checked** when live MCP keys (`vmlr_`, `vvfy_`) are absent (MLR-H4).",
        "",
        "| Tool | Path | Use for | Never for |",
        "|---|---|---|---|",
    ]
    for name, path, use, never in rows:
        lines.append(f"| `{name}` | `{path}` | {use} | {never} |")
    lines += [
        "",
        "## Live connectors (optional)",
        "When `vmlr_` is present, MCP tools on server `vital-mlr-review` may mirror the offline CLIs.",
        "When `vvfy_` is present, VERIFY handoff may be tool-checked. Never invent tool fields.",
        "Always use fully qualified `vital-mlr-review:<tool>` names if calling MCP.",
        "",
        "## Invocation rule",
        "Offline first. Stamp every user-facing close with "
        f"`python {STAMP} --skill {skill} --status <status>`.",
        "Written 8 November 2026 (READY world-class content uplift).",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Specialized method-standards + without-connector
# ---------------------------------------------------------------------------

STANDARDS: dict[str, str] = {
    "mlr-intake": """# Method standards — mlr-intake

Access date: 8 November 2026. Teaching citations; confirm live before relying in a real board.

| Standard | Why it matters here | URL |
|---|---|---|
| EMA SmPC / QRD templates | DE/EU label basis structure for authorized-use paste | https://www.ema.europa.eu/en/human-regulatory/marketing-authorisation/product-information/product-information-templates-human |
| Swissmedic product information | CH label excerpts | https://www.swissmedic.ch/swissmedic/en/home.html |
| FDA Prescribing Information resources | Only when US is person-listed — never default | https://www.fda.gov/drugs/drug-approvals-and-databases/drugsfda-data-files |

Never treat a URL fetch as intake complete without the person pasting the governing label text into the packet.
""",
    "mlr-capability-map": """# Method standards — mlr-capability-map

Access date: 8 November 2026.

| Standard | Why it matters here | URL |
|---|---|---|
| VITAL READY Pilot governance | Pack boundaries, never-approve, Pilot state | (in-repo) `references/governance.md` / plugin README |
| PhRMA Code / EFPIA (orientation) | Explains why promo vs exchange is a separate skill | https://www.phrma.org/codes-and-guidelines |

This skill cites orientation material only; it does not apply advertising law.
""",
    "mlr-channel-intent": """# Method standards — mlr-channel-intent

Access date: 8 November 2026.

| Standard | Why it matters here | URL |
|---|---|---|
| FDA — scientific exchange / off-label communication themes | US channel gate when US listed | https://www.fda.gov/regulatory-information/search-fda-guidance-documents |
| EFPIA Code of Practice | EU HCP promo vs non-promo boundaries | https://www.efpia.eu/relationships-code/the-efpia-code/ |
| PhRMA Code on Interactions with HCPs | US industry code orientation | https://www.phrma.org/codes-and-guidelines |

Channel classification is a human gate when artefact signals conflict with the declared channel.
""",
    "mlr-claims-matrix": """# Method standards — mlr-claims-matrix

Access date: 8 November 2026.

| Standard | Why it matters here | URL |
|---|---|---|
| ICMJE recommendations (data sharing / attribution culture) | Locator discipline for claim evidence | https://www.icmje.org/recommendations/ |
| CONSORT 2010 | How trial endpoints should be cited when CSR/passage supplied | https://www.consort-spirit.org/ |
| FDA — brief summary / fair balance themes | Claims cannot float free of risk context (cross fair-balance) | https://www.fda.gov/drugs/advertising-and-promotion |

A claim without a locator is a [GAP], not a supported row.
""",
    "mlr-fair-balance-isi": """# Method standards — mlr-fair-balance-isi

Access date: 8 November 2026. See also `standards-by-market.md`.

| Standard | Why it matters here | URL |
|---|---|---|
| 21 CFR 202.1 (prescription drug ads) | US fair balance / ISI themes | https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-202 |
| FDA — product name placement / ISI guidance index | Prominence and risk presentation | https://www.fda.gov/drugs/advertising-and-promotion |
| Germany HWG (Heilmittelwerbegesetz) overview | DE advertising constraints | https://www.gesetze-im-internet.de/hwg/ |

Presence of an ISI block does not equal fair balance.
""",
    "mlr-medical-chair": """# Method standards — mlr-medical-chair

Access date: 8 November 2026.

| Standard | Why it matters here | URL |
|---|---|---|
| EMA SmPC guideline | Indication / posology / contraindications structure | https://www.ema.europa.eu/en/human-regulatory/marketing-authorisation/product-information |
| FDA Prescribing Information PLR format | US PI sections when US listed | https://www.fda.gov/drugs/laws-acts-and-rules/prescription-drug-labeling-resources |
| MedDRA (orientation) | Adverse reaction term discipline when person supplies safety text | https://www.meddra.org/ |

Medical findings cite pasted label or study passages only (MLR-H1).
""",
    "mlr-legal-chair": """# Method standards — mlr-legal-chair

Access date: 8 November 2026.

| Standard | Why it matters here | URL |
|---|---|---|
| FTC truth-in-advertising (US orientation) | Misleadingness / substantiation culture | https://www.ftc.gov/business-guidance/advertising-marketing |
| EU Unfair Commercial Practices Directive overview | Comparative / misleading commercial practices | https://commission.europa.eu/business-economy-euro/doing-business-eu/consumer-protection_en |
| GDPR / privacy notice basics | DE/EU data-capture on materials | https://gdpr.eu/ |

Legal chair does not clear clinical accuracy; it flags comparative, ranking, and privacy presentation risks.
""",
    "mlr-regulatory-chair": """# Method standards — mlr-regulatory-chair

Access date: 8 November 2026.

| Standard | Why it matters here | URL |
|---|---|---|
| FDA advertising & promotion hub | US process / ISI / pre-approval risk orientation | https://www.fda.gov/drugs/advertising-and-promotion |
| EMA advertising / promotional material national competence note | EU national rules still apply | https://www.ema.europa.eu/ |
| Form 2253 (FDA) | **Deferred in this Pilot** — cite only as [DEFERRED] gap | https://www.fda.gov/media/72611/download |

Do not simulate filings. Pre-approval efficacy promo is human_gate_required until approval status is person-confirmed.
""",
    "mlr-compile": """# Method standards — mlr-compile

Access date: 8 November 2026.

| Standard | Why it matters here | URL |
|---|---|---|
| In-repo packet schema | Shape validation before board | `schema/` under this plugin |
| ICH E6 GCP (orientation) | Why evidence locators matter in compiled packs | https://www.ich.org/page/efficacy-guidelines |

Compile enforces honesty of open items; it is not itself a regulatory standard.
""",
    "mlr-verify-handoff": """# Method standards — mlr-verify-handoff

Access date: 8 November 2026.

| Standard | Why it matters here | URL |
|---|---|---|
| VITAL VERIFY pack contract | Passage / claim faithfulness when vvfy_ present | (sibling pack vital-verify) |
| ICMJE / quotation discipline | Person-pasted passages only | https://www.icmje.org/recommendations/ |

Overlap with a passage is not MLR approval.
""",
    "mlr-board-prep": """# Method standards — mlr-board-prep

Access date: 8 November 2026.

| Standard | Why it matters here | URL |
|---|---|---|
| Corporate record / signature culture (orientation) | Named human cleared_by | — internal SOP of the sponsor |
| VITAL MLR-H5 | Refuse AI/model/assistant as cleared_by | in-repo governance |

prep_complete ≠ approved for use. Board minutes stay with the sponsor.
""",
}


WITHOUT: dict[str, str] = {
    "mlr-intake": """# Without connector — mlr-intake

1. Collect markets from the person (refuse US default).
2. Paste authorized-use excerpts per market; tag missing PDFs [GAP].
3. Run `tools/mlr_intake_offline.py` + `mlr_list_rulesets_offline.py`.
4. Stamp with `stamp_ready_line.py --skill mlr-intake`.
5. Label the turn **not tool-checked** if no `vmlr_` key.
""",
    "mlr-capability-map": """# Without connector — mlr-capability-map

1. Answer from the skill table in the good draft / SKILL boundaries.
2. Optionally list ruleset coverage offline.
3. Stamp. Never promise marketplace Released features while Pilot.
""",
    "mlr-channel-intent": """# Without connector — mlr-channel-intent

1. Compare declared channel to artefact signals (branding, ISI, claims).
2. If conflict and no unsolicited-request record → `human_gate_required`.
3. Do not rewrite the piece; stamp and hand to human.
""",
    "mlr-claims-matrix": """# Without connector — mlr-claims-matrix

1. Build claim rows from person-highlighted text only.
2. Run `mlr_claims_matrix_offline.py` / `mlr_align_claims_offline.py`.
3. Every missing locator is [GAP]; stamp status `revise` when any gap remains.
""",
    "mlr-fair-balance-isi": """# Without connector — mlr-fair-balance-isi

1. Score presence + prominence using `standards-by-market.md`.
2. Never author replacement ISI presented as final.
3. Stamp `revise` when prominence imbalance is visible.
""",
    "mlr-medical-chair": """# Without connector — mlr-medical-chair

1. One finding per clinical/label issue; cite pasted lines.
2. Run finding-shape + forbidden-phrase scripts.
3. Stamp; leave Legal/Regulatory themes to those chairs.
""",
    "mlr-legal-chair": """# Without connector — mlr-legal-chair

1. Focus comparative, ranking, privacy, misleadingness.
2. Gate unsubstantiated superiority claims.
3. Stamp; do not score dose/indication (Medical).
""",
    "mlr-regulatory-chair": """# Without connector — mlr-regulatory-chair

1. Check approval status known per market; gate pre-approval promo.
2. Record Form 2253 as [DEFERRED] in this Pilot.
3. Stamp; cross-link fair-balance for prominence detail.
""",
    "mlr-compile": """# Without connector — mlr-compile

1. Validate packet schema offline.
2. Emit checklist of open items; refuse prep_complete while gaps remain unless human explicitly accepts residuals (then board-prep).
3. Stamp `revise` when checklist non-empty.
""",
    "mlr-verify-handoff": """# Without connector — mlr-verify-handoff

1. Build handoff JSON with person-pasted passage via offline CLI.
2. Do not claim tool-checked VERIFY without `vvfy_`.
3. Note omissions (e.g. missing comparator) for chairs; stamp findings_only.
""",
    "mlr-board-prep": """# Without connector — mlr-board-prep

1. Require a real human name in cleared_by.
2. Run `mlr_build_prep_record_offline.py`; reject AI names.
3. Stamp `prep_complete` only as board-prep readiness, never use-approval.
""",
}


def thicken_knowledge(skill: str, existing: str) -> str:
    addenda = {
        "mlr-intake": """
## World-class depth notes (8 November 2026)
- Markets are a closed list from the person; empty list is a hard fail, not a US fill.
- Ruleset coverage `stub` means limited automation — say so on the intake card.
- Authorized-use text must be pasted; linking a URL without paste is [GAP].
- Channel may be unknown at intake; do not invent promo vs exchange — hand to mlr-channel-intent.
- Artefact version + hash (when supplied) travel with every downstream card.
""",
        "mlr-capability-map": """
## World-class depth notes (8 November 2026)
- Map is orientation only; it never runs chairs.
- Pilot release_state must be visible when describing pack power.
- Eleven-skill funnel: intake → channel → claims/ISI → M/L/R → compile → verify → board-prep.
""",
        "mlr-channel-intent": """
## World-class depth notes (8 November 2026)
- Declared channel loses to artefact signals when they conflict.
- Unsolicited MI request records are evidence; absence is [GAP], not "probably fine."
- Mixed channel pieces are usually `human_gate_required`.
- Branding + efficacy + ISI footer strongly suggests promotional posture.
""",
        "mlr-claims-matrix": """
## World-class depth notes (8 November 2026)
- One row per atomic claim; do not bundle numerics with qualitative superiority.
- Locators name document + section + page/line when known.
- Comparative claims always dual-route to Legal.
- Align is structural vs authorized-use, not clinical judgment.
""",
        "mlr-fair-balance-isi": """
## World-class depth notes (8 November 2026)
- Score presence, proximity, type-size/contrast, and market-specific panels separately.
- US and DE fair-balance are not interchangeable checklists.
- Refusing to draft "final ISI" is a feature (never-approve).
- See standards-by-market.md for per-jurisdiction rows.
""",
        "mlr-medical-chair": """
## World-class depth notes (8 November 2026)
- Population, dose, indication, contraindication, and safety statement mismatches are in-scope.
- Each finding needs pasted evidence; "generally known" is invalid (MLR-H1).
- Do not absorb comparative-ad or privacy issues (Legal).
""",
        "mlr-legal-chair": """
## World-class depth notes (8 November 2026)
- Ranking (#1), superiority, and implied uniqueness need auditable sources on the packet.
- Privacy notice gaps on data capture are Legal findings even on "medical" pieces.
- Misleading omission may be shared with fair-balance/Regulatory — still record a Legal id.
""",
        "mlr-regulatory-chair": """
## World-class depth notes (8 November 2026)
- Approval status unknown + efficacy promo → human_gate_required.
- Form 2253 is deferred in Pilot — record [DEFERRED], do not fake a filing path.
- National advertising rules (e.g. HWG) stay market-scoped.
""",
        "mlr-compile": """
## World-class depth notes (8 November 2026)
- Schema validity is necessary, not sufficient.
- Checklist items map to owning skills; compile does not close them silently.
- prep_complete is owned by board-prep after human acceptance, not by compile alone.
""",
        "mlr-verify-handoff": """
## World-class depth notes (8 November 2026)
- Handoff packet preserves claim text + passage + locator.
- Without vvfy_, never print tool-checked VERIFY results.
- Passage support can coexist with misleading-omission flags for chairs.
""",
        "mlr-board-prep": """
## World-class depth notes (8 November 2026)
- cleared_by must resolve to a natural person name; role optional.
- Residual risks remain on the prep record when human accepts them.
- prep_complete is readiness for human board, not marketplace or promotional clearance.
""",
    }
    block = addenda.get(skill, "")
    if "World-class depth notes" in existing:
        return existing
    return existing.rstrip() + "\n" + block


def thicken_failure(skill: str, existing: str) -> str:
    addenda = {
        "mlr-intake": """
## Additional failure modes
- Silent US market inject when person listed only EU/CH markets.
- Treating CH stub ruleset as full automation coverage.
- Pasting competitor label text as if it were the product FI.
- Closing intake with status prep_complete (wrong skill).
""",
        "mlr-capability-map": """
## Additional failure modes
- Claiming the pack can "approve" materials.
- Hiding Pilot state or implying marketplace Released.
- Routing privacy questions to Medical chair.
""",
        "mlr-channel-intent": """
## Additional failure modes
- Accepting "scientific exchange" on a branded efficacy leave-behind with no MI request record.
- Auto-rewriting channel without human_gate_required.
- Applying US-only channel doctrine to DE-only packets without saying so.
""",
        "mlr-claims-matrix": """
## Additional failure modes
- Filling CSR page numbers from memory.
- Marking comparative claims findings_only without Legal route.
- Collapsing three claims into one row to look cleaner.
""",
        "mlr-fair-balance-isi": """
## Additional failure modes
- Equating ISI presence with fair balance.
- Generating substitute ISI presented as final approved text.
- Using US 21 CFR checks alone on a DE-only artefact.
""",
        "mlr-medical-chair": """
## Additional failure modes
- Expanding indication to adolescents without label support.
- Blending Legal comparative themes into Medical cards.
- Using "medically accurate" as a status synonym for approved.
""",
        "mlr-legal-chair": """
## Additional failure modes
- Inventing IMS/#1 data to close LEG ranking gaps.
- Clearing comparative claims because Medical liked the tolerability sentence.
- Ignoring DE privacy notice gaps on email capture.
""",
        "mlr-regulatory-chair": """
## Additional failure modes
- Soft-pedaling pre-approval trade-name efficacy charts.
- Simulating Form 2253 submission while deferred.
- Treating compile schema-OK as regulatory clearance.
""",
        "mlr-compile": """
## Additional failure modes
- Dropping open checklist items to reach prep_complete.
- Merging M/L/R into a single approve score.
- Hiding CH stub warnings from the board packet.
""",
        "mlr-verify-handoff": """
## Additional failure modes
- Claiming tool-checked VERIFY without vvfy_.
- Treating passage overlap as MLR approval.
- Omitting "versus placebo" style qualifiers when the passage has them and the claim does not.
""",
        "mlr-board-prep": """
## Additional failure modes
- Accepting ChatGPT / Claude / Assistant as cleared_by.
- Equating prep_complete with approved-for-use.
- Removing residual risk lines the human accepted.
""",
    }
    block = addenda.get(skill, "")
    if "Additional failure modes" in existing:
        return existing
    return existing.rstrip() + "\n" + block


FAIR_BALANCE_STANDARDS = """# Standards by market — fair balance / ISI

Access date: 8 November 2026. Orientation only; confirm current law/guidance before a live board.

| Market | Instrument / theme | What to score on the artefact | URL |
|---|---|---|---|
| US | 21 CFR 202.1 fair balance | Risk info comparable in scope to benefit claims; ISI presence + prominence | https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-202 |
| US | FDA advertising & promotion hub | Product name / ISI placement themes; pre-approval limits | https://www.fda.gov/drugs/advertising-and-promotion |
| DE | HWG (Heilmittelwerbegesetz) | Absolute claims, consumer vs HCP face, mandatory information themes | https://www.gesetze-im-internet.de/hwg/ |
| DE | Fachinformation as label basis | Safety statements consistent with FI; DE panel not a translated US ISI dump | https://www.ema.europa.eu/en/human-regulatory/marketing-authorisation/product-information |
| CH | Swissmedic product information | CH-facing safety consistent with Swiss PI; do not assume DE FI equals CH | https://www.swissmedic.ch/swissmedic/en/home.html |
| UK | MHRA Blue Guide (orientation) | If UK listed — risk/benefit presentation in promo materials | https://www.gov.uk/government/publications/blue-guide-advertising-and-promoting-medicines |

## Scoring discipline
1. Run only rows for markets on the intake card.
2. Record presence, proximity, typography/contrast, and market-panel completeness separately.
3. Never output "fair balanced / approved for use."
"""


def patch_skill_md(text: str, skill: str) -> str:
    if "stamp_ready_line" in text:
        return text
    # Insert Scripts / stamp note before Hard rules or at end of Tool path
    stamp_block = (
        f"\n## Closing stamp\n\n"
        f"End every user-facing turn with "
        f"`python tools/stamp_ready_line.py --skill {skill} --status <status>` "
        f"(see `templates/check-line-stamp.md`). "
        f"Optional `--letter-lines` prints the liability line.\n"
    )
    if "## Hard rules" in text:
        return text.replace("## Hard rules", stamp_block + "\n## Hard rules", 1)
    return text.rstrip() + "\n" + stamp_block


def unique_gate(skill: str) -> str:
    return f"wc-{skill}-" + hashlib.sha256(skill.encode()).hexdigest()[:10]


def upgrade_expected(path: Path, skill: str) -> None:
    data = {}
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            data = {}
    data["unique_gate"] = unique_gate(skill)
    data.setdefault("skill", skill)
    data.setdefault("never_approve", True)
    data.setdefault("allowed_statuses", ["findings_only", "revise", "human_gate_required", "prep_complete"])
    data["world_class_uplift"] = "2026-11-08"
    write(path, json.dumps(data, indent=2, sort_keys=True))


def prune_assets() -> int:
    removed = 0
    for assets in SKILLS.glob("*/assets"):
        if assets.is_dir():
            shutil.rmtree(assets)
            removed += 1
    return removed


def main() -> int:
    for skill_dir in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        name = skill_dir.name
        if name not in GOODS:
            print("skip unknown", name)
            continue
        write(skill_dir / "examples" / "good-sourced-draft.md", GOODS[name])
        write(skill_dir / "references" / "tools.md", tools_md(name))
        write(skill_dir / "references" / "method-standards.md", STANDARDS[name])
        write(skill_dir / "references" / "without-connector.md", WITHOUT[name])

        know_p = skill_dir / "references" / "knowledge.md"
        know = know_p.read_text(encoding="utf-8") if know_p.exists() else f"# Knowledge — {name}\n"
        write(know_p, thicken_knowledge(name, know))

        fail_p = skill_dir / "references" / "failure-modes.md"
        fail = fail_p.read_text(encoding="utf-8") if fail_p.exists() else f"# Failure modes — {name}\n"
        write(fail_p, thicken_failure(name, fail))

        skill_md = skill_dir / "SKILL.md"
        write(skill_md, patch_skill_md(skill_md.read_text(encoding="utf-8"), name))

        upgrade_expected(skill_dir / "evals" / "known-answer" / "expected.json", name)

        # ensure poor example exists
        poor = list(skill_dir.glob("examples/poor*.md"))
        if not poor:
            write(
                skill_dir / "examples" / "poor-approval-language.md",
                f"""# Poor example — {name}

Bad close: "This material is approved for use and mlr_reviewed."

Why poor: Violates MLR-H3 / FORBIDDEN_PHRASES. Correct status is findings_only|revise|human_gate_required|prep_complete with liability line — never use-approval.
""",
            )

    fb = SKILLS / "mlr-fair-balance-isi" / "references" / "standards-by-market.md"
    write(fb, FAIR_BALANCE_STANDARDS)

    n = prune_assets()
    print(f"upgraded skills; pruned assets dirs={n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
