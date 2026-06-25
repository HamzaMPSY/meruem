# Presentation Data Schema

Use this schema for `presentation_data.json`. Keep the JSON valid, explicit, and useful for a later deck, report, React slide artifact, or diagram generator.

## Required Top-Level Shape

```json
{
  "schema_version": "1.0",
  "generated_at": "YYYY-MM-DD",
  "project": {
    "name": "string",
    "root_path": "string",
    "one_sentence_summary": "string",
    "audiences": ["string"],
    "current_state": "Production | Alpha | Prototype | Archived | Unknown"
  },
  "summary": {
    "what_this_is": "string",
    "problem_it_solves": "string",
    "how_it_works": ["string"],
    "who_its_for": ["string"],
    "current_state_and_limitations": ["string"]
  },
  "analysis": {
    "main_components": [
      {
        "name": "string",
        "description": "string",
        "source_paths": ["string"]
      }
    ],
    "data_flow": [
      {
        "step": "string",
        "description": "string"
      }
    ],
    "tech_stack": [
      {
        "name": "string",
        "category": "Language | Framework | Database | Tool | Infrastructure | Service | Other",
        "plain_english_role": "string",
        "why_it_matters": "string"
      }
    ],
    "runbook": {
      "setup": ["string"],
      "run": ["string"],
      "test": ["string"],
      "deploy": ["string"]
    },
    "complexity": {
      "codebase_size": "Low | Medium | High",
      "integrations": "Low | Medium | High",
      "architecture": "Low | Medium | High",
      "domain": "Low | Medium | High"
    },
    "limitations": ["string"],
    "open_questions": ["string"]
  },
  "slides": [
    {
      "id": "slide-01",
      "title": "string",
      "type": "title | problem | solution | architecture | component | workflow | tech-stack | status | next-steps",
      "speaker_goal": "string",
      "bullets": ["string"],
      "visual": {
        "kind": "none | diagram | screenshot | table | code | image",
        "description": "string"
      },
      "speaker_notes": "string"
    }
  ]
}
```

## Requirements

- Include at least 6 slides.
- Give every slide a stable `id`, title, type, speaker goal, non-empty bullets, visual object, and speaker notes.
- Keep bullets short enough for slides. Put detail in `speaker_notes`.
- Use plain language for non-technical audiences.
- Include concrete source paths where possible, using paths relative to the analyzed project.
- Use `Unknown` and explain uncertainty in `open_questions` when the repository does not provide enough evidence.

## Recommended Slide Flow

1. Title and plain-language summary.
2. Problem or context.
3. How the project solves it.
4. Main building blocks.
5. Data flow or architecture.
6. Tech stack and operations.
7. Current state, limitations, and next steps.

## Markdown Outline Mapping

The companion Markdown outline should be generated from the same JSON and include:

- Project title and one-sentence summary.
- TL;DR.
- One section per slide.
- Bullets, visual suggestion, and speaker notes for each slide.
- A final section with open questions and limitations.
