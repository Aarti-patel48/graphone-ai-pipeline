
import requests
import pandas as pd
import os
from datetime import datetime, timezone

print("Fetching AI products from Hugging Face Models API...")

headers = {
    "User-Agent": "GraphOne-Internship/1.0"
}

response = requests.get(
    "https://huggingface.co/api/models?limit=1000",
    headers=headers
)

if response.status_code != 200:
    print("API Error:", response.status_code)
    exit()

models = response.json()

records = []

for model in models:
    records.append({
        "schemaVersion": "1.0",
        "recordType": "PRODUCT",
        "source_name": "Hugging Face Models API",
        "source_url": f"https://huggingface.co/{model['id']}",
        "startupName": model.get("author", "Unknown"),
        "productName": model["id"],
        "pricingModel": "FREE",
        "collectedAt": datetime.now(timezone.utc).isoformat()
    })

os.makedirs("data/processed", exist_ok=True)

df = pd.DataFrame(records)
df.drop_duplicates(subset=["productName"], inplace=True)

df.to_csv("data/processed/products.csv", index=False)

print("Done!", len(df), "real products saved.")