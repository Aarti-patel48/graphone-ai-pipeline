
import requests
import pandas as pd
import os
from datetime import datetime, timezone

# AI companies using Greenhouse
companies = {
    "OpenAI": "openai",
    "Anthropic": "anthropic",
    "Cohere": "cohere",
    "Scale AI": "scaleai",
    "Perplexity": "perplexityai"
}

jobs = []

for company, board in companies.items():
    url = f"https://boards-api.greenhouse.io/v1/boards/{board}/jobs"

    print(f"Fetching jobs from {company}...")

    response = requests.get(url)

    if response.status_code != 200:
        print("Failed:", company)
        continue

    data = response.json()

    for job in data["jobs"]:
        jobs.append({
            "schemaVersion": "1.0",
            "recordType": "JOB",
            "company": company,
            "role": job["title"],
            "date": job.get("updated_at", ""),
            "is_remote": "remote" in job["title"].lower(),
            "role_family": "Engineering",
            "source_url": job["absolute_url"],
            "collectedAt": datetime.now(timezone.utc).isoformat()
        })

os.makedirs("data/processed", exist_ok=True)

df = pd.DataFrame(jobs)
df.to_csv("data/processed/jobs.csv", index=False)

print("\nDone!", len(df), "jobs saved.")