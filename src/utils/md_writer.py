"""Markdown writer utilities for exporting summaries."""

from src.models.summary import Summary


def render_markdown(summary: Summary) -> str:
    """Render the Summary model into a Markdown string."""
    sections = [
        ("Research Question", summary.research_question),
        ("10-Second Summary", summary.ten_second_summary),
        ("Main Findings", summary.main_findings),
        ("Significance", summary.significance),
        ("Real-World Applications", summary.real_world_applications),
        ("Cross-Disciplinary Insights", summary.cross_disciplinary_insights),
    ]

    lines = ["# Paper Summary"]
    for title, content in sections:
        lines.append(f"\n## {title}\n")
        lines.append(content or "_Pending data_")

    return "\n".join(lines)
