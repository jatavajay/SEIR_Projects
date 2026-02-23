# Webpage Similarity Checker using SimHash

## Description

This project is a Python program that:

- Extracts title, body text, and links from a given webpage URL
- Counts word frequency of the webpage content
- Generates a 64-bit SimHash fingerprint of the document
- Compares two webpages and calculates their similarity percentage

This helps in detecting how similar two web documents are.

---

## Features

- Extract webpage title
- Extract webpage body text
- Extract all external links
- Count frequency of each word
- Generate polynomial rolling hash
- Generate SimHash fingerprint
- Compare similarity between two documents

---

## Technologies Used

- Python 3
- BeautifulSoup (for HTML parsing)
- urllib.request (for fetching webpage)
- collections.Counter (for word frequency)

---

## Requirements

Install BeautifulSoup before running:

```bash
pip install beautifulsoup4
