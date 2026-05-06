---
paths:
  - "**/*.py"
  - "**/*.pyi"
---
# Python Automation

> This file extends [common/hooks.md](../common/hooks.md) with Python specific content.

## Automated Verification

- **black/ruff**: Run auto-formatting after significant edits to `.py` files using `run_shell_command`.
- **mypy/pyright**: Run type checking to verify changes.
- **pytest**: Always run relevant tests after modifying logic.

## Warnings

- Favor the `logging` module over `print()` statements for persistent code.
- Ensure `venv` is activated before running any Python tools.
