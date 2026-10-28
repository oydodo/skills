# ChatGPT Plugin: natural-trigger dogfood — 2026-10-29

**Verdict:** Actual automatic Skill loading was observed for **6 of 8** Plugin Skill names, plus a correct negative control. The remaining two names were selected from pre-existing **local** Skill installations instead of the Plugin, and some simple writing prompts did not load a Skill at all. This is **not** a claim of 6/8 statistical precision or behavioral improvement.

## Environment and evidence

- ChatGPT Marketplace: `skills__list` in the active ChatGPT conversation exposed all eight independent `skills://plugins/oydodo-skills/<name>` entries, with no remaining legacy `crux-first-reasoning` entry in that list.
- End-to-end tests: fresh, ephemeral sessions using the **ChatGPT desktop-bundled Codex CLI**, ChatGPT authentication, model `gpt-6.1-sol`, read-only sandbox, and a normal task prompt without naming the Skill.
- To avoid the earlier CLI hangs, close stdin with `</dev/null` and override the user's custom model provider with `-c 'model_provider="openai"'`. A non-supported hard-coded model was the primary earlier blocker.
- Observe actual `command_execution.command` from `--json` events. **Only an explicit read of `.../plugins/cache/oydodo/oydodo-skills/.../skills/<name>/SKILL.md` counts as a successful Plugin auto-trigger**. Reads of `~/.agents/skills/<name>/SKILL.md` are tracked separately; answering well or mentioning the Skill name is insufficient.
- The tests used `HOME=/tmp/oydodo-skill-testhome` and `CODEX_HOME` pointing to the user's existing authenticated Codex configuration. This prevented some, **but not all**, selection of old local Skills. Do not consider it a fully clean baseline.
- Raw JSONL traces remain under temporary files on the authorized Mac; they are not uploaded to this public GitHub repository because an agent command may have read local personal instruction files.

## Case-level observations

| Normal user request (no Skill name) | Plugin `SKILL.md` actually read | Legacy local `SKILL.md` read | Finding |
| --- | --- | --- | --- |
| Critically challenge a plan to split one service into 20 microservices | `grilling` | None in main test | **PASS:** correct pressure-test method and design questions |
| Unclear team tool idea; ask questions before proposing a plan | `interview-me` | None in isolated-run main test | **PASS:** one question at a time |
| AI product: happy trial users, no actual purchases, validated server costs | `crux-first-reasoning` | None | **PASS:** prioritizes willingness-to-pay evidence |
| Demand full database replacement without investigating higher API latency | `independent-judgment` | `diagnosing-bugs` | **PASS:** constructive evidence-based pushback |
| Fix Python unique function while preserving order with minimal change | `ponytail` | None | **PASS:** minimal implementation with assertion |
| Edit one English release-note sentence | None | None | **MISS on first, simple prompt:** answer acceptable but Skill not loaded |
| Edit a longer release note using controlled technical English rules | `technical-language` | None | **PASS on second, clearer prompt** |
| Rewrite one Chinese sentence for a leadership security report | None | None | **MISS on first, simple prompt** |
| Write structured Chinese internal security technical proposal | None | `technical-writing` | **Local-shadowed:** correct named Skill, not Plugin |
| Create a new developer CLI README, without inventing unknown details | None | `technical-documentation` | **Local-shadowed:** correct named Skill, not Plugin |
| Audit and rewrite a developer README with missing behavioral details | None | `technical-documentation` | **Local-shadowed again** |
| Translate `rollback plan` | None | None | **PASS negative:** direct concise translation |

An extra attempt to create a no-plugin control using `--ignore-user-config` was **contaminated**: Codex still read a pre-existing `~/.agents/skills/grilling/SKILL.md`. Thus it **cannot** serve as a valid no-Skill A/B comparator.

## What this does and does not establish

**Established:** A natural task in a new desktop Codex session can automatically load a specific Skill **from the newly imported Plugin**. We observed exact Plugin-path reads for `grilling`, `interview-me`, `crux-first-reasoning`, `independent-judgment`, `ponytail`, and `technical-language`. Correct negative routing was also observed.

**Not established:** Consistent Plugin selection for all tasks, guaranteed precedence over old local Skills, any reduction in token spend, controlled answer-quality uplift, or the same per-prompt routing on ChatGPT Web/iOS. `skills__list` confirms ChatGPT runtime discovery, not web-session A/B.

**Primary issue:** Multiple older third-party Skills already exist under `~/.agents/skills` (the user's `~/.codex/skills` is a symlink). The Plugin has its own copies. The same logical Skill can be loaded from different places. The two writing categories showed that this happens in practice.

## Recommendation

**Do not immediately change Skill wording or add an orchestration Skill.** First perform a **non-destructive, reversible** de-duplication of the matching old *local* Skill directories (back them up, do not delete them), after the user explicitly agrees. Then repeat the two shadowed writing cases and the short English editing case with a verified clean baseline. Keep the workspace GitHub Marketplace version as the managed source of truth.

This report supersedes the prior statement in [runtime smoke test](chatgpt-plugin-runtime-2026-10-29.md) that automatic triggering had not yet been observed; that earlier report remains valid for its installation and reference-file checks.
