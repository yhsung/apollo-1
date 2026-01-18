# Apollo-1 Agent Configuration

## Python Environment
Use the virtual environment located at `./venv` for all Python operations.

## Version Tracking
Maintain a version counter that increments with each user request (features, bug fixes, refactoring, etc.) to ensure traceability.

- Use semantic versioning: `vMAJOR.MINOR.PATCH`
- Increment PATCH for bug fixes and minor changes
- Increment MINOR for new features
- Increment MAJOR for breaking changes or major refactors
- Update the Version History table in `README.md` for each version

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
