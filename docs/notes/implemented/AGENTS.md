# AGENTS.md — Implemented Agent Notes

Adapted from [DeepSeek Harness `687f282e8625c6b8d11ff58211a90524be2e4317`](https://github.com/deepseek-ai/deepseek-harness/blob/687f282e8625c6b8d11ff58211a90524be2e4317/.agents/notes/implemented/AGENTS.md).

## Responsibility

Maintain shipped Note facts and this lifecycle's reading and maintenance entry.

## Boundary

The [Note rules](../AGENTS.md) own policy; this Agent supplies lifecycle instructions.

## Work

These Agent Notes describe shipped decisions. Follow the [root instructions](../../../AGENTS.md), `codas-prose-standard`, and [Agent Note format](../AGENTS.md#the-file-format); the format Note check gates the lifecycle-specific structure.

## Keep an implemented Agent Note current with what actually shipped

Keep paths, symbols, defaults, and mechanisms current in the same change that alters them. Rewrite stale facts in place; do not append change history.

When a shipped note is unlikely to guide future work, archive its Markdown file through `codas-note-archive` instead of continuing to maintain it.

### This is not a license to rewrite the *decision*

Update factual realization in place. A reversal of the decision or its rationale requires a new Agent Note and cross-link; a fully superseded old note may be deleted only through the consolidation rule in the [Agent Note rules](../AGENTS.md).
