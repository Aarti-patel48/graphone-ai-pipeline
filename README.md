# GraphOne AI Intelligence Pipeline

A Python-based AI Intelligence Pipeline that collects AI startups, AI products, research papers, AI jobs, and AI news from public sources, processes them using LLMs, and exports structured datasets.

## Project Overview

GraphOne automates AI ecosystem data collection and processing. It combines asynchronous scraping, retry handling, payload chunking, entity mapping, and LLM orchestration into one pipeline.

## Features

* Async scraping using `asyncio` and `aiohttp`
* Retry Logic for HTTP 429 errors
* Payload Chunking for HTTP 413 errors
* LLM Fallback using Gemini Flash
* Entity Mapping and data cleaning
* CSV export for all processed datasets
* Google Sheets integration

## Tech Stack

* Python
* Pandas
* Requests
* aiohttp
* BeautifulSoup
* Google Gemini API
* Git & GitHub

## Project Structure

graphone-ai-pipeline/
├── README.md
├── architecture.pdf
├── requirements.txt
├── src/
│ ├── async_startup_scraper.py
│ ├── arxiv_scraper.py
│ ├── product_scraper.py
│ ├── jobs_scraper.py
│ ├── news_scraper.py
│ ├── jobs_scraper.py
│ ├── llm_orchestrator.py
│ ├── retry_utils.py
│ └── chunking.py
└── data/
└── processed/

## Generated Datasets

| Dataset            | Records   |
| ------------------ | --------- |
| AI Startups        | 1432      |
| AI Products        | 1000+     |
| Research Papers    | 1000      |
| AI Jobs            | 797       |
| AI News            | 40        |
| Entity Mapping Log | Generated |

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run ArXiv scraper:

```bash
python src/arxiv_scraper.py
```

Run LLM pipeline:

```bash
python src/llm_orchestrator.py
```

## Output

All processed files are saved inside:

```text
data/processed/
```

Files include:

* startups.csv
* products.csv
* research_papers.csv
* jobs.csv
* news.csv
* entity_mapping_log.csv

## Project Highlights

* Automated AI ecosystem data collection.
* Structured CSV dataset generation.
* Google Sheets integration.
* Reliable API handling using retry logic and chunking.
* Production-style AI data pipeline built using Python.

## Author

**Aarti Patel**

B.Tech Computer Science Engineering

Shri Dadaji Institute of Technology and Science, Khandwa
