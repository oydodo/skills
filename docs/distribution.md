# Unified ChatGPT / Claude plugin distribution

`registry/skills.yaml` is the source of truth for the selected Skill set and curated trigger descriptions. The four maintained Skill bodies (three reasoning cores plus one CodeGraph adapter) live in `skills/`; the canonical advisory always-on text and hook definition live in `core/always-on.md` and `core/hooks.json`; eleven third-party bodies and their resources come from pinned Git submodules under `upstream/`. Do not edit the generated `plugins/oydodo-skills/skills/` tree.

## Updating

- **Maintained Skill**: edit `skills/<name>/`, commit and push to `main`.
- **Third-party Skill**: review upstream changes and advance that submodule's *pinned gitlink*, then push. No unattended upstream auto-upgrades.
- **Selection or trigger**: edit `registry/skills.yaml` and its `description_override` entries, then push.
- **Always-on core or Hook**: edit `core/always-on.md` or `core/hooks.json`. The build copies them into the generated Plugin `core/` and `hooks/` directories. Do not edit those generated copies.
- **Formal release history / handoff**: edit root [`CHANGELOG.md`](../CHANGELOG.md) with the **next** patch version heading before publishing any changed Plugin content. The build gates version changes on this entry and copies the canonical file into each Plugin ZIP. Do not edit the generated Plugin copy.

The [publish workflow](../.github/workflows/publish-plugins.yml) fetches only selected submodules; rebuilds `skills/`, `licenses/`, `core/`, `hooks/`, `SOURCES.md` and `CHANGELOG.md` inside the plugin; increments patch versions of ChatGPT and Claude manifests when generated data changes; commits the result to `main`; creates both ZIPs; and publishes a [GitHub Release](https://github.com/oydodo/skills/releases/latest).

The GitHub Release notes are taken from the matching version section of `CHANGELOG.md`, rather than generic boilerplate. The workflow requires `GITHUB_TOKEN` with repository **contents: write** and a branch policy allowing the Actions bot to push. If either disallows it, the workflow will fail rather than silently distribute stale sources.

## Local reproduction

```bash
python3 -m pip install PyYAML==6.0.2
git submodule update --init upstream/addyosmani-agent-skills upstream/mattpocock-skills upstream/ponytail upstream/technical-writing upstream/wondelai-skills upstream/technical-language-skill upstream/visual-explainer
python3 scripts/build_plugins.py --write
python3 scripts/build_plugins.py --check
python3 -m unittest discover -s tests -p test_core_hook.py -v
python3 scripts/package_plugins.py --platform all
```

Artifacts: `dist/oydodo-skills-claude.zip` and `dist/oydodo-skills-chatgpt.zip`.

## CodeGraph adapter (optional local tool)

The [`codegraph` Skill](../skills/codegraph/SKILL.md) guides an Agent through the separately installed [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) CLI/MCP. The Plugin includes neither its executable nor an MCP server. Installing the Plugin alone cannot index a repository or enable CodeGraph in a Web-only chat. No global `codegraph install` or per-project `codegraph init` is executed automatically; follow the version-pinned guide if explicitly requested.

## Visual report skill (optional)

The upstream [visual-explainer](https://github.com/nicobailon/visual-explainer) skill is pinned at v0.14.0 and bundled **with its renderer and reference files** through `upstream/visual-explainer/plugins/visual-explainer`. Use the curated trigger metadata only for genuinely visual explanations, audit/status reports, architecture diagrams, comparisons or slide requests. It is not a global SessionStart rule: a regular chat or short status answer does not require HTML. Rendering uses local files, Node and often a browser; Web-only sessions may not support the same artifact workflow. Use the platform's supported native diagrams/charts where appropriate, and never claim an uncreated local HTML page. The visual-explainer body remains unmodified; the registry overrides **discovery metadata**, not the runtime content.

## Advisory core Hook (local runtimes only)

The Plugin includes a fail-open `SessionStart` Hook with no external script path: it reads `core/always-on.md` relative to the installed Plugin root, and silently returns success on missing/unreadable/empty text. Supported session sources: startup, resume, clear, compact, fork. On Codex the Hook must first be trusted via `/hooks`; updates to its definition may require renewed trust. This is an advisory prompt, not a safety control. It does not bypass platform restrictions, and cannot guarantee injection in Web-only ChatGPT or Claude chats. The build **fails strictly** when core files or hook configuration are missing; the running Agent **fails open** when the optional text is unavailable.

## Platform update behavior

| Platform | Distribution | Automatic update |
| --- | --- | --- |
| ChatGPT Web workspace | GitHub Marketplace watching `main` | Via workspace GitHub sync, subject to policy |
| ChatGPT desktop CLI | GitHub Marketplace | Plugin marketplace upgrade procedure |
| Claude Code | GitHub marketplace | Plugin marketplace update procedure |
| Claude Web personal | GitHub marketplace `oydodo/skills` (preferred); [Claude ZIP](https://github.com/oydodo/skills/releases/latest) as fallback | Repository-backed marketplace supports sync; automatic refresh cadence **not yet verified**. ZIP uploads remain manual. |
| Claude organization | Eligible private/internal repository marketplace | Possible after separate mirror/admin setup; **not configured** |

Do not equate successful ZIP building with actual auto-invocation accuracy. Maintain separate behavioral tests.

## Claude Web personal: recommended GitHub installation

1. In Claude Web, open **Customize → Plugins → Add → Add marketplace → Add from a repository** (labels can vary by rollout).
2. Enter `oydodo/skills` or `https://github.com/oydodo/skills`, add the marketplace, then add the **single** `oydodo-skills` plugin.
3. Start a fresh chat and verify the fifteen independent skills with the `/` menu or chat `+` menu. Avoid keeping duplicate standalone skill names active.

Anthropic [documents personal Git marketplace installation](https://support.claude.com/en/articles/13837440-use-plugins-in-claude). This is preferable to repeatedly uploading ZIP files, but **do not claim every push automatically reaches an installed personal plugin** until the sync cadence has been observed on the actual account. If the marketplace UI is unavailable, upload `oydodo-skills-claude.zip` from the [latest release](https://github.com/oydodo/skills/releases/latest) and manually replace it for updates.
