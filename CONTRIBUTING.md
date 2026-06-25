# Contributing To Meruem

Meruem is a workflow repository. Contributions should improve how agents plan, coordinate, design, build, verify, or document work.

## Good Contributions

- Clearer workflow rules
- Better ticket or decision-brief templates
- Installation improvements
- Skill source updates
- Safer orchestration guidance
- Better examples of scoped agent work
- Documentation that helps humans operate Meruem in real repositories

## Before You Change The Workflow

Use Meruem on Meruem:

1. Read [skills/meruem/SKILL.md](skills/meruem/SKILL.md).
2. Create or update a decision brief if the change affects workflow behavior.
3. Keep the change small and explain what problem it solves.
4. Update every affected doc.
5. Update [docs/SKILL_SOURCES.md](docs/SKILL_SOURCES.md) if skill names, descriptions, or sources change.

## Pull Request Checklist

- [ ] The change has a narrow purpose.
- [ ] Docs and templates still agree with the skill.
- [ ] New rules are actionable, not vague preferences.
- [ ] Required tools are named with fallback behavior.
- [ ] Examples do not include secrets, private repo data, or machine-only paths unless the file is explicitly a local source inventory.

## Style

Write like an experienced engineer leaving instructions for another experienced engineer:

- Direct
- Concrete
- Testable
- No hype
- No fake precision
- No ceremony without a reason

## Public Source Policy

Do not publish private skill contents from your local machine unless you own them or have permission to share them. It is fine to list a skill as an influence or dependency; it is not always fine to copy the skill text.
