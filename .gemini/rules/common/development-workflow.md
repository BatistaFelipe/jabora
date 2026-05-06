# Development Workflow

> This file extends [common/git-workflow.md](./git-workflow.md) with the full development process.

## Feature Implementation Workflow

0. **Research & Reuse** (mandatory before any new implementation)
   - **Gemini Search First**: Use `google_web_search` to find existing implementations, documentation, and patterns.
   - **Internal Search Second**: Use `grep_search` and `glob` to find similar patterns already in the codebase.
   - **Documentation Review**: Use `web_fetch` on primary vendor documentation to confirm API behavior and version-specific details.
   - **Check Package Registries**: Verify packages in `requirements.txt` or relevant package managers before writing utility code.

1. **Plan Mode**
   - Use `enter_plan_mode` for complex tasks to draft a strategy and design document.
   - Propose an action plan with smaller, numbered steps.
   - Identify dependencies and risks.

2. **Test-Driven Development (TDD)**
   - Write tests first (RED) using `pytest`.
   - Implement to pass tests (GREEN).
   - Refactor (IMPROVE).
   - Verify 80%+ coverage.

3. **Code Review**
   - Use `invoke_agent` with `code-reviewer` immediately after implementing.
   - Address CRITICAL and HIGH issues.

4. **Commit & Push**
   - Follow Conventional Commits format.
   - See [git-workflow.md](./git-workflow.md) for details.

5. **Validation**
   - Run full test suite and linters via `run_shell_command`.
   - Ensure `GEMINI.md` and `README.md` are updated if architectural changes occurred.
