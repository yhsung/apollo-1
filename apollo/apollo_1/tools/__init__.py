"""
Reusable LangChain Tools for Apollo-1 Agents.

This module provides reusable tools that can be imported by any agent:
- Knowledge Base tools for hierarchical document retrieval
- Redmine tools for issue tracking and wiki integration
"""

from .knowledge_base import (
    search_knowledge_base,
    Search_Knowledge_Base,
    hierarchical_retriever,
)

from .redmine import (
    get_issue_status,
    update_srs_wiki,
    Get_Realtime_Issue_Status,
    Update_SRS_Wiki,
    redmine,
)

# Pre-built tools list for convenience
all_tools = [
    Search_Knowledge_Base,
    Get_Realtime_Issue_Status,
    Update_SRS_Wiki,
]

__all__ = [
    # Knowledge Base
    "search_knowledge_base",
    "Search_Knowledge_Base",
    "hierarchical_retriever",
    # Redmine
    "get_issue_status",
    "update_srs_wiki",
    "Get_Realtime_Issue_Status",
    "Update_SRS_Wiki",
    "redmine",
    # Convenience
    "all_tools",
]
