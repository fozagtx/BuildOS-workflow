#!/bin/bash
# Install Design ProMax skill for agent harnesses.
# Usage:
#   ./install.sh                         # -> ~/.agents/skills/design-promax
#   ./install.sh ~/.claude/skills        # -> ~/.claude/skills/design-promax
#   ./install.sh ~/.claude/skills design-promax

set -euo pipefail

SKILLS_DIR="${1:-$HOME/.agents/skills}"
SKILL_NAME="${2:-design-promax}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DEST="$SKILLS_DIR/$SKILL_NAME"

echo "Installing $SKILL_NAME to $DEST ..."

mkdir -p "$SKILLS_DIR"
rm -rf "$DEST"
mkdir -p "$DEST"

# Full repo (minus .git)
if command -v rsync >/dev/null 2>&1; then
  rsync -a --exclude .git "$SCRIPT_DIR/" "$DEST/"
else
  cp -R "$SCRIPT_DIR/." "$DEST/"
  rm -rf "$DEST/.git"
fi

# Flatten critical skill entry files to DEST root so agents that only
# list the skill root still see STYLE_PRESETS, THEMES, case-studies, registries.
if [ -d "$DEST/skill" ]; then
  cp -f "$DEST/skill/SKILL.md" \
        "$DEST/skill/THEMES.json" \
        "$DEST/skill/themes.css" \
        "$DEST/skill/STYLE_PRESETS.json" \
        "$DEST/skill/ROUTE_REGISTRY.json" \
        "$DEST/skill/ROUTING.md" \
        "$DEST/skill/ARCHITECTURE.md" \
        "$DEST/" 2>/dev/null || true
  mkdir -p "$DEST/case-studies"
  if [ -d "$DEST/skill/case-studies" ]; then
    cp -f "$DEST/skill/case-studies/"* "$DEST/case-studies/" 2>/dev/null || true
  fi
  # sources: keep nested, also link at root if missing
  if [ ! -e "$DEST/sources" ] && [ -d "$DEST/skill/sources" ]; then
    ln -sfn skill/sources "$DEST/sources"
  fi
fi

# Sanity checks
missing=0
for f in SKILL.md THEMES.json themes.css STYLE_PRESETS.json ROUTE_REGISTRY.json case-studies/vault-otp.md; do
  if [ ! -e "$DEST/$f" ] && [ ! -e "$DEST/skill/$f" ]; then
    echo "  ERROR: missing $f after install"
    missing=1
  else
    echo "  OK $f"
  fi
done

if [ "$missing" -ne 0 ]; then
  echo "Install incomplete."
  exit 1
fi

echo ""
echo "Installed $SKILL_NAME"
echo "  Pro themes     -> THEMES.json + themes.css (ask Default|Brutalism|Glass|Mouve)"
echo "  clean_product  -> STYLE_PRESETS.json"
echo "  case study     -> case-studies/vault-otp.md"
echo "  routes         -> ROUTE_REGISTRY.json"
echo "  showcase       -> Map navigation · Pro AI chat · Music player · Shopping"
echo ""
echo "Try: Build a settings page with design-promax — pick a Pro theme first"
