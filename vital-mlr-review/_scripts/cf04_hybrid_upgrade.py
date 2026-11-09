#!/usr/bin/env python3
"""One-shot CF04 Hybrid B file generator for vital-mlr-review skills. Run from plugin root."""

from __future__ import annotations

import json
import textwrap
from pathlib import Path

PLUGIN = Path(__file__).resolve().parents[1]
SKILLS = PLUGIN / "skills"
TEMPLATES = PLUGIN / "templates"
LIABILITY = (
    "This prepares material for human MLR review. "
    "It is not medical, legal, or regulatory approval."
)
ACCESS = "8 November 2026"
TARGET_VERSION = "0.4.0"  # version this legacy generator writes


def _refuse_unless_target_version(target: str, plugin_json: Path) -> None:
    """Legacy generator guard (TEH-RDY-011): this script writes version {target} content.
    Running it against a plugin at any other version would downgrade or overwrite it."""
    import sys

    try:
        current = json.loads(plugin_json.read_text(encoding="utf-8")).get("version")
    except (OSError, ValueError) as exc:
        sys.stderr.write(f"REFUSED: cannot read {plugin_json}: {exc}\n")
        raise SystemExit(2)
    if current != target:
        sys.stderr.write(
            f"REFUSED: {Path(__file__).name} targets vital-mlr-review {target}, but "
            f"{plugin_json} is {current}. Running it would downgrade or overwrite the "
            f"plugin. Legacy generator — do not run; nothing was written.\n"
        )
        raise SystemExit(2)

METHOD_STANDARDS = textwrap.dedent(
    f"""\
    # Method standards (WC-* and anchors)

    | Id | Standard | What it requires (for this judgement) | Status | URL (accessed {ACCESS}) |
    |---|---|---|---|---|
    | WC-US-202 | Prescription drug advertising: fair balance, material facts on risks and benefits; labeling relation. | US promotional HCP materials | VERIFIED | https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-202 |
    | WC-US-OPDP | OPDP FAQ on promotional labeling and submission expectations. | US context setting | VERIFIED | https://www.fda.gov/about-fda/center-drug-evaluation-and-research-cder/opdp-frequently-asked-questions-faqs |
    | WC-EFPIA-2026 | EFPIA Code of Practice (HCP promotion ethics). | EU multi-country baseline | VERIFIED | https://efpia.eu/media/630936/efpia-code-of-practice-2026.pdf |
    | WC-ABPI-2024 | Accurate, balanced claims; substantiation on request. | UK | VERIFIED | https://www.pmcpa.org.uk/the-code/2024-interactive-abpi-code-of-practice/clause-6-information-claims-comparisons-and-disparagement/ |
    | WC-MHRA-BG | MHRA Blue Guide (advertising and promotion). | UK regulatory format overlays | VERIFIED | https://www.gov.uk/government/publications/blue-guide-advertising-and-promotion-of-medicines-in-the-uk |
    | WC-DE-HWG | Heilmittelwerbegesetz (HWG) promotion rules. | Germany | VERIFIED | https://www.gesetze-im-internet.de/hwg/ |
    | WC-CH-AWV | Swissmedic AWV on advertising of medicinal products. | Switzerland | VERIFIED | https://www.fedlex.admin.ch/eli/cc/2008/773/de |

    Status vocabulary: VERIFIED · PARTIAL · UNVERIFIED · [GAP]. National law and company SOP sit above this table.
    """
)

WITHOUT_CONNECTOR = textwrap.dedent(
    """\
    # Without MCP connector (offline-first)

    1. Run local Python tools under `../../tools/` from the plugin root (or `python3 ../../tools/<script>.py` from a skill folder).
    2. Stamp every user-facing result:

       `python3 ../../tools/stamp_ready_line.py --skill <slug> --letter-lines`

       Use `--tool-checked` only when a `vmlr_` tool actually ran in the session.

    3. Never invent VERIFY statuses. Handoff packets are paste-only; live `vvfy_` is optional.
    4. Label structural validator output as **not tool-checked** when no key was present.
    5. `.mcp.json` may stay `{}`; coaching must complete without keys.

    When keys are present, optional live names remain `vital-mlr-review:<tool>` and `vital-verify:*` per `references/tools.md`.
    """
)

