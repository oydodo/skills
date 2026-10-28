# ChatGPT Plugin runtime smoke test — 2026-10-29

**Test subject:** `oydodo-skills` Plugin, imported from `oydodo/skills`. This test was run from an active ChatGPT conversation **after the user confirmed marketplace import**. It distinguishes actual runtime discovery from model-controlled automatic routing.

## Verified in ChatGPT runtime

| Check | Observed result | Verdict |
| --- | --- | --- |
| Plugin Skill discovery | `skills__list` exposes all 8 separately as `skills://plugins/oydodo-skills/<name>` | **PASS 8/8** |
| Entrypoint loading | `skills__read` loads every bundled `SKILL.md` | **PASS 8/8** |
| Content integrity | Each loaded Skill body is an exact prefix of the current GitHub-bundled file; ChatGPT appends only its own *available file URIs* section | **PASS 8/8** |
| Trigger description registration | Each `skills__list` description matches the parsed `SKILL.md` frontmatter description | **PASS 8/8** |
| Supporting files | Every explicitly tested optional reference, script and README can be resolved by Skill URI | **PASS 14/14** |
| Executable helper | Local installed `technical-language/techlang-lint.py --selftest` exits successfully with `selftest ok` | **PASS 1/1** |
| Name uniqueness across all ChatGPT Skills | `skills://crux-first-reasoning` (legacy) and `skills://plugins/oydodo-skills/crux-first-reasoning` coexist | **ISSUE** |
| Natural prompt → model-triggered Skill routing | No independent successful invocation was observed | **NOT TESTED** |

Installed plugin entries:
`independent-judgment`, `crux-first-reasoning`, `interview-me`, `grilling`, `ponytail`, `technical-writing`, `technical-documentation`, `technical-language`.

**Supporting files checked:** `independent-judgment` sources (1); `crux-first-reasoning` evaluation and sources (2); all seven `technical-documentation/references/*.md` (7); `technical-language` README, reference rules, lint script and optional hook (4). Total: 14.

## Routing boundaries: description-level review only

- `interview-me`: clarify a missing critical requirement; use an interview, one question at a time.
- `grilling`: stress-test a defined plan and work through a design decision tree, multiple frontier questions per round.
- `technical-writing`: Chinese professional technical writing; `technical-documentation`: creating/auditing developer documentation; `technical-language`: editing English technical wording without rewriting entire documentation.
- `crux-first-reasoning`: substantive, decision-changing analysis, **not** trivial translation. `independent-judgment`: evidence calibration and constructive pushback.

These distinctions appear consistently in registered metadata. **They have not been independently proven by observing a model choose these Skills from natural prompts.**

## Attempted live prompts and blocker

From the authorized Mac, using the ChatGPT desktop-bundled Codex CLI with read-only sandbox and ephemeral sessions:

1. Tried a plan stress-test prompt: split a monolith into 20 microservices, critique decisions in rounds. No model output arrived after more than a minute, so the stalled process was stopped.
2. Tried a simple `OK` prompt with `--ignore-user-config` to isolate user/plugin setup. This control also gave no model output, and was stopped.
3. CLI `login status` confirmed **Logged in using ChatGPT**. The plugin installation previously returned a valid ID and cache path, and local `~/.codex/config.toml` contains `[plugins."oydodo-skills@oydodo"] enabled = true`.

Because even the no-user-config control failed, the CLI blocker **cannot be attributed to this plugin**. It also means neither the route-selection behavior nor comparative answer quality was tested end-to-end.

## Issues and recommendations

1. **P1 – Duplicate `crux-first-reasoning`:** disable/remove the legacy standalone Skill in ChatGPT, if user-accessible, and keep the Plugin version. Verify the older root URI disappears from `skills__list` before relying on consistent routing. Do not delete the plugin copy.
2. **P2 – Actual routing A/B pending:** in fresh ChatGPT sessions, test direct translation (none), unscoped requirements (`interview-me`), explicit stress test (`grilling`), consequential architectural choice (`crux-first-reasoning`), simple code fix (`ponytail`), Chinese technical writing, new developer README, and wording-only technical English. Observe actual invocation rather than scoring a self-generated imitation.
3. **P2 – No observed quality uplift:** no controlled prompt-level A/B was completed. Do not describe the plugin as improving reliability or token costs until measured.

**Conclusion:** ChatGPT Marketplace import, all eight independent Skill manifests, their metadata, their full bodies and supporting files are operational. Natural automatic selection and behavioral gains remain unverified.
