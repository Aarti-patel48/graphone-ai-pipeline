
import requests
import pandas as pd
import os
from datetime import datetime, timezone

orgs = [
    "openai","huggingface","mistralai","cohere-ai","stability-ai",
    "runwayml","perplexity-ai","scaleapi","elevenlabs","deepmind",
    "togethercomputer","replit","wandb","langchain-ai","ollama",
    "modal-labs","pinecone-io","groq","crewAIInc","continue-revolution"
]

records = []

headers = {"User-Agent": "GraphOne-Internship"}

print("Fetching startup data from GitHub Organizations API...")

for org in orgs:
    url = f"https://api.github.com/users/{org}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Skipped:", org)
        continue

    data = response.json()

    records.append({
        "schemaVersion": "1.0",
        "recordType": "STARTUP",
        "source_name": "GitHub Organization API",
        "source_url": data["html_url"],
        "entityName": data["login"],
        "employeeCount": None,
        "collectedAt": datetime.now(timezone.utc).isoformat()
    })

os.makedirs("data/processed", exist_ok=True)

df = pd.DataFrame(records)
df.to_csv("data/processed/startups.csv", index=False)

print("Done!", len(df), "real startups saved.")