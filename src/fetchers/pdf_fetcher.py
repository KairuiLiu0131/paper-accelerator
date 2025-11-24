"""Fetcher for downloading PDF files for further parsing."""

from src.fetchers.base import AbstractPaperFetcher
from src.models.paper import Paper


class PDFFetcher(AbstractPaperFetcher):
    """Fetches and returns PDF payloads for downstream parsing."""

    # TODO: support local paths and remote URLs with retries.
    def fetch(self, url: str) -> Paper:
        """Download a PDF and wrap it in a Paper model."""
        raise NotImplementedError
