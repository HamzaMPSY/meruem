---
name: prompt-preflight
description: Critique and improve draft prompts before model execution. Use when a user asks to refine, optimize, polish, rewrite, or quality-check a prompt; when requirements are ambiguous; when outputs are inconsistent; when planning agent instructions; or when the user wants stronger prompts with clear context, constraints, output format, and acceptance criteria. Apply this skill broadly to prompt-writing and prompt-evaluation work.
---

# Prompt Preflight

## Overview

Critique prompts before execution, remove ambiguity, ask clarifying questions when needed, and produce an optimized prompt with explicit context, constraints, output contract, and acceptance criteria.

Follow a question-first policy for prompt-improvement work: resolve critical blockers before presenting a final prompt.

## Workflow

1. Inspect the draft prompt or instruction request for ambiguity, missing inputs, conflicts, output-format gaps, and unverifiable success criteria.
2. Ask one high-impact clarifying question at a time when a blocker would materially change the final prompt.
3. Prioritize questions in this order: success criteria, required inputs or source data, output format and detail level, constraints or do-not-do rules, deadline or latency or cost limits.
4. Stop asking when the remaining unknowns can be handled as explicit assumptions.
5. If the user refuses or skips critical answers, produce a provisional prompt and clearly list unresolved blockers and assumptions.
6. Do not label a prompt final when critical blockers remain unresolved.

## Prompt Construction

Build the optimized prompt in this order:

1. Objective
2. Context
3. Inputs
4. Constraints
5. Output Contract
6. Quality Bar
7. Execution Notes, only if they materially improve quality

Use direct, specific language. Remove redundant instructions and resolve conflicts instead of preserving them.

## Response Format

Return prompt-preflight results in this structure:

```markdown
## Prompt Critique
- ...

## Clarifying Questions
1. ...

## Final Prompt
[Prompt text ready to execute]

## Assumptions
- ...
```

If questions are still unanswered and they are critical, label the third section `## Provisional Prompt` instead of `## Final Prompt`.

## Quality Requirements

- Keep critique concise and actionable.
- Make the final prompt directly executable by a model without extra interpretation.
- Include an explicit output contract and acceptance criteria.
- Remove conflicting or duplicated instructions.
- State assumptions instead of hiding uncertainty.
- Ask the maximum number of useful high-impact questions, not redundant questions.

## Reference

When the quality bar is unclear or the prompt is high-stakes, read `references/prompt-quality-rubric.md` and apply its checklist.
