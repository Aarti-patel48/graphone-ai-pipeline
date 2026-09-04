
import requests
import feedparser
import pandas as pd

BASE_URL = "http://export.arxiv.org/api/query"

def fetch_arxiv_papers(start=0):
    response = requests.get(
        BASE_URL,
        params={
            "search_query": "cat:cs.AI",
            "start": start,
            "max_results": 100
        }
    )

    feed = feedparser.parse(response.text)
    papers = []

    for entry in feed.entries:
        papers.append({
            "title": entry.title,
            "authors": ", ".join(a.name for a in entry.authors),
            "published_date": entry.published,
            "paper_url": entry.link
        })

    return papers


print("Fetching papers...")

all_papers = []

for start in range(0, 1000, 100):
    print("Batch:", start)
    all_papers.extend(fetch_arxiv_papers(start))

df = pd.DataFrame(all_papers)
df.to_csv("data/processed/research_papers.csv", index=False)

print("Done!", len(df), "papers saved.")