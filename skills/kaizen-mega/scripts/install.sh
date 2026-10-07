#!/usr/bin/env bash
# Install the kaizen-mega skill into all known agent harnesses.
# Creates symlinks from the canonical ~/.agents/skills/kaizen-mega/ source.

set -euo pipefail

SOURCE="$HOME/.agents/skills/kaizen-mega"

if [[ ! -d "$SOURCE" ]]; then
  echo "Error: canonical source not found at $SOURCE" >&2
  exit 1
fi

HARNESS_DIRS=(
  "$HOME/.claude/skills"
  "$HOME/.codex/skills"
  "$HOME/.cursor/skills"
  "$HOME/.grok/skills"
  "$HOME/.config/devin/skills"
  "$HOME/.devin/skills"
  "$HOME/.augment/skills"
  "$HOME/.kilo/skills"
  "$HOME/.pi/skills"
)

for dir in "${HARNESS_DIRS[@]}"; do
  if [[ -d "$dir" ]]; then
    target="$dir/kaizen-mega"
    if [[ -e "$target" || -L "$target" ]]; then
      echo "Skipping $target (already exists)"
    else
      ln -s "$SOURCE" "$target"
      echo "Linked $target -> $SOURCE"
    fi
  else
    echo "Skipping $dir (does not exist)"
  fi
done

echo "Done. Restart your agent harnesses to load kaizen-mega."
