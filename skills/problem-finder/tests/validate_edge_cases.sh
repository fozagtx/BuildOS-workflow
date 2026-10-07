#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FAIL=0

fail() {
  echo "$1" >&2
  FAIL=1
}

python3 -m json.tool "$ROOT_DIR/evals/edge-cases.json" >/dev/null
python3 -m json.tool "$ROOT_DIR/evals/ai-for-x.json" >/dev/null
python3 -m json.tool "$ROOT_DIR/evals/triggers.json" >/dev/null

skill_lines="$(wc -l < "$ROOT_DIR/skill/SKILL.md" | tr -d ' ')"
if (( skill_lines > 200 )); then
  fail "skill/SKILL.md is $skill_lines lines; must stay under 200."
fi

for heading in \
  "**Original framing:**" \
  "**Who does the work:**" \
  "**Current workarounds:**" \
  "**Signal scores:**" \
  "**Rejected obvious framings:**" \
  "**Ranked sharpened problems:**"
do
  if ! grep -qF "$heading" "$ROOT_DIR/skill/sharpen.md"; then
    fail "sharpen.md missing report heading: $heading"
  fi
  if ! grep -qF "$heading" "$ROOT_DIR/skill/edge-cases.md"; then
    fail "edge-cases.md suspect report missing heading: $heading"
  fi
done

if ! grep -q 'problem-workflow.md' "$ROOT_DIR/skill/SKILL.md" || ! grep -q 'sharpen.md' "$ROOT_DIR/skill/SKILL.md"; then
  fail "Full-run routing must name problem-workflow.md and sharpen.md."
fi

if ! grep -q 'edge-cases.md' "$ROOT_DIR/skill/SKILL.md"; then
  fail "SKILL.md does not link edge-cases.md"
fi

if ! grep -q 'router.md' "$ROOT_DIR/skill/SKILL.md"; then
  fail "SKILL.md does not link router.md"
fi

if ! grep -q 'The report template is required' "$ROOT_DIR/skill/SKILL.md"; then
  fail "SKILL.md must say the report template is required."
fi

if ! grep -q 'obvious' "$ROOT_DIR/skill/router.md" || ! grep -q 'non-obvious' "$ROOT_DIR/skill/router.md"; then
  fail "router.md must classify obvious vs non-obvious before solutions."
fi

for q in \
  "Whose hands are on the mess" \
  "What do they already do that day" \
  "Who would have to change a rule"
do
  if ! grep -q "$q" "$ROOT_DIR/skill/workaround-map.md"; then
    fail "workaround-map.md missing doer question: $q"
  fi
done

if ! grep -q 'Do not invent workarounds' "$ROOT_DIR/skill/workaround-map.md"; then
  fail "workaround-map.md must forbid inventing workarounds."
fi

if ! grep -q 'No solution section' "$ROOT_DIR/skill/sharpen.md"; then
  fail "sharpen.md must forbid a solution section."
fi

if ! grep -q 'stay inside the #1' "$ROOT_DIR/skill/sharpen.md"; then
  fail "sharpen.md must lock after-report follow-ups to #1."
fi

missing_ids="$(python3 - <<'PY' "$ROOT_DIR"
import json, re, sys
from pathlib import Path
root = Path(sys.argv[1])
text = (root / "skill/edge-cases.md").read_text()
table_ids = re.findall(r"\|\s*(E\d{2})\s*\|", text)
if table_ids != [f"E{i:02d}" for i in range(1, 31)]:
    print("edge-cases.md IDs are not E01-E30 in order: " + ",".join(table_ids))
evals = json.loads((root / "evals/edge-cases.json").read_text())
eval_ids = [item["id"] for item in evals["evals"]]
if eval_ids != [f"E{i:02d}" for i in range(1, 31)]:
    print("evals/edge-cases.json IDs are not E01-E30 in order: " + ",".join(eval_ids))
