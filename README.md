# paper-accelerator

Level 1 MVP - Universal Paper Thought Accelerator.

This repository currently contains minimal scaffolding for fetchers, parsers, LLM integration, and summarization strategies following a modular Python layout.

## Quickstart (vertical slice demo)

1. Install dependencies: `pip install -r requirements.txt`
2. (Optional) Export your OpenAI key: `export OPENAI_API_KEY=...`
3. Run the demo: `python -m src.main https://example.com/mock-paper`

The demo uses a mock URL, fake paper content, a pass-through parser, an LLM call with a simple prompt (with offline fallback), and renders a Markdown summary to STDOUT.
