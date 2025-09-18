def analyze_topic(topic: str) -> dict:
    dummy_data = {
        "Climate Change": {
            "topic": "Climate Change",
            "polarization_score": 0.65,
            "clusters": [
                {"label": "Pro", "share": 50,
                    "examples": ["We must act now."]},
                {"label": "Against", "share": 30,
                    "examples": ["This is exaggerated."]},
                {"label": "Neutral", "share": 20,
                    "examples": ["Uncertain evidence."]}
            ],
            "summary": "Climate change debates are polarized..."
        },
        "AI Regulation": {
            "topic": "AI Regulation",
            "polarization_score": 0.55,
            "clusters": [
                {"label": "Pro", "share": 40,
                    "examples": ["We need guardrails."]},
                {"label": "Against", "share": 40, "examples": [
                    "Overregulation stifles progress."]},
                {"label": "Neutral", "share": 20,
                    "examples": ["Balance is required."]}
            ],
            "summary": "AI regulation discussions center around..."
        },
        "Universal Basic Income": {
            "topic": "Universal Basic Income",
            "polarization_score": 0.70,
            "clusters": [
                {"label": "Pro", "share": 60,
                    "examples": ["It reduces poverty."]},
                {"label": "Against", "share": 25,
                    "examples": ["Too expensive."]},
                {"label": "Neutral", "share": 15,
                    "examples": ["Still experimental."]}
            ],
            "summary": "UBI generates strong support but also strong opposition..."
        }
    }
    return dummy_data.get(topic, {"topic": topic, "polarization_score": 0, "clusters": [], "summary": "No data"})
