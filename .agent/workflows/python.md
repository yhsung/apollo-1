---
description: How to run, test, and develop Python code in this project
---

# Python Development Workflow

// turbo-all

## Setup

1. Create virtual environment (if not exists):
   ```bash
   test -d ./venv || python -m venv ./venv
   ```

2. Activate virtual environment:
   ```bash
   source ./venv/bin/activate
   ```

3. Install package in development mode:
   ```bash
   pip install -e .
   ```

4. Install dev dependencies (optional):
   ```bash
   pip install -e ".[dev]"
   ```

## Running Code

1. Verify imports work:
   ```bash
   source ./venv/bin/activate && python -c "from apollo.apollo_1 import __version__; print(f'Apollo-1 v{__version__}')"
   ```

2. Run a module:
   ```bash
   source ./venv/bin/activate && python -m apollo.apollo_1.agents.srs_analyst
   ```

## Testing

1. Run all tests:
   ```bash
   source ./venv/bin/activate && pytest
   ```

2. Run with coverage:
   ```bash
   source ./venv/bin/activate && pytest --cov=apollo
   ```

## Code Quality

1. Check syntax of all Python files:
   ```bash
   source ./venv/bin/activate && python -m py_compile apollo/apollo_1/**/*.py
   ```

2. Run type checking (if mypy installed):
   ```bash
   source ./venv/bin/activate && mypy apollo/
   ```

## Package Build

1. Build distribution:
   ```bash
   source ./venv/bin/activate && python -m build
   ```

2. Check built package:
   ```bash
   source ./venv/bin/activate && twine check dist/*
   ```

## Environment Variables

Required environment variables for full functionality:
- `OPENAI_API_KEY` - OpenAI API key
- `REDMINE_URL` - Redmine server URL
- `REDMINE_API_KEY` - Redmine API key
- `LANGFUSE_PUBLIC_KEY` - Langfuse public key
- `LANGFUSE_SECRET_KEY` - Langfuse secret key
- `LANGFUSE_HOST` - Langfuse host URL
