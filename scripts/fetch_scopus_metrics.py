from pybliometrics.scopus import AuthorRetrieval, ScopusSearch
from pybliometrics.scopus.utils import create_config
import os, json

# Set up config properly on GitHub Action runner
api_key = os.getenv("SCOPUS_API_KEY")
create_config(api_key)

# Your Scopus Author ID
AUTHOR_ID = "57219532607"

# Make _data dir
os.makedirs("_data", exist_ok=True)

# Fetch author metrics
author = AuthorRetrieval(AUTHOR_ID)

metrics = {
    "name": author.indexed_name,
    "affiliation": author.affiliation_current[0].name if author.affiliation_current else "N/A",
    "h_index": author.h_index,
    "citation_count": author.citation_count,
    "document_count": author.document_count,
    "profile_url": f"https://www.scopus.com/authid/detail.uri?authorId={AUTHOR_ID}"
}

with open("_data/scopus.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("✅ Saved Scopus metrics to _data/scopus.json")

# Get top 5 publications
search = ScopusSearch(f"AU-ID({AUTHOR_ID})")
results = search.results

top_pubs = sorted(results, key=lambda x: int(x.get("citedby_count", 0)), reverse=True)[:5]

pubs = []
for pub in top_pubs:
    pubs.append({
        "title": pub.get("title"),
        "journal": pub.get("publicationName"),
        "year": pub.get("coverDate", "")[:4],
        "doi": pub.get("doi"),
        "citations": pub.get("citedby_count", "0")
    })

with open("_data/publications.json", "w") as f:
    json.dump(pubs, f, indent=2)

print("✅ Saved top publications to _data/publications.json")
