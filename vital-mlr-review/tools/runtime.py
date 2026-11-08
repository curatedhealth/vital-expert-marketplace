"""READY offline runtime — port of mcps/mlr_review/tools.py for the Cowork plugin.\n\nNon-generative. Never approves. Labels READY-local / not tool-checked / not metered.\nLive MCP remains optional for metering, cloud prep record, and VERIFY clearance.\n"""

from __future__ import annotations

import hashlib
import json
import re
import uuid
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path
from typing import Any

from contract import (
    AUDIENCES,
    CHAIRS,
    CHANNELS,
    CHAIR_DECISIONS,
    COUNTED_TOOLS,
    DISPLAY_NAME,
    FORBIDDEN_PHRASES,
    LIABILITY_LINE,
    METHOD_VERSION,
    MLR_STATUSES,
    PRODUCT,
    TOOL_NAMES,
)

_ROOT = Path(__file__).resolve().parent.parent  # plugin root
_RULESETS = _ROOT / "rulesets"
_SCHEMA_PATH = _ROOT / "schema" / "mlr-packet.schema.json"
# ready-sessions resolved at write time via Path.cwd()
_PREP: dict[str, dict[str, Any]] = {}

_DEPTH = {
    ("internal", "med_info"): "light",
    ("internal", "promo"): "short",
    ("hcp", "scientific_exchange"): "short",
    ("hcp", "promo"): "full",
    ("patient", "promo"): "full",
    ("payer", "promo"): "full",
}


def run_tool(tool: str, args: dict[str, Any] | None = None) -> dict[str, Any]:
    try:
        return _provenance(_dispatch(tool, args or {}))
    except (TypeError, ValueError) as exc:
        return _provenance(
            {
                "product": PRODUCT,
                "tool": tool,
                "ok": False,
                "gaps": [str(exc)[:240]],
                "liability_line": LIABILITY_LINE,
            }
        )


def _provenance(payload: dict[str, Any]) -> dict[str, Any]:
    out = dict(payload)
    out.setdefault("product", PRODUCT)
    out.setdefault("method_version", METHOD_VERSION)
    out.setdefault("liability_line", LIABILITY_LINE)
    out.setdefault("mode", "READY-local")
    out.setdefault("metered", False)
    if out.get("ok") is not False and "tool_checked" not in out:
        out.setdefault("tool_checked", False)
        out.setdefault("stamp_hint", "READY-local · not tool-checked · not metered")
    out["provenance"] = {
        "tool_id": out.get("tool") or out.get("tool_name"),
        "product": PRODUCT,
        "method_version": METHOD_VERSION,
        "server_time": datetime.now(timezone.utc).isoformat(),
        "capture_policy": "none",
        "transport": "offline-plugin",
    }
    return out


def _dispatch(tool: str, args: dict[str, Any]) -> dict[str, Any]:
    if tool not in TOOL_NAMES:
        raise ValueError(f"unknown tool: {tool}")
    if tool == "mlr_intake":
        return _intake(args)
    if tool == "mlr_list_rulesets":
        return _list_rulesets(args)
    if tool == "mlr_get_ruleset":
        return _get_ruleset(args)
    if tool == "mlr_get_packet_schema":
        return _packet_schema()
    if tool == "mlr_validate_packet":
        return _validate_packet(args)
    if tool == "mlr_align_claims":
        return _align_claims(args)
    if tool == "mlr_compile_checklist":
        return _compile_checklist(args)
    if tool == "mlr_handoff_verify":
        return _handoff_verify(args)
    if tool == "mlr_build_prep_record":
        return _build_prep_record(args)
    if tool == "my_usage":
        return {
            "tool": "my_usage",
            "display_name": DISPLAY_NAME,
            "plan": "unset",
            "cap": None,
            "remaining": None,
            "counted": False,
            "counted_tools": sorted(COUNTED_TOOLS),
            "gaps": ["Connect mint sets the design-partner cap (D5)."],
        }
    raise ValueError(f"unknown tool: {tool}")


