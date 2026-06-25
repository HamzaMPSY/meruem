# Meruem

![Meruem workflow artwork](assets/meruem-artwork.svg)

Meruem is a public workflow pack for Codex-style coding agents: a disciplined way to plan, delegate, design, build, review, and finish software work without turning every request into either chaos or ceremony.

It is not a framework, package, or runtime. It is a shared operating system for agentic development: the rules, handoffs, decision gates, and documentation patterns that tell an AI coding agent how to behave inside a repository.

## What Meruem Gives You

- A canonical `$meruem` skill in [skills/meruem/SKILL.md](skills/meruem/SKILL.md)
- Agent-facing repository instructions in [AGENTS.md](AGENTS.md)
- A public installation guide in [docs/INSTALL.md](docs/INSTALL.md)
- A fast first-run guide in [docs/QUICKSTART.md](docs/QUICKSTART.md)
- A practical workflow manual in [docs/WORKFLOW.md](docs/WORKFLOW.md)
- Best practices in [docs/BEST_PRACTICES.md](docs/BEST_PRACTICES.md)
- Ticket templates in [.tickets/templates/](.tickets/templates)
- A full source inventory for every known skill in [docs/SKILL_SOURCES.md](docs/SKILL_SOURCES.md)
- Contributor guidance in [CONTRIBUTING.md](CONTRIBUTING.md)

## The Short Version

Meruem makes an agent do four things before it changes code:

1. Understand the request and local repo context.
2. Create or read the ticket that defines the work.
3. Choose the smallest useful approach, with council review only when the decision is genuinely high impact.
4. Build first, verify practically, and avoid fake productivity.

For UI work, Meruem raises the bar: it requires human-centered UX, design-skill coordination, accessible states, purposeful motion, and the removal of generic placeholder design.

For multi-agent work, Meruem keeps delegation bounded: Aura handles orchestration, Swarm informs clean handoff design, and each sub-agent gets a narrow job with an explicit output contract.

## Install

Clone this repository, then run the bundled installer:

```sh
sh scripts/install.sh
```

This installs Meruem and the bundled workflow skills it depends on: Aura, Graphify, Karpathy Guidelines, Impeccable, Frontend Design, Design Taste Frontend, Emil Design Engineering, Codebase Explainer, Deep Research, and Prompt Preflight.

Verify the install:

```sh
sh scripts/doctor.sh
```

Then start a task with:

```text
$meruem <your task>
```

See [docs/INSTALL.md](docs/INSTALL.md) for more options.

## How To Use Meruem

Use Meruem when you want agents to work with repository discipline:

- Feature implementation
- Bug fixes
- Code review
- Refactors
- UI and product design work
- Multi-agent research or implementation
- Ticket creation
- Architecture decisions
- Prompt and workflow design

Meruem is intentionally opinionated. It rewards local evidence, scoped tickets, concrete acceptance criteria, and visible verification. It rejects speculative abstractions, unnecessary test theater, uncontrolled delegation, and design that looks like a generic mockup.

## Project Shape

```text
.
├── AGENTS.md
├── CHANGELOG.md
├── SECURITY.md
├── meruem.manifest.json
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── docs/
│   ├── BEST_PRACTICES.md
│   ├── INSTALL.md
│   ├── QUICKSTART.md
│   ├── RELEASE.md
│   ├── SKILL_SOURCES.md
│   └── WORKFLOW.md
├── scripts/
│   ├── doctor.sh
│   ├── install.sh
│   └── uninstall.sh
├── skills/
│   ├── aura/
│   ├── meruem/
│   ├── codebase-explainer/
│   ├── deep-research/
│   ├── design-taste-frontend/
│   ├── emil-design-eng/
│   ├── frontend-design/
│   ├── graphify/
│   ├── impeccable/
│   ├── karpathy-guidelines/
│   └── prompt-preflight/
└── .tickets/
    └── templates/
        ├── decision-brief.md
        └── ticket.md
```

## Philosophy

Meruem treats an AI coding agent like a careful senior collaborator:

- Read before changing.
- Plan only as much as the work deserves.
- Use sub-agents when they reduce risk, not when they create theater.
- Keep design grounded in real user moments.
- Prefer working software over elaborate scaffolding.
- Record the decision trail so future contributors can understand why the code looks the way it does.

## License

MIT. See [LICENSE](LICENSE).
