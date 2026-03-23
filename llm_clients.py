import os

from google import genai
from google.genai import types
from openai import OpenAI


# Interact with Google's Gemini model.
def call_gemini(text_input: str):

    if not os.environ.get("GEMINI_API_KEY"):
        return "Gemini API key missing."

    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    model = "gemini-2.5-pro"
    # system = types.GenerateContentConfig(system_instruction=config.SYSTEM_PROMPT)

    response = client.models.generate_content(
        model=model,
        contents=text_input,  # config=system
    )

    return response.text


def call_ollama(text_input: str, model_name: str):

    client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama-local")

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": config.SYSTEM_PROMPT},
            {"role": "user", "content": text_input},
        ],
        # temperature = 0.1
    )

    return response.choices[0].message.content