@lru_cache(maxsize=1)
def _registry() -> dict[str, Any]:
    return json.loads((_RULESETS / "REGISTRY.json").read_text(encoding="utf-8"))


@lru_cache(maxsize=32)
def _load_pack(filename: str) -> dict[str, Any]:
    path = _RULESETS / filename
    if not path.is_file():
        raise ValueError(f"ruleset file missing: {filename}")
    raw = path.read_bytes()
    pack = json.loads(raw.decode("utf-8"))
    pack = dict(pack)
    pack["ruleset_hash"] = "sha256:" + hashlib.sha256(raw).hexdigest()
    return pack


def _norm_jurisdictions(args: dict[str, Any]) -> list[str]:
    raw = args.get("jurisdictions")
    if raw is None and args.get("jurisdiction"):
        raw = [args.get("jurisdiction")]
    if not isinstance(raw, list) or not raw:
        raise ValueError("jurisdictions required — no US (or other) default")
    out: list[str] = []
    for item in raw:
        code = str(item).strip().upper()
        if not code:
            continue
        if code not in out:
            out.append(code)
    if not out:
        raise ValueError("jurisdictions required — no US (or other) default")
    return out


def _coverage_for(jurisdiction: str, audience: str, channel: str) -> dict[str, Any]:
    packs = _registry().get("packs") or []
    match = None
    for row in packs:
        if (
            str(row.get("jurisdiction", "")).upper() == jurisdiction.upper()
            or (jurisdiction.upper() == "GLOBAL" and row.get("jurisdiction") == "global")
        ):
            if row.get("audience") == audience and row.get("channel") == channel:
                match = row
                break
    if match is None:
        # fall back to any pack for that jurisdiction + audience
        for row in packs:
            j = str(row.get("jurisdiction", ""))
            if j.upper() == jurisdiction.upper() or (jurisdiction.upper() == "GLOBAL" and j == "global"):
                if row.get("audience") == audience:
                    match = row
                    break
    if match is None:
        return {
            "jurisdiction": jurisdiction,
            "status": "missing",
            "ruleset_id": None,
            "authority_hints": [],
            "gap": f"[GAP] no ruleset catalogue row for {jurisdiction}/{audience}/{channel}",
        }
    return {
        "jurisdiction": jurisdiction,
        "status": match.get("status"),
        "ruleset_id": match.get("ruleset_id"),
        "authority_hints": match.get("authority_hints") or [],
        "gap": None
        if match.get("status") == "full"
        else f"[GAP] stub pack {match.get('ruleset_id')} — checklist not authored",
    }


def _intake(args: dict[str, Any]) -> dict[str, Any]:
    jurisdictions = _norm_jurisdictions(args)
    audience = str(args.get("audience") or "").strip().lower()
    channel = str(args.get("channel") or "").strip().lower()
    missing: list[str] = []
    if audience not in AUDIENCES:
        missing.append("audience")
        audience = audience or ""
    if channel not in CHANNELS:
        missing.append("channel")
        channel = channel or ""
    body = args.get("body")
    artefact_id = args.get("artefact_id")
    if not body and not artefact_id:
        missing.append("body_or_artefact_id")
    artefact_version = str(args.get("artefact_version") or "").strip()
    if not artefact_version:
        missing.append("artefact_version")

    coverage = []
    if audience in AUDIENCES and channel in CHANNELS:
        coverage.append(_coverage_for("global", audience, channel))
        for j in jurisdictions:
            coverage.append(_coverage_for(j, audience, channel))

    depth = _DEPTH.get((audience, channel), "full" if channel == "promo" else "short")
    context = {
        "artefact_id": artefact_id or str(uuid.uuid4()),
        "artefact_version": artefact_version or None,
        "content_hash": args.get("content_hash"),
        "jurisdictions": jurisdictions,
        "audience": audience or None,
        "channel": channel or None,
        "product_name": args.get("product_name"),
        "authorized_use_by_jurisdiction": args.get("authorized_use_by_jurisdiction"),
        "authorized_use_text": args.get("authorized_use_text"),
        "company_sop_ref": args.get("company_sop_ref"),
        "body_present": bool(body),
    }
    if isinstance(context["authorized_use_by_jurisdiction"], dict) is False and context.get(
        "authorized_use_text"
    ):
        if len(jurisdictions) == 1:
            context["authorized_use_by_jurisdiction"] = {
                jurisdictions[0]: {"text": str(args.get("authorized_use_text"))}
            }

    return {
        "tool": "mlr_intake",
        "ok": not missing,
        "context": context,
        "missing_fields": missing,
        "suggested_depth": depth,
        "ruleset_coverage": coverage,
        "notes": args.get("notes"),
        "next": "Call mlr_get_ruleset with the same jurisdictions, audience, and channel.",
    }


