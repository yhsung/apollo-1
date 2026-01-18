"""Tests for apollo.apollo_1.tools.redmine module.

These tests mock the Redmine client to test tool functions in isolation.
"""

import pytest
from unittest.mock import patch, MagicMock


class TestRedmineFunctions:
    """Test Redmine tool functions with mocked client."""
    
    @pytest.fixture
    def mock_redmine(self):
        """Create a mock Redmine instance."""
        with patch('apollo.apollo_1.tools.redmine.redmine') as mock:
            yield mock
    
    def test_get_issue_status_success(self, mock_redmine):
        """Test get_issue_status returns formatted string."""
        # Setup mock
        mock_issue = MagicMock()
        mock_issue.subject = "Test Subject"
        mock_issue.status.name = "Open"
        mock_issue.description = "Test Description"
        mock_redmine.issue.get.return_value = mock_issue
        
        from apollo.apollo_1.tools.redmine import get_issue_status
        result = get_issue_status("123")
        
        assert "Subject: Test Subject" in result
        assert "Status: Open" in result
        assert "Description: Test Description" in result
    
    def test_get_issue_status_strips_hash(self, mock_redmine):
        """Test that # prefix is stripped from issue ID."""
        mock_issue = MagicMock()
        mock_issue.subject = "Test"
        mock_issue.status.name = "Open"
        mock_issue.description = "Desc"
        mock_redmine.issue.get.return_value = mock_issue
        
        from apollo.apollo_1.tools.redmine import get_issue_status
        get_issue_status("#456")
        
        mock_redmine.issue.get.assert_called_with("456", include='journals')
    
    def test_get_issue_status_error_handling(self, mock_redmine):
        """Test get_issue_status handles errors gracefully."""
        mock_redmine.issue.get.side_effect = Exception("Not found")
        
        from apollo.apollo_1.tools.redmine import get_issue_status
        result = get_issue_status("999")
        
        assert "Error fetching issue" in result
        assert "Not found" in result
    
    def test_update_srs_wiki_success(self, mock_redmine):
        """Test update_srs_wiki returns success message."""
        from apollo.apollo_1.tools.redmine import update_srs_wiki
        result = update_srs_wiki("project-1", "SRS_Page", "# Content")
        
        assert "Successfully updated Wiki" in result
        assert "SRS_Page" in result
        mock_redmine.wiki_page.update.assert_called_once_with(
            "SRS_Page", project_id="project-1", text="# Content"
        )
    
    def test_update_srs_wiki_error_handling(self, mock_redmine):
        """Test update_srs_wiki handles errors gracefully."""
        mock_redmine.wiki_page.update.side_effect = Exception("Permission denied")
        
        from apollo.apollo_1.tools.redmine import update_srs_wiki
        result = update_srs_wiki("project-1", "SRS_Page", "# Content")
        
        assert "Failed to update Wiki" in result
        assert "Permission denied" in result


class TestRedmineToolWrappers:
    """Test LangChain tool wrappers."""
    
    def test_get_realtime_issue_status_is_tool(self):
        """Test Get_Realtime_Issue_Status is a LangChain tool."""
        from apollo.apollo_1.tools.redmine import Get_Realtime_Issue_Status
        
        assert hasattr(Get_Realtime_Issue_Status, 'name')
        assert hasattr(Get_Realtime_Issue_Status, 'description')
        assert hasattr(Get_Realtime_Issue_Status, 'func')
        assert Get_Realtime_Issue_Status.name == "Get_Realtime_Issue_Status"
    
    def test_update_srs_wiki_is_structured_tool(self):
        """Test Update_SRS_Wiki is a LangChain structured tool."""
        from apollo.apollo_1.tools.redmine import Update_SRS_Wiki
        
        assert hasattr(Update_SRS_Wiki, 'name')
        assert hasattr(Update_SRS_Wiki, 'description')
        assert Update_SRS_Wiki.name == "Update_SRS_Wiki"
