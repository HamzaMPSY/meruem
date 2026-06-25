#!/usr/bin/env sh
set -eu

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
CODEX_HOME=${CODEX_HOME:-"$HOME/.codex"}
SKILLS_DIR="$CODEX_HOME/skills"
MERUEM_HOME="$CODEX_HOME/meruem"

echo "Installing Meruem workflow pack"
echo "Repository: $ROOT_DIR"
echo "Codex home: $CODEX_HOME"

mkdir -p "$SKILLS_DIR" "$MERUEM_HOME"

for skill_dir in "$ROOT_DIR"/skills/*; do
  [ -d "$skill_dir" ] || continue
  skill_name=$(basename "$skill_dir")
  target="$SKILLS_DIR/$skill_name"

  if [ -e "$target" ] || [ -L "$target" ]; then
    backup="$target.backup.$(date +%Y%m%d%H%M%S)"
    echo "Backing up existing skill: $target -> $backup"
    mv "$target" "$backup"
  fi

  echo "Installing skill: $skill_name"
  cp -R "$skill_dir" "$target"
done

mkdir -p "$MERUEM_HOME/docs" "$MERUEM_HOME/templates"
cp -R "$ROOT_DIR/docs/." "$MERUEM_HOME/docs/"
cp -R "$ROOT_DIR/.tickets/templates/." "$MERUEM_HOME/templates/"
cp "$ROOT_DIR/AGENTS.md" "$MERUEM_HOME/AGENTS.md"

echo
echo "Meruem installed."
echo "Start a new Codex session, then use:"
echo "  \$meruem <your task>"
echo
echo "Bundled skills installed into:"
echo "  $SKILLS_DIR"
echo
echo "Support docs and templates installed into:"
echo "  $MERUEM_HOME"
