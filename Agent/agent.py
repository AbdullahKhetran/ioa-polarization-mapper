import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_ENDPOINT = os.getenv("API_ENDPOINT")  # fallback default
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o")
MAX_TOKENS = int(os.getenv("MODEL_TOKEN", 500))
TEMPERATURE = float(os.getenv("MODEL_TEMPERATURE", 0.1))

def get_sentiment_and_method(text):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a data analyst AI. "
                    "Given the user text, you must decide **autonomously** which method to use for a polarization graph. "
                    "Available methods: Entropy Score, Balance Metric, Sentiment Variance, Network Modularity, Diversity Index (Gini-Simpson). "
                    "Analyze the sentiment of the text and return the response **strictly in JSON format** with the following keys: "
                    "`method` (the selected method), `sentiment` (positive, negative, neutral), and `score` (sentiment score between -1 and 1). "
                    "Do NOT include explanations, only the JSON."
                )
            },
            {"role": "user", "content": text}
        ],
        "max_tokens": MAX_TOKENS,
        "temperature": TEMPERATURE
    }

    response = requests.post(API_ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()
    result = response.json()

    try:
        content = result['choices'][0]['message']['content']
    except KeyError:
        content = str(result)
    return content

if __name__ == "__main__":
    sample_texts = [
        "Who decides what's 'ethical' in AI, and are we okay with how that process is happening?",
        "What are the ethical questions that proponents of AI often avoid addressing?",
        "Ethical AI—has it effectively become a dead concept in practice?",
        "What would you consider to be ethical uses of AI?",
        "Many hope AI will discover ethical truths. How do humans remain responsible for deciding what is right?",
        "I’m not an AI expert, but I wrote an ethics framework. How would you evaluate its effectiveness?",
        "AI is being used in law, but it produces inaccuracies and ethical violations. How should this be mitigated?",
        "Ethics alone is not a sufficient reason to avoid using AI. How do we balance ethics with practical use?",
        "What are the key ethical considerations and practical challenges for AI startups in ensuring responsible development and deployment?",
        "Can AI truly have ethics without human bias influencing it?",
    ]

    for text in sample_texts:
        try:
            result = get_sentiment_and_method(text)
            print("Text:", text)
            print("AI Output:", result)
            print("="*50)
        except requests.exceptions.RequestException as e:
            print("API call failed:", e)
