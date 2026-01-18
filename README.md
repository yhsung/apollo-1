# Apollo-1

LangChain-based agent project for automotive software requirements engineering, following ASPICE and ISO 26262 standards.

## Project Structure

```
src/
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

**Current Version**: v0.1.0

| Version | Date | Type | Description |
|---------|------|------|-------------|
| v0.1.0 | 2026-01-18 | feature | Refactored tools from srs_analyst.py into reusable src/tools/ module |

## Setup

1. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## License

See [LICENSE](LICENSE) for details.