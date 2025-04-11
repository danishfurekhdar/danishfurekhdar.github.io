from elsapy.elsclient import ElsClient
from elsapy.elsauthor import ElsAuthor
from elsapy.elssearch import ElsSearch
import os, json

# Get credentials from GitHub secrets
API_KEY = os.getenv("SCOPUS_API_KEY")
INST_TOKEN = os.getenv("SCOPUS_INST_TOKEN", "")  # optional
AUTHOR_ID = "57219532607"

# Initialize Scopus API client
client = ElsClient(API_KEY)
client.inst_token = INST_TOKEN

# Create data folder
os.makedirs("_data", exist_ok=True)

# Initialize and read author data
author = ElsAuthor(author_id=AUTHOR_ID)
if author.read(client):
    print(f"✅ Loaded author: {author.full_name}")
    data = {
        "name": author.full_name,
        "affiliation": author.affiliation,
        "h_index": author.h_index,
        "citation_count": author.citation_count,
        "document_count": author.document_count,
        "profile_url": f"https://www.scopus.com/authid/detail.uri?authorId={AUTHOR_ID}"
    }

    with open("_data/scopus.json", "w") as f:
        json.dump(data, f, indent=2)

    print("✅ Saved metrics to _data/scopus.json")

else:
    print("❌ Failed to fetch author data from Scopus.")
    exit(1)

# Fetch top 5 cited publications
search = ElsSearch(f"AU-ID({AUTHOR_ID})", "scopus")
search.execute(client)

top_pubs = sorted(search.results, key=lambda x: int(x.get("citedby-count", 0)), reverse=True)[:5]

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

print("✅ Saved top publications to _data/publications.json")
