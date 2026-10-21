from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def build_vectorstore(docs, persist_directory: str = "chroma_db"):
    """
    Build a vector store from a list of documents.

    Args:
        docs (List[Document]): A list of text chunks.
        persist_directory (str): Directory to persist the vector store.
    Returns:
        Chroma: A Chroma vector store instance.     
"""
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorstore = Chroma.from_documents(docs, embeddings, persist_directory=persist_directory)
    return vectorstore

def load_vectorstore(persist_directory: str = "chroma_db"):
    """
    Load a vector store from a persisted directory.

    Args:
        persist_directory (str): Directory where the vector store is persisted.
    Returns:
        Chroma: A Chroma vector store instance.
    """
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorstore = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    return vectorstore