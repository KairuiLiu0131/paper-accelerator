"""Generic fetcher for arbitrary web URLs containing paper content."""

from src.fetchers.base import AbstractPaperFetcher
from src.models.paper import Paper


class URLFetcher(AbstractPaperFetcher):
    """Fetches paper-like content from generic URLs."""

    def fetch(self, url: str) -> Paper:
        """Fetch content from a generic URL and wrap it as a Paper."""
        fake_content = (
            "This paper studies the effect of AI on productivity. "
            "We find significant improvements."
        )
        return Paper(source_url=url, raw_content=fake_content)
