
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

doc = SimpleDocTemplate("architecture.pdf")
styles = getSampleStyleSheet()
story = []

story.append(Paragraph("<b>GraphOne AI Intelligence Pipeline Architecture</b>", styles["Title"]))

story.append(Paragraph("<b>Page 1 — System Overview</b>", styles["Heading2"]))
story.append(Paragraph(
    "Data Sources: arXiv, Greenhouse API, RSS Feeds, AI Company Websites.",
    styles["BodyText"]
))
story.append(Paragraph(
    "Scraper Layer: Python requests, aiohttp, feedparser, BeautifulSoup.",
    styles["BodyText"]
))
story.append(Paragraph(
    "LLM Layer: Gemini Flash → Groq Llama 3 → DeepSeek fallback chain.",
    styles["BodyText"]
))
story.append(Paragraph(
    "Entity Resolution Layer: Canonical mapping and deduplication.",
    styles["BodyText"]
))
story.append(Paragraph(
    "Output Layer: CSV files, PostgreSQL, Neo4j, Google Sheets.",
    styles["BodyText"]
))

story.append(Paragraph("<br/><b>Page 2 — Scalability Strategy</b>", styles["Heading2"]))
story.append(Paragraph(
    "The crawler is horizontally scalable using asynchronous workers.",
    styles["BodyText"]
))
story.append(Paragraph(
    "Massive crawling uses pagination and concurrent workers.",
    styles["BodyText"]
))
story.append(Paragraph(
    "<b>429 Handling:</b> Exponential Backoff (2s, 4s, 8s, 16s).",
    styles["BodyText"]
))
story.append(Paragraph(
    "<b>413 Handling:</b> HTML is chunked into semantic blocks before LLM extraction.",
    styles["BodyText"]
))

story.append(Paragraph("<br/><b>Page 3 — Freshness & Storage</b>", styles["Heading2"]))
story.append(Paragraph(
    "Freshness Tracking uses source URL + publication timestamp to avoid duplicates.",
    styles["BodyText"]
))
story.append(Paragraph(
    "Entity Resolution converts inconsistent startup names into canonical entities.",
    styles["BodyText"]
))
story.append(Paragraph(
    "PostgreSQL stores structured entities, Neo4j stores relationships, and vector storage enables semantic retrieval.",
    styles["BodyText"]
))

doc.build(story)

print("architecture.pdf created successfully!")