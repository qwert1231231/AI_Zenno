# Zenno AI (scaffold)

This repository is a scaffold for a modular AI assistant with a high-performance core, Python backend, and simple web UI.

Structure

├── README.md               # Project info + setup
├── .env                    # API keys, DB config
│
├── core/                   # ⚙️ High-performance engine
│   ├── rust/               # Rust logic (speed-critical)
│   │   └── src/lib.rs
│   ├── cpp/                # C++ modules (optional)
│   │   └── src/ai_core.cpp
│   └── bindings/           # Bridge to Python
│       └── py_bindings.py
│
├── backend/                # 🧠 FastAPI + Python AI brain
│   ├── main.py             # App entry point
│   ├── ai_core.py          # Model + logic
│   ├── memory.py           # Chat memory (ChromaDB / JSON)
│   ├── auth.py             # Optional user system
│   ├── utils.py
│   └── requirements.txt
│
├── web/                    # 🌐 Website frontend
│   ├── index.html          # Chat UI
│   ├── css/style.css
│   ├── js/app.js           # Handles chat + API calls
│   └── assets/zenno_logo.png
│
└── docs/                   # 📚 Setup & vision
    ├── setup_guide.md
    └── roadmap.md

Quickstart

- Backend (FastAPI):
  - Create a virtual environment: `python -m venv .venv`
  - Install: `pip install -r backend/requirements.txt`
  - Run: `uvicorn backend.main:app --reload`

- Web UI:
  - Open `web/index.html` in your browser and point it at the backend API.

Notes

This is a scaffold with placeholder implementations for Rust/C++ components and a simple Python backend suitable for local development and extension.