"""Tests for apollo.apollo_1.agents.srs_analyst module.

These tests verify the SRS analyst agent structure and configuration.
"""

import pytest


class TestSrsAnalystPrompt:
    """Test SRS analyst prompt configuration."""
    
    def test_srs_instructions_defined(self):
        """Test that SRS instructions constant is defined."""
        from apollo.apollo_1.agents.srs_analyst import SRS_SWE1_FOR_SWE2_INSTRUCTIONS
        assert SRS_SWE1_FOR_SWE2_INSTRUCTIONS is not None
        assert isinstance(SRS_SWE1_FOR_SWE2_INSTRUCTIONS, str)
        assert len(SRS_SWE1_FOR_SWE2_INSTRUCTIONS) > 100
    
    def test_srs_instructions_mentions_aspice(self):
        """Test that instructions reference ASPICE."""
        from apollo.apollo_1.agents.srs_analyst import SRS_SWE1_FOR_SWE2_INSTRUCTIONS
        assert "ASPICE" in SRS_SWE1_FOR_SWE2_INSTRUCTIONS
        assert "SWE.1" in SRS_SWE1_FOR_SWE2_INSTRUCTIONS
        assert "SWE.2" in SRS_SWE1_FOR_SWE2_INSTRUCTIONS
    
    def test_srs_instructions_mentions_iso26262(self):
        """Test that instructions reference ISO 26262."""
        from apollo.apollo_1.agents.srs_analyst import SRS_SWE1_FOR_SWE2_INSTRUCTIONS
        assert "ISO 26262" in SRS_SWE1_FOR_SWE2_INSTRUCTIONS
    
    def test_srs_instructions_has_output_structure(self):
        """Test that instructions define output structure."""
        from apollo.apollo_1.agents.srs_analyst import SRS_SWE1_FOR_SWE2_INSTRUCTIONS
        assert "Traceability" in SRS_SWE1_FOR_SWE2_INSTRUCTIONS
        assert "Software Requirements Specification" in SRS_SWE1_FOR_SWE2_INSTRUCTIONS
        assert "Functional Safety" in SRS_SWE1_FOR_SWE2_INSTRUCTIONS


class TestSrsAnalystWorkflow:
    """Test SRS analyst workflow function."""
    
    def test_workflow_function_exists(self):
        """Test that run_srs_to_swe2_workflow function exists."""
        from apollo.apollo_1.agents.srs_analyst import run_srs_to_swe2_workflow
        assert callable(run_srs_to_swe2_workflow)
    
    def test_workflow_function_signature(self):
        """Test run_srs_to_swe2_workflow has correct parameters."""
        import inspect
        from apollo.apollo_1.agents.srs_analyst import run_srs_to_swe2_workflow
        
        sig = inspect.signature(run_srs_to_swe2_workflow)
        params = list(sig.parameters.keys())
        
        assert "issue_id" in params
        assert "project_id" in params
        assert len(params) == 2
