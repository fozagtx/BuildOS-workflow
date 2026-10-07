#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

required_files=(
  ".gitignore"
  "ARTICLE.md"
  "README.md"
  "LICENSE"
  "CLAUDE.md"
  "SUBMISSION.md"
  "install.sh"
  "install-custom.sh"
  "skill/SKILL.md"
  "skill/router.md"
  "skill/problem-workflow.md"
  "skill/workaround-map.md"
  "skill/signal-scores.md"
  "skill/framing-reject.md"
  "skill/sharpen.md"
  "skill/worked-example.md"
  "skill/edge-cases.md"
  "evals/canonical-market-woman.md"
  "evals/edge-cases.json"
  "evals/ai-for-x.json"
  "evals/triggers.json"
  "evals/results.md"
  "evals/trigger-results.md"
  "scripts/package_skill.sh"
  "agents/problem-analyst.md"
  "agents/workaround-mapper.md"
  "agents/framing-rejector.md"
  "agents/skill-demo-coach.md"
  "commands/problem-sprint.md"
  "commands/map-workaround.md"
  "commands/reject-framing.md"
  "commands/skill-demo.md"
  "commands/check-edges.md"
  "commands/route.md"
  "rules/no-solutioning.md"
  "tests/validate_structure.sh"
  "tests/validate_edge_cases.sh"
)

for file in "${required_files[@]}"; do
  if [[ ! -f "$ROOT_DIR/$file" ]]; then
    echo "Missing required file: $file" >&2
    exit 1
  fi
done

if ! grep -q '^name: problem-finder$' "$ROOT_DIR/skill/SKILL.md"; then
  echo "Missing skill name frontmatter." >&2
  exit 1
fi

if ! grep -q '^description: .*Use when ' "$ROOT_DIR/skill/SKILL.md"; then
  echo "Missing actionable description frontmatter." >&2
  exit 1
fi

for linked in router.md problem-workflow.md workaround-map.md signal-scores.md framing-reject.md sharpen.md worked-example.md edge-cases.md; do
  if ! grep -q "$linked" "$ROOT_DIR/skill/SKILL.md"; then
    echo "SKILL.md does not link $linked" >&2
    exit 1
  fi
done

for heading in \
  "**Original framing:**" \
  "**Who does the work:**" \
  "**Current workarounds:**" \
  "**Signal scores:**" \
  "**Rejected obvious framings:**" \
  "**Ranked sharpened problems:**"
do
  if ! grep -qF "$heading" "$ROOT_DIR/skill/sharpen.md"; then
    echo "sharpen.md missing report heading: $heading" >&2
    exit 1
  fi
done

bash -n "$ROOT_DIR/install.sh"
bash -n "$ROOT_DIR/install-custom.sh"
bash -n "$ROOT_DIR/scripts/package_skill.sh"
bash -n "$ROOT_DIR/tests/validate_structure.sh"
bash -n "$ROOT_DIR/tests/validate_edge_cases.sh"

if ! grep -q 'Clone elsewhere → install into a skills dir. Never install onto the clone.' "$ROOT_DIR/README.md"; then
  echo "README must say: clone elsewhere → install into a skills dir. Never install onto the clone." >&2
  exit 1
fi

if ! grep -q 'TARGET_DIR/.git' "$ROOT_DIR/install-custom.sh" || ! grep -q 'TARGET_DIR/install.sh' "$ROOT_DIR/install-custom.sh"; then
  echo "install-custom.sh must refuse if TARGET_DIR has .git and install.sh." >&2
  exit 1
fi

if ! grep -q 'GitHub Releases' "$ROOT_DIR/README.md" || ! grep -q 'problem-finder.skill' "$ROOT_DIR/README.md"; then
  echo "README Installation must mention the GitHub Release download of problem-finder.skill." >&2
  exit 1
fi

blocked_terms=(
  "$(printf "%s%s" "Co" "dex")"
  "$(printf "%s%s" "Anth" "ropic")"
  "$(printf "%s%s%s" "Co-Authored-" "By:" " ")"
  "$(printf "%s%s" "noreply@" "anthropic.com")"
)

for term in "${blocked_terms[@]}"; do
  if grep -R -n --exclude-dir=.git -- "$term" "$ROOT_DIR" >/tmp/problem_finder_hygiene.txt; then
    cat /tmp/problem_finder_hygiene.txt >&2
    echo "Attribution hygiene check failed." >&2
    exit 1
  fi
done

"$ROOT_DIR/tests/validate_edge_cases.sh"

echo "Structure validation passed."
