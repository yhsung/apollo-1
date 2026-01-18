"""
Apollo-1: LangChain-based agent for automotive SRS engineering.

This package provides agents and tools for ASPICE SWE.1/SWE.2 workflows,
following ISO 26262 functional safety standards.
"""

__version__ = "0.2.0"

from apollo.apollo_1.tools import all_tools
from apollo.apollo_1.agents.srs_analyst import run_srs_to_swe2_workflow

__all__ = [
    "__version__",
    "all_tools",
    "run_srs_to_swe2_workflow",
]
