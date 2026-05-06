# Performance Optimization

## Model Selection Strategy

**Gemini 2.0 Flash**:
- Default for code implementation, refactoring, and tool execution.
- Optimized for speed and cost-efficiency.
- Use for 90% of development tasks.

**Gemini 2.0 Pro**:
- Use for complex architectural planning, deep reasoning, and large-scale analysis.
- Best for solving ambiguous bugs or designing complex systems.

## Context Window Management

- **Strategic Reads**: Use `grep_search` to narrow down files before reading them.
- **Surgical Edits**: Use `replace` with minimal required context to keep the session history clean.
- **Delegation**: Use subagents (e.g., `generalist`) for high-volume tasks to "compress" history.

## Strategic Orchestration

For complex tasks requiring deep reasoning:
1. Use `enter_plan_mode` to research and design without polluting the codebase.
2. Utilize subagents for exploratory research.
3. Consolidate findings into `MEMORY.md` or `GEMINI.md` to persist context across sessions efficiently.

## Build Troubleshooting

If build fails:
1. Analyze the stack trace locally using `run_shell_command`.
2. Use `grep_search` to find related symbols or configurations.
3. Apply fixes incrementally and verify with tests.
