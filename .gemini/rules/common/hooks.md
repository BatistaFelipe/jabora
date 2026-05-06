# Hooks and Automation

## Session Management

- **Memory Persistence**: Use `MEMORY.md` to track long-running task progress and state.
- **Topic Updates**: Use `update_topic` to maintain clear visibility of current strategic intent and progress for the user.
- **Validation Hooks**: Always run project-specific validation (e.g., `pytest`, `lint`) after significant changes.

## Tool Best Practices

- **Parallelism**: Group independent tool calls (e.g., reading multiple files, searching different terms) into a single turn to minimize context usage.
- **Wait for Previous**: Set `wait_for_previous: true` when a tool's execution depends on the output of a preceding tool in the same turn.
- **Strategic Search**: Prefer `grep_search` with context over reading entire large files.

## Documentation Maintenance

- **GEMINI.md**: Update this file for team-wide architectural changes.
- **MEMORY.md**: Use as a private, project-specific index for your current workspace state. Do not commit.
- **CLAUDE.md**: (If still in use) Keep updated with command references and environment setup. Recommend migrating to `GEMINI.md`.
