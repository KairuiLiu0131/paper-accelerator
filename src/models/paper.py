"""Data model describing a paper's metadata and raw content."""

from pydantic import BaseModel


class Paper(BaseModel):
    """Represents a paper with minimal metadata and source payload."""

    # TODO: expand fields for authors, title, and fetched content details.
    source_url: str
    raw_content: str | bytes | None = None
