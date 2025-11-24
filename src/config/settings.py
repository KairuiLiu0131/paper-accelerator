"""Application configuration setup for environment-driven settings."""

from dataclasses import dataclass
from os import getenv

from dotenv import load_dotenv


@dataclass
class Settings:
    """Container for global configuration values loaded from environment."""

    openai_api_key: str | None = None
    openai_model: str = "gpt-4o-mini"


def load_settings() -> Settings:
    """Load and return application settings."""
    load_dotenv()
    return Settings(
        openai_api_key=getenv("OPENAI_API_KEY"),
        openai_model=getenv("OPENAI_MODEL", "gpt-4o-mini"),
    )