def _list_rulesets(args: dict[str, Any]) -> dict[str, Any]:
    j_filter = str(args.get("jurisdiction") or "").strip().upper() or None
    audience = str(args.get("audience") or "").strip().lower() or None
    channel = str(args.get("channel") or "").strip().lower() or None
    status = str(args.get("status") or "any").strip().lower()
    rows = []
    for row in _registry().get("packs") or []:
        if j_filter and str(row.get("jurisdiction", "")).upper() not in {j_filter, "GLOBAL"}:
            if not (j_filter == "GLOBAL" and row.get("jurisdiction") == "global"):
                if str(row.get("jurisdiction", "")).upper() != j_filter:
                    continue
        if audience and row.get("audience") != audience:
            continue
        if channel and row.get("channel") != channel:
            continue
        if status != "any" and row.get("status") != status:
            continue
        rows.append(
            {
                "ruleset_id": row.get("ruleset_id"),
                "jurisdiction": row.get("jurisdiction"),
                "audience": row.get("audience"),
                "channel": row.get("channel"),
                "status": row.get("status"),
                "authority_hints": row.get("authority_hints") or [],
                "ruleset_hash": None
                if row.get("status") != "full" or not row.get("file")
                else _load_pack(row["file"]).get("ruleset_hash"),
            }
        )
    return {"tool": "mlr_list_rulesets", "ok": True, "counted": False, "packs": rows}


def _find_registry_row(jurisdiction: str, audience: str, channel: str) -> dict[str, Any] | None:
    want_global = str(jurisdiction).lower() == "global"
    for row in _registry().get("packs") or []:
        rj = str(row.get("jurisdiction") or "")
        if want_global:
            if rj.lower() != "global":
                continue
        elif rj.upper() != str(jurisdiction).upper():
            continue
        if row.get("audience") == audience and row.get("channel") == channel:
            return row
    return None


