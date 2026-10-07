#!/usr/bin/env bash
# Install BuildOS-workflow skills into all known agent harnesses.
# Symlinks each skill from BuildOS-workflow/skills/ into the harness skills directory.

set -euo pipefail

REPO_SKILLS="$HOME/BuildOS-workflow/skills"

if [[ ! -d "$REPO_SKILLS" ]]; then
  echo "Error: $REPO_SKILLS not found" >&2
  exit 1
fi

HARNESS_DIRS=(
  "$HOME/.agents/skills"
  "$HOME/.claude/skills"
  "$HOME/.codex/skills"
  "$HOME/.cursor/skills"
  "$HOME/.grok/skills"
  "$HOME/.config/devin/skills"
  "$HOME/.devin/skills"
  "$HOME/.augment/skills"
  "$HOME/.pi/skills"
)

for dir in "${HARNESS_DIRS[@]}"; do
  if [[ -d "$dir" ]]; then
    for skill_path in "$REPO_SKILLS"/*; do
      name=$(basename "$skill_path")
      target="$dir/$name"
      if [[ -e "$target" || -L "$target" ]]; then
        echo "Skipping $target (already exists)"
      else
        ln -s "$skill_path" "$target"
        echo "Linked $target -> $skill_path"
      fi
    done
  else
    echo "Skipping $dir (does not exist)"
  fi
done

echo "Done. Restart your agent harnesses to load the BuildOS-workflow skills."
