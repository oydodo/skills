# Evaluation

Use [crux-first-reasoning behavioral test cases](../skills/crux-first-reasoning/references/evaluation.md) as a **manual** A/B protocol, not as a performance benchmark.

Compare the same model and prompts in three setups:

- A: existing writing skills only (baseline);
- B: A + `skills/independent-judgment/`;
- C: B + `skills/crux-first-reasoning/`.

Score problem framing, decision-relevant focus, calibration, independence, evidence-driven revision, and clarity. Record whether improvements persist across multiple rounds rather than comparing just response length. Do not claim validation before testing.

Latest exploratory report: [ChatGPT dogfood — 2026-10-28](chatgpt-dogfood-2026-10-28.md). Package checks are separate from account installation and routing A/B tests.

Mac install smoke test: [ChatGPT desktop Plugin install — 2026-10-29](chatgpt-plugin-install-2026-10-29.md). It verifies 8 bundled entrypoints and enabled config, not cloud sync or auto-routing.

Runtime smoke test after workspace import: [ChatGPT Plugin runtime, 2026-10-29](chatgpt-plugin-runtime-2026-10-29.md). Verifies ChatGPT 8/8 discovery, 14/14 supporting files and helper script; documents the unresolved legacy-name conflict and untested prompt routing.
