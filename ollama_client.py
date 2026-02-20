import requests

OLLAMA_URL = "http://localhost:11434/api/chat"

def ask_model(prompt: str) -> str:
    payload = {
        "model": "llama3",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    return response.json()["message"]["content"]