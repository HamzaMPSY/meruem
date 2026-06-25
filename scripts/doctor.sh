#!/usr/bin/env sh
set -eu

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
CODEX_HOME=${CODEX_HOME:-"$HOME/.codex"}
SKILLS_DIR="$CODEX_HOME/skills"
MERUEM_HOME="$CODEX_HOME/meruem"

required_skills="aura meruem codebase-explainer deep-research design-taste-frontend emil-design-eng frontend-design graphify impeccable karpathy-guidelines prompt-preflight"
status=0

echo "Meruem doctor"
echo "Repository: $ROOT_DIR"
echo "Codex home: $CODEX_HOME"
echo

for skill in $required_skills; do
  if [ -f "$SKILLS_DIR/$skill/SKILL.md" ]; then
    echo "ok   skill installed: $skill"
  else
    echo "miss skill missing:    $skill"
    status=1
  fi
done

echo

if [ -d "$MERUEM_HOME/docs" ]; then
  echo "ok   support docs installed"
else
  echo "miss support docs missing"
  status=1
fi

if [ -d "$MERUEM_HOME/templates" ]; then
  echo "ok   ticket templates installed"
else
  echo "miss ticket templates missing"
  status=1
fi

if command -v python3 >/dev/null 2>&1; then
  echo "ok   python3 available for Graphify runtime paths"
else
  echo "warn python3 not found; Graphify package install may fail when invoked"
fi

echo

if [ "$status" -eq 0 ]; then
  echo "Meruem installation looks complete."
else
  echo "Meruem installation is incomplete. Run: sh scripts/install.sh"
fi

exit "$status"
