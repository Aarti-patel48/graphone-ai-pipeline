
import pandas as pd

# Read research papers
df = pd.read_csv("data/processed/research_papers.csv")

# Add new columns
df["github_url"] = ""
df["github_stars"] = 0
df["github_forks"] = 0

# Sample GitHub mappings (demo for known papers)
github_map = {
    "transformer": (
        "https://github.com/huggingface/transformers",
        180000,
        38000
    ),
    "llama": (
        "https://github.com/meta-llama/llama",
        65000,
        11000
    ),
    "diffusion": (
        "https://github.com/CompVis/stable-diffusion",
        85000,
        14000
    )
}

for i, row in df.iterrows():
    title = str(row["title"]).lower()

    for keyword, info in github_map.items():
        if keyword in title:
            df.at[i, "github_url"] = info[0]
            df.at[i, "github_stars"] = info[1]
            df.at[i, "github_forks"] = info[2]

df.to_csv("data/processed/research_papers_with_github.csv", index=False)

print("Done!")
print("Rows:", len(df))