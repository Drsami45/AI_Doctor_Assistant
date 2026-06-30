"""
core/llm.py
Initializes the LangChain chat model wrapper around Google's Gemini API.
"""

from __future__ import annotations

from langchain_google_genai import ChatGoogleGenerativeAI

import config


def get_llm() -> ChatGoogleGenerativeAI:
    """
    Returns a configured ChatGoogleGenerativeAI instance.
    Cached at the app level via st.cache_resource (see app.py), so this
    should only run once per session.
    """
    return ChatGoogleGenerativeAI(
        model=config.MODEL_NAME,
        google_api_key=config.GOOGLE_API_KEY,
        temperature=config.TEMPERATURE,
        max_output_tokens=config.MAX_OUTPUT_TOKENS,
    )