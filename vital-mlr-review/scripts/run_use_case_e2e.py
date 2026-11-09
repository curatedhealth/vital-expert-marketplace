#!/usr/bin/env python3
"""Offline E2E: registry integrity + probes + DE/CH journey + workflows + meter.

Exit 0 only if all hard checks PASS. Runs on behalf of the operator without a host LLM.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

PLUGIN = Path(__file__).resolve().parents[1]
TOOLS = PLUGIN / "tools"
REGISTRY = PLUGIN / "evals" / "USE_CASE_REGISTRY.json"
sys.path.insert(0, str(TOOLS))

from channel_intent_gate import gate  # noqa: E402
from check_isi_presence import scan  # noqa: E402
from check_submission_pack import check  # noqa: E402
from contract import FORBIDDEN_PHRASES, LIABILITY_LINE  # noqa: E402
from runtime import run_tool  # noqa: E402


def fail(msg: str, fails: list[str]) -> None:
    fails.append(msg)


def run_journey(name: str, fails: list[str]) -> None:
    if name == "de_ch_offline_prep":
        intake = run_tool(
            "mlr_intake",
            {
                "jurisdictions": ["DE", "CH"],
                "audience": "hcp",
                "channel": "promo",
                "artefact_version": "v0.9",
                "body": "Once-daily oral. HbA1c claim synthetic.",
                "authorized_use_by_jurisdiction": {
                    "DE": {"text": "Indiziert fuer Erwachsene mit Typ-2-Diabetes. Einmal taeglich."},
                    "CH": {"text": "Indiziert zur Behandlung von Erwachsenen mit Typ-2-Diabetes."},
                },
            },
        )
        if not intake.get("ok"):
            fail(f"journey intake: {intake.get('gaps')}", fails)
        listed = run_tool("mlr_list_rulesets", {"audience": "hcp", "channel": "promo"})
        if not listed.get("ok"):
            fail("journey list_rulesets", fails)
        g = gate(
            {
                "channel": "promo",
                "proactive_or_reactive": "proactive",
                "offlabel_or_unlicensed": "no",
                "body": "prescribe once daily",
            }
        )
        if g.get("decision") != "treat_as_promo":
            fail(f"journey channel expected treat_as_promo got {g.get('decision')}", fails)
        align = run_tool(
            "mlr_align_claims",
            {
                "jurisdictions": ["DE"],
                "authorized_use_text": "Indicated for adults. Once daily oral.",
                "claims": ["Once-daily oral dosing", "superior efficacy guaranteed"],
            },
        )
        if not align.get("ok"):
            fail("journey align", fails)
        compile_ = run_tool(
            "mlr_compile_checklist",
            {
                "jurisdictions": ["DE", "CH"],
                "chairs": {
                    "medical": {"decision": "revise", "findings": []},
                    "legal": {"decision": "revise", "findings": []},
                    "regulatory": {"decision": "revise", "findings": []},
                },
            },
        )
        if not compile_.get("ok"):
            fail("journey compile", fails)
        packet = {
            "jurisdictions": ["DE", "CH"],
            "ruleset_ids": ["mlr-de-hcp-promo-v0"],
            "artefact_version": "v0.9.1",
            "mlr_status": "findings_only",
            "liability_line": LIABILITY_LINE,
            "chairs": {
                "medical": {
                    "chair": "medical",
                    "decision": "revise",
                    "artefact_version": "v0.9.1",
                    "findings": [],
                    "summary": "m",
                },
                "legal": {
                    "chair": "legal",
                    "decision": "revise",
                    "artefact_version": "v0.9.1",
                    "findings": [],
                    "summary": "l",
                },
                "regulatory": {
                    "chair": "regulatory",
                    "decision": "revise",
                    "artefact_version": "v0.9.1",
                    "findings": [],
                    "summary": "r",
                },
            },
        }
        with tempfile.TemporaryDirectory() as tmp:
            os.chdir(tmp)
            bad = run_tool("mlr_build_prep_record", {"packet": packet, "cleared_by": {"name": "Assistant"}})
            if bad.get("ok"):
                fail("journey must refuse AI cleared_by", fails)
            ok = run_tool(
                "mlr_build_prep_record",
                {"packet": packet, "cleared_by": {"name": "Jordan Lee"}},
            )
            if not ok.get("ok"):
                fail(f"journey prep human: {ok}", fails)
            else:
                data = json.loads(Path(ok["local_path"]).read_text(encoding="utf-8"))
                if data.get("mlr_reviewed") is not False:
                    fail("journey prep mlr_reviewed must be false", fails)
        return

    if name == "channel_gate_then_stop":
        g = gate(
            {
                "channel": "scientific_exchange",
                "proactive_or_reactive": "proactive",
                "offlabel_or_unlicensed": "yes",
                "body": "pipeline efficacy prescribe",
            }
        )
        if g.get("decision") != "human_gate_required":
            fail(f"channel journey decision {g.get('decision')}", fails)
        return

    if name == "approval_pressure":
        # Structural: forbidden phrases must remain configured; stamp must never emit them
        proc = subprocess.run(
            [sys.executable, str(TOOLS / "stamp_ready_line.py"), "--skill", "mlr-intake", "--status", "findings_only"],
            capture_output=True,
            text=True,
            check=False,
        )
        low = (proc.stdout + proc.stderr).lower()
        for ph in FORBIDDEN_PHRASES:
            if ph in low:
                fail(f"stamp emitted forbidden {ph}", fails)
        if "approved for use" in low or "mlr_reviewed" in low:
            fail("stamp clearance language", fails)
        return

    if name == "refuse_2253":
        bad = check({"audience": "hcp", "channel": "promo", "form_2253_filed": True})
        if bad.get("ok"):
            fail("2253 journey should not ok", fails)
        return

    if name == "verify_then_compile":
        handoff = run_tool("mlr_handoff_verify", {"claims": ["Lowers HbA1c by 1.2% at week 24"]})
        if not handoff.get("ok") or handoff.get("called_verify"):
            fail("verify journey handoff", fails)
        compile_ = run_tool(
            "mlr_compile_checklist",
            {
                "jurisdictions": ["DE"],
                "chairs": {
                    "medical": {"decision": "revise", "findings": [{"id": "omit"}]},
                    "legal": {"decision": "revise", "findings": []},
                    "regulatory": {"decision": "revise", "findings": []},
                },
            },
        )
        if not compile_.get("ok"):
            fail("verify journey compile", fails)
        return

    fail(f"unknown journey {name}", fails)


def _dig(obj: object, dotted: str) -> object:
    for part in dotted.split("."):
        obj = obj.get(part) if isinstance(obj, dict) else None
    return obj


def run_input_steps(case: dict, probe: dict, fails: list[str]) -> None:
    """Probe steps fed by the case's person-supplied input (TEH-RDY-020)."""
    cid = case["id"]
    inp = case.get("inputs") or {}
    path = PLUGIN / str(inp.get("path") or "")
    if not inp.get("path") or not path.is_file():
        fail(f"{cid} supplied input file missing: {inp.get('path')!r}", fails)
        return
    supplied = json.loads(path.read_text(encoding="utf-8"))
    if json.loads(inp.get("text") or "null") != supplied:
        fail(f"{cid} registry input text differs from {inp['path']} — rerun the builder", fails)
    try:
        home = os.getcwd()
    except FileNotFoundError:  # an earlier journey may have left a removed temp folder as cwd
        home = str(PLUGIN)
    with tempfile.TemporaryDirectory() as tmp:
        os.chdir(tmp)  # the prep-record tool writes ready-sessions/ under the working folder
        try:
            for i, step in enumerate(probe["steps"], 1):
                data = json.loads(json.dumps(supplied))
                for key in step.get("drop_keys") or []:
                    data.pop(key, None)
                args = dict(data) if step.get("input_as") == "args" else {step["input_as"]: data}
                args.update(step.get("args") or {})
                out = run_tool(step["tool"], args)
                tag = f"{cid} step {i} {step['tool']}"
                want = step.get("assert_ok")
                if want is True and not out.get("ok"):
                    fail(f"{tag} expected ok: {out.get('errors') or out.get('gaps')}", fails)
                    continue
                if want is False and out.get("ok"):
                    fail(f"{tag} expected fail", fails)
                if "expect_status" in step:
                    got = out.get("mlr_status")
                    if got != step["expect_status"]:
                        fail(f"{tag} status {got!r} != expected {step['expect_status']!r}", fails)
                for dotted, expected in (step.get("expect_record") or {}).items():
                    got = _dig(out.get("record"), dotted)
                    if got != expected:
                        fail(f"{tag} record.{dotted}={got!r} != {expected!r}", fails)
        finally:
            os.chdir(home)


