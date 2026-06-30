# 🩺 AI Doctor Assistant

A real-time, chat-based AI health insights assistant built with **Streamlit**,
**LangChain**, and the **Google Gemini API**, managed with **uv**.

> ⚠️ This project provides general health information only. It is not a substitute
> for professional medical advice, diagnosis, or treatment.

## Project Structure

```
ai-doctor-assistant/
├── app.py                  # Main Streamlit entry point (UI only)
├── config.py                # Loads env vars, API keys, constants
├── pyproject.toml            # uv project + dependency definition
├── requirements.txt          # pip fallback (mirrors pyproject.toml)
├── .env                       # GOOGLE_API_KEY stored here (never committed)
├── .gitignore
│
├── core/
│   ├── __init__.py
│   ├── llm.py                 # LangChain + Gemini model setup
│   ├── prompts.py             # System prompt / chat template
│   ├── chains.py               # LCEL chain (prompt -> model -> parser)
│   └── memory.py               # Conversation history handling
│
├── utils/
│   ├── __init__.py
│   ├── validators.py           # Input sanitization, emergency-keyword checks
│   └── disclaimers.py          # Medical disclaimer text, safety guardrails
│
├── ui/
│   ├── __init__.py
│   ├── components.py           # Reusable Streamlit UI components (chat bubbles, sidebar)
│   └── styles.py                # Custom CSS for an attractive interface
│
└── data/
    └── sample_symptoms.json     # Quick-select symptom options
```

## Setup Instructions (using uv)

### 1. Install uv (skip if already installed)
```bash
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Install project dependencies
From the project root (where `pyproject.toml` lives):
```bash
uv sync
```
This creates a `.venv/` folder automatically and installs every dependency listed
in `pyproject.toml`, picking the newest compatible versions with working
prebuilt wheels for your platform.

### 3. Get a Google API key
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in and click **"Create API key"**
3. Copy the key

### 4. Configure your environment
Open the `.env` file in the project root and replace the placeholder:
```
GOOGLE_API_KEY=your_actual_key_here
```

### 5. Run the app
```bash
uv run streamlit run app.py
```
`uv run` automatically uses the project's `.venv` — no manual activation needed.
The app opens in your browser, usually at `http://localhost:8501`.

## VS Code setup (recommended)
1. Open the project folder in VS Code.
2. Press `Ctrl+Shift+P` → **"Python: Select Interpreter"**.
3. Choose the interpreter inside `.venv` (created by `uv sync`).
   This removes false "import could not be resolved" warnings, since VS Code
   will then look in the same environment uv installed packages into.

## How It Works

1. The user types a symptom/question in the chat input, or clicks a quick-symptom
   button in the sidebar.
2. The message is checked for emergency keywords (e.g., "chest pain", "suicidal").
   If matched, a red emergency alert is shown immediately, in addition to the
   normal response.
3. The message, plus recent conversation history, is sent through a LangChain
   LCEL chain: **Prompt Template → Gemini Model → String Output Parser**.
4. The model's reply (structured into possible causes / self-care tips / when to
   see a doctor) is displayed as a chat bubble.
5. Conversation history is kept in `st.session_state`, so follow-up questions
   retain context within the session.

## Notes

- Model used: `gemini-1.5-flash` (fast and cost-effective). Change it in `config.py`
  if you want `gemini-1.5-pro` instead.
- Never commit your `.env` file — it's already excluded via `.gitignore`.
- For deployment on Streamlit Community Cloud, add `GOOGLE_API_KEY` under
  **App settings → Secrets** instead of relying on `.env`.
- `requirements.txt` is kept in sync with `pyproject.toml` for anyone who prefers
  plain `pip install -r requirements.txt` over `uv`.