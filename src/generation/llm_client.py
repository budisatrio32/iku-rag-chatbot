"""
llm_client.py
Membuat klien LLM dengan format OpenAI. Mesinnya dipilih dari file .env, jadi kode
yang sama bisa dipakai untuk Gemini, Ollama (lokal), atau OpenAI:

    LLM_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
    LLM_MODEL=gemini-3.8-flash
    LLM_API_KEY=<API key dari Google AI Studio>
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


def get_client() -> tuple[OpenAI, str]:
    """Kembalikan (klien, nama model) sesuai isi .env."""
    base_url = os.getenv("LLM_BASE_URL")
    api_key = os.getenv("LLM_API_KEY")
    model = os.getenv("LLM_MODEL")

    missing = [name for name, value in
               (("LLM_BASE_URL", base_url), ("LLM_API_KEY", api_key), ("LLM_MODEL", model)) if not value]
    if missing:
        raise RuntimeError(f"Isi {', '.join(missing)} di file .env (contoh ada di .env.example).")

    # max_retries: percobaan ulang otomatis bila kena batas pemakaian (429) atau gangguan server
    client = OpenAI(base_url=base_url, api_key=api_key, max_retries=5, timeout=120)
    return client, model
