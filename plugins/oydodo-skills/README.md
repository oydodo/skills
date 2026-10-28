# oydodo Skills Plugin

**One Plugin, eight distinct Skills.** Individual `skills/<name>/SKILL.md` entrypoints remain intact. This is not a merged umbrella Skill or a mandatory eight-step workflow.

This is a **skills-only** Agent Plugin using root `plugin.json` and a backward-compatible `.codex-plugin/plugin.json`. All required Skill contents and references are vendored: Git submodules are NOT required by consumers. The plugin has no connected MCP server, secrets, or automatically registered hooks.

## Install on ChatGPT desktop (macOS)

```bash
codex plugin marketplace add oydodo/skills
codex plugin add oydodo-skills@oydodo
```

If `codex` is absent from PATH, the ChatGPT desktop app may supply `/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex`.

Restart ChatGPT desktop and test the installed plugin in a **new conversation**. This repo marketplace is a local installation mechanism; it does **not** by itself publish or sync the plugin to ChatGPT web/iOS. Availability depends on desktop version and workspace settings.

For updates, use `codex plugin marketplace upgrade oydodo` and the plugin management workflow. If a standalone older `crux-first-reasoning` already exists, check duplicate Skill names and disable or replace the old version to prevent ambiguous routing.

See [SOURCES.md](SOURCES.md) for upstream SHAs, licenses and documented trigger adaptations; see [routing tests](../../tests/core-routing.md) for behavior tests. Packaging success is not proof of automatic triggering.

**Observed local installation:** 2026-10-29, ChatGPT's bundled Codex CLI successfully installed v0.1.0 and enabled the plugin with 8 Skill entrypoints; see [smoke test](../../tests/chatgpt-plugin-install-2026-10-29.md). Cloud sync and natural triggering remain unverified.
