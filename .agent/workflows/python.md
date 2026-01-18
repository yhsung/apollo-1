---
description: How to run, test, and develop Python code in this project
---

# Python Development Workflow

## Setup

1. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

// turbo
2. Install package in development mode:
   ```bash
   pip install -e .
   ```

// turbo
3. Install dev dependencies (optional):
   ```bash
   pip install -e ".[dev]"
   ```

## Running Code

// turbo
1. Verify imports work:
   ```bash
   python -c "from apollo.apollo_1 import __version__; print(f'Apollo-1 v{__version__}')"
   ```

2. Run a module:
   ```bash
   python -m apollo.apollo_1.agents.srs_analyst
   ```

## Testing

// turbo
1. Run all tests:
   ```bash
   pytest
   ```

// turbo
2. Run with coverage:
   ```bash
   pytest --cov=apollo
   ```

## Code Quality

// turbo
1. Check syntax of all Python files:
   ```bash
   python -m py_compile apollo/apollo_1/**/*.py
   ```

// turbo
2. Run type checking (if mypy installed):
   ```bash
   mypy apollo/
   ```

## Package Build

1. Build distribution:
   ```bash
   python -m build
   ```

2. Check built package:
   ```bash
   twine check dist/*
   ```

## Environment Variables

Required environment variables for full functionality:
- `OPENAI_API_KEY` - OpenAI API key
- `REDMINE_URL` - Redmine server URL
- `REDMINE_API_KEY` - Redmine API key
- `LANGFUSE_PUBLIC_KEY` - Langfuse public key
- `LANGFUSE_SECRET_KEY` - Langfuse secret key
- `LANGFUSE_HOST` - Langfuse host URL
