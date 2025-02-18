from src.prompt import construct_prompt
from src.vector_store import vector_store
from config.config import COHERE_API_KEY, OPENWEATHERMAP_API_KEY
import cohere, requests, os
from langchain_community.utilities import SerpAPIWrapper
from dotenv import load_dotenv

load_dotenv()
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
co = cohere.Client(COHERE_API_KEY)

def rag_query(query):
    
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 1})
    docs = retriever.invoke(query)

    # Combine retrieved chunks into a single text block
    retrieved_content = "\n\n".join([doc.page_content for doc in docs])

    # Construct the LLM prompt
    prompt = construct_prompt(query, retrieved_content)

    # Generate answer using Cohere LLM
    response = co.generate(
        model="command-r-plus",
        prompt=prompt,
        max_tokens=500,
        temperature=0.3
    )

    return response.generations[0].text.strip(), docs


def get_weather(location: str) -> str:
    """Fetches weather information for a given location."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
    response = requests.get(url).json()
    
    if "main" in response:
        temp = response["main"]["temp"]
        return f"The temperature in {location} is {temp}°C."
    
    return "Weather data not found."

def search(query):
    search = SerpAPIWrapper()
    return search.run(query)