#!/usr/bin/env python3
"""Load and structurally validate a DAZ Genesis 9 rig capture.

This validates the exported JSON shape and explicit availability markers. It does
not infer missing DAZ transforms or claim that raw orientation/joint vectors have
a verified coordinate frame.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


EXPECTED_GROUPS = {
    "pelvis": {"pelvis"},
    "shoulders": {"l_shoulder", "r_shoulder"},
    "upper_arms": {"l_upperarm", "r_upperarm"},
    "forearms": {"l_forearm", "r_forearm"},
    "hands": {"l_hand", "r_hand"},
    "thighs": {"l_thigh", "r_thigh"},
    "shins": {"l_shin", "r_shin"},
    "feet": {"l_foot", "r_foot"},
    "neck": {"neck1", "neck2"},
    "head": {"head"},
}


def validate(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("schema_version") != "1.0":
        errors.append("schema_version must be '1.0'")

    figure = data.get("figure", {})
    if figure.get("name") not in {"Genesis9", "Genesis9Female", "Genesis9Male"}:
        errors.append(f"unexpected figure internal name: {figure.get('name')!r}")

    skeleton = data.get("skeleton", {})
    bones = skeleton.get("bones")
    if not isinstance(bones, list) or not bones:
        errors.append("skeleton.bones must be a non-empty list")
        bones = []

    by_name: dict[str, dict[str, Any]] = {}
    ids: set[int] = set()
    for i, bone in enumerate(bones):
        name = bone.get("name")
        if not isinstance(name, str) or not name:
            errors.append(f"bone[{i}] has no internal name")
            continue
        if name in by_name:
            errors.append(f"duplicate bone internal name in main skeleton: {name}")
        by_name[name] = bone

        element_id = bone.get("element_id")
        if not isinstance(element_id, int):
            errors.append(f"{name}: element_id is not an integer")
        elif element_id in ids:
            errors.append(f"{name}: duplicate element_id {element_id}")
        else:
            ids.add(element_id)

        for field in ("local_position", "world_position"):
            vec = bone.get(field)
            if not isinstance(vec, list) or len(vec) != 3:
                errors.append(f"{name}: {field} must contain three coordinates")
            elif any(not isinstance(v, (int, float)) for v in vec):
                errors.append(f"{name}: {field} contains a non-numeric coordinate")

        channels = bone.get("rotation_channels_deg", {})
        for axis in ("X", "Y", "Z"):
            channel = channels.get(axis)
            if not isinstance(channel, dict):
                errors.append(f"{name}: missing {axis} rotation channel record")
                continue
            for key in ("value", "min", "max", "default_value", "clamped"):
                if key not in channel:
                    errors.append(f"{name}: {axis} rotation channel missing {key}")

    for bone in bones:
        parent = bone.get("parent")
        if parent is not None and parent.get("name") not in by_name:
            errors.append(f"{bone.get('name')}: parent {parent.get('name')!r} not in main skeleton")

    reported_count = skeleton.get("main_skeleton_bone_count")
    if reported_count != len(bones):
        errors.append(f"main_skeleton_bone_count={reported_count!r}, actual={len(bones)}")

    groups = data.get("identified_bone_groups", {})
    for group, expected in EXPECTED_GROUPS.items():
        records = groups.get(group, [])
        present = {r.get("requested_name") for r in records if r.get("present")}
        missing = expected - present
        if missing:
            errors.append(f"required bone group {group} is missing: {', '.join(sorted(missing))}")
        for record in records:
            if record.get("present") and record.get("requested_name") not in by_name:
                errors.append(f"{group}: marked present but absent from skeleton: {record.get('requested_name')}")

    if data.get("capture", {}).get("scene_was_modified_by_capture") is not False:
        errors.append("capture metadata does not confirm read-only scene capture")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_file", nargs="?", default="genesis9_rig.json")
    args = parser.parse_args()
    path = Path(args.json_file)
    data = json.loads(path.read_text(encoding="utf-8"))
    errors = validate(data)
    if errors:
        print(f"Invalid rig capture ({len(errors)} issue(s)):")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Valid rig capture: {len(data['skeleton']['bones'])} bones; "
          f"{len(data['mcp_tool_inventory']['available_tools'])} DAZ MCP tools recorded.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

