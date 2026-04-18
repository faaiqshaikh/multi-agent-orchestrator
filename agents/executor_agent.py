from openai import OpenAI
from config import OPENAI_API_KEY, MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def executor_agent(task, research):
    prompt = f"""
    You are an Execution Agent.

    Task: {task}

    Research:
    {research}

    Produce a final structured solution.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
