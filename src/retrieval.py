from langchain.chains import RetrievalQA
from src.vector_store import vector_store


def get_retriever():
    """Returns a retriever instance from the vector store."""
    return vector_store.as_retriever()

def get_qa_chain():
    """Returns a RetrievalQA chain using Cohere."""
    retriever = get_retriever()
    return RetrievalQA.from_chain_type(llm=get_cohere_llm(), chain_type="stuff", retriever=retriever)
