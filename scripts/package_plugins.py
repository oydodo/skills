#!/usr/bin/env python3
"""Create deterministic Claude and ChatGPT Plugin ZIP files from one Skill tree."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import zipfile

from build_plugins import ROOT, BUNDLE, catalog, versions

FILE_PARTS = ("skills", "licenses", "core", "hooks")
COMMON_FILES = ("README.md", "SOURCES.md", "CHANGELOG.md")
PLATFORM_FILES = {
    "claude": (".claude-plugin",),
    "chatgpt": (".codex-plugin", "plugin.json"),
}


def package(platform: str, output: Path) -> None:
    expected = {entry["name"] for entry in catalog()[1]}
    version, _ = versions()
    manifest = BUNDLE / (".claude-plugin/plugin.json" if platform == "claude"
                         else "plugin.json")
    data = json.loads(manifest.read_text(encoding="utf-8"))
    if data["name"] != "oydodo-skills" or data["version"] != version:
        raise ValueError(f"Invalid {platform} plugin manifest")
    names = {d.parent.name for d in (BUNDLE / "skills").glob("*/SKILL.md")}
    if names != expected:
        raise ValueError(f"Expected {sorted(expected)}, got {sorted(names)}")

    contents = []
    for folder in (*FILE_PARTS, *PLATFORM_FILES[platform]):
        path = BUNDLE / folder
        if path.is_dir():
            contents.extend(p for p in path.rglob("*") if p.is_file())
        else:
            contents.append(path)
    contents.extend(BUNDLE / name for name in COMMON_FILES)
    if any(not p.is_file() or p.is_symlink() for p in contents):
        raise ValueError("Plugin references a missing or symlinked file")

    output = output.resolve()
    if BUNDLE in output.parents:
        raise ValueError("ZIP must be outside the source plugin directory")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(contents, key=lambda p: p.relative_to(BUNDLE).as_posix()):
            info = zipfile.ZipInfo(path.relative_to(BUNDLE).as_posix(),
                                   date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100644 << 16)
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED)

    with zipfile.ZipFile(output) as verify:
        inside = set(verify.namelist())
        entrypoints = {x.split("/")[1] for x in inside
                       if re.fullmatch(r"skills/[^/]+/SKILL.md", x)}
        if entrypoints != expected or verify.testzip() is not None:
            raise ValueError("ZIP payload verification failed")
        if "CHANGELOG.md" not in inside:
            raise ValueError("Versioned Changelog is missing from the Plugin ZIP")
        notes = verify.read("CHANGELOG.md").decode("utf-8")
        released = re.search(r"(?m)^## \[([0-9]+\.[0-9]+\.[0-9]+)\] - [0-9]{4}-[0-9]{2}-[0-9]{2}\s*$", notes)
        if released is None or released.group(1) != version:
            raise ValueError(f"Changelog version does not match packaged v{version}")
        if not {"core/always-on.md", "hooks/hooks.json"}.issubset(inside):
            raise ValueError("Required always-on policy or SessionStart Hook missing from ZIP")
        hooks = json.loads(verify.read("hooks/hooks.json").decode("utf-8"))
        if not hooks.get("hooks", {}).get("SessionStart"):
            raise ValueError("SessionStart Hook missing from packaged configuration")
        if any(x not in inside for x in
               (".claude-plugin/plugin.json",) if platform == "claude"):
            raise ValueError("Claude manifest missing from ZIP")
        if platform == "chatgpt" and (
            "plugin.json" not in inside or ".codex-plugin/plugin.json" not in inside
        ):
            raise ValueError("ChatGPT plugin manifests missing from ZIP")
    print(f"OK: {platform} {output} ({len(expected)} skills, v{version})")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform", choices=("all", "claude", "chatgpt"),
                        default="all")
    parser.add_argument("--output", type=Path,
                        help="ZIP path for one platform; directory when --platform=all")
    args = parser.parse_args()
    platforms = ("claude", "chatgpt") if args.platform == "all" else (args.platform,)
    if args.platform == "all" and args.output is not None and args.output.suffix == ".zip":
        parser.error("--platform all requires an output directory, not a ZIP path")
    for platform in platforms:
        path = args.output if len(platforms) == 1 and args.output is not None else (
            (args.output or ROOT / "dist") / f"oydodo-skills-{platform}.zip"
        )
        package(platform, path)


if __name__ == "__main__":
    main()
