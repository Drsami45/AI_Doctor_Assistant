"""
app.py
Main entry point for the AI Doctor Assistant Streamlit app.
Run with: streamlit run app.py   (or: uv run streamlit run app.py)
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import streamlit as st
from langchain_core.runnables import Runnable

import config
from core.chains import build_chain, get_response
from core.memory import add_message, get_langchain_history, init_history
from UI.components import (
    render_chat_history,
    render_emergency_alert,
    render_header,
    render_sidebar,
)
from UI.styles import CUSTOM_CSS
from utils.validators import contains_emergency_keywords, is_empty_input, sanitize_input

# ---------- Page config (must be the first Streamlit call) ----------
st.set_page_config(
    page_title=config.APP_TITLE,
    page_icon=config.APP_ICON,
    layout="centered",
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# ---------- Cached resources ----------
@st.cache_resource
def load_chain() -> Runnable:
    """Builds the LangChain chain once and caches it across reruns/sessions."""
    return build_chain()


@st.cache_data
def load_quick_symptoms() -> list[str]:
    """Loads the quick-select symptom phrases from the data file."""
    data_path = Path(__file__).parent / "data" / "sample_symptoms.json"
    with data_path.open("r", encoding="utf-8") as f:
        data: dict[str, Any] = json.load(f)
    return list(data["quick_symptoms"])


# ---------- Initialize session state ----------
init_history(st.session_state)
chain: Runnable = load_chain()
quick_symptoms: list[str] = load_quick_symptoms()

# ---------- Render static UI ----------
render_header()
clicked_symptom: str | None = render_sidebar(quick_symptoms)
render_chat_history(st.session_state.chat_history)

# ---------- Handle input ----------
typed_input: str | None = st.chat_input("Describe your symptoms or ask a health question...")
user_input: str | None = clicked_symptom if clicked_symptom else typed_input

if user_input:
    cleaned_input: str = sanitize_input(user_input)

    if is_empty_input(cleaned_input):
        st.warning("Please enter a valid message.")
    else:
        add_message(st.session_state, "user", cleaned_input)

        if contains_emergency_keywords(cleaned_input):
            render_emergency_alert()

        with st.spinner("Analyzing your symptoms..."):
            try:
                history = get_langchain_history(st.session_state)
                reply: str = get_response(chain, cleaned_input, history)
            except Exception as exc:  # noqa: BLE001 - surface any API/runtime error to the user
                reply = (
                    "⚠️ Sorry, something went wrong while generating a response. "
                    f"Please try again. (Error: {exc})"
                )

        add_message(st.session_state, "assistant", reply)
        st.rerun()