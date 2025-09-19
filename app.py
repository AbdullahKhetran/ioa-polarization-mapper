import streamlit as st
from typing import Dict, Any
from components.results import show_results
from services.api import get_polarization_score

st.set_page_config(page_title="Polarization Mapper")
st.title("Polarization Mapper")

# Predefined topics
topics = ["Climate Change", "AI Regulation", "Universal Basic Income"]

# Dropdown to choose
selected_topic: str = st.selectbox("Choose a topic:", topics)

# Get data
response: Dict[str, Any] = get_polarization_score(selected_topic)

if response:
    show_results(response)

# --- Footer ---
st.caption(
    "Built at [Internet of Agents Hackathon](https://lablab.ai/event/internet-of-agents) by [Super Agents](https://lablab.ai/event/internet-of-agents/super-agents)"
)
