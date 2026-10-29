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

## ChatGPT Web / iOS via workspace GitHub import

For account-level deployment across ChatGPT surfaces (not just local desktop), a **workspace admin** can import this repository's marketplace:

1. Open **Admin → Plugins → Add → Import marketplace**.
2. Set **Source** to `https://github.com/oydodo/skills`; leave **Path** blank because `.agents/plugins/marketplace.json` is at the repository root. Use branch `main` for updates.
3. Import and review the **single** `oydodo-skills` plugin. Set its **Installation policy** to **Installed** for the intended eligible roles, or let users install this single plugin from the workspace directory.
4. Open a new ChatGPT conversation and confirm that the eight skills are available. Workspace policy and product eligibility still apply.

The plugin bundles no MCP servers, so it does not opt into the MCP-related **Desktop only** restriction. GitHub workspace marketplaces can sync updates automatically (typically daily). The workspace admin import and web/iOS activation **have not been performed or verified**.

Official docs: [Plugin management — GitHub import](https://learn.chatgpt.com/docs/enterprise/plugin-management).

## Claude Web and Claude Code — one-plugin distribution

The **same eight independent `skills/<name>/SKILL.md` files** are compatible with
Claude. Claude uses `.claude-plugin/plugin.json` while ChatGPT uses the existing
`plugin.json` / `.codex-plugin/plugin.json`; no forked Skill content is needed.

### Claude Web (Pro / Max / Team / Enterprise)

1. Download the `oydodo-skills-claude-zip` artifact from the latest successful
   [Package Claude Plugin GitHub Action](https://github.com/oydodo/skills/actions/workflows/package-claude-plugin.yml);
   unzip the **GitHub artifact container** once to obtain `oydodo-skills-claude.zip`.
   Alternatively, clone the repository and run:
   ```bash
   python3 scripts/package_claude_plugin.py
   ```
2. In claude.ai open **Customize → Plugins → Upload custom plugin**, or the
   new **Plugins** sidebar experience if it has reached your account.
3. Upload **one** `oydodo-skills-claude.zip`. Claude registers the eight Skills
   as a single plugin; you may want to disable old standalone installations
   with duplicate names. Verify them using `/` or the chat `+` menu.

**Important:** personal Claude Pro / Max accounts support ZIP upload, but
installing a ZIP does **not** establish automatic update from public GitHub.
GitHub Actions automates **creation of the ZIP only**; uploading a new version
to the personal Claude account is still an explicit action.

### Claude Code — public GitHub marketplace

```bash
claude plugin marketplace add oydodo/skills
claude plugin install oydodo-skills@oydodo
```

This uses `../../.claude-plugin/marketplace.json` and is **not** a way to
import a GitHub marketplace directly into personal Claude Web.

### Claude Team / Enterprise workspace automatic updates

An administrator can synchronize a marketplace from **a private/internal**
GitHub (or GitLab) mirror and distribute this same Claude-compatible Plugin
to its members. Anthropic does **not** accept a **public** GitHub repository
as the direct source of its organization-synced marketplace. This public
`oydodo/skills` repository must therefore be mirrored to a private source
for organization GitHub sync. Manual ZIP upload is an alternative.

For GitHub-synced workspaces, automatic sync uses the documented webhook and
plugin version-update conditions (not every ordinary push); admins may also
use **Re-sync**. Keep the two platform manifests' version values aligned.

Docs: [Use plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude),
[Manage plugins for your organization](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization),
[Claude plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces).

### Source-of-truth caveat

Both platform bundles **share** the vendored Skill tree
`plugins/oydodo-skills/skills/`. The repository's separate top-level
`skills/` and registry may contain originals/pins; the mirroring of changes
from top-level sources into the vendored tree is **not yet automated**.
Until a sync build is added, update the vendored distribution tree when
publishing changes, or the two platforms can receive stale content.
