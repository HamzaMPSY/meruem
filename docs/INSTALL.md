# Install Meruem

Meruem is distributed as a workflow pack. Installing Meruem should install Meruem and the supporting skills it calls during real work.

## One Command Install

From the repository root:

```sh
sh scripts/install.sh
```

By default, this installs skills into:

```text
~/.codex/skills/
```

and Meruem support docs/templates into:

```text
~/.codex/meruem/
```

Set `CODEX_HOME` if your Codex home lives somewhere else:

```sh
CODEX_HOME=/path/to/codex-home sh scripts/install.sh
```

Restart your Codex session if your environment only loads skills at startup.

## Verify Installation

Run:

```sh
sh scripts/doctor.sh
```

The doctor checks that all bundled skills, support docs, and ticket templates are installed.

## Bundled Skills

The installer brings these skills together:

| Skill | Why Meruem Needs It |
| --- | --- |
| `meruem` | Main workflow, gates, ticket rules, and completion checklist. |
| `aura` | Orchestration and sub-agent routing. |
| `codebase-explainer` | Repository onboarding, architecture summaries, and presentation-ready explanations. |
| `graphify` | Knowledge graph workflow for domain entities, relationships, and data flow. |
| `karpathy-guidelines` | Surgical coding discipline and verification guardrails. |
| `impeccable` | Frontend UX, visual hierarchy, accessibility, and quality review. |
| `frontend-design` | Production-grade frontend creation with distinctive visual direction. |
| `design-taste-frontend` | Anti-template frontend and redesign taste checks. |
| `emil-design-eng` | UI polish, interaction feel, and motion details. |
| `deep-research` | External research workflow when the user explicitly allows it. |
| `prompt-preflight` | Prompt, ticket, council, and sub-agent brief quality checks. |

## Development Install

Use a symlink if you want edits in this repository to affect your local skill immediately:

```sh
mkdir -p ~/.codex/skills
for skill in skills/*; do
  name=$(basename "$skill")
  if [ -e "$HOME/.codex/skills/$name" ] || [ -L "$HOME/.codex/skills/$name" ]; then
    mv "$HOME/.codex/skills/$name" "$HOME/.codex/skills/$name.backup.$(date +%Y%m%d%H%M%S)"
  fi
  ln -s "$(pwd)/$skill" "$HOME/.codex/skills/$name"
done
```

This is for contributors. The normal install command is safer because it backs up existing skill folders before replacing them.

## Uninstall

Uninstall requires explicit confirmation:

```sh
MERUEM_UNINSTALL_CONFIRM=yes sh scripts/uninstall.sh
```

Set `CODEX_HOME` the same way as installation if you installed into a custom location.

## Vendor Into Another Repo

Copy these files into another project:

```text
skills/
AGENTS.md
scripts/install.sh
docs/WORKFLOW.md
docs/BEST_PRACTICES.md
docs/SKILL_SOURCES.md
.tickets/templates/
```

Then update `AGENTS.md` in the target repo so agents know where the local Meruem pack lives.

## Quick Test

Start a new agent session and ask:

```text
$meruem read this repo and tell me the workflow gates before you edit anything
```

A correct installation should mention local context gathering, pre-ticket brainstorming, ticket workflow, Aura orchestration, council gating, design-skill coordination, Graphify, and practical verification.

## Requirements

The repository bundles the workflow skills. Your machine still needs:

- Codex skills
- Local sub-agent spawning for council review
- A shell that can run `sh scripts/install.sh`
- Python/pip only when you actually invoke Graphify's Python package workflow

If one of these is unavailable, Meruem requires the agent to state the gap and continue with the closest honest fallback.
