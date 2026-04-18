# AGENTS.md -- Project Guidance Entry Point

This project uses the `.agent` framework for structured development guidance.

## Where to Find Project Rules

- **Architecture overview:** `.agent/ARCHITECTURE.md`
- **Master config:** `.agent/rules/GEMINI.md`
- **Language-specific rules:**
  - Python: `.agent/rules/python/style.md`
  - Web (JS/TS): `.agent/rules/web/style.md`
- **Common rules:**
  - Coding style: `.agent/rules/common/coding-style.md`
  - Git workflow: `.agent/rules/common/git-workflow.md`
  - Security: `.agent/rules/common/security.md`
  - Testing: `.agent/rules/common/testing.md`

## Skills (Domain Knowledge)

Skills live in `.agent/skills/<name>/SKILL.md`. Read the relevant one when working on that domain:

- `search-first` -- Research existing solutions before writing custom code
- `security-review` -- Security checklist when handling auth, input, secrets
- `coding-standards` -- Code quality: immutability, KISS, DRY
- `python-patterns` -- Python conventions and async patterns
- `react-patterns` -- React hooks, state, performance
- `database-design` -- Schema design and query optimization
- `api-patterns` -- REST/GraphQL design decisions
- `testing-patterns` -- Test strategies and coverage
- `docker-expert` -- Containerization patterns
- `systematic-debugging` -- Root cause analysis methodology

## Project Preferences

- When user writes in Vietnamese, respond in Vietnamese. Code stays in English.
- Prefer researching existing libraries before writing custom code.
- For complex changes, outline a plan before implementing.
- Use conventional commits: `feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:`
- Validate user input with schema-based validation (Pydantic for Python, Zod for JS/TS).
- No hardcoded secrets -- use environment variables.

## Agents and Workflows

Agent definitions: `.agent/agents/`
Workflow procedures: `.agent/workflows/`

These define specialist personas and step-by-step procedures available in this project.
