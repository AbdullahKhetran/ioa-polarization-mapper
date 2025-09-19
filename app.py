import streamlit as st
from typing import Dict, Any
from components.results import show_results
from services.api import get_polarization_score

st.set_page_config(page_title="Polarization Mapper")
st.title("Polarization Mapper")

# Predefined topics
topics: list[str] = ["Climate Change",
                     "AI Regulation", "Universal Basic Income"]

# Dropdown to choose
selected_topic: str = st.selectbox("Choose a topic:", topics)


# Button to trigger analysis
if st.button("Analyze"):
    response = get_polarization_score(selected_topic)

    if response and "error" not in response:
        # Restructure backend data
        selected_method = response.get("selected_method", "unknown")
        reason = response.get("reason", "")
        polarization_score = response.get("polarization_score", 0.0)

        # Display results in frontend
        st.subheader(f"Results for: {selected_topic}")
        st.metric(label="Polarization Score",
                  value=f"{polarization_score*100:.1f}%")
        st.info(f"Selected Method: **{selected_method}**")
        st.caption(f"Reason: {reason}")

        # Optional: display clusters if your backend sends them
        if "clusters" in response:
            show_results(response)

    elif response and "error" in response:
        st.error(f"Error: {response['error']}")


# --- Footer ---
st.caption(
    "Built at [Internet of Agents Hackathon](https://lablab.ai/event/internet-of-agents) by [Super Agents](https://lablab.ai/event/internet-of-agents/super-agents)"
)
