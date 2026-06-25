---
name: codebase-explainer
description: Read documentation and source code to explain, summarize, document, or present a codebase or technical project in plain language. Use when the user asks to understand a repo, directory, uploaded files, docs, architecture, source code, technical project, or wants presentation-ready output for prompts such as "explain this codebase", "understand this repo", "what does this code do", "read the docs and summarize", "document this project", "explain this to non-technical people", "prepare a presentation about this repo", or similar codebase walkthrough requests.
---

# Codebase Explainer

Use this skill to inspect a project, synthesize a plain-language explanation, and produce reusable presentation data.

## Output Contract

Always produce:

1. A short TL;DR in chat.
2. A plain-language summary in chat.
3. `presentation_data.json`.
4. `presentation_outline.md`.

Use `/mnt/user-data/outputs` when it exists. Otherwise create an `outputs/` directory in the analyzed project if writable, or fall back to `/tmp/codebase-explainer-outputs`.

If a `present_files` tool is available, call it with both output files. If it is unavailable, provide direct file paths in the final response.

Before writing JSON, read `references/presentation-schema.md`.

## Phase 1: Discover

Map what exists before reading deeply.

```bash
find <root> -maxdepth 4 \
  -not -path '*/node_modules/*' \
  -not -path '*/.git/*' \
  -not -path '*/dist/*' \
  -not -path '*/build/*' \
  -not -path '*/__pycache__/*' \
  -not -path '*/venv/*' \
  -not -path '*/.next/*' \
  | sort
```

Identify entry points in this order:

1. Root docs: `README.md`, `README.rst`, `README.txt`.
2. Documentation folders: `docs/`, `doc/`, `site/`.
3. Project guides: `ARCHITECTURE.md`, `CHANGELOG.md`, `CONTRIBUTING.md`.
4. Metadata: `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `pom.xml`, `build.gradle`.
5. Run files: `Makefile`, `justfile`, `Taskfile.yml`, `docker-compose.yml`.
6. Main entry files: `main.py`, `app.py`, `index.js`, `src/main.*`, `cmd/*`, `server.*`.
7. Config examples: `.env.example`, `config.*`, deployment manifests.

Estimate scale:

```bash
find <root> -type f \( -name "*.py" -o -name "*.ts" -o -name "*.tsx" -o -name "*.js" \
  -o -name "*.jsx" -o -name "*.go" -o -name "*.rs" -o -name "*.java" \
  -o -name "*.rb" -o -name "*.cs" \) \
  -not -path '*/node_modules/*' \
  -not -path '*/.git/*' \
  -not -path '*/dist/*' \
  -not -path '*/build/*' \
  | xargs wc -l 2>/dev/null | tail -1
```

## Phase 2: Read

Read documentation first. Read root README files and every Markdown, reStructuredText, or text file in `docs/` fully. Note external links, but fetch them only when the user asks or when the docs cannot be understood without them.

Read project metadata and extract:

- Project name, description, version.
- Dependencies and frameworks.
- Build, test, run, and deploy commands.

Read architecture docs fully when present.

Read source strategically:

- Trace the execution spine from the main entry point into the main modules it imports.
- Inspect top-level source directories such as `src/`, `app/`, `lib/`, `pkg/`, `backend/`, `frontend/`.
- Prioritize files whose names include `core`, `engine`, `service`, `model`, `schema`, `api`, `router`, `controller`, `worker`, `pipeline`, or `adapter`.
- Skim tests for behavioral intent. Read at least one representative test file when tests exist.

Do not read every file in large repositories. For projects above roughly 50k lines, focus on docs, package boundaries, entry points, and representative modules.

## Phase 3: Analyze

Answer these before writing:

- What problem does this project solve in one non-jargony sentence?
- Who uses it?
- What are the 3 to 6 main components or layers?
- What is the data flow: what goes in, what happens, what comes out?
- What technology choices were made, and what role does each choice play?
- What key concepts does a new contributor need?
- How is it run, tested, and deployed?
- What is the current state: production, alpha, prototype, archived, or unclear?
- What limitations, risks, missing docs, or unfinished pieces are visible?

Score complexity as `Low`, `Medium`, or `High` for:

- Codebase size.
- Integrations and dependencies.
- Architectural complexity.
- Domain complexity.

## Phase 4: Explain

Write for a smart non-technical reader. Avoid jargon; define technical terms the first time they matter.

Use this structure:

```markdown
## What This Is
[1-2 sentences.]

## The Problem It Solves
[2-3 sentences.]

## How It Works (Simply)
[3-5 sentences or a short numbered list.]

## Main Building Blocks
[3-6 bullets, one line each.]

## Who It's For
[Primary users and how they use it.]

## Tech Stack (Plain English)
[Language/framework/tool plus its role in plain English.]

## How to Get It Running
[3-6 key steps from the docs.]

## Current State & Limitations
[What works, what is missing, what is uncertain.]
```

## Phase 5: Write Presentation Files

Create presentation data with at least 6 slides. Use the schema in `references/presentation-schema.md`.

Recommended slide flow:

1. What this project is.
2. Problem or context.
3. How it works.
4. Main components.
5. Data flow or architecture.
6. Tech stack and operations.
7. Current state, limitations, and next steps.

Prefer the bundled writer to validate and generate the companion Markdown outline:

```bash
python3 <skill_dir>/scripts/write_output.py \
  --data <prepared-json-file> \
  --json <output-dir>/presentation_data.json \
  --md <output-dir>/presentation_outline.md
```

The script can also read JSON from standard input. It creates parent directories, validates required fields, writes formatted JSON, and generates the Markdown outline from the JSON.

## Phase 6: Present

In the final response, include:

- A 3-sentence TL;DR.
- The plain-language summary.
- The paths to `presentation_data.json` and `presentation_outline.md`.
- Practical next steps, such as turning the JSON into a PowerPoint deck, building an interactive presentation, generating architecture diagrams, or drilling into a specific component.
