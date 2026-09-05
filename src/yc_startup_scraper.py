import requests
import pandas as pd
import os
from datetime import datetime

print("Fetching YC startups...")

API_URL = "https://www.ycombinator.com/api/companies"

headers = {
    "User-Agent": "Mozilla/5.0"
}

startups = []

page = 1

while True:
    response = requests.get(
        API_URL,
        params={"page": page},
        headers=headers,
        timeout=30
    )

    if response.status_code != 200:
        print("Stopped at page", page)
        break

    data = response.json()

    if not data:
        break

    for item in data:
        startups.append({
            "schemaVersion": "1.0",
            "recordType": "STARTUP",
            "source_name": "Y Combinator API",
            "source_url": f"https://www.ycombinator.com/companies/{item['slug']}",
            "entityName": item["name"],
            "employeeCount": item.get("team_size"),
            "collectedAt": datetime.utcnow().isoformat()
        })

    print(f"Page {page}: {len(data)} companies")
    page += 1

df = pd.DataFrame(startups)
df.drop_duplicates(subset=["entityName"], inplace=True)

os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/yc_startups.csv", index=False)

print(f"Done! {len(df)} YC startups saved.")