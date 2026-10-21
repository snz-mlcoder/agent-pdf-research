from langchain_openai import ChatOpenAI 
from src.schema import Citation, Answer

def query_documents(vectorstore, query: str, top_k: int = 3) -> Answer:
    results = vectorstore.similarity_search(query, k=top_k)

    context_parts = []
    for doc in results:
        source = doc.metadata.get("source", "Unknown")
        page_number = doc.metadata.get("page", -1) + 1  # Adjust for 0-based index
        context_parts.append(doc.page_content + f"\n\nSource: {source}, Page: {page_number}")

    context = "\n\n".join(context_parts)

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, max_tokens=300)
    structured_llm =llm.with_structured_output(Answer)

    prompt =f"""Answer the question using ONLY the context below. 
    For each claim, cite the exact source file and page number shown in the context.

    Context:
    {context}

    Question: {query}"""

    return structured_llm.invoke(prompt)