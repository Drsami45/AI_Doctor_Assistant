"""
utils/validators.py
Basic input validation and emergency-keyword detection.
"""

from __future__ import annotations

import config


def is_empty_input(text: str) -> bool:
    """Returns True if the input is empty or just whitespace."""
    return not text or not text.strip()


def contains_emergency_keywords(text: str) -> bool:
    """
    Checks if the user's message contains any emergency-related keywords.
    This is a simple, fast safety net — not a substitute for real triage.
    """
    lowered = text.lower()
    return any(keyword in lowered for keyword in config.EMERGENCY_KEYWORDS)


def sanitize_input(text: str) -> str:
    """Basic cleanup of user input before sending it to the LLM."""
    return text.strip()