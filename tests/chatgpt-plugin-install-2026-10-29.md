# ChatGPT desktop Plugin installation smoke test — 2026-10-29

Source: [oydodo/skills](https://github.com/oydodo/skills), Plugin `oydodo-skills` v0.1.0, Git commit `0cb1b141867d2358116b6872b24ace40497f66ae`.

## Procedure and observed result

Authorized computer: macOS, ChatGPT desktop app installed. Used the bundled Codex CLI at `/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex`.

1. `codex plugin marketplace add oydodo/skills --ref main --json` returned `marketplaceName: oydodo` and `alreadyAdded: false`.
2. `codex plugin add oydodo-skills@oydodo --json` returned `pluginId: oydodo-skills@oydodo`, `version: 0.1.0`, and a valid local installation path.
3. Confirmed installed cache at `~/.codex/plugins/cache/oydodo/oydodo-skills/0.1.0/`, containing both manifest formats and exactly **eight** independent `skills/<name>/SKILL.md` entrypoints:
   `independent-judgment`, `crux-first-reasoning`, `interview-me`, `grilling`, `ponytail`, `technical-writing`, `technical-documentation`, `technical-language`.
4. Verified `~/.codex/config.toml` contains `[plugins."oydodo-skills@oydodo"]` with `enabled = true`.

**Result: PASS for local plugin installation, file delivery, and enabled config.** This is one plugin installation, not eight separate uploads.

## Not yet demonstrated

- Skill visibility and routing in a fresh ChatGPT desktop conversation after app restart.
- ChatGPT Web/iOS cloud availability or workspace publication; local repo marketplace installation does not prove sync.
- Correct precedence if a pre-existing standalone `crux-first-reasoning` has the same skill name.
- Comparative behavior improvement from the bundled skills (requires new-session A/B tests).

One diagnostic `codex plugin list --json` call stalled and was stopped; the installation command, file count and enabled configuration checks succeeded independently.

## References

- [Plugin source and usage](../plugins/oydodo-skills/README.md)
- [Existing routing cases](core-routing.md)
- [Earlier exploratory test](chatgpt-dogfood-2026-10-28.md)
