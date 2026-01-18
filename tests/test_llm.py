"""Tests for apollo.apollo_1.llm module."""

import os
import pytest
from unittest.mock import patch, MagicMock
from apollo.apollo_1.llm import get_llm, LLMProvider

class TestLLMFactory:
    """Test LLM factory function."""

    @patch('apollo.apollo_1.llm.ChatOpenAI')
    def test_get_llm_openai_default(self, mock_chat_openai):
        """Test default provider is OpenAI."""
        with patch.dict(os.environ, {}, clear=True):
            get_llm()
            mock_chat_openai.assert_called_with(
                model="gpt-4-turbo",
                temperature=0
            )

    @patch('apollo.apollo_1.llm.ChatOpenAI')
    def test_get_llm_openai_explicit(self, mock_chat_openai):
        """Test explicit OpenAI provider."""
        with patch.dict(os.environ, {"LLM_PROVIDER": "openai", "OPENAI_MODEL": "gpt-3.5-turbo"}):
            get_llm()
            mock_chat_openai.assert_called_with(
                model="gpt-3.5-turbo",
                temperature=0
            )

    @patch('apollo.apollo_1.llm.ChatOpenAI')
    def test_get_llm_local(self, mock_chat_openai):
        """Test local provider configuration."""
        env_vars = {
            "LLM_PROVIDER": "local",
            "LOCAL_LLM_BASE_URL": "http://localhost:1234/v1",
            "LOCAL_LLM_API_KEY": "test-key",
            "LOCAL_LLM_MODEL": "test-model"
        }
        with patch.dict(os.environ, env_vars):
            get_llm()
            mock_chat_openai.assert_called_with(
                base_url="http://localhost:1234/v1",
                api_key="test-key",
                model="test-model",
                temperature=0
            )

    def test_get_llm_anthropic_import_error(self):
        """Test Anthropic provider raises error if package missing."""
        with patch.dict(os.environ, {"LLM_PROVIDER": "anthropic"}), \
             patch.dict('sys.modules', {'langchain_anthropic': None}):
            with pytest.raises(ImportError, match="langchain-anthropic not installed"):
                get_llm()

    def test_get_llm_unsupported_provider(self):
        """Test error for unsupported provider."""
        with pytest.raises(ValueError, match="Unsupported LLM provider"):
            get_llm(provider="invalid")
