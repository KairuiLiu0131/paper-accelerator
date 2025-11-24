"""Structured summary schema for LLM-generated outputs."""

from pydantic import BaseModel


class Summary(BaseModel):
    """Represents the structured summary fields for a paper."""

    # TODO: include richer sections and formatting metadata as needed.
    research_question: str | None = None
    ten_second_summary: str | None = None
    main_findings: str | None = None
    significance: str | None = None
    real_world_applications: str | None = None
    cross_disciplinary_insights: str | None = None
