from openai import OpenAI
from config import OPENAI_API_KEY, MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def researcher_agent(task: str):
    prompt = f"""
    You are a Research Agent.
    Gather useful information for:

    Task: {task}

    Provide key insights and facts.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
