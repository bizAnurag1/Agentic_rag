from src.agents import get_agent_executor

def answer_query(query: str):
    """Determines whether to use RAG system or external tools."""
    get_agent_executor().invoke(query)
    

# Example Queries
if __name__ == "__main__":
    # print(answer_query("Is there any possibilities of snowfall in Manali, India next week?"))
    print(answer_query("What is Threshold Logic Units?"))
    # print(answer_query("Who is the prime minister of India?"))