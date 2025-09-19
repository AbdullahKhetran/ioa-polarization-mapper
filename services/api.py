import requests
from typing import Dict, Any
import streamlit as st


BACKEND_URL = st.secrets["BACKEND_URL"]
BACKEND_API_KEY = st.secrets["BACKEND_API_KEY"]


def get_polarization_score(topic: str) -> Dict[str, Any]:
    payload = {"topic": topic}
    headers = {"Authorization": BACKEND_API_KEY}

    try:
        response = requests.post(
            f"{BACKEND_URL}/analyze", json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Backend error {response.status_code}"}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