def run_probe(case: dict, fails: list[str]) -> None:
    probe = case.get("offline_probe")
    if not probe:
        return
    cid = case["id"]
    if "steps" in probe:
        run_input_steps(case, probe, fails)
        return
    if "journey" in probe:
        run_journey(probe["journey"], fails)
        return
    if "tool" in probe:
        out = run_tool(probe["tool"], probe.get("args") or {})
        want = probe.get("assert_ok")
        if want is True and not out.get("ok"):
            fail(f"{cid} tool {probe['tool']} expected ok: {out.get('gaps') or out.get('errors')}", fails)
        if want is False and out.get("ok"):
            fail(f"{cid} tool {probe['tool']} expected fail", fails)
        return
    if probe.get("module") == "channel_intent_gate":
        out = gate(probe.get("args") or {})
        if "expect_decision" in probe and out.get("decision") != probe["expect_decision"]:
            fail(f"{cid} channel decision {out.get('decision')}", fails)
        if "expect_decision_in" in probe and out.get("decision") not in probe["expect_decision_in"]:
            fail(f"{cid} channel decision {out.get('decision')} not in {probe['expect_decision_in']}", fails)
        return
    if probe.get("module") == "check_isi_presence":
        out = scan(probe["args"]["text"])
        if probe.get("expect_isi") and not out.get("isi_markers_found"):
            fail(f"{cid} ISI markers missing", fails)
        return
    if probe.get("module") == "check_submission_pack":
        out = check(probe.get("args") or {})
        want = probe.get("assert_ok")
        if want is False and out.get("ok"):
            fail(f"{cid} submission expected fail", fails)
        if want is True and not out.get("ok"):
            fail(f"{cid} submission expected ok", fails)
        return
    fail(f"{cid} unknown probe", fails)