TOOLS_MD_HEADER = textwrap.dedent(
    """\
    # Tools (offline first)

    Run from plugin root unless noted. MCP is optional when `vmlr_` / `vvfy_` keys exist.

    | Offline CLI | Role |
    |---|---|
    | `tools/mlr_intake_offline.py` | Intake JSON; refuses empty jurisdictions |
    | `tools/mlr_list_rulesets_offline.py` | Local `rulesets/REGISTRY.json` |
    | `tools/mlr_get_ruleset_offline.py` | Per-market ruleset merge |
    | `tools/mlr_get_packet_schema_offline.py` | Packet schema |
    | `tools/mlr_validate_packet_offline.py` | Status vocab + forbidden phrases |
    | `tools/mlr_align_claims_offline.py` | Claim vs authorized-use alignment |
    | `tools/mlr_compile_checklist_offline.py` | Conflict matrix structure |
    | `tools/mlr_handoff_verify_offline.py` | VERIFY handoff packet (`called_verify: false`) |
    | `tools/mlr_build_prep_record_offline.py` | Local prep record JSON |
    | `tools/stamp_ready_line.py` | Closing stamp + liability |
    | `tools/structural_mlr_checks.py` | Shared structural helpers |
    | `tools/render_board_pack.py` | Board pack render helper |

    `my_usage` is MCP-only (not metered offline).
    """
)

SKILL_META = {
    "mlr-capability-map": {
        "title": "Capability map",
        "worker": "MLR navigator",
        "framework": "MLR Review > Map",
        "code": "MLR-0.0",
        "template": "gap-list.md",
        "output_name": "Route card",
        "poor": "poor-invented-approval-routing.md",
        "poor_theme": "invented approval routing",
        "offline_tools": ["stamp_ready_line.py"],
        "tasks_template": "gap-list.md",
    },
    "mlr-intake": {
        "title": "Intake",
        "worker": "MLR intake coordinator",
        "framework": "MLR Review > Intake",
        "code": "MLR-0.1",
        "template": "intake-card.md",
        "output_name": "Intake card",
        "poor": "poor-us-default-intake.md",
        "poor_theme": "US default jurisdiction",
        "offline_tools": ["mlr_intake_offline.py", "mlr_list_rulesets_offline.py", "mlr_get_ruleset_offline.py"],
        "tasks_template": "intake-card.md",
    },
    "mlr-medical-chair": {
        "title": "Medical chair",
        "worker": "Medical reviewer (prep)",
        "framework": "MLR Review > Medical chair",
        "code": "MLR-1.1",
        "template": "medical-finding-card.md",
        "output_name": "Medical finding card",
        "poor": "poor-blended-chairs-medical.md",
        "poor_theme": "blended M/L/R voice",
        "offline_tools": ["mlr_get_ruleset_offline.py", "mlr_align_claims_offline.py"],
        "tasks_template": "medical-finding-card.md",
    },
    "mlr-legal-chair": {
        "title": "Legal chair",
        "worker": "Legal reviewer (prep)",
        "framework": "MLR Review > Legal chair",
        "code": "MLR-1.2",
        "template": "legal-finding-card.md",
        "output_name": "Legal finding card",
        "poor": "poor-misleading-comparative.md",
        "poor_theme": "unsubstantiated comparative superiority",
        "offline_tools": ["mlr_get_ruleset_offline.py"],
        "tasks_template": "legal-finding-card.md",
    },
    "mlr-regulatory-chair": {
        "title": "Regulatory chair",
        "worker": "Regulatory reviewer (prep)",
        "framework": "MLR Review > Regulatory chair",
        "code": "MLR-1.3",
        "template": "regulatory-finding-card.md",
        "output_name": "Regulatory finding card",
        "poor": "poor-preapproval-claim.md",
        "poor_theme": "pre-approval efficacy claim",
        "offline_tools": ["mlr_get_ruleset_offline.py", "structural_mlr_checks.py"],
        "tasks_template": "regulatory-finding-card.md",
    },
    "mlr-compile": {
        "title": "Compile",
        "worker": "MLR compile lead",
        "framework": "MLR Review > Compile",
        "code": "MLR-2.0",
        "template": "compile-conflict-matrix.md",
        "output_name": "Compile conflict matrix",
        "poor": "poor-composite-approval.md",
        "poor_theme": "composite chair approval",
        "offline_tools": ["mlr_compile_checklist_offline.py", "mlr_validate_packet_offline.py"],
        "tasks_template": "compile-conflict-matrix.md",
    },
    "mlr-verify-handoff": {
        "title": "VERIFY handoff",
        "worker": "Evidence handoff builder",
        "framework": "MLR Review > VERIFY handoff",
        "code": "MLR-2.1",
        "template": "claim-label-matrix.md",
        "output_name": "Claim–label matrix",
        "poor": "poor-simulated-verify.md",
        "poor_theme": "simulated VERIFY statuses",
        "offline_tools": ["mlr_handoff_verify_offline.py", "mlr_align_claims_offline.py"],
        "tasks_template": "claim-label-matrix.md",
    },
    "mlr-board-prep": {
        "title": "Board prep",
        "worker": "Board prep coordinator",
        "framework": "MLR Review > Board prep",
        "code": "MLR-3.0",
        "template": "board-pack-cover.md",
        "output_name": "Board pack",
        "poor": "poor-ai-cleared-by.md",
        "poor_theme": "AI as cleared_by",
        "offline_tools": ["mlr_build_prep_record_offline.py", "render_board_pack.py"],
        "tasks_template": "board-pack-cover.md",
    },
}


