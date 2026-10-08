# Web Scraper

A simple Python web scraper that retrieves a webpage using Requests, parses its HTML with BeautifulSoup, and extracts headings from the page.

## Requirements

- Python3
- requests
- beautifulsoup4

## Installation

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the scraper:

```bash
python scraper.py
```

Enter the URL of the webpage when prompted.

The scraper extracts `h1`, `h2`, and `h3` headings and displays them as a numbered list.

## Limitations

- Only headings (`h1`, `h2`, and `h3`) are extracted.
- Some websites may reject automated requests.
- The scraper does not execute JavaScript.
- The scraper handles one webpage at a time.
