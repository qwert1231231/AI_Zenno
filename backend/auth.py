"""
Minimal auth helpers (placeholder).

In production, replace with proper password hashing, session management, and storage.
"""
import os
from typing import Optional

SECRET = os.getenv('SECRET_KEY', 'change-this-to-a-secret')


def verify_token(token: str) -> Optional[str]:
    # placeholder: token equals SECRET returns a fixed user
    if token == SECRET:
        return "admin"
    return None


def hash_password(pw: str) -> str:
    # placeholder; DO NOT use in production
    return pw[::-1]