def _get_ruleset(args: dict[str, Any]) -> dict[str, Any]:
    audience = str(args.get("audience") or "").strip().lower()
    channel = str(args.get("channel") or "").strip().lower()
    if audience not in AUDIENCES or channel not in CHANNELS:
        raise ValueError("audience and channel required")

    pin = args.get("ruleset_id") or args.get("ruleset_ids")
    jurisdictions: list[str]
    if pin:
        pins = pin if isinstance(pin, list) else [pin]
        jurisdictions = []
        packs_meta = []
        for rid in pins:
            row = next((r for r in _registry()["packs"] if r.get("ruleset_id") == rid), None)
            if not row:
                raise ValueError(f"unknown ruleset_id: {rid}")
            packs_meta.append(row)
            jurisdictions.append(str(row.get("jurisdiction")))
    else:
        jurisdictions = _norm_jurisdictions(args)

    # Always layer global when a global pack exists for audience/channel
    ordered: list[str] = []
    if "global" not in {j.lower() for j in jurisdictions}:
        ordered.append("global")
    for j in jurisdictions:
        if j.lower() != "global" and j not in ordered:
            ordered.append(j)

    applied: list[dict[str, Any]] = []
    coverage: list[dict[str, Any]] = []
    chairs: dict[str, list[dict[str, Any]]] = {c: [] for c in CHAIRS}
    forbidden: list[str] = list(FORBIDDEN_PHRASES)

    for j in ordered:
        row = _find_registry_row(j, audience, channel)
        cov = _coverage_for(j if j.lower() != "global" else "global", audience, channel)
        coverage.append(cov)
        if not row or row.get("status") != "full" or not row.get("file"):
            continue
        pack = _load_pack(row["file"])
        applied.append(
            {
                "ruleset_id": pack.get("ruleset_id"),
                "jurisdiction": pack.get("jurisdiction"),
                "ruleset_hash": pack.get("ruleset_hash"),
            }
        )
        for phrase in pack.get("forbidden_output_phrases") or []:
            if phrase not in forbidden:
                forbidden.append(phrase)
        for chair in CHAIRS:
            for rule in (pack.get("chairs") or {}).get(chair) or []:
                item = dict(rule)
                item.setdefault("applies_to", [pack.get("jurisdiction")])
                chairs[chair].append(item)

    if not applied:
        raise ValueError(
            "no full ruleset loaded for requested markets — see coverage gaps; "
            "never substitute another country's pack"
        )

    return {
        "tool": "mlr_get_ruleset",
        "ok": True,
        "jurisdictions": [j for j in ordered if j.lower() != "global"]
        or jurisdictions,
        "ruleset_ids": [a["ruleset_id"] for a in applied],
        "also_applied": applied,
        "coverage": coverage,
        "chairs": chairs,
        "forbidden_output_phrases": forbidden,
        "retrieved_at": datetime.now(timezone.utc).date().isoformat(),
    }


def _packet_schema() -> dict[str, Any]:
    schema = json.loads(_SCHEMA_PATH.read_text(encoding="utf-8"))
    return {
        "tool": "mlr_get_packet_schema",
        "ok": True,
        "counted": False,
        "schema": schema,
    }


def _scan_forbidden(text: str) -> list[str]:
    hits = []
    lower = text.lower()
    for phrase in FORBIDDEN_PHRASES:
        if phrase in lower:
            hits.append(phrase)
    return hits


def _walk_strings(obj: Any) -> list[str]:
    if isinstance(obj, str):
        return [obj]
    if isinstance(obj, dict):
        out: list[str] = []
        for v in obj.values():
            out.extend(_walk_strings(v))
        return out
    if isinstance(obj, list):
        out = []
        for v in obj:
            out.extend(_walk_strings(v))
        return out
    return []


