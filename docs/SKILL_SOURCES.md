# Skill Sources

This file records the skill inventory visible while this public Meruem package was created. Bundled skills have public copies in this repository under `skills/`.

## Core Meruem Skill

| Skill | Purpose | Source |
| --- | --- | --- |
| `meruem` | Project workflow rules for tickets, orchestration, council review, design, Graphify, and completion checks. | `skills/meruem/SKILL.md` |

## System Skills

| Skill | Purpose | Source |
| --- | --- | --- |
| `imagegen` | Generate or edit raster images. | `/Users/hamzaelmakrini/.codex/skills/.system/imagegen/SKILL.md` |
| `openai-docs` | Use official OpenAI docs for OpenAI product/API questions. | `/Users/hamzaelmakrini/.codex/skills/.system/openai-docs/SKILL.md` |
| `plugin-creator` | Create and scaffold Codex plugins. | `/Users/hamzaelmakrini/.codex/skills/.system/plugin-creator/SKILL.md` |
| `skill-creator` | Create or update Codex skills. | `/Users/hamzaelmakrini/.codex/skills/.system/skill-creator/SKILL.md` |
| `skill-installer` | Install Codex skills from curated lists or GitHub repo paths. | `/Users/hamzaelmakrini/.codex/skills/.system/skill-installer/SKILL.md` |

## Project And Personal Skills

| Skill | Purpose | Source |
| --- | --- | --- |
| `academic-pptx` | Structure academic presentations. | `/Users/hamzaelmakrini/.codex/skills/academic-pptx-skill/SKILL.md` |
| `aura` | Full-stack orchestration, modes, security hooks, agents, and development engine. | `skills/aura/SKILL.md` |
| `codebase-explainer` | Explain, summarize, document, or present codebases. | `skills/codebase-explainer/SKILL.md` |
| `deep-research` | Multi-source web research with citations. | `skills/deep-research/SKILL.md` |
| `design-taste-frontend` | Anti-template frontend design for landing pages, portfolios, and redesigns. | `skills/design-taste-frontend/SKILL.md` |
| `emil-design-eng` | UI polish, component design, motion, and interaction details. | `skills/emil-design-eng/SKILL.md` |
| `frontend-design` | Create distinctive production-grade frontend interfaces. | `skills/frontend-design/SKILL.md` |
| `graphify` | Convert inputs into knowledge graphs, communities, HTML, JSON, and audit reports. | `skills/graphify/SKILL.md` |
| `impeccable` | Audit and improve frontend UX, IA, hierarchy, accessibility, motion, and design systems. | `skills/impeccable/SKILL.md` |
| `karpathy-guidelines` | Coding discipline for surgical changes, assumptions, and verification. | `skills/karpathy-guidelines/SKILL.md` |
| `prompt-preflight` | Critique and improve prompts before model execution. | `skills/prompt-preflight/SKILL.md` |
| `redwood-powerpoint-builder` | Build Oracle Redwood PowerPoint presentations from the bundled template. | `/Users/hamzaelmakrini/.codex/skills/redwood-powerpoint-builder/SKILL.md` |
| `ruflo` | Multi-agent orchestration, swarm planning, memory, and coordination with Ruflo. | `/Users/hamzaelmakrini/.codex/skills/ruflo/SKILL.md` |
| `vizarr-implementation` | Implement and review the Vizarr satellite Zarr viewer repository. | `/Users/hamzaelmakrini/.codex/skills/vizarr-implementation/SKILL.md` |

The project-specific or brand-specific skills above are listed for provenance but are not bundled by default. Keep Meruem's default bundle general-purpose unless a skill supports a broad workflow used by many repositories.

## Plugin Skills

| Skill | Purpose | Source |
| --- | --- | --- |
| `browser:control-in-app-browser` | Control the in-app browser for inspection and UI verification. | `/Users/hamzaelmakrini/.codex/plugins/cache/openai-bundled/browser/26.527.60818/skills/control-in-app-browser/SKILL.md` |
| `slack:slack` | Read Slack context and route Slack workflows. | `/Users/hamzaelmakrini/.codex/plugins/cache/openai-curated-remote/slack/0.1.2/skills/slack/SKILL.md` |
| `slack:slack-channel-summarization` | Summarize activity from one Slack channel. | `/Users/hamzaelmakrini/.codex/plugins/cache/openai-curated-remote/slack/0.1.2/skills/slack-channel-summarization/SKILL.md` |
| `slack:slack-daily-digest` | Create a daily Slack digest. | `/Users/hamzaelmakrini/.codex/plugins/cache/openai-curated-remote/slack/0.1.2/skills/slack-daily-digest/SKILL.md` |
| `slack:slack-notification-triage` | Triage recent Slack activity into priorities or tasks. | `/Users/hamzaelmakrini/.codex/plugins/cache/openai-curated-remote/slack/0.1.2/skills/slack-notification-triage/SKILL.md` |
| `slack:slack-outgoing-message` | Compose, draft, or refine outbound Slack content. | `/Users/hamzaelmakrini/.codex/plugins/cache/openai-curated-remote/slack/0.1.2/skills/slack-outgoing-message/SKILL.md` |
| `slack:slack-reply-drafting` | Draft Slack replies from available context. | `/Users/hamzaelmakrini/.codex/plugins/cache/openai-curated-remote/slack/0.1.2/skills/slack-reply-drafting/SKILL.md` |
| `workspace-agents:workspace-agents-api-triggers` | Plan Workspace Agents API-trigger integrations. | `/Users/hamzaelmakrini/.codex/plugins/cache/openai-curated-remote/workspace-agents/0.1.10/skills/workspace-agents-api-triggers/SKILL.md` |
| `workspace-agents:workspace-agents-build-agent` | Build or edit workspace/custom agents. | `/Users/hamzaelmakrini/.codex/plugins/cache/openai-curated-remote/workspace-agents/0.1.10/skills/workspace-agents-build-agent/SKILL.md` |
| `workspace-agents:workspace-agents-manage-agent` | Find, inspect, and compare workspace/custom agents. | `/Users/hamzaelmakrini/.codex/plugins/cache/openai-curated-remote/workspace-agents/0.1.10/skills/workspace-agents-manage-agent/SKILL.md` |

## External Concepts Referenced By Meruem

These are not bundled as skill files in this repository, but Meruem uses them as workflow influences:

| Source | How Meruem Uses It |
| --- | --- |
| Aura Kit | Required orchestration layer for sub-agent spawning, skill routing, and workflow coordination. |
| OpenAI Swarm patterns | Educational handoff pattern for bounded agents, context variables, and explicit transfers. |
| OpenAI Agents SDK | Preferred production direction over Swarm for runtime agent implementations. |
| Plan Plus-style brainstorming | Pre-ticket discovery structure: intent, local research, alternatives, YAGNI, and decision brief. |
| Local GPT-5.5 Council | Local sub-agent review pattern for high-impact choices. |
| Fable-style prompt architecture | Prompt structure inspiration for execution frames, precedence, context hygiene, and output contracts. |

## Maintenance Rule

When adding, removing, or renaming a skill used by Meruem:

1. Update `skills/meruem/SKILL.md`.
2. Update this source inventory.
3. Update `meruem.manifest.json`.
4. Update installation or workflow docs if the user-facing behavior changes.
