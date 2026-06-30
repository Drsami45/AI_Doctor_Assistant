"""
core/memory.py
Manages chat history for the conversation. Streamlit reruns the whole script
on every interaction, so history is stored in st.session_state and converted
to LangChain message objects whenever the chain needs it.
"""

from __future__ import annotations

from typing import Any, Literal, TypedDict

from langchain_core.messages import AIMessage, BaseMessage, HumanMessage

import config


class ChatMessage(TypedDict):
    """A single turn stored in session state."""
    role: Literal["user", "assistant"]
    content: str


def init_history(session_state: Any) -> None:
    """Ensures chat_history exists in session state before first use."""
    if "chat_history" not in session_state:
        session_state.chat_history = [] 


def get_langchain_history(
    session_state: Any, max_turns: int = config.MAX_HISTORY_TURNS
) -> list[BaseMessage]:
    """
    Converts the last `max_turns` exchanges from session_state into
    LangChain message objects for the prompt's MessagesPlaceholder.
    """
    messages: list[BaseMessage] = []
    recent: list[ChatMessage] = session_state.chat_history[-(max_turns * 2):]
    for msg in recent:
        if msg["role"] == "user":
            messages.append(HumanMessage(content=msg["content"]))
        else:
            messages.append(AIMessage(content=msg["content"]))
    return messages


def add_message(session_state: Any, role: Literal["user", "assistant"], content: str) -> None:
    """Appends a single message to the session history."""
    session_state.chat_history.append(ChatMessage(role=role, content=content))


def clear_history(session_state: Any) -> None:
    """Resets the conversation history."""
    session_state.chat_history = []