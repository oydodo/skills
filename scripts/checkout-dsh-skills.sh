#!/usr/bin/env bash
# Fetch only DeepSeek Harness's .agents/skills subtree (not the entire Harness worktree).
# Third-party source is NOT committed to the skills repository.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SOURCE_URL="https://github.com/deepseek-ai/deepseek-harness.git"
DEST="$ROOT/upstream/dsh-skills"
PIN_FILE="$ROOT/registry/dsh-upstream.sha"

if [[ "$#" -gt 1 ]]; then
  echo "Usage: bash scripts/checkout-dsh-skills.sh [--latest]" >&2
  exit 2
fi
ACTION=""
if [[ "$#" -eq 1 ]]; then
  ACTION="$1"
fi
if [[ -n "$ACTION" && "$ACTION" != "--latest" ]]; then
  echo "Usage: bash scripts/checkout-dsh-skills.sh [--latest]" >&2
  exit 2
fi

if [[ "$ACTION" == "--latest" ]]; then
  SHA="$(git ls-remote "$SOURCE_URL" refs/heads/master | awk 'NR==1 {print $1}')"
  [[ "$SHA" =~ ^[0-9a-f]{40}$ ]] || { echo "Failed to resolve upstream master" >&2; exit 1; }
else
  SHA="$(tr -d '[:space:]' < "$PIN_FILE")"
fi

[[ "$SHA" =~ ^[0-9a-f]{40}$ ]] || { echo "Invalid pinned SHA in $PIN_FILE" >&2; exit 1; }

if [[ -e "$DEST" && ! -d "$DEST/.git" ]]; then
  echo "Destination exists but is not a standalone Git clone: $DEST" >&2
  exit 1
fi

if [[ ! -d "$DEST/.git" ]]; then
  mkdir -p "$(dirname "$DEST")"
  # No initial checkout: avoid downloading application blobs before enabling sparse patterns.
  git clone --depth=1 --filter=blob:none --branch master --no-checkout "$SOURCE_URL" "$DEST"
else
  [[ -z "$(git -C "$DEST" status --porcelain)" ]] || {
    echo "Local DSH checkout has changes; refusing to overwrite them" >&2
    exit 1
  }
fi

# Non-cone mode excludes even root-level application files.
git -C "$DEST" sparse-checkout set --no-cone '/.agents/skills/'

if ! git -C "$DEST" cat-file -e "$SHA^{commit}" 2>/dev/null; then
  git -C "$DEST" fetch --depth=1 --filter=blob:none origin "$SHA"
fi
git -C "$DEST" checkout --detach "$SHA"

[[ -d "$DEST/.agents/skills" ]] || {
  echo "Pinned revision lacks .agents/skills" >&2
  exit 1
}

if [[ "$ACTION" == "--latest" ]]; then
  printf '%s\n' "$SHA" > "$PIN_FILE"
  echo "Updated revision pin: $PIN_FILE"
fi

echo "DSH Skills available at: $DEST/.agents/skills"
echo "Pinned revision: $SHA"
