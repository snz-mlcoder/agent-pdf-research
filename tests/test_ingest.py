from src.ingest import load_and_split_pdf

def test_load_and_split_pdf_returns_chunks():
    chunks = load_and_split_pdf("tests/fixtures/sample.pdf")
    assert len(chunks) > 0

def test_load_chunks_have_source_metadata():
    chunks = load_and_split_pdf("tests/fixtures/sample.pdf")
    assert chunks[0].metadata["source"] == "tests/fixtures/sample.pdf"