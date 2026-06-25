---
name: deep-research
description: Multi-source deep research using available web research tools. Searches the web, synthesizes findings, and delivers cited reports with source attribution. Use when the user wants thorough research on any topic with evidence and citations.
origin: ECC
---

# Deep Research

Produce thorough, cited research reports from multiple sources.

## When to Activate

- The user asks to research a topic in depth
- Competitive analysis, technology evaluation, or market sizing
- Due diligence on companies, investors, or technologies
- Any question requiring synthesis from multiple sources
- The user says "research", "deep dive", "investigate", or "what's the current state of"

## Tools

Prefer dedicated research MCP tools if configured:
- `firecrawl`
- `exa`

If they are unavailable, fall back to `web.run`.

## Workflow

### Step 1: Understand the Goal

Ask 1-2 quick clarifying questions only when needed:
- "What's your goal: learning, deciding, or writing something?"
- "Any specific angle or depth you want?"

If the user says to just research it, proceed with reasonable defaults.

### Step 2: Plan the Research

Break the topic into 3-5 sub-questions.

Example:
- What are the main applications today?
- What outcomes or metrics have been measured?
- What constraints or regulatory issues matter?
- Which companies or institutions are leading?
- What is the likely trajectory over the next 1-3 years?

### Step 3: Execute Multi-Source Search

For each sub-question:
- Search with 2-3 keyword variants
- Mix general sources, recent sources, and primary sources
- Aim for 15-30 useful unique sources total

Prioritize:
- Official docs
- Academic papers
- Regulators
- Reputable reporting
- Industry analysis

### Step 4: Deep-Read Key Sources

Read full content from the strongest sources, not only snippets.

Aim to fully inspect 3-5 of the most important sources.

### Step 5: Synthesize

Write a report with:
- Executive summary
- Major themes
- Key takeaways
- Source list
- Methodology

Every significant factual claim should be sourced.

### Step 6: Deliver

- For short topics: provide the report directly in chat
- For long topics: provide a concise summary in chat and offer or save a longer report

## Report Shape

```markdown
# [Topic]: Research Report
*Generated: [date] | Sources: [N] | Confidence: [High/Medium/Low]*

## Executive Summary
[3-5 sentence overview]

## 1. [Theme]
[Findings with citations]

## 2. [Theme]
[Findings with citations]

## 3. [Theme]
[Findings with citations]

## Key Takeaways
- [Insight 1]
- [Insight 2]
- [Insight 3]

## Sources
1. [Title] — [why it mattered]
2. ...

## Methodology
Searched [N] queries and analyzed [M] sources.
```

## Quality Rules

1. Every important claim needs a source.
2. Cross-check claims when possible.
3. Prefer recent sources unless historical context is needed.
4. State gaps clearly when evidence is weak.
5. Separate fact from inference.
6. Prefer primary sources for technical and factual questions.

## Notes

- When using `web.run`, follow all citation rules from the system instructions.
- If official or primary documentation exists, prefer it over secondary summaries.
- For recommendations that could cost the user time or money, verify current options rather than relying on memory.
