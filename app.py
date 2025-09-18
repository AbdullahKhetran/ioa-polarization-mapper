import streamlit as st
import plotly.express as px

# ---------------------------
# Mock Data (replace with backend API later)
# ---------------------------
mock_response = {
    "topic": "Climate Change",
    "polarization_score": 0.72,
    "clusters": [
        {
            "label": "Pro Climate Action",
            "share": 55,
            "examples": [
                "We need urgent policies to stop global warming!",
                "Renewable energy is the only way forward."
            ]
        },
        {
            "label": "Skeptical/Against Action",
            "share": 30,
            "examples": [
                "Climate change is exaggerated by the media.",
                "Why waste money on this when economies are struggling?"
            ]
        },
        {
            "label": "Neutral/Unclear",
            "share": 15,
            "examples": [
                "Not sure if climate change is man-made or natural.",
                "I don’t know enough about the science."
            ]
        }
    ],
    "summary": "Most posts lean towards supporting climate action, but there is a strong skeptical minority, indicating significant polarization."
}

# ---------------------------
# Streamlit UI
# ---------------------------

st.set_page_config(page_title="Polarization Mapper", layout="wide")

# Title & Description
st.title("🧭 Polarization Mapper")
st.markdown("Analyze how polarized online discussions are around any topic.")

# Sidebar - Input
st.sidebar.header("Input")
topic = st.sidebar.text_input("Enter a topic", value="Climate Change")
analyze_btn = st.sidebar.button("Analyze")

# Use mock response until backend is ready
response = mock_response

# ---------------------------
# Results Section
# ---------------------------
if response:
    st.subheader(f"Results for: **{response['topic']}**")

    # Polarization Score (row 1)
    score = float(response["polarization_score"])
    st.metric(label="Polarization Score", value=f"{score*100:.1f}%")
    st.progress(score)

    # Cluster Chart
    cluster_labels = [c["label"] for c in response["clusters"]]
    cluster_shares = [c["share"] for c in response["clusters"]]

    # explicit hex mapping for the normalized keys
    color_map = {
        "green": "#065929",      # green
        "red": "#e74c3c",  # red
        "blue": "#056db2"   # blue
    }

    colors = list(color_map.values())[:len(cluster_labels)]

    fig = px.pie(
        values=cluster_shares,
        names=cluster_labels,
        title="Cluster Distribution",
        color=cluster_labels,               # just use labels directly
        color_discrete_sequence=colors      # assign colors in order
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # Cluster Breakdown
    st.subheader("Cluster Breakdown")
    for cluster in response["clusters"]:
        with st.expander(f"{cluster['label']} examples ({cluster['share']}%)"):
            for ex in cluster['examples']:
                st.markdown(f"> {ex}")

    st.divider()

    # Insights Section
    st.subheader("Insights")
    st.info(response["summary"])

# Footer
st.markdown("---")
st.caption("Built at [Internet of Agents Hackathon](https://lablab.ai/event/internet-of-agents-hackathon) with [Coral Protocol](https://coralprotocol.org)")
