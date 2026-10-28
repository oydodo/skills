# Source provenance

Eight independent Skills are physically bundled, with third-party upstream content pinned to the commits below. Their full source LICENSE files are included under `licenses/`. No MCP servers or lifecycle hooks are enabled.

| Skill | Upstream | Commit | Plugin adaptation |
| --- | --- | --- | --- |
| independent-judgment | [oydodo/skills](https://github.com/oydodo/skills) | `40c70f8bfd2ce4bdcf5c16e949f19273f3de2fd1` | None |
| crux-first-reasoning | [oydodo/skills](https://github.com/oydodo/skills) | `40c70f8bfd2ce4bdcf5c16e949f19273f3de2fd1` | None |
| interview-me | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | `aeac41d4d005999432bb7312f7ff06383a91d59d` | Clarified trigger to avoid grilling collision; added UI metadata |
| grilling | [mattpocock/skills](https://github.com/mattpocock/skills) | `59db609eb1e18aaf59b63284d0e52255aff0c63c` | None |
| ponytail | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | `09c434ab73ca43761c5d8b0c5d341926c2fba710` | Normalized Skill frontmatter; added UI metadata |
| technical-writing | [luoling8192/technical-writing](https://github.com/luoling8192/technical-writing) | `5f684e950319bee8f773c3b5f5265c8bdda2900a` | None |
| technical-documentation | [wondelai/skills](https://github.com/wondelai/skills) | `c172996495bed0fcd26896a9416b2093fd7073f0` | Clarified trigger for document authoring; added UI metadata |
| technical-language | [jjsnack/technical-language-skill](https://github.com/jjsnack/technical-language-skill) | `cb441ebedbf8d48a7a45cc357e58d5bb7a71dadc` | Clarified trigger for English wording edits; added UI metadata |

All third-party Skill body text is unchanged. The packaged frontmatter is adapted only where documented to improve routing or format compatibility. Scripts bundled with technical-language are optional; the plugin does not configure their hooks.
