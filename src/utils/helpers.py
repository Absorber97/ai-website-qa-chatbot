import os
from dotenv import load_dotenv

def load_api_key():
    """Load and return the OpenAI API key from environment variables."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OpenAI API key not found. Please check your .env file.")
    return api_key

def truncate_text(text, max_length=4000):
    """Truncate text to a maximum length."""
    return text[:max_length]