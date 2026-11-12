// Source: https://github.com/deepseek-ai/deepseek-harness/blob/687f282e8625c6b8d11ff58211a90524be2e4317/scripts/verify-archived-agent-notes.ts
/** Verify and append-seal the frozen Agent Note archive. */

import { spawnSync } from 'node:child_process'
import { existsSync, readFileSync, readdirSync, writeFileSync } from 'node:fs'
import { resolve } from 'node:path'
import { readAgentNoteClasses, agentNoteRoot, repoRoot } from './agent-note-tree.ts'
import {
  extendArchiveManifest,
  parseArchiveManifest,
  renderArchiveManifest,
  validateArchiveArtifacts,
  validateArchiveManifestExtension,
  type ArchiveManifest,
} from './archived-agent-notes.ts'

const args = process.argv.slice(2)
const writeMode = args.length === 1 && args[0] === '--write'
if (args.length > 0 && !writeMode) {
  console.error(`verify-archived-agent-notes: usage: npx --yes tsx@4.21.0 ${process.argv[1]} [--write]`)
  process.exit(1)
}

const archiveRoot = resolve(agentNoteRoot, 'archived')
const manifestPath = resolve(archiveRoot, 'manifest.json')
const classes = readAgentNoteClasses()
const manifestRepoPath = 'docs/notes/archived/manifest.json'
const errors: string[] = []
const allowedRootFiles = new Set(['AGENTS.md', 'manifest.json'])
const kinds = new Set<string>()

if (existsSync(archiveRoot) && !existsSync(resolve(archiveRoot, 'AGENTS.md'))) errors.push('archived/AGENTS.md is required')
const artifacts = new Map<string, Buffer>()
// An absent archive is empty; baseline checks still reject removal of sealed notes.
for (const entry of existsSync(archiveRoot) ? readdirSync(archiveRoot, { withFileTypes: true }) : []) {
  if (entry.isFile()) {
    if (!allowedRootFiles.has(entry.name)) errors.push(`archived/${entry.name}: unexpected root file`)
    continue
  }
  if (!entry.isDirectory()) {
    errors.push(`archived/${entry.name}: only regular files and kind directories are allowed`)
    continue
  }
  if (!classes.includes(entry.name)) {
    errors.push(`archived/${entry.name}/: unknown Agent Note kind`)
    continue
  }
  kinds.add(entry.name)
  for (const child of readdirSync(resolve(archiveRoot, entry.name), { withFileTypes: true })) {
    const rel = `${entry.name}/${child.name}`
    if (!child.isFile()) {
      errors.push(`${rel}: archived kind directories contain regular files only`)
      continue
    }
    artifacts.set(rel, readFileSync(resolve(archiveRoot, rel)))
  }
}
errors.push(...validateArchiveArtifacts(artifacts))

function runGit(args: string[]): string {
  const result = spawnSync('git', args, { cwd: repoRoot, encoding: 'utf8' })
  if (result.error !== undefined) throw result.error
  if (result.status !== 0) throw new Error(result.stderr.trim() || `git exited with status ${result.status}`)
  return result.stdout
}

function readBaselineManifest(ref: string): ArchiveManifest {
  runGit(['cat-file', '-e', `${ref}^{commit}`])
  const manifestEntry = runGit(['ls-tree', '--name-only', ref, '--', manifestRepoPath]).trim()
  if (manifestEntry === '') return { version: 1, files: {} }
  return parseArchiveManifest(runGit(['show', `${ref}:${manifestRepoPath}`]))
}

let manifest: ArchiveManifest = { version: 1, files: {} }
if (existsSync(manifestPath)) {
  try {
    manifest = parseArchiveManifest(readFileSync(manifestPath, 'utf8'))
  } catch (error: unknown) {
    errors.push(`archived/manifest.json: ${error instanceof Error ? error.message : String(error)}`)
  }
} else if (!writeMode && existsSync(archiveRoot)) {
  errors.push(`archived/manifest.json is required; seal new artifacts with \`npx --yes tsx@4.21.0 ${process.argv[1]} --write\``)
}

// CI supplies its trusted pre-change commit; local writes compare with committed HEAD.
const baselineRef = process.env.DSH_ARCHIVE_BASE_REF ?? 'HEAD'
try {
  // Before a repository's first commit there are no seals to preserve. An explicit
  // CI baseline still has to resolve, and other Git errors remain failures.
  const head = spawnSync('git', ['rev-parse', '--verify', '--quiet', 'HEAD'], { cwd: repoRoot })
  const branch = spawnSync('git', ['symbolic-ref', '--quiet', 'HEAD'], { cwd: repoRoot, encoding: 'utf8' })
  const unborn = process.env.DSH_ARCHIVE_BASE_REF === undefined && head.status === 1 && branch.status === 0
    && spawnSync('git', ['show-ref', '--verify', '--quiet', branch.stdout.trim()], { cwd: repoRoot }).status === 1
  const baseline = unborn ? { version: 1 as const, files: {} } : readBaselineManifest(baselineRef)
  errors.push(...validateArchiveManifestExtension(baseline, manifest))
} catch (error: unknown) {
  errors.push(`archived/manifest.json: cannot read baseline ${JSON.stringify(baselineRef)}: ${error instanceof Error ? error.message : String(error)}`)
}

const extended = extendArchiveManifest(manifest, artifacts)
errors.push(...extended.errors)
if (!writeMode) {
  for (const path of extended.added) errors.push(`${path}: archived artifact is not sealed in manifest.json`)
}

if (errors.length > 0) {
  console.error('verify-archived-agent-notes: archive rules violated:')
  for (const error of errors) console.error(`  ${error}`)
  process.exit(1)
}

if (writeMode && existsSync(archiveRoot)) {
  const rendered = renderArchiveManifest(extended.files)
  if (!existsSync(manifestPath) || readFileSync(manifestPath, 'utf8') !== rendered) {
    writeFileSync(manifestPath, rendered)
  }
  console.log(`verify-archived-agent-notes: sealed ${extended.added.length} new artifact(s); existing seals unchanged.`)
} else {
  console.log(`verify-archived-agent-notes: ${artifacts.size} frozen artifact(s) checked across ${kinds.size} kind(s).`)
}
