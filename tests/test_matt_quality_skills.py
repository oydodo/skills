"""Check curated Matt skills, source pin and cross-runtime invocation metadata."""
from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import unittest

import yaml

from scripts.build_plugins import normalized_skill

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "upstream/mattpocock-skills"
BUNDLE = ROOT / "plugins/oydodo-skills"
PIN = "59db609eb1e18aaf59b63284d0e52255aff0c63c"
NEW_SKILLS = {
    "writing-for-agents": "skills/productivity/writing-for-agents",
    "diagnosing-bugs": "skills/engineering/diagnosing-bugs",
    "retro": "skills/engineering/retro",
}


class MattQualitySkillsTest(unittest.TestCase):
    def test_pinned_registry_and_curation(self):
        pinned = subprocess.check_output(
            ["git", "-C", str(ROOT), "ls-tree", "HEAD", "--", "upstream/mattpocock-skills"],
            text=True,
        )
        self.assertIn(PIN, pinned)
        registry = yaml.safe_load((ROOT / "registry/skills.yaml").read_text(encoding="utf-8"))
        entries = registry["skills"]
        self.assertEqual(len(entries), 18)
        self.assertEqual(len({e["name"] for e in entries}), 18)
        by_name = {e["name"]: e for e in entries}
        for name, source_path in NEW_SKILLS.items():
            with self.subTest(name=name):
                item = by_name[name]
                self.assertEqual(item["source"], "mattpocock")
                self.assertEqual(item["skill_path"], f"upstream/mattpocock-skills/{source_path}")
                self.assertTrue(item["description_override"])
        self.assertIn("not routine small fixes", by_name["diagnosing-bugs"]["description_override"])
        self.assertIn("not an automatic status summary", by_name["retro"]["description_override"])
        self.assertIn("not invoke for ordinary", by_name["writing-for-agents"]["description_override"])
        curation = yaml.safe_load((ROOT / "registry/curation.yaml").read_text(encoding="utf-8"))
        self.assertEqual(curation["selected_count"], 18)
        selected = {n for group in curation["selected"].values() for n in group}
        self.assertEqual(len(selected), 18)
        self.assertTrue(set(NEW_SKILLS) <= selected)
        self.assertTrue(set(NEW_SKILLS).isdisjoint(set(curation["not_selected"]["matt"])))

    def test_normalize_preserves_claude_manual_only_and_body(self):
        for name, rel in NEW_SKILLS.items():
            with self.subTest(name=name):
                original = (SOURCE / rel / "SKILL.md").read_bytes()
                generated = normalized_skill(original, name, "Narrowed description").decode("utf-8")
                self.assertIn("description: \"Narrowed description\"", generated)
                original_text = original.decode("utf-8")
                original_body = re.split(r"\A---\s*\n[\s\S]*?\n---\s*\n", original_text, maxsplit=1)[1]
                generated_body = re.split(r"\A---\s*\n[\s\S]*?\n---\s*\n", generated, maxsplit=1)[1]
                self.assertEqual(original_body, generated_body)
                self.assertEqual("disable-model-invocation: true" in generated, name == "retro")
        self.assertIn("disable-model-invocation: true", normalized_skill(
            (SOURCE / "skills/engineering/wayfinder/SKILL.md").read_bytes(),
            "wayfinder", None).decode("utf-8"))
        with self.assertRaises(ValueError):
            normalized_skill(b"---\nname: retro\ndescription: Test\ndisable-model-invocation: manual\n---\nBody", "retro", None)

    def test_bundles_license_resources_and_invocation_policy(self):
        lic = (SOURCE / "LICENSE").read_bytes()
        self.assertIn(b"MIT License", lic)
        for name, rel in NEW_SKILLS.items():
            with self.subTest(name=name):
                packaged = BUNDLE / "skills" / name
                self.assertTrue((packaged / "SKILL.md").is_file())
                self.assertEqual((BUNDLE / "licenses" / f"{name}-LICENSE").read_bytes(), lic)
        self.assertEqual(
            (BUNDLE / "skills/writing-for-agents/SKILL-MECHANICS.md").read_bytes(),
            (SOURCE / "skills/productivity/writing-for-agents/SKILL-MECHANICS.md").read_bytes(),
        )
        self.assertEqual(
            (BUNDLE / "skills/diagnosing-bugs/scripts/hitl-loop.template.sh").read_bytes(),
            (SOURCE / "skills/engineering/diagnosing-bugs/scripts/hitl-loop.template.sh").read_bytes(),
        )
        self.assertIn("writing-for-agents", (BUNDLE / "skills/retro/SKILL.md").read_text(encoding="utf-8"))
        for name in ("retro", "wayfinder"):
            with self.subTest(explicit_only=name):
                front = (BUNDLE / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
                self.assertIn("disable-model-invocation: true", front.split("---", 2)[1])
                meta = yaml.safe_load((BUNDLE / "skills" / name / "agents/openai.yaml").read_text(encoding="utf-8"))
                self.assertIs(meta["policy"]["allow_implicit_invocation"], False)
        for name in ("diagnosing-bugs", "writing-for-agents"):
            front = (BUNDLE / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertNotIn("disable-model-invocation: true", front.split("---", 2)[1])

    def test_release_and_not_always_on(self):
        manifests = ["plugin.json", ".codex-plugin/plugin.json", ".claude-plugin/plugin.json"]
        for manifest in manifests:
            meta = json.loads((BUNDLE / manifest).read_text(encoding="utf-8"))
            self.assertEqual(meta["version"], "0.1.13")
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        self.assertIn("## [0.1.12] - 2026-10-30", changelog)
        core = (ROOT / "core/always-on.md").read_text(encoding="utf-8")
        for name in NEW_SKILLS:
            self.assertNotIn(name, core)


if __name__ == "__main__":
    unittest.main()
