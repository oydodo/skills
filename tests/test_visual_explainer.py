"""Distribution and headless-render smoke checks for pinned visual-explainer."""
from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "upstream/visual-explainer/plugins/visual-explainer"
BUNDLE = ROOT / "plugins/oydodo-skills"
OUTPUT = BUNDLE / "skills/visual-explainer"
PIN = "5f378868e0ea745a6284b51e710c390f0c76f72c"


class VisualExplainerTest(unittest.TestCase):
    def test_pinned_upstream_and_license(self):
        expected = subprocess.check_output(
            ["git", "-C", str(ROOT), "ls-tree", "HEAD", "--", "upstream/visual-explainer"],
            text=True,
        )
        self.assertIn(PIN, expected)
        self.assertTrue((ROOT / "upstream/visual-explainer/LICENSE").is_file())
        license_text = (ROOT / "upstream/visual-explainer/LICENSE").read_text(
            encoding="utf-8"
        )
        self.assertIn("MIT License", license_text)
        self.assertEqual(
            (BUNDLE / "licenses/visual-explainer-LICENSE").read_text(encoding="utf-8"),
            license_text,
        )
        self.assertTrue((OUTPUT / "kit/vendor/PELE-LICENSE").is_file())

    def test_selection_and_discovery_scope(self):
        catalog = yaml.safe_load((ROOT / "registry/skills.yaml").read_text(encoding="utf-8"))
        curation = yaml.safe_load(
            (ROOT / "registry/curation.yaml").read_text(encoding="utf-8")
        )
        entries = catalog["skills"]
        self.assertEqual(len(entries), 18)
        (item,) = [e for e in entries if e["name"] == "visual-explainer"]
        self.assertEqual(item["source"], "visual-explainer")
        self.assertEqual(
            item["skill_path"], "upstream/visual-explainer/plugins/visual-explainer"
        )
        desc = item["description_override"]
        self.assertIn("explicitly asks", desc)
        self.assertIn("Web", desc) if "Web" in desc else self.assertIn("clients", desc)
        self.assertIn("do not turn routine", desc)
        self.assertEqual(curation["selected_count"], 18)
        self.assertIn("visual-explainer", curation["selected"]["visualization"])
        self.assertNotIn("visual-explainer", curation["not_selected"]["other"])

    def test_generated_files_and_changelog(self):
        source = (SOURCE / "SKILL.md").read_text(encoding="utf-8")
        generated = (OUTPUT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("# Visual Explainer", source)
        self.assertIn("# Visual Explainer", generated)
        self.assertIn("name: visual-explainer", generated)
        self.assertIn("description: ", generated)
        self.assertTrue((OUTPUT / "kit/render.mjs").is_file())
        self.assertEqual(
            (OUTPUT / "kit/render.mjs").read_bytes(), (SOURCE / "kit/render.mjs").read_bytes()
        )
        self.assertTrue((OUTPUT / "references/style-guide.md").is_file())
        self.assertTrue((OUTPUT / "templates/slide-deck.html").is_file())
        metadata = yaml.safe_load(
            (OUTPUT / "agents/openai.yaml").read_text(encoding="utf-8")
        )
        self.assertEqual(metadata["interface"]["display_name"], "Visual Explainer")
        version = json.loads((BUNDLE / "plugin.json").read_text(encoding="utf-8"))[
            "version"
        ]
        self.assertEqual(version, "0.1.14")
        self.assertIn(
            "## [0.1.11] - 2026-10-30",
            (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"),
        )

    def test_no_unintended_global_activation(self):
        core = (ROOT / "core/always-on.md").read_text(encoding="utf-8")
        hook = (ROOT / "core/hooks.json").read_text(encoding="utf-8")
        self.assertNotIn("visual-explainer", core)
        self.assertNotIn("visual-explainer", hook)
        self.assertNotIn("visual-explainer", json.dumps(json.loads(hook)))

    @unittest.skipUnless(shutil.which("node"), "Node is needed for renderer smoke test")
    def test_headless_render_creates_readable_html(self):
        """Render real bundled assets without browser or network access."""
        with tempfile.TemporaryDirectory(prefix="visual-explainer-test-") as td:
            directory = Path(td)
            source = directory / "status.src.html"
            output = directory / "status.html"
            source.write_text(
                '<!doctype html><html lang="zh-CN" data-register="instrument">'
                '<head><title>项目进度可视化</title>'
                '<link rel="stylesheet" href="kit.css" data-ve-kit></head>'
                '<body><main><header><h1>10 of 12 tasks done</h1></header>'
                '<figure><ve-bars unit="t" max="12" '
                'label="10 of 12 tasks completed">'
                '<ve-bar value="10" hot>done</ve-bar>'
                '<ve-bar value="2">left</ve-bar></ve-bars>'
                '<figcaption>Ten tasks are done, two remain.</figcaption>'
                '</figure></main></body></html>',
                encoding="utf-8",
            )
            p = subprocess.run(
                ["node", str(OUTPUT / "kit/render.mjs"), str(source), "--no-check"],
                text=True,
                capture_output=True,
                timeout=20,
            )
            self.assertEqual(p.returncode, 0, p.stdout + "\n" + p.stderr)
            rendered = output.read_text(encoding="utf-8")
            self.assertIn("项目进度可视化", rendered)
            self.assertIn("<style data-ve-kit>", rendered)
            self.assertIn("<figcaption>", rendered)
            self.assertIn("<svg", rendered)


if __name__ == "__main__":
    unittest.main()
