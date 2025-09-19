import requests
from typing import Dict, Any
import os
from dotenv import load_dotenv


load_dotenv()
# fallback to localhost
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")


def get_polarization_score(topic: str) -> Dict[str, Any]:
    payload = {"topic": topic}
    try:
        response = requests.post(f"{BACKEND_URL}/analyze", json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Backend error {response.status_code}"}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