def _skill_meta_version(skill_md: Path) -> str | None:
    """metadata.version from SKILL.md front matter (no yaml dependency)."""
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    front = text.split("---", 2)[1]
    m = re.search(r"^  version:\s*\"?([^\"\n]+?)\"?\s*$", front, re.MULTILINE)
    return m.group(1).strip() if m else None


def _version_labels() -> list[tuple[str, object]]:
    labels: list[tuple[str, object]] = []
    for rel in ("evals/suite-evals.json", "evals/USE_CASE_REGISTRY.json", "hooks/routing-hints.json"):
        path = PLUGIN / rel
        if path.is_file():
            labels.append((rel, json.loads(path.read_text(encoding="utf-8")).get("version")))
        else:
            labels.append((rel, "<missing file>"))
    for skill_dir in sorted(p for p in (PLUGIN / "skills").iterdir() if p.is_dir()):
        labels.append((f"skills/{skill_dir.name}/SKILL.md metadata.version", _skill_meta_version(skill_dir / "SKILL.md")))
        ev = skill_dir / "evals" / "evals.json"
        if ev.is_file():
            labels.append((f"skills/{skill_dir.name}/evals/evals.json", json.loads(ev.read_text(encoding="utf-8")).get("version")))
    return labels


def main() -> int:
    fails: list[str] = []
    if not REGISTRY.is_file():
        print("FAIL: missing USE_CASE_REGISTRY.json — run evals/build_use_case_registry.py")
        return 1
    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    cases = reg["cases"]
    if len(cases) < 60:
        fail(f"registry count {len(cases)} < 60", fails)
    skills = {c["skill"] for c in cases if c["skill"] != "journey"}
    expected_skills = {
        "mlr-capability-map",
        "mlr-intake",
        "mlr-channel-intent",
        "mlr-claims-matrix",
        "mlr-fair-balance-isi",
        "mlr-medical-chair",
        "mlr-legal-chair",
        "mlr-regulatory-chair",
        "mlr-compile",
        "mlr-verify-handoff",
        "mlr-board-prep",
    }
    if skills != expected_skills:
        fail(f"skill set mismatch {skills ^ expected_skills}", fails)

    # per-skill daily sync
    for skill in expected_skills:
        ev = json.loads((PLUGIN / "skills" / skill / "evals" / "evals.json").read_text(encoding="utf-8"))
        daily = ev.get("daily_user_evals") or []
        if len(daily) < 5:
            fail(f"{skill} daily_user_evals={len(daily)} < 5", fails)
        if len(ev.get("should_trigger") or []) < 10:
            fail(f"{skill} should_trigger < 10", fails)
        if len(ev.get("must_refuse") or []) < 1:
            fail(f"{skill} missing must_refuse", fails)

    # Hybrid B empty mcp
    mcp = json.loads((PLUGIN / ".mcp.json").read_text(encoding="utf-8"))
    if mcp != {}:
        fail(f".mcp.json not empty Hybrid B: {mcp}", fails)

    # Version is read from plugin.json itself (no hard pin); it must be a
    # well-formed semver string. release_state must be a known pilot-or-later state.
    pj = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    version = pj.get("version")
    if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version):
        fail(f"plugin.json version missing or not semver: {version!r}", fails)
    allowed_states = {"Pilot", "Back-tested", "Released"}
    if pj.get("release_state") not in allowed_states:
        fail(f"release_state {pj.get('release_state')!r} not in {sorted(allowed_states)}", fails)

    # Version agreement (TEH-RDY-010): every version label the pack carries must equal
    # plugin.json — suite evals, the use-case registry, the routing-hint table, and each
    # skill's SKILL.md metadata.version and evals/evals.json version.
    for label, value in _version_labels():
        if value != version:
            fail(f"version mismatch: {label}={value!r} != plugin.json {version!r}", fails)

    # workflows exist
    for name in (
        "offline-prep-e2e.md",
        "claims-first-pre-review.md",
        "scientific-exchange-gate.md",
        "reconcile-after-findings.md",
        "post-clearance-human-ops-deferred.md",
    ):
        if not (PLUGIN / "workflows" / name).is_file():
            fail(f"missing workflow {name}", fails)

    # templates exist
    for name in (
        "intake-card.md",
        "channel-intent-card.md",
        "claims-matrix-card.md",
        "isi-fair-balance-checklist.md",
        "medical-finding-card.md",
        "legal-finding-card.md",
        "regulatory-finding-card.md",
        "prep-record.md",
        "check-line-stamp.md",
    ):
        if not (PLUGIN / "templates" / name).is_file():
            fail(f"missing template {name}", fails)

    # probes
    for case in cases:
        run_probe(case, fails)

    # meter
    meter = subprocess.run(
        [sys.executable, str(PLUGIN / "scripts" / "world_class_meter.py")],
        capture_output=True,
        text=True,
        check=False,
    )
    if meter.returncode != 0:
        fail("world_class_meter FAIL\n" + meter.stdout[-500:], fails)

    # unit tests
    for test in ("test_offline_tools.py", "test_world_class_meter.py"):
        proc = subprocess.run(
            [sys.executable, str(TOOLS / test)],
            cwd=str(TOOLS),
            capture_output=True,
            text=True,
            check=False,
        )
        if proc.returncode != 0:
            fail(f"{test} FAIL\n{proc.stdout[-400:]}\n{proc.stderr[-400:]}", fails)

    print(f"READY use-case E2E — cases={len(cases)} version={pj.get('version')} release_state={pj.get('release_state')}")
    if fails:
        print(f"FAIL ({len(fails)}):")
        for f in fails:
            print(" -", f)
        return 1
    print("PASS all registry + probe + journey + meter + unit gates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
