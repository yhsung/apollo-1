"""Pytest configuration and fixtures for apollo.apollo_1 tests.

Note: The apollo.apollo_1 package has module-level LangChain initialization
that requires API keys. These tests require the environment variables to be set.
"""

import os
import pytest


def pytest_configure(config):
    """Set up environment variables before any test collection."""
    # These are test values that allow the modules to load
    os.environ.setdefault("OPENAI_API_KEY", "test-api-key-for-testing")
    os.environ.setdefault("REDMINE_URL", "http://localhost:3000")
    os.environ.setdefault("REDMINE_API_KEY", "test-redmine-key")
    os.environ.setdefault("LANGFUSE_PUBLIC_KEY", "test-langfuse-public")
    os.environ.setdefault("LANGFUSE_SECRET_KEY", "test-langfuse-secret")
    os.environ.setdefault("LANGFUSE_HOST", "http://localhost:3001")
