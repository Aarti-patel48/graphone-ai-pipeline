
import feedparser
import pandas as pd
import os
from datetime import datetime

# 5 working AI RSS feeds
feeds = {
    "Hugging Face": "https://huggingface.co/blog/feed.xml",
    "Google AI": "https://blog.google/technology/ai/rss/",
    "VentureBeat AI": "https://venturebeat.com/ai/feed/",
    "MIT AI News": "https://news.mit.edu/rss/topic/artificial-intelligence2",
    "NVIDIA Blog": "https://blogs.nvidia.com/feed/"
}

news = []

for source, url in feeds.items():
    print("Reading:", source)
    feed = feedparser.parse(url)

    print("Articles found:", len(feed.entries))

    for entry in feed.entries[:10]:
        news.append({
            "schemaVersion": "1.0",
            "recordType": "NEWS",
            "source": source,
            "title": entry.title,
            "url": entry.link,
            "published_date": entry.get("published", ""),
            "collectedAt": datetime.utcnow().isoformat()
        })

os.makedirs("data/processed", exist_ok=True)

df = pd.DataFrame(news)
df.to_csv("data/processed/news.csv", index=False)

print("\nDone!", len(df), "news articles saved.")