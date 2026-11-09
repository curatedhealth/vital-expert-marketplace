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
    INTENTS,
    split_channel,
    CHAIR_DECISIONS,
    COUNTED_TOOLS,
    DISPLAY_NAME,
    FORBIDDEN_PATTERNS,
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


def _no_pack_for_channel(jurisdiction: str, audience: str, channel: str) -> str:
    """Specific coverage gap when no catalogue pack matches market + audience + intent (TEH-RDY-052).

    `channel` here is the rule-pack catalogue key: the communication intent (TEH-RDY-057)."""
    where = "global" if jurisdiction.upper() == "GLOBAL" else jurisdiction
    for row in _registry().get("packs") or []:
        j = str(row.get("jurisdiction", ""))
        if (j.upper() == jurisdiction.upper()) and row.get("audience") == audience:
            return f"[GAP] no rule pack for intent {channel} in {where}"
    return f"[GAP] no ruleset catalogue row for {jurisdiction}/{audience}/{channel}"


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
        # TEH-RDY-052: never substitute a pack for another intent. A pack for the same market and
        # audience but a different intent is not coverage — report the specific gap instead.
        return {
            "jurisdiction": jurisdiction,
            "status": "missing",
            "ruleset_id": None,
            "authority_hints": [],
            "gap": _no_pack_for_channel(jurisdiction, audience, channel),
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


def _channel_notes(split: dict[str, Any] | None) -> str:
    """Report the intent/medium split back to the person (TEH-RDY-057): never a silent mapping."""
    if not split:
        return ""
    notes = []
    for m in split.get("mapping") or []:
        if m.get("read_as") == "intent" and m.get("supplied", "").strip().lower() != m.get("value"):
            notes.append(f"Intent word {m['supplied']!r} read as intent {m['value']} — report this mapping.")
    if split.get("medium"):
        notes.append(f"Medium {split['medium']!r} recorded; a delivery medium never binds a rule pack.")
    if split.get("conflict"):
        notes.append("Supplied intent values conflict — ask which intent applies; do not choose.")
    return (" " + " ".join(notes)) if notes else ""


def _intake_next(missing: list[str], unmatched_channel: str, jurisdictions: list[str],
                 coverage: list[dict[str, Any]] | None = None, split: dict[str, Any] | None = None) -> str:
    """The intake `next` line: binding instruction, the specific intent gap, or the bind-later ask."""
    notes = _channel_notes(split)
    if "audience" in missing or "channel" in missing:
        text = ("Rule pack binds once audience and channel are supplied — ask the person; do not guess (TEH-RDY-043). "
                "Channel here is the communication intent the rule-pack catalogue keys on (promo or "
                "scientific_exchange), not the delivery medium (TEH-RDY-057).")
        if unmatched_channel:
            text += (f" Supplied value {unmatched_channel!r} is neither a known intent nor a known medium — ask which "
                     "intent applies; do not map it yourself.")
        return text + notes
    if unmatched_channel:
        markets = ", ".join(jurisdictions)
        return (
            f"No rule pack for intent {unmatched_channel} in {markets} (supplied value {unmatched_channel!r} is neither "
            f"an intent in the catalogue vocabulary ({', '.join(INTENTS)}) nor a known delivery medium). Report this "
            "gap per market; ask the person which intent applies — do not map it yourself and do not bind another "
            "intent's pack (TEH-RDY-052)." + notes
        )
    gaps = [c["gap"] for c in coverage or [] if c.get("status") == "missing" and c.get("jurisdiction") != "global"]
    if gaps:
        return ("Report each market's coverage exactly as returned, including: " + "; ".join(gaps)
                + ". Never substitute another intent's or market's pack (TEH-RDY-052)." + notes)
    return "Call mlr_get_ruleset with the same jurisdictions, audience, and channel (intent)." + notes


def _intake(args: dict[str, Any]) -> dict[str, Any]:
    jurisdictions = _norm_jurisdictions(args)
    audience = str(args.get("audience") or "").strip().lower()
    # TEH-RDY-057: split the supplied channel words into the ruleset intent and the delivery medium.
    # The intent binds (market + audience + intent); the medium is recorded and never binds. Intent
    # words are mapped transparently ("promotional" -> promo) and the mapping is returned.
    split = split_channel(args.get("channel"), args.get("intent"), args.get("medium"))
    channel = split["intent"]
    missing: list[str] = []
    if audience not in AUDIENCES:
        missing.append("audience")
        audience = audience or ""
    # TEH-RDY-052: a supplied value that is neither an intent nor a known medium is not "missing" and
    # is never mapped to another intent here: each supplied market reports that specific gap.
    unmatched_channel = split["unmatched"] if not channel and not split["conflict"] else ""
    if not channel and not unmatched_channel:
        missing.append("channel")
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
    elif audience in AUDIENCES and unmatched_channel:
        for j in ["global", *jurisdictions]:
            coverage.append({
                "jurisdiction": j,
                "status": "missing",
                "ruleset_id": None,
                "authority_hints": [],
                "gap": f"[GAP] no rule pack for intent {unmatched_channel} in {j}",
            })

    depth = _DEPTH.get((audience, channel), "full" if channel == "promo" else "short")
    context = {
        "artefact_id": artefact_id or str(uuid.uuid4()),
        "artefact_version": artefact_version or None,
        "content_hash": args.get("content_hash"),
        "jurisdictions": jurisdictions,
        "audience": audience or None,
        "channel": channel or None,
        "medium": split["medium"] or None,
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
        "ok": not missing and not unmatched_channel,
        "context": context,
        "missing_fields": missing,
        "suggested_depth": depth,
        "ruleset_coverage": coverage,
        "notes": args.get("notes"),
        "next": _intake_next(missing, unmatched_channel, jurisdictions, coverage, split),
        "medium": split["medium"] or None,
        "channel_mapping": split["mapping"],
    }


def _list_rulesets(args: dict[str, Any]) -> dict[str, Any]:
    j_filter = str(args.get("jurisdiction") or "").strip().upper() or None
    audience = str(args.get("audience") or "").strip().lower() or None
    # TEH-RDY-057: filter on the intent only; a medium is recorded and never selects packs.
    split = split_channel(args.get("channel"), args.get("intent"), args.get("medium"))
    channel = split["intent"] or (str(split["unmatched"]).strip().lower() or None)
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
    return {"tool": "mlr_list_rulesets", "ok": True, "counted": False, "packs": rows,
            "medium": split["medium"] or None, "channel_mapping": split["mapping"]}


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
    split = split_channel(args.get("channel"), args.get("intent"), args.get("medium"))
    channel = split["intent"]
    if audience not in AUDIENCES or channel not in CHANNELS:
        if split["medium"] and not channel:
            raise ValueError(
                f"audience and channel (intent) required — medium {split['medium']!r} recorded; a delivery medium "
                "never binds a rule pack (TEH-RDY-057)"
            )
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
        "medium": split["medium"] or None,
        "channel_mapping": split["mapping"],
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
    for pattern in FORBIDDEN_PATTERNS:  # TEH-RDY-019 regulator-cleared forms
        for m in re.finditer(pattern, lower):
            if m.group(0) not in hits:
                hits.append(m.group(0))
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


_STATUS_RANK = {"findings_only": 0, "revise": 1, "human_gate_required": 2}
# Validation errors a copy or record edit can fix (TEH-RDY-050).
_CORRECTABLE_ERROR_PREFIXES = ("artefact_version mismatch",)


def _status_after_failed_validation(chairs: Any, errors: list[str], force_gate: bool, supplied: Any) -> str:
    """Status for a packet that failed validation (TEH-RDY-046, TEH-RDY-050).

    Never prep_complete. Precedence on what is open: reject / abstain / a forced gate →
    human_gate_required; an open revise decision and/or a correctable validation error (for example
    an artefact_version mismatch) → revise; otherwise findings_only. A status the packet already
    carries is kept when it is higher.
    """
    decisions = [
        chairs[c].get("decision")
        for c in CHAIRS
        if isinstance(chairs, dict) and isinstance(chairs.get(c), dict)
    ]
    if force_gate or any(d in {"reject", "abstain"} for d in decisions):
        derived = "human_gate_required"
    elif any(d == "revise" for d in decisions) or any(
        e.startswith(_CORRECTABLE_ERROR_PREFIXES) for e in errors
    ):
        derived = "revise"
    else:
        derived = "findings_only"
    if supplied in _STATUS_RANK and _STATUS_RANK[supplied] > _STATUS_RANK[derived]:
        return supplied
    return derived


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

    # TEH-RDY-046: every chair packet carries the packet header's artefact_version. A mismatch is
    # an error naming each version exactly as supplied; prep_complete is never derived over it.
    header_version = str(packet.get("artefact_version") or "").strip()
    if header_version:
        for name in CHAIRS:
            chair = chairs.get(name)
            if not isinstance(chair, dict):
                continue
            ver = str(chair.get("artefact_version") or "").strip()
            if ver and ver != header_version:
                errors.append(
                    f"artefact_version mismatch: packet header {header_version} vs {name} {ver}"
                )

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
        # A packet that fails validation is never prep_complete (TEH-RDY-046). Its status follows the
        # precedence order on what is open, never a blanket findings_only (TEH-RDY-050).
        status = _status_after_failed_validation(chairs, errors, force_gate, status)

    normalised = dict(packet)
    normalised["mlr_status"] = status
    normalised["liability_line"] = LIABILITY_LINE
    if versions and len(set(versions)) == 1 and not header_version:
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
    # TEH-RDY-046: chair artefact versions must equal the packet header version (exactly as supplied).
    header_version = str(args.get("artefact_version") or "").strip()
    chair_versions = {
        name: str(chairs[name].get("artefact_version") or "").strip()
        for name in CHAIRS
        if isinstance(chairs.get(name), dict)
    }
    seen = {v for v in chair_versions.values() if v}
    if (header_version and any(v and v != header_version for v in chair_versions.values())) or len(seen) > 1:
        detail = ", ".join(f"{n} {v or '[GAP]'}" for n, v in chair_versions.items())
        slots.append(
            {
                "topic": "artefact_version_mismatch",
                "chairs_disagree": len(seen) > 1,
                "markets_disagree": False,
                "detail": f"Artefact versions differ: packet header {header_version or '[GAP]'}; {detail}",
            }
        )
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


# MLR-H5: a named human owns the prep record. Token-based, case-insensitive refusal of
# AI / automation / placeholder owners. Whole-token match (word boundaries), so real
# names that merely contain a token ("Aileen", "Claudette", "Gaia") are not refused.
CLEARED_BY_REFUSED_TOKENS = frozenset(
    {
        "assistant",
        "ai",
        "model",
        "system",
        "auto",
        "automated",
        "automation",
        "bot",
        "chatbot",
        "chatgpt",
        "gpt",
        "openai",
        "claude",
        "anthropic",
        "copilot",
        "gemini",
        "llm",
        "agent",
        "tbd",
        "unknown",
    }
)
_H5_GPT_VARIANT = re.compile(r"^gpt[0-9][a-z0-9]*$")  # gpt4, gpt4o, gpt35 ...
_H5_AI_DOTTED = re.compile(r"\ba\.i\b\.?")  # "A.I." / "a.i"
_H5_NA = re.compile(r"(?<![a-z0-9])n\s*/\s*a(?![a-z0-9])")  # "n/a", "N / A"


def cleared_by_refusal(name: Any) -> str | None:
    """Return the refusal reason for a cleared_by name, or None when it may be a named human."""
    text = str(name or "").strip()
    if not text:
        return "empty"
    low = text.lower()
    if _H5_NA.search(low):
        return "n/a"
    low = _H5_AI_DOTTED.sub(" ai ", low)
    tokens = [t for t in re.split(r"[\W_]+", low) if t]
    if not tokens:
        return "empty"
    for tok in tokens:
        if tok in CLEARED_BY_REFUSED_TOKENS or _H5_GPT_VARIANT.match(tok):
            return tok
    return None


# TEH-RDY-017 (MLR-H1): never build a prep record on a stand-in packet. The tool cannot see
# provenance, so this is a narrow, fail-closed guard: an explicit synthetic / stand-in flag on the
# packet or a chair, or a placeholder token in an artefact_version or chair summary, is refused.
STAND_IN_FLAGS = ("synthetic", "stand_in", "placeholder", "is_placeholder")
STAND_IN_TOKENS = frozenset({"placeholder", "placeholders", "stand", "standin", "dummy", "fake", "mock", "tbd", "synthetic"})


def stand_in_packet_refusal(packet: Any) -> str | None:
    """Return why a packet looks invented to make the tool run, or None."""
    if not isinstance(packet, dict):
        return None
    for flag in STAND_IN_FLAGS:
        if packet.get(flag) is True:
            return f"packet flag {flag}=true"
    chairs = packet.get("chairs") if isinstance(packet.get("chairs"), dict) else {}
    texts = [("artefact_version", packet.get("artefact_version"))]
    for cname, chair in chairs.items():
        if not isinstance(chair, dict):
            continue
        for flag in STAND_IN_FLAGS:
            if chair.get(flag) is True:
                return f"{cname} flag {flag}=true"
        texts.append((f"{cname}.artefact_version", chair.get("artefact_version")))
        texts.append((f"{cname}.summary", chair.get("summary")))
    for where, value in texts:
        low = str(value or "").lower()
        tokens = [t for t in re.split(r"[\W_]+", low) if t]
        for i, tok in enumerate(tokens):
            if tok == "stand" and i + 1 < len(tokens) and tokens[i + 1] == "in":
                return f"{where}: stand-in"
            if tok in STAND_IN_TOKENS and tok != "stand":
                return f"{where}: {tok}"
    return None


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
    stand_in = stand_in_packet_refusal(packet)
    if stand_in:
        return {
            "tool": "mlr_build_prep_record",
            "ok": False,
            "status": "draft",
            "errors": [
                "packet looks like a stand-in, not the person's validated compile output — "
                "supply the real packet; never invent packets, versions or chair decisions (MLR-H1)",
                f"refused: {stand_in}",
            ],
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
    # MLR-H5: refuse AI / automation / placeholder names as cleared_by (token-based)
    refused = cleared_by_refusal(name)
    if refused:
        return {
            "tool": "mlr_build_prep_record",
            "ok": False,
            "status": "draft",
            "errors": [
                "cleared_by must be a named human — refuse AI/model/assistant/system (MLR-H5)",
                f"refused token: {refused}",
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
