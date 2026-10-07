#!/bin/bash
# Install Design ProMax skill — custom location selector
# Usage: ./install-custom.sh

set -e

SKILL_NAME="design-promax"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=== Design ProMax — Custom Installer ==="
echo ""
echo "Select installation location:"
echo "  1) ~/.agents/skills/ (personal — default)"
echo "  2) ~/.claude/skills/  (Claude Code)"
echo "  3) ./skills/          (local project)"
echo "  4) Custom path"
read -p "Choice [1]: " choice

case "${choice:-1}" in
  1) SKILLS_DIR="$HOME/.agents/skills" ;;
  2) SKILLS_DIR="$HOME/.claude/skills" ;;
  3) SKILLS_DIR="$(pwd)/skills" ;;
  4) read -p "Enter path: " SKILLS_DIR ;;
  *) SKILLS_DIR="$HOME/.agents/skills" ;;
esac

echo ""
echo "Installing $SKILL_NAME to $SKILLS_DIR/$SKILL_NAME..."

mkdir -p "$SKILLS_DIR"

if [ -d "$SKILLS_DIR/$SKILL_NAME" ]; then
  echo "Removing existing installation..."
  rm -rf "$SKILLS_DIR/$SKILL_NAME"
fi

cp -r "$SCRIPT_DIR" "$SKILLS_DIR/$SKILL_NAME"
rm -rf "$SKILLS_DIR/$SKILL_NAME/.git"

echo "✅ $SKILL_NAME installed to $SKILLS_DIR/$SKILL_NAME"
echo ""
echo "Available commands: build-ui, component-research, design-audit"
echo "Try: 'Build me a pricing page with HeroUI'"
