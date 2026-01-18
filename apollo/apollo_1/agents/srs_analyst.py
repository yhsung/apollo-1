import os
from langchain.agents import AgentExecutor, create_react_agent
from langchain_openai import ChatOpenAI
from langchain import hub
from langfuse.callback import CallbackHandler

# Import reusable tools from the tools module
from apollo.apollo_1.tools import all_tools as tools

# Initialize Langfuse Tracking
langfuse_handler = CallbackHandler(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST")
)

# --- Optimized SWE.1 to SWE.2 Transition Prompt ---

SRS_SWE1_FOR_SWE2_INSTRUCTIONS = """You are a professional Automotive Software Requirements Engineer. 
Your goal is to produce a Software Requirements Specification (SRS) that directly supports ASPICE SWE.2 (Software Architecture Design).
In addition to following SWE.1 and ISO 26262 standards, you must ensure the output is "allocatable" and contains "architectural impact analysis."

### Key Guiding Principles (For SWE.2 Seamless Integration):
1. **Requirement Atomicity**: Ensure each requirement describes only one function, making it easy to allocate to a single software component later.
2. **Arch-Impact Assessment**: Include an "Architectural Impact" field in requirement attributes, marking whether the requirement dictates CPU, memory, or specific communication designs.
3. **Interface Boundary Pre-definition**: If a requirement involves external modules, clearly define the interface parameter types. This will serve as the foundation for SWE.2 interface design.

### Produced Markdown SRS must follow this structure:
- ## 1. Traceability Link
  - [Stakeholder ID] -> [Redmine Issue Link]
- ## 2. Software Requirements Specification Table
  | Req_ID | Description (Shall/Should) | ASIL | Category | Arch Constraint? (Yes/No) | Target Component Type |
  | :--- | :--- | :--- | :--- | :--- | :--- |
- ## 3. Performance & Non-Functional Requirements
  - Explicitly list Timing, Memory, and Throughput constraints essential for SWE.2 dynamic analysis.
- ## 4. Functional Safety Considerations (ISO 26262 Integration)
  - List associated Safety Mechanisms.
- ## 5. SWE.2 Architectural Hints
  - Based on the requirements, suggest design patterns for SWE.2 (e.g., Redundancy, Error Correction Code, Layered Architecture).
"""

llm = ChatOpenAI(model="gpt-4-turbo", temperature=0)
base_prompt = hub.pull("hwchase17/react")

# Inject the English-optimized instructions
design_prompt = base_prompt.partial(
    instructions=SRS_SWE1_FOR_SWE2_INSTRUCTIONS
)

agent = create_react_agent(llm, tools, design_prompt)
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=20
)

def run_srs_to_swe2_workflow(issue_id, project_id):
    query = f"""
    Task: Initiate SWE.1 analysis for Redmine Issue #{issue_id} and prepare data for SWE.2.
    
    Steps:
    1. Retrieve the original stakeholder requirements.
    2. Search the knowledge base for ISO 26262 regulations and internal architectural guidelines.
    3. Generate a structured SRS annotated with architectural constraints and allocation suggestions.
    4. Save the results to Wiki titled 'SRS_SWE1_{issue_id}'.
    """
    
    response = agent_executor.invoke(
        {"input": query},
        {"callbacks": [langfuse_handler]}
    )
    return response

if __name__ == "__main__":
    # Example usage:
    # run_srs_to_swe2_workflow("102", "adas-platform")
    pass