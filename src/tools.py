from langchain.tools import Tool
from src.rag_query import rag_query, get_weather, search
from langchain_community.agent_toolkits import load_tools



# Initialize tools
rag_tool = Tool(
    name="RAG Retrieval", 
    func=rag_query, 
    description="Retrieve relevant information from stored documents using Retrieval-Augmented Generation (RAG). Ideal for answering questions based on indexed PDFs, knowledge bases, or databases. the function returns response and retrived documents."
)

search_tool = Tool(
    name="Web Search", 
    func=search, 
    description="Perform a real-time web search to retrieve up-to-date information from the internet. Useful for news, recent events, and topics not covered in stored documents."
)

weather_tool = Tool(
    name="Weather Information", 
    func=get_weather, 
    description="Fetch real-time weather updates, including temperature, humidity, and forecasts, based on a specified location."
)

# weather_tool = load_tools(['openweathermap-api'])
# search_tool = load_tools(['serpapi'])

tools = [
    rag_tool,
    weather_tool,
    search_tool
]