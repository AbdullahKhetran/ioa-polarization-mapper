import requests
from typing import Dict, Any
import streamlit as st
import jwt
import time
from dotenv import load_dotenv
import os

# # for localhost
# load_dotenv()
# BACKEND_URL = os.getenv("BACKEND_URL")
# JWT_SECRET = os.getenv("JWT_SECRET")


BACKEND_URL = st.secrets["BACKEND_URL"]
JWT_SECRET = st.secrets["JWT_SECRET"]
JWT_ALGORITHM = "HS256"


def get_jwt():
    payload = {
        "iss": "frontend",
        "exp": int(time.time()) + 60 * 5  # 5 min expiry
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token


def get_polarization_score(topic: str) -> Dict[str, Any]:
    token = get_jwt()
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"topic": topic}

    try:
        response = requests.post(
            f"{BACKEND_URL}/analyze", json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Backend error {response.status_code}"}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
