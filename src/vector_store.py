from pymongo import MongoClient
# from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain_mongodb import MongoDBAtlasVectorSearch
# from langchain.embeddings import CohereEmbeddings
from langchain_cohere import CohereEmbeddings
from config.config import MONGO_CONNECTION_STRING, MONGO_DB_NAME, MONGO_COLLECTION_NAME, ATLAS_VECTOR_SEARCH_INDEX_NAME, COHERE_API_KEY
from src.doc_processing import load_and_process_pdfs


# Initialize Cohere Embeddings
embeddings = CohereEmbeddings(
    model="embed-english-v3.0", 
    cohere_api_key=COHERE_API_KEY,
    user_agent="langchain")


# Initialize MongoDB Client
mongo_client = MongoClient(MONGO_CONNECTION_STRING)
MONGODB_COLLECTION = mongo_client[MONGO_DB_NAME][MONGO_COLLECTION_NAME]
vector_store = MongoDBAtlasVectorSearch(
    collection=MONGODB_COLLECTION, 
    embedding=embeddings, 
    index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
    relevance_score_fn="cosine",
    )


def store_documents(pdf_files):
    """Embeds and stores documents into MongoDB."""
    documents = load_and_process_pdfs(pdf_files)
    for i in range(0, len(documents), 50):
        batch = documents[i:i+50]
        vector_store.add_documents(batch) 
