import requests
import pandas as pd
import os
from datetime import datetime
import time

print("Fetching AI organizations from GitHub...")

headers = {
    "User-Agent": "Mozilla/5.0"
}

startups = []

# 10 pages × 100 = up to 1000 organizations
for page in range(1, 11):

    url = f"https://api.github.com/search/users?q=AI&type=org&per_page=100&page={page}"

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Stopped at page", page, "Status:", response.status_code)
        break

    data = response.json()

    items = data.get("items", [])

    print(f"Page {page}: {len(items)} organizations")

    if len(items) == 0:
        break

    for item in items:
        startups.append({
            "schemaVersion": "1.0",
            "recordType": "STARTUP",
            "source_name": "GitHub Organization API",
            "source_url": item["html_url"],
            "entityName": item["login"],
            "employeeCount": None,
            "collectedAt": datetime.utcnow().isoformat()
        })

    time.sleep(1)

df = pd.DataFrame(startups)

df.drop_duplicates(subset=["entityName"], inplace=True)

os.makedirs("data/processed", exist_ok=True)

df.to_csv("data/processed/github_startups.csv", index=False)

print(f"Done! {len(df)} GitHub startups saved.")