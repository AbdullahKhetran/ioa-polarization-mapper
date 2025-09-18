import streamlit as st
from components.results import show_results
from services.api import analyze_topic

# st.title("Polarization Mapper")

# # --- Input Area ---
# topic = st.text_input("Enter a topic to analyze", "Climate Change")

# if st.button("Analyze"):
#     with st.spinner("Analyzing polarization..."):
#         time.sleep(2)  # simulate delay
#         response = analyze_topic(topic)
#         show_results(response)
# else:
#     st.info("👆 Enter a topic and click *Analyze* to see results.")

# # --- Footer ---
# st.caption("Built at [Internet of Agents Hackathon](https://lablab.ai/event/internet-of-agents-hackathon) with [Coral Protocol](https://coralprotocol.org)")


st.set_page_config(page_title="Polarization Mapper", layout="wide")
st.title("Polarization Mapper")

# Predefined topics
topics = ["Climate Change", "AI Regulation", "Universal Basic Income"]

# Dropdown to choose
selected_topic = st.selectbox("Choose a topic:", topics)

# Get data
response = analyze_topic(selected_topic)

if response:
    show_results(response)


# --- Footer ---
st.caption(
    "Built at [Internet of Agents Hackathon](https://lablab.ai/event/internet-of-agents) by [Super Agents](https://lablab.ai/event/internet-of-agents/super-agents)")
