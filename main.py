from fastapi import FastAPI
from pydantic import BaseModel
from src.agents import get_agent_executor

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def answer_query(request: QueryRequest):
    """Determines whether to use RAG system or external tools."""
    response = get_agent_executor().run(request.query)
    if isinstance(response, bytes):  
        response = response.decode("utf-8")  # Convert bytes to string if needed
    
    response = response.strip().strip('"') 
    return response
    

# Example Queries
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # print(answer_query("Is there any possibilities of snowfall in Manali, India next week?"))
    # print(answer_query("What is Threshold Logic Units?"))
    # print(answer_query("Who is the prime minister of India?"))