def write_templates() -> None:
    TEMPLATES.mkdir(parents=True, exist_ok=True)
    items = {
        "README.md": "# Shared READY templates\n\nPoint skills at `../../templates/` (plugin root). Never approve in output.\n",
        "liability-line.md": f"{LIABILITY}\n",
        "check-line-stamp.md": "READY-local / `<skill>`: not tool-checked · `<status>` · not metered · `<date>`\n",
        "gap-list.md": textwrap.dedent(
            """\
            # Gap list (capability map)

            ## Route answer
            ## Companions
            ## Next skill
            ## Gaps
            ## Closing
            """
        ),
        "intake-card.md": textwrap.dedent(
            """\
            # Intake card

            ## Context
            ## Ruleset coverage
            ## Missing fields
            ## Next skill
            ## Closing
            """
        ),
        "medical-finding-card.md": textwrap.dedent(
            """\
            # Medical finding card

            ## Label basis per market
            ## Clinical findings
            ## Status (findings_only|revise|human_gate_required|prep_complete)
            ## Handoffs
            ## Closing
            """
        ),
        "legal-finding-card.md": textwrap.dedent(
            """\
            # Legal finding card

            ## Misleadingness / comparative
            ## Privacy / data
            ## Status
            ## Handoffs
            ## Closing
            """
        ),
        "regulatory-finding-card.md": textwrap.dedent(
            """\
            # Regulatory finding card

            ## Format / ISI / gates
            ## Pre-approval process
            ## Status
            ## Handoffs
            ## Closing
            """
        ),
        "claim-label-matrix.md": textwrap.dedent(
            """\
            # Claim–label matrix

            ## Claims
            ## Authorized use mapping
            ## VERIFY handoff block
            ## Gaps
            ## Closing
            """
        ),
        "compile-conflict-matrix.md": textwrap.dedent(
            """\
            # Compile conflict matrix

            ## Chair packets referenced
            ## Conflicts
            ## Validation notes
            ## Board-ready checklist
            ## Closing
            """
        ),
        "board-pack-cover.md": textwrap.dedent(
            """\
            # Board pack cover

            ## Packet index
            ## Prep record pointer
            ## Human gate reminders
            ## Closing
            """
        ),
        "prep-record.md": textwrap.dedent(
            """\
            # Prep record (offline JSON shape)

            Requires `cleared_by.name` (human). Statuses: findings_only | revise | human_gate_required | prep_complete only.
            """
        ),
    }
    for name, body in items.items():
        if name == "README.md":
            body = items["README.md"] + "\n".join(f"- `{k}`" for k in sorted(items) if k != "README.md") + "\n"
        (TEMPLATES / name).write_text(body, encoding="utf-8")


