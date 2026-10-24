from unittest.mock import patch, MagicMock
from langchain_core.documents import Document
import src
from src.schema import Answer, Citation
from src.query import query_documents

def test_query_documents_returns_structured_answer():
    fake_documents = [
        Document(page_content="This is a test document.", metadata={"source": "test_source.pdf", "page": 1})
    ]   

    mock_vector_store = MagicMock()
    mock_vector_store.similarity_search.return_value = fake_documents

    fake_answer = Answer(answer="This is a test answer.",
                        citations=[Citation(text="This is a test citation.", page_number=1, source="test_source.pdf")],
                        confidence="high")
    with patch("src.query.ChatOpenAI") as mock_chat_openai:
        mock_llm = MagicMock()
        mock_llm.with_structured_output.return_value.invoke.return_value = fake_answer
        mock_chat_openai.return_value = mock_llm

        result = query_documents(mock_vector_store, "test query")

    assert result == fake_answer
    mock_vector_store.similarity_search.assert_called_once()