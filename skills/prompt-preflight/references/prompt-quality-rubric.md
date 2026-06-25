# Prompt Quality Rubric

Use this rubric to evaluate and improve prompts before execution.

## Checklist

- Objective: The task goal is specific, outcome-oriented, and easy to verify.
- Context: The prompt includes relevant background, audience, domain assumptions, and current state.
- Inputs: Required source material, examples, data, files, or links are named explicitly.
- Constraints: The prompt states style, policy, tooling, scope, exclusions, and do-not-do rules.
- Output Contract: The prompt defines format, structure, length, tone, and required sections.
- Quality Bar: The prompt states what success looks like and how the answer should be checked.
- Ambiguity Handling: Critical unknowns are asked as clarifying questions or listed as assumptions.
- Conflict Removal: Instructions do not contradict each other or repeat the same requirement unnecessarily.
- Executability: A model can act on the prompt without needing hidden context or follow-up interpretation.
- Verification: The prompt requests tests, citations, examples, checks, or acceptance criteria when appropriate.

## Scoring Guide

- 5: Clear, complete, constrained, verifiable, and directly executable.
- 4: Mostly complete, with minor assumptions that do not change the likely outcome.
- 3: Usable but under-specified; output quality may vary.
- 2: Ambiguous or missing major context, format, or success criteria.
- 1: Not executable without substantial clarification.

## Improvement Pattern

1. Identify blockers that would materially change the output.
2. Ask the highest-impact blocker question first.
3. Convert implicit expectations into explicit instructions.
4. Replace vague terms with observable criteria.
5. Add examples only when they reduce ambiguity.
6. Mark remaining uncertainty as assumptions if the user does not answer.