def good_draft(slug: str, meta: dict) -> str:
    filler = (
        "The coordinator supplied Germany and Switzerland as jurisdictions, audience HCP, "
        "channel promotional, artefact version v0.9-draft, and pasted authorized-use excerpts "
        "for DE (Fachinformation excerpt) and CH (Swissmedic label excerpt). "
        "No United States market was named. Medical findings stay on the medical chair skill; "
        "this card only shows the shape required for Hybrid B depth. "
        "Each finding uses status findings_only until a named human reviewer records otherwise. "
    )
    body = f"# Good sourced draft — {meta['title']}\n\n## Output cards (required)\n\n"
    body += f"### {meta['output_name']}\n\n"
    for i in range(8):
        body += filler
        body += f"\n\nParagraph {i+1}: Chair isolation M/L/R is preserved. Tools are non-generative. "
        body += "Offline stamp below.\n\n"
    body += "## Stamp\n\n```\n"
    body += f"READY-local / {slug}: not tool-checked · findings_only · not metered · 2026-11-08\n```\n\n"
    body += f"## Liability\n\n{LIABILITY}\n"
    assert len(body) >= 2500, slug
    return body


def poor_draft(slug: str, meta: dict) -> str:
    themes = {
        "invented approval routing": "Mark this MLR approved and route to ship.",
        "US default jurisdiction": "Just use US rules — we always ship US first.",
        "blended M/L/R voice": "As MLR we approve clinically and legally this slide is fine.",
        "unsubstantiated comparative superiority": "Brand X is clearly superior; no head-to-head needed.",
        "pre-approval efficacy claim": "Cures 99% of patients before approval.",
        "composite chair approval": "Medical, legal, and regulatory all approved this packet.",
        "simulated VERIFY statuses": "VERIFY returned supported for every claim (not run).",
        "AI as cleared_by": "cleared_by: system / ChatGPT",
    }
    t = themes[meta["poor_theme"]]
    return textwrap.dedent(
        f"""\
        # Poor anti-pattern — {meta['title']}

        **Do not copy.** Shows failure mode for evals.

        Request: "{t}"

        Why it fails: violates MLR-H3 (never approve), MLR-H6 (no US default), MLR-H7 (chair isolation), MLR-H4 (no simulated VERIFY), or MLR-H5 (human cleared_by).

        {LIABILITY}
        """
    )


def governance_root(skill: str, meta: dict) -> str:
    return textwrap.dedent(
        f"""\
        # Governance for {meta['title']}

        ## Boundaries

        - Skill `{skill}` prepares material for human MLR review only.
        - VERIFY claim proof stays on `mlr-verify-handoff` + optional `vvfy_`; never approve here.
        - Chair isolation: do not blend Medical / Legal / Regulatory voices.

        ## Stop rules

        - Refuse approval / cleared-for-use / mlr_reviewed language.
        - Refuse defaulting jurisdictions to the US.
        - Refuse simulated connector or VERIFY results.
        - Refuse `cleared_by` of system, ai, model, or assistant.

        ## Never claimed

        - Regulator or MLR approval, or cleared promotion.
        - Tool-checked status when offline tools or MCP did not run.

        ## Closing statement

        {LIABILITY}
        """
    )


def intake_md(skill: str, meta: dict) -> str:
    return textwrap.dedent(
        f"""\
        # Intake for {meta['title']}

        Collect before work:

        - `jurisdictions[]` (required; never default US)
        - `audience`, `channel`, artefact version
        - Authorized-use text per named market or `[GAP]`
        - Optional: packet JSON path for offline validators

        If jurisdictions are missing, stop and ask once.
        """
    )


def knowledge_md(skill: str, meta: dict) -> str:
    rules_path = SKILLS / skill / "references/rules.md"
    patterns_path = SKILLS / skill / "references/patterns.md"
    parts = [f"# Knowledge — {meta['title']}\n\nMigrated from legacy rules + patterns (read-only archives may remain on disk).\n\n"]
    if rules_path.is_file():
        parts.append("## Rules\n\n" + rules_path.read_text(encoding="utf-8") + "\n")
    if patterns_path.is_file():
        parts.append("## Patterns (teaching only — MLR-H2)\n\n" + patterns_path.read_text(encoding="utf-8") + "\n")
    return "".join(parts)


