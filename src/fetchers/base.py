"""Abstract interface for fetching paper content from various sources."""

from abc import ABC, abstractmethod
from src.models.paper import Paper


class AbstractPaperFetcher(ABC):
    """Defines the contract for source-specific paper fetchers."""

    @abstractmethod
    def fetch(self, url: str) -> Paper:
        """Retrieve paper content and return a populated Paper model."""
        raise NotImplementedError
