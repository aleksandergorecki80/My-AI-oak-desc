"""
Reusable Groq client setup: loads environment variables and returns a ready
client plus the configured model name.
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq


def init_groq_client():
    """Initialize Groq client using .env config."""
    project_root = Path(__file__).parent.parent.parent
    env_path = project_root / ".env"
    load_dotenv(dotenv_path=env_path, override=True)

    groq_api_key = os.getenv("GROQ_API_KEY")
    groq_model = os.getenv("GROQ_MODEL")

    if not groq_api_key:
        print("Error: GROQ_API_KEY not found in environment variables!")
        print("Please add GROQ_API_KEY to your .env file in the project root.")
        exit(1)

    print(f"✓ Groq API Key found (begins with: {groq_api_key[:8]})")
    client = Groq(api_key=groq_api_key)
    print("✓ Groq client created successfully")

    return client, groq_model