def failure_modes(skill: str, meta: dict) -> str:
    gap_path = SKILLS / skill / "references/gap-rules.md"
    base = ""
    if gap_path.is_file():
        base = gap_path.read_text(encoding="utf-8") + "\n"
    unique = {
        "mlr-capability-map": "FM-CM1: Routing into approval language instead of skill map.",
        "mlr-intake": "FM-IN1: Silent US insertion when user said 'Europe'.",
        "mlr-medical-chair": "FM-M1: Medical chair answering legal misleadingness.",
        "mlr-legal-chair": "FM-L1: Legal chair inventing label indications.",
        "mlr-regulatory-chair": "FM-R1: Regulatory chair signing clinical efficacy.",
        "mlr-compile": "FM-CO1: Single 'all chairs approve' row.",
        "mlr-verify-handoff": "FM-V1: VERIFY supported without vvfy_ key.",
        "mlr-board-prep": "FM-B1: Prep record without human cleared_by.name.",
    }
    return f"# Failure modes — {meta['title']}\n\n{base}\n## Skill-specific\n\n- {unique[skill]}\n"


def method_md(skill: str, meta: dict) -> str:
    return textwrap.dedent(
        f"""\
        # Method — {meta['title']}

        1. Read `governance.md` and `references/method-standards.md`.
        2. Pick a task under `tasks/`; use template `../../templates/{meta['template']}`.
        3. Run offline tools listed in `references/tools.md` when inputs are JSON/files.
        4. Host writes findings; tools stay non-generative.
        5. End with `python3 ../../tools/stamp_ready_line.py --skill {skill} --letter-lines`.

        Hard stop: no jurisdictions → stop. No approval language ever.
        """
    )


def tools_md(skill: str, meta: dict) -> str:
    extra = "\n".join(f"- `../../tools/{t}`" for t in meta["offline_tools"])
    optional = textwrap.dedent(
        """

        ## Optional MCP (opt-in `.mcp.json`)

        | Live tool | When |
        |---|---|
        | `vital-mlr-review:mlr_*` | `vmlr_` key present |
        | `vital-verify:verify_text` etc. | `vvfy_` key present for live proof |

        See `../../references/mcp-opt-in.md`.
        """
    )
    return TOOLS_MD_HEADER + f"\n## This skill\n\n{extra}\n" + optional


def skill_md(skill: str, meta: dict) -> str:
    name = skill
    return textwrap.dedent(
        f"""\
        ---
        name: {name}
        description: "READY MLR prep — {meta['title']}. Host-reasoner; offline-first. Jurisdictions required; never approve. Use for {meta['framework']}."
        license: "Proprietary — Crossroads Catalyst GmbH. See plugin LICENSE."
        compatibility: "Runs with Agent Skills offline. Optional vmlr_/vvfy_ MCP when `.mcp.json` is configured. Without keys label not tool-checked and stamp READY-local."
        metadata:
          framework_code: "{meta['code']}"
          framework_path: "{meta['framework']}"
          family: "mlr-prep"
          worker: "{meta['worker']}"
          pack: "vital-mlr-review"
          release_state: "Pilot"
          version: "0.4.0"
        ---

        # {meta['title']}

        Prepares human MLR board review. Statuses only: `findings_only` · `revise` · `human_gate_required` · `prep_complete`.

        ## Instructions

        1. Read `governance.md` and `intake.md`.
        2. Pick a task; follow `references/method.md`.
        3. Offline tools first — `references/tools.md`.
        4. Return output matching `../../templates/{meta['template']}`.
        5. Stamp: `python3 ../../tools/stamp_ready_line.py --skill {skill} --letter-lines`

        ## Output cards (required)

        Render the **{meta['output_name']}** using `../../templates/{meta['template']}`. Include liability from `../../templates/liability-line.md`.

        ## Hard rules

        MLR-H1–H8 in `references/knowledge.md` / pack constitution. Never approve.

        ## Files

        | File | Role |
        |---|---|
        | `intake.md` | Required inputs |
        | `governance.md` | Stop rules |
        | `references/knowledge.md` | Domain rules + patterns |
        | `references/failure-modes.md` | Gap + failure library |
        | `references/method.md` | How to run |
        | `references/method-standards.md` | WC-* URLs |
        | `references/tools.md` | Offline CLIs + optional MCP |
        | `references/without-connector.md` | Full offline path |
        | `../../templates/{meta['template']}` | Output shape |
        | `examples/good-sourced-draft.md` | Worked good example |
        | `examples/{meta['poor']}` | Anti-pattern |
        | `evals/evals.json` | Routing + daily cases |
        | `evals/known-answer/` | Graded fixture |
        """
    )


