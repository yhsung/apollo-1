# Apollo-1

LangChain-based agent project for automotive software requirements engineering, following ASPICE and ISO 26262 standards.

## Installation

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install package in development mode
pip install -e .
```


## Configuration

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your API keys and configuration:
   - **LLM_PROVIDER**: Choose `openai`, `local` (alias `lm_studio`), or `anthropic`.
   - **Redmine**: Set URL and API key for issue tracking.
   - **Langfuse**: Set keys for observability (optional).

## Usage


```python
from apollo.apollo_1 import run_srs_to_swe2_workflow
from apollo.apollo_1.tools import all_tools
```

## Project Structure

```
apollo/
└── apollo_1/
    ├── agents/          # Agent implementations
    │   └── srs_analyst.py
    └── tools/           # Reusable LangChain tools
        ├── knowledge_base.py
        └── redmine.py
docs/
├── plans/           # Versioned implementation plans
└── walkthroughs/    # Versioned walkthrough documentation
```

## Version History

**Current Version**: v0.2.0

| Version | Date | Type | Description |
|---------|------|------|-------------|
| v0.2.0 | 2026-01-18 | feature | Refactored to Python namespace package `apollo.apollo_1` |
| v0.1.0 | 2026-01-18 | feature | Refactored tools from srs_analyst.py into reusable src/tools/ module |

## License

See [LICENSE](LICENSE) for details.