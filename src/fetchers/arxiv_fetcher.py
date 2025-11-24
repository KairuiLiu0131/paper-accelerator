"""Fetcher for retrieving paper data from arXiv sources."""

from src.fetchers.base import AbstractPaperFetcher
from src.models.paper import Paper


class ArxivFetcher(AbstractPaperFetcher):
    """Fetches papers using arXiv APIs or page scraping."""

    # TODO: add initialization for client/session handling.
    def fetch(self, url: str) -> Paper:
        """Fetch arXiv paper metadata and content."""
        raise NotImplementedError
