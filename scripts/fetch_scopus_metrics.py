from pybliometrics.scopus import AuthorRetrieval, ScopusSearch
import os, json

AUTHOR_ID = "57219532607"
API_KEY = os.getenv("SCOPUS_API_KEY")

with open(os.path.expanduser("~/.config/pybliometrics.cfg"), "w") as f:
    f.write(f"""[Authentication]

# 1. Write config file for pybliometrics
config_dir = os.path.expanduser("~/.config")
os.makedirs(config_dir, exist_ok=True)

with open(os.path.join(config_dir, "pybliometrics.cfg"), "w") as f:
    f.write(f"""[Authentication]
APIKey = {API_KEY}
InstToken =

[Directories]
AbstractRetrieval = /tmp/pybliometrics/abstract_retrieval
AffiliationRetrieval = /tmp/pybliometrics/affiliation_retrieval
AuthorRetrieval = /tmp/pybliometrics/author_retrieval
CitationOverview = /tmp/pybliometrics/citation_overview
ScopusSearch = /tmp/pybliometrics/scopus_search
SerialTitle = /tmp/pybliometrics/serial_title
SubjectClassifications = /tmp/pybliometrics/subject_classifications
DownloadFolder = /tmp/pybliometrics/download
""")

# 2. Create _data folder for Jekyll
os.makedirs("_data", exist_ok=True)

# 3. Fetch Scopus author metrics
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

print("✅ Metrics saved to _data/scopus.json")

# 4. Fetch top 5 cited publications
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

print("✅ Top publications saved to _data/publications.json")
