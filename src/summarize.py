import json
import re
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text: str) -> str:
    if not text.strip():
        return "No text found in the document."

    prompt = f"""
    You are a legal document assistant specializing in trust and estate paperwork.

    Read the following document and:
    1. Write a concise, professional summary in paragraph form (2–4 sentences).
    2. Extract the key fields and return them as valid JSON.

    Respond in exactly this format:

    Summary: \n
    <summary>

    Extracted Info:
    <valid JSON>

    Document:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    raw_output = response.choices[0].message.content

    # Split into sections
    parts = re.split(r"Extracted Info:", raw_output, maxsplit=1)
    summary = parts[0].strip()
    json_part = parts[1].strip() if len(parts) > 1 else "{}"

    # Format JSON nicely
    try:
        parsed = json.loads(json_part)
        formatted_json = json.dumps(parsed, indent=2)
    except Exception:
        formatted_json = json_part  # leave raw if not valid JSON

    # Combine for display
    return f"{summary}\n\nExtracted Info:\n```json\n{formatted_json}\n```"