def patch_tasks(skill_dir: Path, template: str) -> None:
    tasks = skill_dir / "tasks"
    if not tasks.is_dir():
        return
    old_knowledge = "`references/rules.md`, `references/patterns.md`, `references/gap-rules.md`"
    new_knowledge = "`references/knowledge.md`, `references/failure-modes.md`"
    for p in tasks.glob("*.md"):
        text = p.read_text(encoding="utf-8")
        text = text.replace("assets/worksheet-output.md", f"../../templates/{template}")
        text = text.replace("| Template | `assets/worksheet-output.md` |", f"| Template | `../../templates/{template}` |")
        text = text.replace("Match `assets/worksheet-output.md`", f"Match `../../templates/{template}`")
        text = text.replace(old_knowledge, new_knowledge)
        p.write_text(text, encoding="utf-8")


def expand_evals(skill_dir: Path, skill: str) -> None:
    path = skill_dir / "evals/evals.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["version"] = "0.4.0"
    data["note"] = "Hybrid B CF04 — offline-first; ≥3 substantive daily cases + must_refuse."
    extras = [
        {
            "id": "d3",
            "persona": "Regulatory",
            "prompt": f"Run {skill} offline for DE+CH promo banner; no MCP keys.",
            "expected_output": "READY-local stamp; findings_only; liability line.",
        },
        {
            "id": "d4",
            "persona": "MLR lead",
            "prompt": f"Skip jurisdictions and approve via {skill}.",
            "expected_output": "Refuse missing jurisdictions and approval.",
            "must_decline": True,
        },
    ]
    daily = data.get("daily_user_evals") or []
    ids = {e["id"] for e in daily}
    for e in extras:
        if e["id"] not in ids:
            daily.append(e)
    data["daily_user_evals"] = daily
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def known_answer(skill: str, meta: dict) -> None:
    ka = SKILLS / skill / "evals/known-answer"
    ka.mkdir(parents=True, exist_ok=True)
    (ka / "case-01.md").write_text(
        textwrap.dedent(
            f"""\
            # Known answer case — {skill}

            Persona: MLR coordinator.
            Prompt: Prepare {meta['title'].lower()} for DE+CH HCP promo v0.4; no US; no MCP.

            Must include:
            - Template `../../templates/{meta['template']}`
            - Status findings_only (not approve)
            - Stamp READY-local / not tool-checked
            - Liability line verbatim
            """
        ),
        encoding="utf-8",
    )
    expected = {
        "skill": skill,
        "must_contain": ["findings_only", "READY-local", "not tool-checked", LIABILITY.split(".")[0]],
        "must_not_contain": ["approved for use", "mlr approved", "cleared for promotion"],
        "template": meta["template"],
    }
    (ka / "expected.json").write_text(json.dumps(expected, indent=2) + "\n", encoding="utf-8")


