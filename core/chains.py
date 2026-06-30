"""
core/chains.py
Builds the LangChain chain (prompt -> LLM -> output parser) using LCEL
(LangChain Expression Language) syntax.
"""

from __future__ import annotations

from langchain_core.messages import BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable

from core.llm import get_llm
from core.prompts import chat_prompt


def build_chain() -> Runnable:
    """
    Builds and returns the runnable chain:
    prompt template -> Gemini model -> string output parser.
    """
    llm = get_llm()
    parser = StrOutputParser()
    return chat_prompt | llm | parser


def get_response(chain: Runnable, user_input: str, history: list[BaseMessage]) -> str:
    """
    Invokes the chain with the current user input and conversation history.

    Args:
        chain: the runnable chain returned by build_chain().
        user_input: the latest message from the user.
        history: prior conversation turns as LangChain message objects.

    Returns:
        The assistant's reply as plain text.
    """
    result = chain.invoke({"input": user_input, "history": history})
    return str(result)