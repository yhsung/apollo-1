# Apollo-1 Agent Configuration

## Python Environment
Use the virtual environment located at `./venv` for all Python operations.

## Version Tracking
Maintain a version counter that increments with each user request (features, bug fixes, refactoring, etc.) to ensure traceability.

**Current Version**: v0.1.0

### Version Format
- Use semantic versioning: `vMAJOR.MINOR.PATCH`
- Increment PATCH for bug fixes and minor changes
- Increment MINOR for new features
- Increment MAJOR for breaking changes or major refactors

### Version History
| Version | Date | Type | Description |
|---------|------|------|-------------|
| v0.1.0 | 2026-01-18 | feature | Refactored tools from srs_analyst.py into reusable src/tools/ module |

## Documentation Paths
Save all documentation with version tags:
- **Implementation Plans**: `docs/plans/v{VERSION}_{feature_name}.md`
- **Walkthroughs**: `docs/walkthroughs/v{VERSION}_{feature_name}.md`

Create directories if they don't exist.

## Project Structure
- `src/agents/` - Agent implementations
- `src/tools/` - Reusable LangChain tools
- `docs/plans/` - Versioned implementation plans
- `docs/walkthroughs/` - Versioned walkthrough documentation
