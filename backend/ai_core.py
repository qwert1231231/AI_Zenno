"""
Simple AI core wrapper. Replace the generate_reply implementation with real model calls
(e.g., OpenAI, local LLM, or call into the Rust/C++ core via bindings).
"""
import os
from dotenv import load_dotenv
from .bindings import py_bindings

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

OPENAI_KEY = os.getenv('OPENAI_API_KEY')


def generate_reply(prompt: str) -> str:
    # placeholder logic: reverse the prompt and add a canned prefix
    try:
        # If we had a native core, call it
        # value = py_bindings.compute_heavy_cpp(len(prompt))
        return "Zenno: " + prompt[::-1]
    except Exception as e:
        return "Zenno: I failed to generate a reply: " + str(e)