def _validate_packet(args: dict[str, Any]) -> dict[str, Any]:
    packet = args.get("packet") or args.get("compile") or args
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(packet, dict):
        raise ValueError("packet object required")

    chairs = packet.get("chairs")
    if not isinstance(chairs, dict):
        errors.append("chairs object required")
        chairs = {}

    versions = []
    for name in CHAIRS:
        chair = chairs.get(name)
        if not isinstance(chair, dict):
            errors.append(f"missing chair: {name}")
            continue
        ver = str(chair.get("artefact_version") or "")
        versions.append(ver)
        if not ver:
            errors.append(f"{name}: artefact_version required")
        decision = chair.get("decision")
        if decision not in CHAIR_DECISIONS:
            errors.append(f"{name}: invalid decision")
        for finding in chair.get("findings") or []:
            if not isinstance(finding, dict):
                continue
            if finding.get("fail_close") and decision == "approve":
                # allow ruleset fail_close on finding via severity critical + flag
                pass
            if finding.get("fail_close") is True and decision == "approve":
                errors.append(f"{name}: fail_close finding with decision approve → human_gate_required")
            # also check rule metadata if present
            if finding.get("severity") == "critical" and decision == "approve":
                warnings.append(f"{name}: critical finding with approve — expect human_gate_required")

    if versions and len(set(versions)) > 1:
        errors.append("artefact_version mismatch across chairs")

    jurisdictions = packet.get("jurisdictions") or []
    if not jurisdictions:
        errors.append("jurisdictions required on compile packet")

    ruleset_ids = packet.get("ruleset_ids") or []
    if not ruleset_ids:
        warnings.append("ruleset_ids empty")

    for text in _walk_strings(packet):
        for hit in _scan_forbidden(text):
            errors.append(f"forbidden phrase: {hit}")

    # fail_close from findings that carry the flag
    force_gate = False
    for name in CHAIRS:
        chair = chairs.get(name) if isinstance(chairs, dict) else None
        if not isinstance(chair, dict):
            continue
        for finding in chair.get("findings") or []:
            if isinstance(finding, dict) and finding.get("fail_close") is True:
                if chair.get("decision") == "approve":
                    force_gate = True
                    if f"{name}: fail_close" not in " ".join(errors):
                        errors.append(
                            f"{name}: fail_close finding cannot stay approve — use revise/reject or human_gate"
                        )

    status = packet.get("mlr_status")
    if status and status not in MLR_STATUSES:
        errors.append("invalid mlr_status")

    # Stub coverage honesty
    for j in jurisdictions:
        # if ruleset_ids only US while DE requested — warn
        pass

    liab = packet.get("liability_line")
    if liab and liab != LIABILITY_LINE:
        warnings.append("liability_line should use the canonical constant")

    ok = not errors
    if ok:
        if force_gate:
            status = "human_gate_required"
        elif not status:
            # derive
            decisions = [
                chairs[c].get("decision")
                for c in CHAIRS
                if isinstance(chairs.get(c), dict)
            ]
            if any(d == "revise" for d in decisions):
                status = "revise"
            elif any(d in {"reject", "abstain"} for d in decisions):
                status = "human_gate_required"
            else:
                status = "prep_complete"
    else:
        status = status if status in MLR_STATUSES else "findings_only"

    normalised = dict(packet)
    normalised["mlr_status"] = status
    normalised["liability_line"] = LIABILITY_LINE
    if versions and len(set(versions)) == 1:
        normalised["artefact_version"] = versions[0]

    return {
        "tool": "mlr_validate_packet",
        "ok": ok,
        "mlr_status": status,
        "errors": errors,
        "warnings": warnings,
        "normalised_packet": normalised,
    }


def _tokenize(text: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9]+", text.lower()) if len(t) > 2}


def _align_claims(args: dict[str, Any]) -> dict[str, Any]:
    claims = args.get("claims") or []
    if not isinstance(claims, list) or not claims:
        raise ValueError("claims[] required")
    jurisdictions = _norm_jurisdictions(args) if args.get("jurisdictions") or args.get("jurisdiction") else []
    by_j = args.get("authorized_use_by_jurisdiction")
    if not isinstance(by_j, dict):
        by_j = {}
    single = args.get("authorized_use_text")
    if single and len(jurisdictions) == 1:
        by_j = {jurisdictions[0]: {"text": str(single)}}
    if not jurisdictions:
        jurisdictions = list(by_j.keys()) or ["UNKNOWN"]
    results = []
    for claim in claims:
        claim_text = claim if isinstance(claim, str) else str(claim.get("text") or claim.get("claim") or "")
        ctoks = _tokenize(claim_text)
        for j in jurisdictions:
            entry = by_j.get(j) or by_j.get(j.upper()) or by_j.get(j.lower())
            text = ""
            if isinstance(entry, dict):
                text = str(entry.get("text") or "")
            elif isinstance(entry, str):
                text = entry
            if not text.strip():
                results.append(
                    {
                        "claim": claim_text,
                        "jurisdiction": j,
                        "label": "gap",
                        "rationale_code": "authorized_use_missing",
                    }
                )
                continue
            atoks = _tokenize(text)
            if not ctoks:
                results.append(
                    {
                        "claim": claim_text,
                        "jurisdiction": j,
                        "label": "gap",
                        "rationale_code": "empty_claim",
                    }
                )
                continue
            overlap = len(ctoks & atoks) / max(len(ctoks), 1)
            # Heuristic labels only — host must still judge
            exceeds_markers = ("superior", "best", "only", "cure", "guaranteed", "off-label")
            lower = claim_text.lower()
            if any(m in lower for m in exceeds_markers) and not any(m in text.lower() for m in exceeds_markers):
                label = "exceeds"
                code = "claim_stronger_than_authorized_use"
            elif overlap >= 0.35:
                label = "matches"
                code = "token_overlap_with_authorized_use"
            elif overlap > 0:
                label = "no_authorization"
                code = "weak_overlap"
            else:
                label = "no_authorization"
                code = "no_overlap"
            results.append(
                {
                    "claim": claim_text,
                    "jurisdiction": j,
                    "label": label,
                    "rationale_code": code,
                }
            )
    return {
        "tool": "mlr_align_claims",
        "ok": True,
        "results": results,
        "note": "Labels are structural heuristics against supplied authorized-use text — not medical or legal clearance.",
    }


