"""Strategy for producing structured paper summaries."""

from typing import List

from src.llm.llm_client import LLMClient
from src.llm.prompts import default_summary_prompt
from src.models.summary import Summary


class StructuredSummarizer:
    """Coordinates LLM calls to produce structured summaries."""

    def __init__(self, llm_client: LLMClient | None = None) -> None:
        self.llm_client = llm_client or LLMClient()

    def _split_sections(self, raw_summary: str) -> List[str]:
        """Split the model response into the six summary sections."""
        sections = [part.strip() for part in raw_summary.split("\n\n") if part.strip()]
        while len(sections) < 6:
            sections.append("")
        return sections[:6]

    def summarize(self, content: str) -> Summary:
        """Generate a structured summary from raw content."""
        prompt = default_summary_prompt()
        raw_summary = self.llm_client.generate_summary(content, prompt)
        parsed_sections = self._split_sections(str(raw_summary))

        return Summary(
            research_question=parsed_sections[0],
            ten_second_summary=parsed_sections[1],
            main_findings=parsed_sections[2],
            significance=parsed_sections[3],
            real_world_applications=parsed_sections[4],
            cross_disciplinary_insights=parsed_sections[5],
        )
