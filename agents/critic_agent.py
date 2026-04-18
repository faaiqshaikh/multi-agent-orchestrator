from openai import OpenAI
from config import OPENAI_API_KEY, MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def critic_agent(output: str):
    prompt = f"""
    You are a Critic Agent.

    Evaluate this output:
    {output}

    Point out mistakes and improvements.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