ai = json.loads((root / "evals/ai-for-x.json").read_text())
x_ids = [item["id"] for item in ai["evals"]]
if x_ids != [f"X{i:02d}" for i in range(1, 11)]:
    print("evals/ai-for-x.json IDs are not X01-X10: " + ",".join(x_ids))
if len(ai["evals"]) != 10:
    print("ai-for-x suite must contain 10 prompts")
triggers = json.loads((root / "evals/triggers.json").read_text())
if len(triggers["should_trigger"]) < 10:
    print("triggers should_trigger must have at least 10 prompts")
if len(triggers["near_miss"]) < 8:
    print("triggers near_miss must have at least 8 prompts")
PY
)"

if [[ -n "$missing_ids" ]]; then
  fail "$missing_ids"
fi

canon_check="$(python3 - <<'PY' "$ROOT_DIR"
import re, sys
from pathlib import Path
root = Path(sys.argv[1])
canon = (root / "evals/canonical-market-woman.md").read_text()
ranked = re.findall(r"^\d+\.\s+(.+)$", canon, re.M)
if len(ranked) != 3:
    print("canonical-market-woman.md must contain exactly 3 ranked sentences")
    raise SystemExit
files = [
    root / "evals/canonical-market-woman.md",
    root / "ARTICLE.md",
    root / "skill/worked-example.md",
    root / "SUBMISSION.md",
    root / "commands/skill-demo.md",
]
for path in files:
    text = path.read_text()
    if "evals/canonical-market-woman.md" not in text and path.name != "canonical-market-woman.md":
        print(f"{path.relative_to(root)} must point at evals/canonical-market-woman.md")
    if path.name in {"skill-demo.md", "SUBMISSION.md"}:
        continue
    for sentence in ranked:
        if sentence not in text:
            print(f"{path.relative_to(root)} missing ranked sentence: {sentence}")
desc = ""
for line in (root / "skill/SKILL.md").read_text().splitlines():
    if line.startswith("description:"):
        desc = line.split(":", 1)[1].strip()
        break
if len(desc) > 1024:
    print(f"skill/SKILL.md description is {len(desc)} characters; must stay under 1024")
if "Use when" not in desc:
    print("skill/SKILL.md description must stay actionable")
skill = (root / "skill/SKILL.md").read_text()
if "find-next-crypto-idea" not in skill:
    print("skill/SKILL.md must hand crypto-idea search to find-next-crypto-idea")
if "pure implementation" not in skill.lower():
    print("skill/SKILL.md must refuse pure implementation")
banned = [
    "They are not.",
    "they are not.",
    "is not the same as",
    "It's not just",
    "it's not just",
    "failure mode is not",
    "Obvious is not",
    "It's not X",
    "It is not ",
]
copy_files = [
    root / "ARTICLE.md",
    root / "README.md",
    root / "SUBMISSION.md",
    root / "CLAUDE.md",
    root / "skill/SKILL.md",
]
for path in copy_files:
    text = path.read_text()
    for phrase in banned:
        if phrase in text:
            print(f"{path.relative_to(root)} still has contrast-slop: {phrase!r}")
PY
)"

if [[ -n "$canon_check" ]]; then
  fail "$canon_check"
fi

pkg_dir="$(mktemp -d)"
bash "$ROOT_DIR/scripts/package_skill.sh" "$pkg_dir" >/dev/null
zip_list="$(unzip -Z1 "$pkg_dir/problem-finder.skill")"
rm -rf "$pkg_dir"
for needed in \
  "problem-finder/SKILL.md" \
  "problem-finder/router.md" \
  "problem-finder/problem-workflow.md" \
  "problem-finder/workaround-map.md" \
  "problem-finder/signal-scores.md" \
  "problem-finder/framing-reject.md" \
  "problem-finder/sharpen.md" \
  "problem-finder/worked-example.md" \
  "problem-finder/edge-cases.md"
do
  if ! grep -qxF "$needed" <<<"$zip_list"; then
    fail "problem-finder.skill missing $needed"
  fi
done

if (( FAIL != 0 )); then
  echo "Edge-case validation failed." >&2
  exit 1
fi

echo "Edge-case validation passed."
