import pandas as pd
import os

# Project root automatically detect karega
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "processed")

hf_path = os.path.join(DATA_DIR, "startups.csv")
gh_path = os.path.join(DATA_DIR, "github_startups.csv")

print("Reading:", hf_path)
print("Reading:", gh_path)

# Read CSV files
hf = pd.read_csv(hf_path)
gh = pd.read_csv(gh_path)

# Merge
merged = pd.concat([hf, gh], ignore_index=True)

# Remove duplicates
merged.drop_duplicates(subset=["entityName"], inplace=True)

# Save merged file
output_path = os.path.join(DATA_DIR, "startups.csv")
merged.to_csv(output_path, index=False)

print(f"🎉 Final startups saved: {len(merged)}")
print("Saved to:", output_path)