# Setup Guide

1. Install Python 3.11+.
2. Create a virtual environment and activate it:

   On Windows (PowerShell):

   ```powershell
   python -m venv .venv; .\.venv\Scripts\Activate.ps1
   ```

3. Install backend dependencies:

   ```powershell
   pip install -r backend/requirements.txt
   ```

4. Run the backend:

   ```powershell
   uvicorn backend.main:app --reload
   ```

5. Open `web/index.html` in your browser.

Notes

- Fill `.env` with API keys before enabling external LLM providers.
- The `core` directory contains placeholders for Rust and C++ modules.