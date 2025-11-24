"""Prompt templates for guiding LLM-based summarization."""

# TODO: add versioned prompt templates and A/B testing hooks.

def default_summary_prompt() -> str:
    """Return the default structured summary prompt template."""
    return (
        "Summarize the following paper content into: research question, 10-second summary, "
        "main findings, significance, real-world applications, and cross-disciplinary insights."
    )
