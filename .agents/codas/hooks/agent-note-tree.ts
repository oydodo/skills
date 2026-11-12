// Source: https://github.com/deepseek-ai/deepseek-harness/blob/687f282e8625c6b8d11ff58211a90524be2e4317/scripts/agent-note-tree.ts
/**
 * Shared Note-tree structure. Classes come from the target repository's Note rules.
 */

import { execFileSync } from 'node:child_process'
import { globSync, readFileSync, readdirSync } from 'node:fs'
import { resolve, sep } from 'node:path'

export const repoRoot = execFileSync('git', ['rev-parse', '--show-toplevel'], { encoding: 'utf8' }).trim()
export const agentNoteRoot = resolve(repoRoot, 'docs/notes')

/** The closed set of active Agent Note lifecycles (top-level folders under docs/notes/). */
const AGENT_NOTE_LIFECYCLES = ['proposed', 'implemented', 'rejected'] as const

/** Read the Classification table's first column; malformed or missing rules fail closed. */
export function readAgentNoteClasses(): string[] {
  const path = resolve(agentNoteRoot, 'AGENTS.md')
  const fail = (reason: string): never => { throw new Error(`${path}: Classification: ${reason}`) }
  let text: string
  try { text = readFileSync(path, 'utf8') } catch { return fail('cannot read Note rules') }
  const lines = text.split(/\r?\n/)
  const start = lines.findIndex(line => /^## Classification\s*$/.test(line))
  if (start < 0) return fail('section is missing')
  const next = lines.findIndex((line, index) => index > start && /^#{1,2} /.test(line))
  const section = lines.slice(start + 1, next < 0 ? undefined : next)
  const header = section.findIndex(line => /^\s*\|\s*Class\s*\|/.test(line))
  if (header < 0 || !/^\s*\|\s*:?-{3,}:?\s*\|/.test(section[header + 1] ?? '')) {
    return fail('expected a Class table with a separator row')
  }
  const classes: string[] = []
  for (const line of section.slice(header + 2)) {
    if (!/^\s*\|/.test(line)) break
    const cell = line.split('|')[1]?.trim() ?? ''
    const name = /^`([a-z0-9]+(?:-[a-z0-9]+)*)`$/.exec(cell)?.[1]
    if (name === undefined) return fail(`class name must be a backtick-quoted slug: ${JSON.stringify(cell)}`)
    if (classes.includes(name)) return fail(`duplicate class ${JSON.stringify(name)}`)
    classes.push(name)
  }
  if (classes.length === 0) return fail('table is empty')
  return classes
}

/** Historical implemented notes live outside the active lifecycle tree. */
const AGENT_NOTE_ARCHIVE = 'archived'

/** Non-Agent Note Markdown allowed to sit directly at a lifecycle root. */
const ROOT_ALLOWLIST = new Set(['AGENTS.md', 'CLAUDE.md'])

/** One Agent Note file, as discovered by the walker. */
export interface AgentNote {
  lifecycle: string
  /** Path relative to agentNoteRoot. */
  rel: string
  /** `yyyy-mm-dd` from the filename. */
  date: string
}

/**
 * Walk the Agent Note tree, enforcing the structure rules. Returns every valid Agent Note
 * plus one error string per violation (unknown lifecycle or class folder, bad
 * depth, or bad filename). Callers treat a non-empty error list as fatal.
 */
export function walkAgentNoteTree(): { notes: AgentNote[]; errors: string[] } {
  const classes = readAgentNoteClasses()
  const notes: AgentNote[] = []
  const errors: string[] = []
  // The lifecycle set is closed too: any directory under agentNoteRoot that is not
  // a known lifecycle would otherwise hold Agent Notes invisible to the walk below.
  for (const entry of readdirSync(agentNoteRoot, { withFileTypes: true })) {
    if (entry.name === 'INDEX.md') {
      errors.push('structure: INDEX.md — centralized Agent Note indexes are forbidden; browse the lifecycle/class tree or search the repository')
      continue
    }
    if (entry.isDirectory()
      && entry.name !== AGENT_NOTE_ARCHIVE
      && !(AGENT_NOTE_LIFECYCLES as readonly string[]).includes(entry.name)) {
      errors.push(`structure: ${entry.name}/ — unknown lifecycle folder (allowed: ${AGENT_NOTE_LIFECYCLES.join(', ')}, plus ${AGENT_NOTE_ARCHIVE}/)`)
    }
  }
  // Check directories as well as Markdown files, including empty and archived classes.
  for (const lifecycle of [...AGENT_NOTE_LIFECYCLES, AGENT_NOTE_ARCHIVE]) {
    for (const entry of globSync(`${lifecycle}/*`, { cwd: agentNoteRoot, withFileTypes: true })) {
      if (entry.isDirectory() && !classes.includes(entry.name)) {
        errors.push(`structure: ${lifecycle}/${entry.name}/ — unknown class folder (allowed: ${classes.join(', ')})`)
      }
    }
  }
  for (const lifecycle of AGENT_NOTE_LIFECYCLES) {
    for (const match of globSync(`${lifecycle}/**/*.md`, { cwd: agentNoteRoot }).map(path => path.split(sep).join('/')).sort()) {
      const segs = match.split('/')
      // Allowlisted file directly at the lifecycle root (e.g. implemented/AGENTS.md).
      if (segs.length === 2 && ROOT_ALLOWLIST.has(segs[1] ?? '')) continue
      // A Chinese counterpart (foo.zh.md, docs/i18n/README.md) is the SAME Agent Note,
      // indexed via its English filename; the pairing gate owns its consistency.
      if (match.endsWith('.zh.md')) continue
      const cls = segs[1]
      const base = segs[2]
      if (segs.length !== 3 || cls === undefined || base === undefined) {
        errors.push(`structure: ${match} — expected {lifecycle}/{class}/file.md (got depth ${segs.length})`)
        continue
      }
      if (!classes.includes(cls)) {
        errors.push(`structure: ${match} — unknown class folder "${cls}" (allowed: ${classes.join(', ')})`)
        continue
      }
      if (!/^\d{4}-\d{2}-\d{2}-.+\.md$/.test(base)) {
        errors.push(`structure: ${match} — filename must be yyyy-mm-dd-topic.md`)
        continue
      }
      notes.push({ lifecycle, rel: match, date: base.slice(0, 10) })
    }
  }
  return { notes, errors }
}
