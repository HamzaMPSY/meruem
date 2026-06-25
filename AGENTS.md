# Agent Instructions

Any AI coding agent working in this repository must use the Meruem workflow in [skills/meruem/SKILL.md](skills/meruem/SKILL.md) before doing project work.

## Required Behavior

1. Read the relevant local docs before editing.
2. If the work is new and no ticket exists, create a decision brief before creating a ticket.
3. Keep scope surgical. Do not invent adjacent features.
4. Use Aura for orchestration when delegation is needed.
5. Use Swarm only as a handoff design pattern unless the user explicitly asks for Swarm runtime code.
6. Use local council review only for ambiguous high-impact choices.
7. Use the coordinated design skills for UI work.
8. Apply Karpathy-style coding discipline for implementation, review, and refactor work.
9. Query Graphify before modeling domain entities, relationships, graph structures, or data flows.
10. Verify the practical happy path before marking work complete.

## Repository Rule

The public source of truth for the Meruem skill is:

```text
skills/meruem/SKILL.md
```

Do not silently diverge local copies from that file. If you change workflow behavior, update the skill, docs, and skill source index together.
