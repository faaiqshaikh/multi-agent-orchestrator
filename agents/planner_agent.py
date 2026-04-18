from openai import OpenAI
from config import OPENAI_API_KEY, MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def planner_agent(task: str):
    prompt = f"""
    You are a Planner Agent.
    Break the following task into steps:

    Task: {task}

    Return clear numbered steps.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
