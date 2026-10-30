# Evaluation

[Visual Explainer](test_visual_explainer.py) now has a pinned-submodule and license check, curated-trigger contract, full renderer/resource packaging check and a headless Node.js HTML smoke test. It does not prove browser appearance, Web Plugin execution, or spontaneous routing; test those separately on the actual Agent runtime.

Matt's three added quality skills have a [pinned-source/packaging/invocation-policy contract test](test_matt_quality_skills.py): checks 18 curated entries, `writing-for-agents` reference and `diagnosing-bugs` reproduction script, upstream MIT licenses, and `retro` / `wayfinder` explicit-only metadata for Claude and Codex. [Positive and negative routing cases](core-routing.md) remain **manual acceptance checks**; static tests do not prove actual client triggering.
CodeGraph integration has a [packaging/safety contract test](test_codegraph_skill.py) plus [positive/negative routing scenarios](../skills/codegraph/references/evaluation.md). Its CLI/MCP is external, so packaging tests do not establish that an Agent has actually indexed or queried a repository.
Formal version history, important design changes and Claude handoff: [CHANGELOG.md](../CHANGELOG.md). This is published with each Plugin ZIP. The build refuses to release changed content without a matching next-version entry.

The Plugin SessionStart Hook has separate [fail-open shell tests](test_core_hook.py): missing/empty/unreadable core content and both Plugin-root environment variable forms must not interrupt startup. In CI, run these tests **after** rebuilding generated Plugin assets. These are command-level checks, not proof of actual Codex/Claude Code hook invocation.

Use [crux-first-reasoning behavioral test cases](../skills/crux-first-reasoning/references/evaluation.md) as a **manual** A/B protocol, not as a performance benchmark.

Compare the same model and prompts in three setups:

- A: existing writing skills only (baseline);
- B: A + `skills/independent-judgment/`;
- C: B + `skills/crux-first-reasoning/`.

Score whether outputs identify the dominant goal-relative constraint, distinguish secondary factors, explain decisive evidence, and only then prioritize decision-changing uncertainties; also assess calibration, independence, evidence-driven revision, and reader understanding. Apply the same rubric to all compared outputs; historical scores need re-scoring after criteria change. Record effects across multiple rounds, not just response length. Do not claim validation before testing.

Latest exploratory report: [ChatGPT dogfood — 2026-10-28](chatgpt-dogfood-2026-10-28.md). Package checks are separate from account installation and routing A/B tests.

Mac install smoke test: [ChatGPT desktop Plugin install — 2026-10-29](chatgpt-plugin-install-2026-10-29.md). It verifies 8 bundled entrypoints and enabled config, not cloud sync or auto-routing.

Runtime smoke test after workspace import: [ChatGPT Plugin runtime, 2026-10-29](chatgpt-plugin-runtime-2026-10-29.md). Verifies ChatGPT 8/8 discovery, 14/14 supporting files and helper script; documents the unresolved legacy-name conflict and untested prompt routing.

Actual automatic-trigger dogfood: [2026-10-29 end-to-end routing](chatgpt-plugin-auto-trigger-2026-10-29.md). Six Plugin Skill names confirmed by executed Skill-file reads, one negative control, and local-installation shadowing for the two writing categories.
