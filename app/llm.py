import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_description(table_name: str) -> str:
    prompt = f"""
    Provide a concise enterprise-grade description of a database table named '{table_name}'.
    Include possible business context and governance considerations.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a data governance expert."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

