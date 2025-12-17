import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def clean_code(llm_output: str) -> str:
    """
    Remove markdown code blocks and return pure Python code.
    """
    lines = llm_output.strip().splitlines()
    cleaned = []

    for line in lines:
        if line.strip().startswith("```"):
            continue
        cleaned.append(line)

    return "\n".join(cleaned).strip()


def generate_fix_from_llm(pytest_output, code):
    prompt = f"""
You are a senior Python engineer.

A pytest test failed.

PYTEST OUTPUT:
{pytest_output}

SOURCE CODE:
{code}

TASK:
- Fix the bug
- Return ONLY valid Python code
- Do NOT use markdown
- Do NOT include explanations
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    raw_code = response.choices[0].message.content
    return clean_code(raw_code)
