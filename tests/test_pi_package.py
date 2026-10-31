"""Pi Git package exposes only curated generated skills, without running extensions."""
from __future__ import annotations

import json
from pathlib import Path
import unittest

from scripts.build_plugins import catalog, PORTABLE, BUNDLE


ROOT = Path(__file__).resolve().parents[1]


class PiPackageContractTest(unittest.TestCase):
    def test_pi_package_points_at_generated_portable_skills(self):
        package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
        self.assertEqual(package["name"], "oydodo-skills")
        self.assertIs(package["private"], True)
        self.assertEqual(package["pi"]["skills"], ["./.agents/skills"])
        self.assertNotIn("extensions", package["pi"])
        self.assertNotIn("scripts", package)
        self.assertNotIn("dependencies", package)
        self.assertNotIn("version", package, "Git package version is tracked by the release/Changelog, not a second manual version")

        expected = {e["name"] for e in catalog()[1]}
        self.assertEqual(len(expected), 18)
        native = {p.parent.name for p in (PORTABLE / "skills").glob("*/SKILL.md")}
        plugin = {p.parent.name for p in (BUNDLE / "skills").glob("*/SKILL.md")}
        self.assertEqual(expected, native)
        self.assertEqual(expected, plugin)

    def test_pi_bulk_update_instructions_are_present(self):
        docs = (ROOT / "docs/distribution.md").read_text(encoding="utf-8")
        self.assertIn("pi install git:github.com/oydodo/skills", docs)
        self.assertIn("pi update --extensions", docs)
        self.assertIn("pi update --all", docs)
        self.assertIn("not run", docs.lower())


if __name__ == "__main__":
    unittest.main()