def _compile_checklist(args: dict[str, Any]) -> dict[str, Any]:
    chairs = args.get("chairs") or {}
    jurisdictions = args.get("jurisdictions") or []
    if not isinstance(chairs, dict):
        raise ValueError("chairs object required")
    slots = []
    decisions = {}
    for name in CHAIRS:
        chair = chairs.get(name)
        if not isinstance(chair, dict):
            slots.append(
                {
                    "topic": f"missing_{name}",
                    "chairs_disagree": True,
                    "markets_disagree": False,
                    "detail": f"Chair packet missing: {name}",
                }
            )
            continue
        decisions[name] = chair.get("decision")
    if len(set(decisions.values())) > 1:
        slots.append(
            {
                "topic": "chair_decisions",
                "chairs_disagree": True,
                "markets_disagree": False,
                "detail": f"Decisions differ: {decisions}",
            }
        )
    # Market disagreement: same claim_span with different severities across applies_to
    by_span: dict[str, list[dict[str, Any]]] = {}
    for name in CHAIRS:
        chair = chairs.get(name)
        if not isinstance(chair, dict):
            continue
        for finding in chair.get("findings") or []:
            if not isinstance(finding, dict):
                continue
            span = str(finding.get("claim_span") or "").strip()
            if not span:
                continue
            by_span.setdefault(span, []).append({"chair": name, **finding})
    for span, items in by_span.items():
        markets = set()
        sevs = set()
        for item in items:
            for m in item.get("applies_to") or []:
                markets.add(str(m))
            sevs.add(item.get("severity"))
        if len(markets) > 1 and len(sevs) > 1:
            slots.append(
                {
                    "topic": "cross_market_severity",
                    "chairs_disagree": len({i["chair"] for i in items}) > 1,
                    "markets_disagree": True,
                    "detail": f"Span differs by market/severity: {span[:120]}",
                }
            )
    return {
        "tool": "mlr_compile_checklist",
        "ok": True,
        "jurisdictions": jurisdictions,
        "conflict_slots": slots,
        "note": "Host skill writes conflict narrative into empty slots — server does not invent synthesis.",
    }


