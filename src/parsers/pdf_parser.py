"""Parser responsible for extracting text from PDF content."""

from src.models.paper import Paper


class PDFParser:
    """Parses PDF payloads into normalized text blocks."""

    def parse(self, paper: Paper) -> str:
        """Return extracted text from the PDF content in the paper."""
        if isinstance(paper.raw_content, bytes):
            return paper.raw_content.decode(errors="ignore")
        return str(paper.raw_content or "")
