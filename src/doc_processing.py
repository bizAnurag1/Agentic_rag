# from langchain.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_process_pdfs(pdf_paths):
    """Loads and processes PDFs, splitting text into chunks."""
    documents = []
    for pdf_path in pdf_paths:
        loader = PyPDFLoader(pdf_path)
        documents.extend(loader.load())

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_docs = text_splitter.split_documents(documents)
    return split_docs