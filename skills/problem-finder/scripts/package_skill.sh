#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="${1:-"$ROOT_DIR/dist"}"
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT

mkdir -p "$STAGE/problem-finder" "$OUT_DIR"
cp -R "$ROOT_DIR/skill/." "$STAGE/problem-finder/"

(
  cd "$STAGE"
  zip -qr "$OUT_DIR/problem-finder.skill" problem-finder
)

echo "Wrote $OUT_DIR/problem-finder.skill"
