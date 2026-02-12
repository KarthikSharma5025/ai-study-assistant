import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

SYSTEM_PROMPT = """
You are an AI Study Assistant for college students.
Use bullet points.
Be concise and accurate.
"""

def ai_agent(user_input):
    payload = {
        "model": "llama3",
        "prompt": f"{SYSTEM_PROMPT}\n\n{user_input}",
        "stream": False,
        "options": {
            "temperature": 0.4,
            "num_ctx": 2048
        }
    }

    response = requests.post(OLLAMA_URL, json=payload)
    data = response.json()

    return data["response"]
