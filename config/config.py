import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

# MongoDB Configuration
MONGO_CONNECTION_STRING = os.getenv("MONGO_CONNECTION_STRING")
MONGO_DB_NAME = "rag_vectors_db"
MONGO_COLLECTION_NAME = "vector_emb"
ATLAS_VECTOR_SEARCH_INDEX_NAME = "index-vectorstores"

# Cohere API Key
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# SERP API Key
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

# Weather API Key
OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")