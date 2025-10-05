"""
Simple JSON-backed chat memory. For production, replace with ChromaDB or a vector DB.
"""
import json
import os
from threading import Lock

_db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'memory.json')
_lock = Lock()


def _ensure_db():
    dirpath = os.path.dirname(_db_path)
    os.makedirs(dirpath, exist_ok=True)
    if not os.path.exists(_db_path):
        with open(_db_path, 'w', encoding='utf-8') as f:
            json.dump({}, f)


def save_message(user_id: str, message: str, incoming: bool = True):
    _ensure_db()
    with _lock:
        with open(_db_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        user_conv = data.get(user_id, [])
        user_conv.append({"incoming": incoming, "message": message})
        data[user_id] = user_conv
        with open(_db_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)


def get_conversation(user_id: str):
    _ensure_db()
    with open(_db_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get(user_id, [])
