
import pandas as pd
import os

# Canonical mapping database
canonical_map = {
    "Open AI": "OpenAI",
    "OpenAI Inc.": "OpenAI",
    "OpenAI, Inc.": "OpenAI",
    "Anthropic AI": "Anthropic",
    "Google Deep Mind": "Google DeepMind",
    "HuggingFace": "Hugging Face",
    "HF": "Hugging Face",
    "Perplexity AI": "Perplexity",
    "ScaleAI": "Scale AI",
    "x AI": "xAI"
}

df = pd.read_csv("data/processed/startups.csv")

mapping_log = []

for i, row in df.iterrows():
    raw = row["entityName"]
    canonical = canonical_map.get(raw, raw)

    mapping_log.append({
        "raw_name": raw,
        "canonical_name": canonical
    })

    df.at[i, "entityName"] = canonical

os.makedirs("data/processed", exist_ok=True)

df.to_csv("data/processed/startups_resolved.csv", index=False)

pd.DataFrame(mapping_log).to_csv(
    "data/processed/entity_mapping_log.csv",
    index=False
)

print("Done!")
print("Resolved startups:", len(df))
print("Mapping log created:", len(mapping_log))