"""
utils/disclaimers.py
Centralized disclaimer and emergency message text.
"""

from __future__ import annotations

GENERAL_DISCLAIMER: str = (
    "⚠️ **Disclaimer:** This assistant provides general health information only. "
    "It is **not** a substitute for professional medical advice, diagnosis, or "
    "treatment. Always consult a qualified healthcare provider for any medical concerns."
)

EMERGENCY_MESSAGE: str = (
    "🚨 **This sounds like it could be a medical emergency.**\n\n"
    "Please **call your local emergency number immediately** or go to the nearest "
    "emergency room. Do not rely on this assistant for urgent or life-threatening "
    "symptoms.\n\n"
    "If you are having thoughts of self-harm or suicide, please reach out right now "
    "to a crisis helpline or emergency services in your country, or talk to someone "
    "you trust."
)

SIDEBAR_ABOUT: str = (
    "**AI Doctor Assistant** uses Google's Gemini model (via LangChain) to offer "
    "general, educational health insights based on the symptoms or questions you "
    "share. It is designed for informational purposes only."
)