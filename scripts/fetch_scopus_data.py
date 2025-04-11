from elsapy.elsclient import ElsClient
from elsapy.elsauthor import ElsAuthor
from elsapy.elssearch import ElsSearch
import os, json

# Get API key from environment (set in GitHub Secrets)
API_KEY = os.getenv("SCOPUS_API_KEY")
if not API_KEY:
    print("❌ Missing SCOPUS_API_KEY environment variable")
    exit(1)

client = ElsClient(API_KEY)

AUTHOR_ID = "57219532607"
author = ElsAuthor(AUTHOR_ID)

# Create _data directory
os.makedirs("_data", exist_ok=True)

# Fetch author metrics
if author.read(client):
    metrics = {
        "name": author.full_name,
        "affiliation": author.affiliation,
        "h_index": author.h_index,
        "citation_count": author.citation_count,
        "document_count": author.document_count,
        "profile_url": f"https://www.scopus.com/authid/detail.uri?authorId={AUTHOR_ID}"
    }

    with open("_data/scopus.json", "w") as f:
        json.dump(metrics, f, indent=2)
    print("✅ Metrics saved to _data/scopus.json")
else:
    print("❌ Failed to fetch author data")

# Fetch top 5 publications
search = ElsSearch(f"AU-ID({AUTHOR_ID})", "scopus")
search.execute(client)
results = search.results

top_pubs = sorted(results, key=lambda x: int(x.get("citedby-count", 0)), reverse=True)[:5]
pubs = []

for pub in top_pubs:
    pubs.append({
        "title": pub.get("dc:title"),
        "journal": pub.get("prism:publicationName"),
        "year": pub.get("prism:coverDate", "")[:4],
        "doi": pub.get("prism:doi", ""),
        "citations": pub.get("citedby-count", "0")
    })

with open("_data/publications.json", "w") as f:
    json.dump(pubs, f, indent=2)

print("✅ Top publications saved to _data/publications.json")
