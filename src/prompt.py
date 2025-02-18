def construct_prompt(query, retrieved_content):
    prompt = """
    You are an expert AI assistant. Answer the question using the retrieved information.
    Incase it is theoritical question and you have enough knowledge to answer it then you can add your points as well. 
    If you don’t have enough context, reply with "I don't have enough information.
    Answer the quetions from the available tools only."

    Retrieved Documents:
    {retrieved_content}

    Question: {query}

    Answer:
    """
    return prompt