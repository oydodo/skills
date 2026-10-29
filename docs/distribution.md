# Unified ChatGPT / Claude plugin distribution

`registry/skills.yaml` is the source of truth for the selected Skill set and curated trigger descriptions. The two maintained Skill bodies live in `skills/`; six third-party bodies and their resources come from pinned Git submodules under `upstream/`. Do not edit the generated `plugins/oydodo-skills/skills/` tree.

## Updating

- **Maintained Skill**: edit `skills/<name>/`, commit and push to `main`.
- **Third-party Skill**: review upstream changes and advance that submodule's *pinned gitlink*, then push. No unattended upstream auto-upgrades.
- **Selection or trigger**: edit `registry/skills.yaml` and its `description_override` entries, then push.

The [publish workflow](../.github/workflows/publish-plugins.yml) fetches only selected submodules; rebuilds `skills/`, `licenses/` and `SOURCES.md` inside the plugin; increments patch versions of ChatGPT and Claude manifests when generated data changes; commits the result to `main`; creates both ZIPs; and publishes a [GitHub Release](https://github.com/oydodo/skills/releases/latest).

The workflow requires `GITHUB_TOKEN` with repository **contents: write** and a branch policy allowing the Actions bot to push. If either disallows it, the workflow will fail rather than silently distribute stale sources.

## Local reproduction

```bash
python3 -m pip install PyYAML==6.0.2
git submodule update --init upstream/addyosmani-agent-skills upstream/mattpocock-skills upstream/ponytail upstream/technical-writing upstream/wondelai-skills upstream/technical-language-skill
python3 scripts/build_plugins.py --write
python3 scripts/build_plugins.py --check
python3 scripts/package_plugins.py --platform all
```

Artifacts: `dist/oydodo-skills-claude.zip` and `dist/oydodo-skills-chatgpt.zip`.

## Platform update behavior

| Platform | Distribution | Automatic update |
| --- | --- | --- |
| ChatGPT Web workspace | GitHub Marketplace watching `main` | Via workspace GitHub sync, subject to policy |
| ChatGPT desktop CLI | GitHub Marketplace | Plugin marketplace upgrade procedure |
| Claude Code | GitHub marketplace | Plugin marketplace update procedure |
| Claude Web personal | Single Claude ZIP from [latest release](https://github.com/oydodo/skills/releases/latest) | **No**; re-upload the new ZIP manually |
| Claude organization | Eligible private/internal repository marketplace | Possible after separate mirror/admin setup; **not configured** |

Do not equate successful ZIP building with actual auto-invocation accuracy. Maintain separate behavioral tests.