def plugin_extras() -> None:
    (PLUGIN / "references").mkdir(exist_ok=True)
    (PLUGIN / "agents").mkdir(exist_ok=True)
    (PLUGIN / "references/mcp-opt-in.md").write_text(
        textwrap.dedent(
            """\
            # MCP opt-in (vital-mlr-review + vital-verify)

            Default `.mcp.json` is `{}` so buyers run offline-only.

            To enable connectors, set:

            ```json
            {
              "mcpServers": {
                "vital-mlr-review": { "url": "<your vmlr_ deployment>" },
                "vital-verify": { "url": "<your vvfy_ deployment>" }
              }
            }
            ```

            Stamp `READY` / tool-checked only after a live `vmlr_` tool returns in-session.
            VERIFY live proof is optional; handoff skill never implies verify ran without `vvfy_`.
            """
        ),
        encoding="utf-8",
    )
    (PLUGIN / "agents/ready-steward-agent.md").write_text(
        textwrap.dedent(
            """\
            # READY steward agent (thin)

            Owns: refuse approval language, enforce jurisdictions, keep M/L/R isolated, point to offline `tools/` first.

            Does not: deploy MCP, flip release_state, or write prep records without human `cleared_by.name`.

            Escalate to Hicham for Released / marketplace promote.
            """
        ),
        encoding="utf-8",
    )
    (PLUGIN / "tools/README.md").write_text(
        textwrap.dedent(
            """\
            # Offline READY tools

            Non-generative CLIs mirroring MCP `mlr_*` tools. Run from this directory:

            ```bash
            python3 mlr_intake_offline.py --help
            python3 stamp_ready_line.py --skill mlr-intake --letter-lines
            ```

            Tests: `python3 -m unittest test_offline_tools -v`

            See plugin `references/mcp-opt-in.md` for optional live connectors.
            """
        ),
        encoding="utf-8",
    )


def main() -> None:
    write_templates()
    plugin_extras()
    for skill, meta in SKILL_META.items():
        skill_dir = SKILLS / skill
        (skill_dir / "governance.md").write_text(governance_root(skill, meta), encoding="utf-8")
        (skill_dir / "intake.md").write_text(intake_md(skill, meta), encoding="utf-8")
        ref = skill_dir / "references"
        ref.mkdir(exist_ok=True)
        (ref / "method.md").write_text(method_md(skill, meta), encoding="utf-8")
        (ref / "method-standards.md").write_text(METHOD_STANDARDS, encoding="utf-8")
        (ref / "knowledge.md").write_text(knowledge_md(skill, meta), encoding="utf-8")
        (ref / "failure-modes.md").write_text(failure_modes(skill, meta), encoding="utf-8")
        (ref / "tools.md").write_text(tools_md(skill, meta), encoding="utf-8")
        (ref / "without-connector.md").write_text(WITHOUT_CONNECTOR, encoding="utf-8")
        # keep references/governance.md aligned
        (ref / "governance.md").write_text(governance_root(skill, meta), encoding="utf-8")
        ex = skill_dir / "examples"
        ex.mkdir(exist_ok=True)
        (ex / "good-sourced-draft.md").write_text(good_draft(skill, meta), encoding="utf-8")
        (ex / meta["poor"]).write_text(poor_draft(skill, meta), encoding="utf-8")
        (skill_dir / "SKILL.md").write_text(skill_md(skill, meta), encoding="utf-8")
        patch_tasks(skill_dir, meta["tasks_template"])
        expand_evals(skill_dir, skill)
        known_answer(skill, meta)
    print("CF04 upgrade files written.")

FORCE_FLAG = "--force-overwrite-teh-fixes"


def _refuse_unless_forced() -> None:
    """Wholesale-rewrite guard (TEH-RDY-032): this script rewrites SKILL.md / references /
    examples wholesale and would overwrite the TEH fix-lane changes. It refuses unless the
    explicit flag is passed."""
    import sys as _sys

    if FORCE_FLAG not in _sys.argv[1:]:
        _sys.stderr.write(
            f"REFUSED: {Path(__file__).name} rewrites SKILL.md and references wholesale and would "
            f"overwrite the TEH fix-lane changes (TEH-RDY-012 to TEH-RDY-032). Run it only on the "
            f"owner's explicit instruction, with {FORCE_FLAG}. Nothing was written.\n"
        )
        raise SystemExit(2)
    _sys.argv.remove(FORCE_FLAG)


if __name__ == "__main__":
    _refuse_unless_forced()
    _refuse_unless_target_version(TARGET_VERSION, PLUGIN / ".claude-plugin" / "plugin.json")
    main()
