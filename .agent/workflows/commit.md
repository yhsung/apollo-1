---
description: How to create git commits following conventional commit format
---

# Git Commit Workflow

// turbo-all

## Pre-commit Checks

1. Check status:
   ```bash
   git status
   ```

2. Review changes:
   ```bash
   git diff
   ```

## Staging Changes

1. Stage specific files:
   ```bash
   git add <file>
   ```

2. Stage all changes:
   ```bash
   git add -A
   ```

## Commit Format

Use conventional commit format:
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation only
- `style` - Formatting, no code change
- `refactor` - Code change, no new feature or fix
- `perf` - Performance improvement
- `test` - Adding/fixing tests
- `chore` - Build process or auxiliary tools

### Guidelines
- Subject line ≤ 50 characters
- Use imperative mood ("add" not "added")
- No period at end of subject
- Blank line between subject and body
- Body explains what and why, not how

## Examples

```bash
git commit -m "feat(auth): add OAuth2 login support"
```

```bash
git commit -m "fix(api): handle null response from server

The API was crashing when the server returned null.
Added null check before processing response.

Closes #42"
```

```bash
git commit -m "refactor(package): migrate to namespace apollo.apollo_1"
```
