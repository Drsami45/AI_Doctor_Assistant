"""
ui/components.py
Reusable Streamlit UI rendering functions, kept separate from app logic.
"""

from __future__ import annotations

import streamlit as st

from core.memory import ChatMessage
from utils.disclaimers import EMERGENCY_MESSAGE, GENERAL_DISCLAIMER, SIDEBAR_ABOUT


def render_header() -> None:
    """Renders the page title, subtitle, and the persistent disclaimer banner."""
    st.markdown('<div class="main-title">🩺 AI Doctor Assistant</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Ask about your symptoms and get general, '
        "easy-to-understand health insights.</div>",
        unsafe_allow_html=True,
    )
    st.markdown(f'<div class="disclaimer-box">{GENERAL_DISCLAIMER}</div>', unsafe_allow_html=True)


def render_emergency_alert() -> None:
    """Renders the red emergency banner above the chat."""
    st.markdown(f'<div class="emergency-box">{EMERGENCY_MESSAGE}</div>', unsafe_allow_html=True)


def render_chat_message(role: str, content: str) -> None:
    """Renders a single chat bubble for either 'user' or 'assistant'."""
    css_class = "chat-bubble-user" if role == "user" else "chat-bubble-assistant"
    label = "🧑 You" if role == "user" else "🩺 AI Doctor Assistant"
    st.markdown(
        f'<div class="{css_class}"><strong>{label}</strong><br>{content}</div>',
        unsafe_allow_html=True,
    )


def render_chat_history(chat_history: list[ChatMessage]) -> None:
    """Renders the full conversation from session state, in order."""
    for msg in chat_history:
        render_chat_message(msg["role"], msg["content"])


def render_sidebar(quick_symptoms: list[str]) -> str | None:
    """
    Renders the sidebar with an About section, quick-select symptom buttons,
    and a clear-chat button.

    Returns:
        The symptom text if a quick-select button was clicked this run,
        otherwise None.
    """
    st.sidebar.title("ℹ️ About")
    st.sidebar.info(SIDEBAR_ABOUT)

    st.sidebar.markdown("---")
    st.sidebar.subheader("⚡ Quick Symptom Check")

    clicked_symptom: str | None = None
    for symptom in quick_symptoms:
        if st.sidebar.button(symptom, use_container_width=True, key=f"quick_{symptom}"):
            clicked_symptom = symptom

    st.sidebar.markdown("---")
    if st.sidebar.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

    return clicked_symptom