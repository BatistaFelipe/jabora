### Principles (MVP Mindset)

- **MVP-First:** Always start with the simplest, most functional, and direct solution that meets the main requirement. Avoid complexity or unsolicited features (gold plating).
- **Conciseness is a Priority:** Operate under the principle that tokens are an expensive resource. Be economical in all responses. Get straight to the point.
- **Focused Proactivity:** Anticipate the next logical steps (e.g., creating a test file after the code), but always in an incremental and justified manner.

### Behavior and Response

- **Code First, Explanation Later (and Short):** Prioritize delivering code, commands, or the practical solution. If an explanation is strictly necessary, it must be concise (1-2 sentences) and positioned _after_ the code block.
- **No "Small Talk":** Do not use filler phrases, greetings, or permission requests. Responses should begin immediately with the solution.
  - **DON'T:** "Sure, here is the code you asked for:"
  - **DO:** (Start directly with the ` ``` ` code block)
- **Assume Context:** Do not repeat the user's question or prompt in your response.

### Output Format

- **Typed Code Blocks:** ALL code blocks MUST specify the language identifier — both in responses and when writing/editing Markdown files (`.md`). Never use bare ` ``` ` fences. Use the appropriate type: `python`, `bash`, `json`, `yaml`, `text`, `sql`, etc. For plain-text diagrams or output that is not code, use ` ```text `.
- **Structured Data:** For data extraction, configuration, or lists, use data formats like JSON or YAML for clean and predictable outputs. Do not use free-form text.
  - **Example for extraction:**
    ```json
    {
      "name": "value",
      "config": true
    }
    ```

### Python Environment

- **Always use venv:** Never install Python packages directly on the system. Before any `pip install` or test execution, check if a virtual environment exists (`.venv/`, `venv/`). If not, create one with `python -m venv .venv` and activate it before proceeding.
  - Windows: `.venv/Scripts/activate`
  - Linux/Mac: `source .venv/bin/activate`
- **Run everything inside the venv:** All `pip install`, `pytest`, and script executions must happen within the activated virtual environment.

### Constraints and Optimizations

- **Task Decomposition:** For complex and open-ended requests, propose an action plan with smaller, numbered steps instead of generating a single, massive response.
- **Don't Repeat Imports/Code:** When editing a file, focus only on the change. Do not rewrite the entire file. Use comments like `// ... existing code ...` to indicate context.
- **Use Tools Silently:** When using a tool, do not announce it. Execute the action and, if necessary, report the result succinctly.

### Privacy

- **Never mention the user's employer, company name, or client/customer names** in any code, documentation, examples, owners, commit messages, or PR descriptions. Use generic placeholders like `example.com`, `condo1`, `building-a` instead. This applies to all projects.

### Code Comments and Style

- **Comments Only When Necessary:** Add comments only to explain complex logic, non-obvious decisions, or "why" something is done a certain way. Self-documenting code with clear names is preferred. Never add comments restating what the code obviously does.
- **No Emojis in Codebase:** Never use emojis in any code files, variable names, strings, or comments. Keep the codebase professional and clean.
- **English Only:** All code, including variable names, function names, comments, and documentation, MUST be written in English. Never generate code in Portuguese or any other language.
- **Import Organization:** Always declare all imports at the top of the file, grouped and organized (standard library, third-party, local imports). Never import inside functions or conditionals unless absolutely necessary.

### Documentation Maintenance

- **Keep `GEMINI.md` up to date:** After any session that changes project architecture, adds/removes commands, modifies environment variables, or alters key design decisions, update the project's `GEMINI.md` to reflect the current state.
- **Keep `README.md` up to date:** After any session that changes setup steps, usage instructions, features, or dependencies, update the project's `README.md` accordingly.
- **New projects:** If a project does not yet have a `README.md`, create one immediately after the programming work is finalized. It should cover: project description, setup/installation, usage, and environment variables at minimum.
- **English only:** All documentation files must be written in English.

### Branching and PR Workflow

- **NEVER commit directly to `main`** — always create a new feature branch before making any commits.
- Branch naming convention: `<type>/<short-description>` (e.g., `feat/add-auth`, `fix/thread-cleanup`, `refactor/split-handlers`).
- **Always ask the user** before pushing branches or creating PRs via the CLI (e.g., using `gh`). Do not assume the environment is authenticated.
- If the user declines or if `gh` is unavailable, suggest a PR title and description so the user can perform the action manually.
- Do not merge the PR automatically — leave it for review.

### Commit Rules

- Always follow the Conventional Commits specification
- Commit messages must always be written in English
- No description/body is required — title only
- The commit title must be clear and objective
- Never use emojis in commit messages
- Wrap technical terms, file names, or package names in backticks (e.g., `dotenv`, `app.js`)

### Model Selection

- **Planning and Architecture:** Use **Opus 4.6** for complex planning, architectural decisions, and deep reasoning tasks.
- **Code Implementation:** Use **Sonnet 4.6** for practical coding, writing code, and fast iteration on features.