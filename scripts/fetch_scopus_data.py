from elsapy.elsclient import ElsClient
from elsapy.elsprofile import ElsAuthor
from elsapy.elssearch import ElsSearch
import json
import os

API_KEY = os.getenv("SCOPUS_API_KEY")
INST_TOKEN = os.getenv("SCOPUS_INST_TOKEN")  # Optional

# Initialize client
client = ElsClient(API_KEY)
if INST_TOKEN:
    client.inst_token = INST_TOKEN

# Scopus Author URI (use your own ID here)
AUTHOR_ID = "57219532607"
author_uri = f"https://api.elsevier.com/content/author/author_id/{AUTHOR_ID}"
author = ElsAuthor(uri=author_uri)

os.makedirs("_data", exist_ok=True)

if author.read(client):
    print("✅ Author data loaded:", author.full_name)

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
    print("✅ Scopus metrics saved to _data/scopus.json")

else:
    print("❌ Failed to read author data")
    exit(1)

# Top 5 cited publications
print("🔎 Fetching publications...")
search = ElsSearch(f"AU-ID({AUTHOR_ID})", "scopus")
search.execute(client)

top_pubs = sorted(search.results, key=lambda x: int(x.get("citedby-count", 0)), reverse=True)[:5]

pubs = []
for pub in top_pubs:
    pubs.append({
        "title":
