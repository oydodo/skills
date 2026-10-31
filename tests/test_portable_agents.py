"""Portable .agents distribution contract for native Codex, Pi and DSH."""
from __future__ import annotations

from pathlib import Path
import tempfile
import unittest
import zipfile

import yaml

from scripts.build_plugins import (
    ROOT, BUNDLE, PORTABLE, PORTABLE_DIRS, PORTABLE_FILES, catalog, signature, versions,
)
from scripts.package_plugins import package_agents


class PortableAgentsTest(unittest.TestCase):
    def test_one_level_skills_are_identical_to_curated_plugin(self):
        expected = {entry["name"] for entry in catalog()[1]}
        self.assertEqual(len(expected), 18)
        native = {p.parent.name for p in (PORTABLE / "skills").glob("*/SKILL.md")}
        self.assertEqual(native, expected)
        self.assertEqual(
            signature(PORTABLE, PORTABLE_DIRS, PORTABLE_FILES),
            signature(BUNDLE, PORTABLE_DIRS, PORTABLE_FILES),
        )
        self.assertTrue((PORTABLE / "plugins" / "marketplace.json").is_file(),
                        "Regeneration must preserve the existing ChatGPT marketplace")
        self.assertFalse((PORTABLE / "hooks").exists(),
                         "Native agents should not receive plugin lifecycle hooks")
        self.assertFalse((PORTABLE / ".codex-plugin").exists())
        self.assertFalse((PORTABLE / ".dsh").exists())

    def test_cross_harness_invocation_policy_and_resources(self):
        for name in ("retro", "wayfinder"):
            with self.subTest(manual=name):
                meta = yaml.safe_load(
                    (PORTABLE / "skills" / name / "agents" / "openai.yaml")
                    .read_text(encoding="utf-8")
                )
                front = (PORTABLE / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
                self.assertIs(meta["policy"]["allow_implicit_invocation"], False)
                self.assertIn("disable-model-invocation: true", front.split("---", 2)[1])
        self.assertTrue((PORTABLE / "skills/diagnosing-bugs/scripts/hitl-loop.template.sh").is_file())
        self.assertTrue((PORTABLE / "skills/writing-for-agents/SKILL-MECHANICS.md").is_file())
        self.assertIn("MIT License",
                      (PORTABLE / "licenses/retro-LICENSE").read_text(encoding="utf-8"))

    def test_portable_zip_install_layout_and_reproducibility(self):
        version, _ = versions()
        with tempfile.TemporaryDirectory() as tmp:
            first, second = Path(tmp) / "first.zip", Path(tmp) / "second.zip"
            package_agents(first)
            package_agents(second)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            with zipfile.ZipFile(first) as z:
                files = set(z.namelist())
                expected = {entry["name"] for entry in catalog()[1]}
                self.assertEqual(
                    {path.split("/")[2] for path in files
                     if path.startswith(".agents/skills/") and path.endswith("/SKILL.md")
                     and path.count("/") == 3}, expected,
                )
                self.assertFalse(any(p.startswith(".agents/plugins/") for p in files))
                self.assertTrue({".agents/SOURCES.md", ".agents/CHANGELOG.md"}
                                .issubset(files))
                self.assertIn(f"## [{version}]", z.read(".agents/CHANGELOG.md").decode())
                external = {entry["name"] for entry in catalog()[1]
                            if entry["source"] != "maintained"}
                for name in external:
                    self.assertIn(f".agents/licenses/{name}-LICENSE", files)
                self.assertEqual(len(external), 14)


if __name__ == "__main__":
    unittest.main()
