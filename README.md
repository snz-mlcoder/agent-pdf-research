# Project Overview
A CLI tool that indexes one or more PDF documents and answers questions about them using an LLM, with citation-backed answers (source file + page number) and a persistent vector store.

# Features
- Multi-PDF ingestion and indexing
- Persistent vector store (no re-embedding on every run)
- Citation-backed answers (source file + page number)
- Confidence level per answer

# Installation
uv sync

# Usage (هر دو دستور ingest و query)
uv run python main.py ingest --pdf tests/fixtures/sample.pdf
uv run python main.py query --question  "What is the Transformer based on?"


# Technologies
- Python
- LangChain
- LangChain-OpenAI
- LangChain-Chroma
- LangChain-Community
- ChromaDB (persistent vector store)
- Pydantic
- PyPDF
- pytest


# Project Structure
agent-pdf-research/
├── main.py
├── src/
│   ├── __init__.py
│   ├── ingest.py
│   ├── vectorstore.py
│   ├── query.py
│   └── schema.py
├── tests/
│   ├── fixtures/
│   │   └── sample.pdf
│   ├── test_ingest.py
│   └── test_query.py
├── pyproject.toml
├── .env.example
└── README.md

# Known Limitations
This tool only works with PDFs that have extractable text. Scanned documents or
image-based PDFs (without an OCR layer) will not be indexed correctly, since no
text can be extracted from them.

# Future Improvements
- Add OCR support for scanned/image-based PDFs
- Support additional file formats (e.g., .docx, .txt)
- Allow querying across all ingested PDFs with source filtering

# Tests
uv run pytest 

# Future Improvements
- Add OCR support for scanned/image-based PDFs
- Support additional file formats (e.g., .docx, .txt)
- Allow querying across all ingested PDFs with source filtering