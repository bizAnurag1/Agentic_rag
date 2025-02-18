from langchain.agents import AgentType, initialize_agent
from src.tools import tools
from langchain_cohere import ChatCohere

llm = ChatCohere(model = 'command-r-plus' , temperature=0)

def get_agent_executor():
    """Returns an agent executor with tools integrated."""
    return initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )