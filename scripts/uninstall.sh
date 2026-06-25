#!/usr/bin/env sh
set -eu

CODEX_HOME=${CODEX_HOME:-"$HOME/.codex"}
SKILLS_DIR="$CODEX_HOME/skills"
MERUEM_HOME="$CODEX_HOME/meruem"
required_skills="aura meruem codebase-explainer deep-research design-taste-frontend emil-design-eng frontend-design graphify impeccable karpathy-guidelines prompt-preflight"

if [ "${MERUEM_UNINSTALL_CONFIRM:-}" != "yes" ]; then
  echo "This removes bundled Meruem skills from: $SKILLS_DIR"
  echo "It also removes support files from: $MERUEM_HOME"
  echo
  echo "Run with confirmation:"
  echo "  MERUEM_UNINSTALL_CONFIRM=yes sh scripts/uninstall.sh"
  exit 2
fi

for skill in $required_skills; do
  target="$SKILLS_DIR/$skill"
  if [ -e "$target" ] || [ -L "$target" ]; then
    echo "Removing skill: $skill"
    rm -rf "$target"
  fi
done

if [ -d "$MERUEM_HOME" ]; then
  echo "Removing Meruem support files"
  rm -rf "$MERUEM_HOME"
fi

echo "Meruem uninstalled."
