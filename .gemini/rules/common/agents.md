# Agent Orchestration

## Available Agents

Located in `.gemini/agents/`:

| Agent | Purpose | When to Use |
|-------|---------|-------------|
| codebase_investigator | Codebase analysis | Understanding architecture, root cause analysis |
| cli_help | CLI usage help | Questions about Gemini CLI features |
| generalist | Batch tasks | Refactoring, running verbose commands |
| code-reviewer | Code review | After writing code |
| security-reviewer | Security analysis | Before commits |

## Immediate Agent Usage

Use subagents for these scenarios:
1. **Vague requests** - Use `codebase_investigator`
2. **Batch refactoring** - Use `generalist`
3. **Complex architecture questions** - Use `codebase_investigator`
4. **Finalizing changes** - Use `code-reviewer`

## Parallel Execution

Gemini CLI executes tools in parallel by default. When delegating tasks, you can invoke multiple subagents in a single turn if they handle independent concerns (e.g., researching different modules).

```markdown
# Example: Parallel Research
Invoke 2 subagents in parallel:
1. codebase_investigator: Map the authentication flow
2. codebase_investigator: Map the database schema
```

## Multi-Agent Collaboration

For complex features, break down the work:
1. Use `codebase_investigator` to map the impact.
2. Use `generalist` to apply batch changes across multiple files.
3. Use `code-reviewer` to validate the final output.
