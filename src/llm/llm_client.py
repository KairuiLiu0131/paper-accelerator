"""Client wrapper for interacting with LLM providers."""

from typing import Any

from openai import OpenAI

from src.config.settings import Settings, load_settings

# TODO: add retry, rate limiting, and provider selection logic.


class LLMClient:
    """Lightweight client facade for LLM API calls."""

    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or load_settings()
        self.client = (
            OpenAI(api_key=self.settings.openai_api_key)
            if self.settings.openai_api_key
            else None
        )

    def _offline_summary(self, content: str) -> str:
        """Provide a stub summary when no API key is configured."""
        return (
            "Research Question: What is the effect of AI on productivity?\n\n"
            "10-Second Summary: AI adoption appears to boost productivity in the mock paper.\n\n"
            "Main Findings: The placeholder study reports significant improvements when AI tools are used.\n\n"
            "Significance: Suggests automation can enhance knowledge work throughput.\n\n"
            "Real-World Applications: Organizations can pilot AI copilots to streamline workflows.\n\n"
            "Cross-Disciplinary Insights: Combines insights from economics, AI, and organizational behavior."
        )

    def generate_summary(self, content: str, prompt: str) -> Any:
        """Call the underlying LLM with the given content and prompt."""
        if not self.client:
            return self._offline_summary(content)

        try:
            response = self.client.chat.completions.create(
                model=self.settings.openai_model,
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": content},
                ],
            )
            return response.choices[0].message.content or ""
        except Exception:
            return self._offline_summary(content)
