// Source: https://github.com/deepseek-ai/deepseek-harness/blob/687f282e8625c6b8d11ff58211a90524be2e4317/scripts/verify-agent-note-classification.ts
/**
 * Enforce Agent Note lifecycle/class paths and dated filenames. Structural rules
 * are shared with `agent-note-tree.ts` and follow the upstream Agent Note rules.
 */

import { existsSync } from 'node:fs'
import { resolve } from 'node:path'
import { agentNoteRoot, repoRoot, walkAgentNoteTree } from './agent-note-tree.ts'

const { notes, errors } = walkAgentNoteTree()

// Keep the former homes unavailable so new notes cannot silently escape this tree.
for (const legacyRoot of ['docs/rfc', 'docs/rfcs']) {
  if (existsSync(resolve(repoRoot, legacyRoot))) {
    errors.push(`legacy-path: ${legacyRoot}/ is forbidden — put Agent Notes under ${agentNoteRoot}/`)
  }
}

if (errors.length === 0) {
  console.log(`verify-agent-note-classification: ${notes.length} Agent Note(s) checked in ${agentNoteRoot}, structure consistent.`)
  process.exit(0)
}

console.error('verify-agent-note-classification: violations found:')
for (const e of errors) console.error(`  ${e}`)
process.exit(1)
