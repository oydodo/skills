#!/usr/bin/env bash
# Initialize the DSH Git submodule with only its .agents/skills worktree.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MODULE="upstream/deepseek-harness"
DEST="$ROOT/$MODULE"
ACTION="${1:-}"
if [[ $# -gt 1 || ( -n "$ACTION" && "$ACTION" != "--latest" ) ]]; then
  echo "Usage: bash scripts/checkout-dsh-skills.sh [--latest]" >&2
  exit 2
fi
ENTRY="$(git -C "$ROOT" ls-files --stage -- "$MODULE")"
if [[ "$ENTRY" != "160000 "* ]]; then
  echo "Expected a tracked Git submodule at $MODULE" >&2
  exit 1
fi
PIN="${ENTRY#160000 }"
PIN="${PIN%% *}"
URL="$(git config -f "$ROOT/.gitmodules" --get "submodule.$MODULE.url")"
BRANCH="$(git config -f "$ROOT/.gitmodules" --get "submodule.$MODULE.branch" || echo master)"

git -C "$ROOT" submodule init -- "$MODULE"

if [[ -e "$DEST" && ! -e "$DEST/.git" ]]; then
  if [[ -n "$(ls -A "$DEST")" ]]; then
    echo "Destination exists with unknown files: $DEST; refusing overwrite" >&2
    exit 1
  fi
fi
NEW_CLONE=0
if [[ ! -e "$DEST/.git" ]]; then
  NEW_CLONE=1
  mkdir -p "$(dirname "$DEST")"
  git clone --depth 1 --filter=blob:none --branch "$BRANCH" --no-checkout "$URL" "$DEST"
fi
if [[ "$NEW_CLONE" -eq 0 && -n "$(git -C "$DEST" status --porcelain)" ]]; then
  echo "DSH checkout has local changes; refusing to overwrite" >&2
  exit 1
fi

git -C "$ROOT" submodule absorbgitdirs -- "$MODULE"
git -C "$DEST" sparse-checkout set --no-cone '/.agents/skills/'

if [[ "$ACTION" == "--latest" ]]; then
  git -C "$DEST" fetch --depth 1 --filter=blob:none origin "$BRANCH"
  TARGET="$(git -C "$DEST" rev-parse FETCH_HEAD)"
else
  TARGET="$PIN"
  if ! git -C "$DEST" cat-file -e "${TARGET}^{commit}" 2>/dev/null; then
    git -C "$DEST" fetch --depth 1 --filter=blob:none origin "$TARGET"
  fi
fi

git -C "$DEST" checkout --detach "$TARGET"
if [[ ! -d "$DEST/.agents/skills" ]]; then
  echo "The selected revision has no .agents/skills/ directory" >&2
  exit 1
fi

echo "DSH source: $URL"
echo "Skills: $DEST/.agents/skills"
echo "Commit: $TARGET"
if [[ "$ACTION" == "--latest" ]]; then
  echo "Review and pin update: git add $MODULE && git commit -m 'chore: update DSH skills'"
fi
