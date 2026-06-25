#!/usr/bin/env python3
"""Validate codebase-explainer presentation JSON and write JSON + Markdown."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any


VALID_STATES = {"Production", "Alpha", "Prototype", "Archived", "Unknown"}
VALID_COMPLEXITY = {"Low", "Medium", "High"}
VALID_VISUAL_KINDS = {"none", "diagram", "screenshot", "table", "code", "image"}
VALID_SLIDE_TYPES = {
    "title",
    "problem",
    "solution",
    "architecture",
    "component",
    "workflow",
    "tech-stack",
    "status",
    "next-steps",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def require_string(obj: dict[str, Any], key: str, context: str) -> str:
    value = obj.get(key)
    require(isinstance(value, str) and value.strip(), f"{context}.{key} must be a non-empty string")
    return value


def require_string_list(obj: dict[str, Any], key: str, context: str) -> list[str]:
    value = obj.get(key)
    require(isinstance(value, list), f"{context}.{key} must be a list")
    require(all(isinstance(item, str) and item.strip() for item in value), f"{context}.{key} must contain non-empty strings")
    return value


def validate(data: dict[str, Any]) -> None:
    require(isinstance(data, dict), "top-level JSON value must be an object")
    require_string(data, "schema_version", "root")

    generated_at = data.get("generated_at")
    require(isinstance(generated_at, str) and generated_at.strip(), "root.generated_at must be a non-empty string")
    try:
        dt.date.fromisoformat(generated_at)
    except ValueError as exc:
        raise ValueError("root.generated_at must use YYYY-MM-DD format") from exc

    project = data.get("project")
    require(isinstance(project, dict), "root.project must be an object")
    for key in ("name", "root_path", "one_sentence_summary", "current_state"):
        require_string(project, key, "project")
    require(project["current_state"] in VALID_STATES, f"project.current_state must be one of {sorted(VALID_STATES)}")
    require_string_list(project, "audiences", "project")

    summary = data.get("summary")
    require(isinstance(summary, dict), "root.summary must be an object")
    for key in ("what_this_is", "problem_it_solves"):
        require_string(summary, key, "summary")
    for key in ("how_it_works", "who_its_for", "current_state_and_limitations"):
        require_string_list(summary, key, "summary")

    analysis = data.get("analysis")
    require(isinstance(analysis, dict), "root.analysis must be an object")
    for key in ("main_components", "data_flow", "tech_stack", "limitations", "open_questions"):
        require(isinstance(analysis.get(key), list), f"analysis.{key} must be a list")

    complexity = analysis.get("complexity")
    require(isinstance(complexity, dict), "analysis.complexity must be an object")
    for key in ("codebase_size", "integrations", "architecture", "domain"):
        value = complexity.get(key)
        require(value in VALID_COMPLEXITY, f"analysis.complexity.{key} must be one of {sorted(VALID_COMPLEXITY)}")

    runbook = analysis.get("runbook")
    require(isinstance(runbook, dict), "analysis.runbook must be an object")
    for key in ("setup", "run", "test", "deploy"):
        require_string_list(runbook, key, "analysis.runbook")

    slides = data.get("slides")
    require(isinstance(slides, list), "root.slides must be a list")
    require(len(slides) >= 6, "root.slides must contain at least 6 slides")

    seen_ids: set[str] = set()
    for index, slide in enumerate(slides, start=1):
        context = f"slides[{index}]"
        require(isinstance(slide, dict), f"{context} must be an object")
        slide_id = require_string(slide, "id", context)
        require(slide_id not in seen_ids, f"{context}.id must be unique")
        seen_ids.add(slide_id)
        require_string(slide, "title", context)
        slide_type = require_string(slide, "type", context)
        require(slide_type in VALID_SLIDE_TYPES, f"{context}.type must be one of {sorted(VALID_SLIDE_TYPES)}")
        require_string(slide, "speaker_goal", context)
        require_string_list(slide, "bullets", context)
        require_string(slide, "speaker_notes", context)

        visual = slide.get("visual")
        require(isinstance(visual, dict), f"{context}.visual must be an object")
        kind = require_string(visual, "kind", f"{context}.visual")
        require(kind in VALID_VISUAL_KINDS, f"{context}.visual.kind must be one of {sorted(VALID_VISUAL_KINDS)}")
        require_string(visual, "description", f"{context}.visual")


def bullet_lines(items: list[str]) -> list[str]:
    return [f"- {item}" for item in items] if items else ["- None noted."]


def build_markdown(data: dict[str, Any]) -> str:
    project = data["project"]
    summary = data["summary"]
    analysis = data["analysis"]

    lines: list[str] = [
        f"# {project['name']}",
        "",
        project["one_sentence_summary"],
        "",
        "## TL;DR",
        "",
        summary["what_this_is"],
        "",
        summary["problem_it_solves"],
        "",
        "## Plain-Language Summary",
        "",
        "### How It Works",
        "",
        *bullet_lines(summary["how_it_works"]),
        "",
        "### Who It's For",
        "",
        *bullet_lines(summary["who_its_for"]),
        "",
        "### Current State and Limitations",
        "",
        *bullet_lines(summary["current_state_and_limitations"]),
        "",
        "## Slide Outline",
        "",
    ]

    for index, slide in enumerate(data["slides"], start=1):
        lines.extend(
            [
                f"### {index}. {slide['title']}",
                "",
                f"Type: {slide['type']}",
                "",
                f"Speaker goal: {slide['speaker_goal']}",
                "",
                "Bullets:",
                "",
                *bullet_lines(slide["bullets"]),
                "",
                f"Visual: {slide['visual']['kind']} - {slide['visual']['description']}",
                "",
                "Speaker notes:",
                "",
                slide["speaker_notes"],
                "",
            ]
        )

    lines.extend(
        [
            "## Open Questions",
            "",
            *bullet_lines(analysis["open_questions"]),
            "",
            "## Limitations",
            "",
            *bullet_lines(analysis["limitations"]),
            "",
        ]
    )
    return "\n".join(lines)


def load_json(args: argparse.Namespace) -> dict[str, Any]:
    if args.data:
        raw = Path(args.data).read_text(encoding="utf-8")
    else:
        raw = sys.stdin.read()
    require(raw.strip() != "", "provide JSON with --data or stdin")
    parsed = json.loads(raw)
    require(isinstance(parsed, dict), "presentation data must be a JSON object")
    return parsed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", help="Input JSON file. If omitted, read JSON from stdin.")
    parser.add_argument("--json", required=True, help="Output path for formatted presentation_data.json.")
    parser.add_argument("--md", required=True, help="Output path for generated presentation_outline.md.")
    args = parser.parse_args()

    try:
        data = load_json(args)
        validate(data)
        json_path = Path(args.json)
        md_path = Path(args.md)
        json_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        md_path.write_text(build_markdown(data), encoding="utf-8")
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"write_output.py: error: {exc}", file=sys.stderr)
        return 1

    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
