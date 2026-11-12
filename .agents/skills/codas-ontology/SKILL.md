---
name: codas-ontology
description: Prepare any Codas work - fix the baseline, read the ontology and the repository's documentation standard, and find the repository's Note rules. Every other Codas Skill starts here.
---

# Codas Ontology

Every other Codas Skill starts here.

1. **Fix the baseline M.** The default branch B is `git symbolic-ref refs/remotes/origin/HEAD`, or
   `main` if that fails. Run `git fetch origin B` first, then compare local and remote B with `git merge-base --is-ancestor` and take the
   newer as M; record its full commit. If they diverge, report both and let the person choose. If the
   fetch fails, use the refs already present and say the remote is unverified. Read other versions only by naming
   the branch and commit.
2. **Read** `docs/ontology/ONTOLOGY.md` at M, then the repository's documentation standard (by default
   `docs/AGENTS.md`), and the Intent it names (by default the root README's opening sections). A missing file is unknown; do not substitute another copy.
3. Be able to say, citing section: which of the four uses a text serves; where each use lives here
   and which homes are missing; what holds now and what counts as drift.
4. **Find the Note rules** from the root `codas.yml` (format in `codas-install`):
   - Note locations: `roots.Note`, otherwise `docs/notes/<lifecycle>/`.
   - Rules file: `notes.rules`, otherwise `docs/notes/AGENTS.md`.
   - Archive Skill: `notes.archiveSkill`, otherwise `codas-note-archive`.
   - Checks: `notes.checks`, otherwise the three `verify-*.ts` under `.agents/codas/hooks/` (in Codas
     itself `src/codas/agent/hooks/notes/`), run from the repository root with `npx --yes tsx@4.21.0`.
   If the configuration does not match the repository, or a candidate is not unique, report and stop.
5. **Host first.** Where the host already has its own Skill or rule for the same situation, use the
   host's; Codas fills only what the host lacks.
6. What is missing or unverified stays unknown, never assumed true.
