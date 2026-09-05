import asyncio
import aiohttp
import pandas as pd
import os
from datetime import datetime

# Hugging Face public models API
API_URL = "https://huggingface.co/api/models?limit=1000"

async def fetch_models(session):
    """Fetch models from Hugging Face API."""
    try:
        async with session.get(API_URL, timeout=30) as response:
            if response.status == 200:
                return await response.json()
            else:
                print("API Error:", response.status)
                return []
    except Exception as e:
        print("Request Error:", e)
        return []

async def collect_startups():
    startups = []

    async with aiohttp.ClientSession() as session:
        models = await fetch_models(session)

        print(f"Fetched {len(models)} models")

        for item in models:
            model_id = item.get("id", "")

            if "/" in model_id:
              startup = model_id.split("/")[0]
            else:
              startup = model_id

            if startup:
              startups.append({
            "schemaVersion": "1.0",
            "recordType": "STARTUP",
            "source_name": "Hugging Face Models API",
            "source_url": f"https://huggingface.co/{startup}",
            "entityName": startup,
            "employeeCount": None,
            "collectedAt": datetime.utcnow().isoformat()
        })
 

    # DataFrame
    df = pd.DataFrame(startups)

    # Remove duplicate startup names
    df.drop_duplicates(subset=["entityName"], inplace=True)

    # Create folder if it doesn't exist
    os.makedirs("data/processed", exist_ok=True)

    # Save CSV
    output_path = "data/processed/startups.csv"
    df.to_csv(output_path, index=False)

    print(f"Done! {len(df)} unique startups saved.")
    print(f"Saved to: {output_path}")

if __name__ == "__main__":
    asyncio.run(collect_startups())