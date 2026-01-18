"""
Redmine Tools - Tools for interacting with Redmine issue tracking and wiki.
"""
import os
from langchain_core.tools import Tool, StructuredTool
from redminelib import Redmine


# Initialize Redmine client
redmine = Redmine(os.getenv("REDMINE_URL"), key=os.getenv("REDMINE_API_KEY"))


def get_issue_status(issue_id: str) -> str:
    """
    Retrieves specific Issue content as the source for Stakeholder Requirements.
    
    Args:
        issue_id: The Redmine issue ID (can include # prefix)
        
    Returns:
        Formatted string with issue subject, status, and description
    """
    try:
        clean_id = str(issue_id).replace('#', '')
        issue = redmine.issue.get(clean_id, include='journals')
        return f"Subject: {issue.subject}\nStatus: {issue.status.name}\nDescription: {issue.description}"
    except Exception as e:
        return f"Error fetching issue: {str(e)}"


def update_srs_wiki(project_id: str, title: str, content: str) -> str:
    """
    Saves the generated SRS to Wiki and prepares for SWE.2 integration.
    
    Args:
        project_id: The Redmine project identifier
        title: The wiki page title
        content: The wiki page content in markdown/textile format
        
    Returns:
        Success or error message
    """
    try:
        redmine.wiki_page.update(title, project_id=project_id, text=content)
        return f"Successfully updated Wiki page: {title}. Data is ready for SWE.2 Ingestion."
    except Exception as e:
        return f"Failed to update Wiki: {str(e)}"


# LangChain Tool wrappers
Get_Realtime_Issue_Status = Tool(
    name="Get_Realtime_Issue_Status",
    func=get_issue_status,
    description="Retrieve real-time stakeholder requirement descriptions from Redmine."
)

Update_SRS_Wiki = StructuredTool.from_function(
    func=update_srs_wiki,
    name="Update_SRS_Wiki",
    description="Save the generated SRS and prepare it for seamless transition to SWE.2 Architecture Design."
)
