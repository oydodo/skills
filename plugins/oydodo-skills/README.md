# oydodo Skills Plugin

**One Plugin, nine distinct Skills.** Individual `skills/<name>/SKILL.md` entrypoints remain intact. This is not a merged umbrella Skill or a mandatory nine-step workflow.

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

**Installation and routing history:** See the [install test](../../tests/chatgpt-plugin-install-2026-10-29.md) and [natural-trigger test](../../tests/chatgpt-plugin-auto-trigger-2026-10-29.md). Results concern the tested release and environment.

## ChatGPT Web / iOS via workspace GitHub import

For account-level deployment across ChatGPT surfaces (not just local desktop), a **workspace admin** can import this repository's marketplace:

1. Open **Admin → Plugins → Add → Import marketplace**.
2. Set **Source** to `https://github.com/oydodo/skills`; leave **Path** blank because `.agents/plugins/marketplace.json` is at the repository root. Use branch `main` for updates.
3. Import and review the **single** `oydodo-skills` plugin. Set its **Installation policy** to **Installed** for the intended eligible roles, or let users install this single plugin from the workspace directory.
4. Open a new ChatGPT conversation and confirm that the nine Skills are available. Workspace policy and product eligibility still apply.

The plugin bundles no MCP servers, so it does not opt into the MCP-related **Desktop only** restriction. GitHub workspace marketplaces can sync updates automatically (typically daily). The user subsequently confirmed ChatGPT Web import, and a Web conversation demonstrated `grilling` activation. Future sync cadence and iOS support still depend on workspace policy and product availability.

Official docs: [Plugin management — GitHub import](https://learn.chatgpt.com/docs/enterprise/plugin-management).

## Claude Web and Claude Code — one-plugin distribution

The **same eight independent `skills/<name>/SKILL.md` files** are compatible with
Claude. Claude uses `.claude-plugin/plugin.json` while ChatGPT uses the existing
`plugin.json` / `.codex-plugin/plugin.json`; no forked Skill content is needed.

### Claude Web (Pro / Max / Team / Enterprise)

**Recommended: import the repository marketplace once, not eight individual Skills or repeated ZIPs.**

1. In Claude Web, open **Customize → Plugins → Add → Add marketplace → Add from a repository** (UI labels may differ by rollout).
2. Enter `oydodo/skills` or `https://github.com/oydodo/skills`; add the marketplace, then add the single `oydodo-skills` plugin.
3. Open a new Claude chat. Use `/` or the chat `+` menu to inspect the nine Skills. Avoid having duplicate old standalone skills enabled.

The [Claude personal marketplace guide](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) explicitly supports Git repositories on github.com. The repository-backed path simplifies updates, but **the cadence and automatic refresh of personal-marketplace installs have not been verified on this account**. Do not describe every push as an automatic install/update.

**Fallback:** upload [`oydodo-skills-claude.zip`](https://github.com/oydodo/skills/releases/latest/download/oydodo-skills-claude.zip) from the latest release under Customize → Plugins. A manually uploaded ZIP is not linked to the repository and requires re-uploading for later versions.

### Claude Code — public GitHub marketplace

```bash
claude plugin marketplace add oydodo/skills
claude plugin install oydodo-skills@oydodo
```

Claude Code uses the same root [`.claude-plugin/marketplace.json`](../../.claude-plugin/marketplace.json) as Claude Web's repository marketplace; no second Skill copy is needed.

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

### Automated single-source publishing

**Do not manually edit `plugins/oydodo-skills/skills/` or `licenses/`.**
The [publishing workflow](../../.github/workflows/publish-plugins.yml)
regenerates both platform distributions from the curated registry,
the three self-maintained Skills, and the six pinned upstream Git submodules.

On a selected source change, the workflow:

1. Rebuilds a single shared Skill tree while retaining supporting resources.
2. Bumps the plugin patch version in all three manifests when contents change.
3. Commits generated output to `main` for GitHub Marketplace syncing.
4. Verifies and publishes directly downloadable Claude and ChatGPT ZIP files.

ChatGPT Web can sync the updated GitHub branch under workspace policy.
Claude Web personal users should use the **GitHub repository marketplace** where available;
personal automatic refresh remains unverified, while a ZIP upload stays manual.
Claude organization GitHub sync needs a private/internal source, not configured
in this public repository.

[Release and maintenance guide](../../docs/distribution.md) ·
[Latest release](https://github.com/oydodo/skills/releases/latest) ·
[Build history](https://github.com/oydodo/skills/actions/workflows/publish-plugins.yml).
