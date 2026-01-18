"""Tests for apollo.apollo_1 package initialization.

These tests verify package metadata without triggering heavy LangChain imports.
"""

import pytest


class TestPackageMetadata:
    """Test package metadata that can be accessed without full imports."""
    
    def test_namespace_package_exists(self):
        """Test that apollo namespace package exists."""
        import apollo
        assert hasattr(apollo, '__path__')
    
    def test_apollo_1_package_exists(self):
        """Test that apollo.apollo_1 package can be found."""
        import importlib.util
        spec = importlib.util.find_spec("apollo.apollo_1")
        assert spec is not None


class TestVersionInfo:
    """Test version information using importlib.metadata."""
    
    def test_package_version_from_metadata(self):
        """Test package version can be retrieved from metadata."""
        try:
            from importlib.metadata import version
            pkg_version = version("apollo-1")
            assert pkg_version == "0.2.0"
        except ImportError:
            pytest.skip("importlib.metadata not available")
