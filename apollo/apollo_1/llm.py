"""
LLM Provider Factory.

This module handles the initialization of Large Language Models (LLMs)
based on the configured provider (OpenAI, Local, Anthropic, etc.).
"""

import os
from typing import Optional
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_openai import ChatOpenAI
# Note: Import other providers as needed (e.g., langchain_anthropic)

class LLMProvider:
    """Supported LLM providers."""
    OPENAI = "openai"
    LOCAL = "local"
    ANTHROPIC = "anthropic"

def get_llm(
    provider: Optional[str] = None,
    temperature: float = 0,
    model_name: Optional[str] = None
) -> BaseChatModel:
    """
    Get an LLM instance based on the provider configuration.
    
    Args:
        provider: Provider name (openai, local, anthropic). 
                  Defaults to LLM_PROVIDER env var or 'openai'.
        temperature: Sampling temperature. Defaults to 0.
        model_name: Model name override. Defaults to env var or provider default.
        
    Returns:
        Configured Chat Model instance.
    """
    # Determine provider
    if not provider:
        provider = os.getenv("LLM_PROVIDER", LLMProvider.OPENAI).lower()
        
    # --- OpenAI ---
    if provider == LLMProvider.OPENAI:
        model = model_name or os.getenv("OPENAI_MODEL", "gpt-4-turbo")
        return ChatOpenAI(
            model=model,
            temperature=temperature
        )
        
    # --- Local (e.g., LM Studio) ---
    elif provider == LLMProvider.LOCAL:
        base_url = os.getenv("LOCAL_LLM_BASE_URL", "http://localhost:1234/v1")
        api_key = os.getenv("LOCAL_LLM_API_KEY", "lm-studio")
        model = model_name or os.getenv("LOCAL_LLM_MODEL", "local-model")
        
        return ChatOpenAI(
            base_url=base_url,
            api_key=api_key,
            model=model,
            temperature=temperature
        )
        
    # --- Anthropic ---
    elif provider == LLMProvider.ANTHROPIC:
        try:
            from langchain_anthropic import ChatAnthropic
        except ImportError:
            raise ImportError(
                "langchain-anthropic not installed. "
                "Install with `pip install langchain-anthropic`."
            )
            
        model = model_name or os.getenv("ANTHROPIC_MODEL", "claude-3-opus-20240229")
        api_key = os.getenv("ANTHROPIC_API_KEY")
        
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable not set.")
            
        return ChatAnthropic(
            model=model,
            temperature=temperature,
            api_key=api_key
        )
        
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")
