"""Fetcher for retrieving paper data from SSRN sources."""

from src.fetchers.base import AbstractPaperFetcher
from src.models.paper import Paper


class SSRNFetcher(AbstractPaperFetcher):
    """Fetches papers using SSRN endpoints or page parsing."""

    # TODO: wire up authentication and resilient requests.
    def fetch(self, url: str) -> Paper:
        """Fetch SSRN paper metadata and content."""
        raise NotImplementedError