def _handoff_verify(args: dict[str, Any]) -> dict[str, Any]:
    packet = args.get("packet") or args.get("compile") or {}
    claims = args.get("claims") or []
    if not claims and isinstance(packet, dict):
        for name in CHAIRS:
            chair = (packet.get("chairs") or {}).get(name) or {}
            for finding in chair.get("findings") or []:
                if isinstance(finding, dict) and finding.get("claim_span"):
                    claims.append(finding["claim_span"])
    steps = [
        {
            "order": 1,
            "connector": "verify",
            "tool": "qualify_source",
            "instruction": "For each URL or document id, call qualify_source with the user question.",
        },
        {
            "order": 2,
            "connector": "verify",
            "tool": "check_claim",
            "instruction": "For each claim, call check_claim with the admitted source object plus a quoted passage.",
        },
        {
            "order": 3,
            "connector": "verify",
            "tool": "build_citation",
            "instruction": "Optional. Free. Build citation lines for admitted sources.",
        },
        {
            "order": 4,
            "connector": "verify",
            "tool": "build_record",
            "instruction": "Optional. Requires human cleared_by.name. Never simulate VERIFY statuses without tools.",
        },
    ]
    return {
        "tool": "mlr_handoff_verify",
        "ok": True,
        "counted": False,
        "called_verify": False,
        "claims_for_host": claims,
        "steps": steps,
        "handoff": {
            "product": "verify",
            "key_prefix": "vvfy_",
            "url": "https://mcp.vital.expert/api/mcp/verify",
        },
        "verify_url": "https://mcp.vital.expert/api/mcp/verify",
        "note": "Host-mediated. Use vvfy_ on the Verify connector — do not add a second Verify server.",
    }


def _build_prep_record(args: dict[str, Any]) -> dict[str, Any]:
    packet = args.get("packet") or args.get("compile")
    if not isinstance(packet, dict):
        raise ValueError("packet required")
    validation = _validate_packet({"packet": packet})
    if not validation.get("ok"):
        return {
            "tool": "mlr_build_prep_record",
            "ok": False,
            "status": "draft",
            "errors": validation.get("errors"),
            "record": None,
        }
    cleared = args.get("cleared_by") or {}
    name = ""
    if isinstance(cleared, dict):
        name = str(cleared.get("name") or "").strip()
    elif isinstance(cleared, str):
        name = cleared.strip()
        cleared = {"name": name}
    if not name:
        return {
            "tool": "mlr_build_prep_record",
            "ok": False,
            "status": "draft",
            "errors": ["cleared_by.name required — a named human must own the prep record"],
            "record": None,
        }
    # MLR-H5: refuse AI / model / assistant / system as cleared_by
    blocked = (
        "chatgpt",
        "claude",
        "assistant",
        "gpt",
        "model",
        "system",
        "ai reviewer",
        "copilot",
        "gemini",
        "llm",
    )
    low = name.lower()
    if any(b == low or b in low.split() or low.startswith(b) for b in blocked) or low in blocked:
        return {
            "tool": "mlr_build_prep_record",
            "ok": False,
            "status": "draft",
            "errors": [
                "cleared_by must be a named human — refuse AI/model/assistant/system (MLR-H5)"
            ],
            "record": None,
        }
    status = "prep_cleared_for_human_mlr"
    record_id = str(uuid.uuid4())
    record = {
        "record_id": record_id,
        "artefact_version": validation["normalised_packet"].get("artefact_version"),
        "compile": validation["normalised_packet"],
        "cleared_by": cleared,
        "purpose": args.get("purpose"),
        "status": status,
        "mlr_reviewed": False,
        "jurisdictions": validation["normalised_packet"].get("jurisdictions"),
        "ruleset_ids": validation["normalised_packet"].get("ruleset_ids"),
        "retention_note": "In-memory on this host process until durable store ships; target 90-day tenant retention.",
    }
    _PREP[record_id] = record
    # Offline durable write (local workspace). Never claims approval.
    sessions = Path.cwd() / "ready-sessions"
    sessions.mkdir(parents=True, exist_ok=True)
    out_path = sessions / f"{record_id}.ready.json"
    out_path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {
        "tool": "mlr_build_prep_record",
        "ok": True,
        "status": status,
        "record": record,
        "local_path": str(out_path),
        "mode": "READY-local",
        "metered": False,
        "note": "prep_cleared_for_human_mlr means ready for human MLR — not approved for use. Written locally; not metered.",
    }
