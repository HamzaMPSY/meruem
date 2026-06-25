# Meruem Workflow

Meruem turns repository work into a repeatable loop:

```text
intent -> local context -> decision brief -> ticket -> build -> smoke check -> outcome notes
```

The loop scales down for tiny exact fixes and scales up for ambiguous, high-impact, UI-heavy, or architecture-level work.

## 1. Intent

The agent starts by naming:

- User goal
- Constraints
- Non-goals
- Risk
- What a good outcome means

If the task is exact and small, the agent can proceed after a short sanity check. If the task is broad, it must produce a decision brief.

## 2. Local Context

The agent inspects local files, docs, tickets, patterns, git history when useful, and any relevant project knowledge base.

External research is allowed only when the user explicitly permits it, except when current facts are required by higher-priority platform instructions.

## 3. Decision Brief

Before a new ticket, Meruem requires a Plan Plus-style decision brief:

- Recommended approach
- Rejected alternatives
- Final scope
- Non-goals
- Acceptance criteria candidates
- Local research sources
- Council result or reason skipped
- Sub-agent findings or reason scaled down

Use [.tickets/templates/decision-brief.md](.tickets/templates/decision-brief.md).

## 4. Ticket

Once scope is stable, create a ticket in `.tickets/` using [.tickets/templates/ticket.md](.tickets/templates/ticket.md).

The ticket should be small enough that the agent can finish it without wandering.

## 5. Build First

Meruem prefers a working implementation over premature test scaffolding.

Do:

- Build the requested feature or fix.
- Add focused tests for pure logic when useful.
- Run one practical smoke check.

Avoid:

- E2E tests unless explicitly required.
- Mocking whole subsystems just to make a test pass.
- Broad refactors that are not required by the ticket.
- More than two loops on nonessential test failures before surfacing the blocker.

## 6. UI Work

For interface work, the agent must identify the user's moment:

```text
The user is <who>, feeling <state>, trying to <goal>.
```

Then it coordinates the design skills:

- `impeccable` for product frame, hierarchy, accessibility, and quality.
- `design-taste-frontend` for avoiding templated landing-page and redesign output.
- `emil-design-eng` for interaction polish, motion, feedback, and micro-details.

The result should include real states: loading, empty, error, disabled, success, permissions, mobile behavior, and focus behavior where relevant.

## 7. Delegation

Meruem uses Aura for sub-agent orchestration. Each delegated agent needs:

- One-sentence goal
- Skill to use
- Ticket or decision-brief context
- Explicit output contract
- Handoff condition

Swarm is used as a pattern for clean handoffs, not as the default runtime.

## 8. Council Review

Use local GPT-5.5 council review only for decisions that can create expensive rework:

- Public API changes
- Data model changes
- Architecture choices
- Storage or performance strategy
- Security posture
- Long-lived operational workflow

Tiny fixes do not need a council.

## 9. Completion

Before completion, the agent checks:

- Acceptance criteria met
- Required docs read
- Scope did not drift
- Verification was run or clearly blocked
- Ticket outcome notes updated when appropriate
- Any unavailable tool or skipped gate was stated honestly
