import streamlit as st
from typing import Dict, Any
from services.api import get_polarization_score, get_example_posts
# from dotenv import load_dotenv  # for localhost
# import os  # for localhost


# # for localhost
# load_dotenv()
# BACKEND_URL = os.getenv("BACKEND_URL")

BACKEND_URL = st.secrets["BACKEND_URL"]

st.set_page_config(page_title="Polarization Mapper")
st.title("Polarization Mapper")

# --- User input ---
st.subheader("Enter a topic to analyze")
topic = st.text_input("Topic:")

# Suggested popular topics (just text, not clickable)
st.caption(
    "💡 Try one of these: *AI Ethics, Climate Change, Universal Basic Income*")


# Button to trigger analysis
if st.button("Analyze"):
    if not topic.strip():
        st.error("Please enter a topic before analyzing.")

    else:

        response = get_polarization_score(topic)

        if response and "error" not in response:
            # Restructure backend data
            selected_method = response.get("selected_method", "unknown")
            reason = response.get("reason", "")
            polarization_score = response.get("polarization_score", 0.0)

            # Display results in frontend
            st.subheader(f"Results for: {topic}")
            st.metric(label="Polarization Score",
                      value=f"{polarization_score*100:.1f}%")
            st.info(f"Selected Method: **{selected_method}**")
            st.caption(f"Reason: {reason}")

            # --- Example posts ---
            st.subheader("Example Posts")
            example_ids = response.get("example_post_ids", [])

            if example_ids:
                posts = get_example_posts(example_ids, topic)
                if posts:
                    for post in posts:
                        text = post.get("text") or post.get(
                            "title") or "[No text]"
                        url = post.get("url", "#")
                        st.markdown(f"{text[:100]}... [view post]({url})")
                else:
                    st.write("No posts found for the returned IDs.")
            else:
                st.write("No example posts returned by AI.")

        elif response and "error" in response:
            st.error(f"Error: {response['error']}")


# --- Footer ---
st.caption(
    "Built at [Internet of Agents Hackathon](https://lablab.ai/event/internet-of-agents) by [Super Agents](https://lablab.ai/event/internet-of-agents/super-agents)"
)
