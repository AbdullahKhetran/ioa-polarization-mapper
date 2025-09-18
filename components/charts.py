import plotly.express as px  # type: ignore


def cluster_pie_chart(clusters: list):
    cluster_labels = [c["label"] for c in clusters]
    cluster_shares = [c["share"] for c in clusters]

    fig = px.pie(
        values=cluster_shares,
        names=cluster_labels,
        title="Cluster Distribution",
        color=cluster_labels,
        # color_discrete_sequence=colors
        color_discrete_sequence=["#065929", "#e74c3c", "#056db2"]
    )
    return fig
