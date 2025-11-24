"""Command-line entrypoint for the paper accelerator MVP."""

import argparse

from src.fetchers.url_fetcher import URLFetcher
from src.parsers.pdf_parser import PDFParser
from src.summarizers.structured_summarizer import StructuredSummarizer
from src.utils.md_writer import render_markdown


def main() -> None:
    """Run the paper processing pipeline from CLI inputs."""
    parser = argparse.ArgumentParser(description="Run the paper summarization demo.")
    parser.add_argument(
        "url",
        nargs="?",
        default="https://example.com/mock-paper",
        help="Mock URL for the demo run.",
    )
    args = parser.parse_args()

    paper = URLFetcher().fetch(args.url)
    content = PDFParser().parse(paper)
    summary = StructuredSummarizer().summarize(content)
    markdown = render_markdown(summary)

    print(markdown)


if __name__ == "__main__":
    main()
