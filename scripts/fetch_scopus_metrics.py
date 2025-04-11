from pybliometrics.scopus import AuthorRetrieval, ScopusSearch
from pybliometrics.scopus.utils import config
import os, json

# === CONFIG ===
AUTHOR_ID = "57219532607"
API_KEY = os.getenv("SCOPUS_API_KEY")

# Directly configure Pybliometrics
config['Authentication']['APIKey'] = API_KEY
config['Directories']['AbstractRetrieval'] = '/tmp/pybliometrics/abstract_retrieval'
# Add other directories as needed

# === Fetch metrics ===
try:
    author = AuthorRetrieval(AUTHOR_ID)
    
    metrics = {
        "name": author.indexed_name,
        "affiliation": author.affiliation_current[0].name if author.affiliation_current else "N/A",
        "h_index": author.h_index,
        "citation_count": author.citation_count,
        "document_count": author.document_count,
        "profile_url": f"https://www.scopus.com/authid/detail.uri?authorId={AUTHOR_ID}"
    }

    os.makedirs("_data", exist_ok=True)
    with open("_data/scopus.json", "w") as f:
        json.dump(metrics, f, indent=2)

    print("✅ Scopus metrics saved")

    # === Top publications ===
    search = ScopusSearch(f"AU-ID({AUTHOR_ID})")
    top_pubs = sorted(search.results, 
                     key=lambda x: int(x.get("citedby_count", 0)), 
                     reverse=True)[:5]

    pubs = [{
        "title": pub.get("title"),
        "journal": pub.get("publicationName"),
        "year": pub.get("coverDate", "")[:4],
        "doi": pub.get("doi", ""),
        "citations": pub.get("citedby_count", "0")
    } for pub in top_pubs]

    with open("_data/publications.json", "w") as f:
        json.dump(pubs, f, indent=2)

    print("✅ Top publications saved")

except Exception as e:
    print(f"❌ Error: {str(e)}")
    raise  # This will make the workflow fail visibly
