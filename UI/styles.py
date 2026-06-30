"""
ui/styles.py
Custom CSS injected into the Streamlit app for a polished look.
"""

from __future__ import annotations

CUSTOM_CSS: str = """
<style>
/* Overall app background */
.stApp {
    background: linear-gradient(135deg, #f0f7ff 0%, #e8f5f0 100%);
}

/* Main title styling */
.main-title {
    font-size: 2.4rem;
    font-weight: 800;
    background: linear-gradient(90deg, #0d9488, #2563eb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.2rem;
}

.subtitle {
    color: #475569;
    font-size: 1.05rem;
    margin-bottom: 1.2rem;
}

/* Chat bubble containers */
.chat-bubble-user {
    background: #2563eb;
    color: white;
    padding: 12px 16px;
    border-radius: 18px 18px 4px 18px;
    margin: 8px 0;
    max-width: 80%;
    margin-left: auto;
    box-shadow: 0 2px 6px rgba(37, 99, 235, 0.25);
}

.chat-bubble-assistant {
    background: #ffffff;
    color: #1e293b;
    padding: 12px 16px;
    border-radius: 18px 18px 18px 4px;
    margin: 8px 0;
    max-width: 80%;
    border: 1px solid #e2e8f0;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
}

/* Disclaimer banner */
.disclaimer-box {
    background: #fff7ed;
    border-left: 4px solid #f97316;
    padding: 10px 14px;
    border-radius: 8px;
    font-size: 0.88rem;
    color: #7c2d12;
    margin-bottom: 1rem;
}

/* Emergency alert box */
.emergency-box {
    background: #fef2f2;
    border-left: 5px solid #dc2626;
    padding: 14px 18px;
    border-radius: 8px;
    color: #7f1d1d;
    font-weight: 500;
    margin: 10px 0;
}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background: #f8fafc;
    border-right: 1px solid #e2e8f0;
}

/* Buttons */
.stButton button {
    border-radius: 10px;
    font-weight: 600;
}
</style>
"""