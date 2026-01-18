"""
Knowledge Base Tool - Hierarchical RAG for searching safety goals, organizational standards,
and historical SRS/SAD documents.
"""
import os
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.tools import Tool
from langchain_classic.retrievers import ParentDocumentRetriever
from langchain_core.stores import InMemoryStore
from langchain_text_splitters import RecursiveCharacterTextSplitter


# --- Hierarchical RAG Configuration ---
embeddings = OpenAIEmbeddings()
vector_db = Chroma(
    collection_name="hierarchical_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_db_my_project"
)
store = InMemoryStore()

parent_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
child_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50)

hierarchical_retriever = ParentDocumentRetriever(
    vectorstore=vector_db,
    docstore=store,
    child_splitter=child_splitter,
    parent_splitter=parent_splitter,
)


def search_knowledge_base(query: str) -> str:
    """
    Performs deep retrieval to find Safety Goals, organizational standards,
    and historical SRS/SAD documents.
    
    Args:
        query: The search query string
        
    Returns:
        Formatted string containing relevant document excerpts with sources
    """
    docs = hierarchical_retriever.invoke(query)
    formatted_docs = []
    for doc in docs[:3]:
        source = doc.metadata.get('filename') or doc.metadata.get('source', 'Unknown')
        formatted_docs.append(f"### Source: {source}\n{doc.page_content}")
    return "\n\n---\n\n".join(formatted_docs)


# LangChain Tool wrapper
Search_Knowledge_Base = Tool(
    name="Search_Knowledge_Base",
    func=search_knowledge_base,
    description="Search for upstream requirements and ISO 26262 safety regulations within the hierarchical knowledge base."
)
