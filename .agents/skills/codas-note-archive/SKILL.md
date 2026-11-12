---
name: codas-note-archive
description: Use when adding, auditing, archiving or deleting Agent Notes in a Codas-governed repository that uses the Codas default Note policy.
---

# Archive Codas Agent Notes

Adapted from [DeepSeek Harness `687f282e8625c6b8d11ff58211a90524be2e4317`](https://github.com/deepseek-ai/deepseek-harness/blob/687f282e8625c6b8d11ff58211a90524be2e4317/.agents/skills/dsh-archive-agent-notes/SKILL.md).

Keep the active Notes few without erasing history that still guides work. Judge each Note by its meaning; length and age are never the reason.

Start with `codas-ontology`, then read the Note rules file it names. This Skill serves the Codas default Note policy.

## When adding a Note

Before drafting, apply the creation criteria in the Note rules file. Every new Note triggers a scoped audit of active Notes covering the same decision, mechanism or rejected alternative. Classify each full or partial supersession while writing the new Note: archive qualifying implemented Notes in the same change, keep and cross-link partial supersessions or independently useful rationale, reject obsolete proposals, and delete rejected Notes that no longer prevent a plausible mistake. Do not defer a known match to a later audit.

## Classify

- **Implemented, delete:** small UI or purely mechanical changes. Fix inbound links.
- **Implemented, keep:** its rationale, rejected alternatives, boundary or reintroduction condition is likely to guide a future change.
- **Implemented, archive:** complete, unlikely to guide future work, but worth keeping as history.
- **Proposed:** never archive; reject it with an honest reason if it is dead.
- **Rejected, keep:** only while the losing idea is still tempting and the Note says why it loses. Otherwise delete.

No quotas; record borderline cases in the handoff.

## Archive one implemented Note

1. Move it from `implemented/<kind>/` to `archived/<kind>/` and insert only `Archived: YYYY-MM-DD` below `Status: implemented`. No other edits.
2. In the same change correct the current text that states its decision, or make the Note that now carries the decision link it; redirect or delete inbound links from active prose.
3. Seal it with the archive check `--write`, then run the normal checks. A sealed Note is never edited, moved or deleted.

## Checks

From the target root (source tree in Codas itself, installed copy elsewhere):

```sh
notes_hook=.agents/codas/hooks
test -f src/codas/agent/hooks/notes/verify-agent-note-format.ts && notes_hook=src/codas/agent/hooks/notes
npx --yes tsx@4.21.0 "$notes_hook/verify-agent-note-format.ts"
npx --yes tsx@4.21.0 "$notes_hook/verify-agent-note-classification.ts"
npx --yes tsx@4.21.0 "$notes_hook/verify-archived-agent-notes.ts"   # add --write to seal
git diff --check
```

Report what was kept, deleted, archived or rejected, and the borderline cases.
