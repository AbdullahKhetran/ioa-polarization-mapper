import streamlit as st
import plotly.express as px  # type: ignore
from components.charts import cluster_pie_chart


def show_results(response: dict):
    if not response:
        return

    st.subheader(f"Results for: **{response['topic']}**")

    # Polarization Score
    score = float(response["polarization_score"])
    st.metric(label="Polarization Score", value=f"{score*100:.1f}%")
    st.progress(score)

    # Cluster Chart
    st.plotly_chart(
        cluster_pie_chart(response["clusters"]),
        use_container_width=True
    )

    st.divider()

    st.subheader("Cluster Breakdown")
    for cluster in response["clusters"]:
        with st.expander(f"{cluster['label']} examples ({cluster['share']}%)"):
            for i, ex in enumerate(cluster['examples']):
                # Take first 7 words as preview
                preview = " ".join(ex.split()[:7])
                if len(ex.split()) > 7:
                    preview += "..."

                # Dummy link (could be replaced with actual URL later)
                post_url = f"https://example.com/post/{i}"

                st.markdown(
                    f"- {preview} [View post]({post_url})"
                )

    st.divider()

    # Insights Section
    st.subheader("Insights")
    st.info(response["summary"])
