# AGENTS.md

This document provides guidelines for agentic coding agents working in this repository.

## Build, Lint, and Test

- **Build**: No explicit build process.
- **Lint**: No linter is configured. Suggested: `ruff check .`
- **Test**: No testing framework is set up. Suggested: `pytest`

To run a single test file (once pytest is configured):
`pytest tests/test_specific_file.py`

## Code Style

- **Imports**:
  - Standard library imports first, then third-party, then local application.
  - Example:
    ```python
    import os
    from dotenv import load_dotenv
    from langchain_deepseek import ChatDeepSeek
    ```
- **Formatting**:
  - Use snake_case for variables and function names.
  - Use 4 spaces for indentation.
- **Types**:
  - No type hints are currently used. Add them where appropriate for clarity.
- **Naming**:
  - Variables should be descriptive (e.g., `llm`, `prompt`, `chain`).
- **Error Handling**:
  - No explicit error handling. Add `try...except` blocks for robustness, especially around I/O and API calls.
