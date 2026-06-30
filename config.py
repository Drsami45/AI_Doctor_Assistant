"""
config.py
Loads environment variables and holds global constants for the app.
"""

from __future__ import annotations

import os
from dotenv import load_dotenv

# Load variables from the .env file into the process environment.
load_dotenv()


def _require_env(name: str) -> str:
    """
    Reads a required environment variable and raises a clear error if missing.
    Returns a plain `str` (never None) so downstream type checkers don't
    complain about Optional[str].
    """
    value = os.getenv(name)
    if not value or not value.strip():
        raise ValueError(
            f"{name} not found or empty. Open the .env file in the project "
            f"root and set {name}=your_actual_key_here."
        )
    return value.strip()


# ---- API Key ----
GOOGLE_API_KEY: str = _require_env("GOOGLE_API_KEY")

# ---- Model Settings ----
MODEL_NAME: str = "gemini-2.5-flash"   # fast + cost-effective, good for chat
TEMPERATURE: float = 0.4                # lower = more focused/safe answers
MAX_OUTPUT_TOKENS: int = 1024

# ---- App Settings ----
APP_TITLE: str = "AI Doctor Assistant"
APP_ICON: str = "🩺"

# ---- Conversation Settings ----
MAX_HISTORY_TURNS: int = 6  # number of user+assistant exchanges kept in context

# Keywords that should trigger an emergency warning instead of a normal answer.
EMERGENCY_KEYWORDS: list[str] = [
    "suicidal",
    "suicide",
    "kill myself",
    "want to die",
    "chest pain",
    "can't breathe",
    "cannot breathe",
    "severe bleeding",
    "unconscious",
    "heart attack",
    "stroke",
    "overdose",
    "not breathing",
    "severe burn",
    "choking",
]