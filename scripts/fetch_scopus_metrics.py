from pybliometrics.scopus import AuthorRetrieval, ScopusSearch
import os, json

# Scopus Author ID
AUTHOR_ID = "57219532607"

# Setup config for pybliometrics
os.makedirs(os.path.expanduser("~/.pybliometrics"), exist_ok=True)
with open(os.path.expanduser("~/.pybliometrics/config.ini"), "w") as f:
    f.write(f"""
[Authentication]
APIKey = {os.getenv("SCOPUS_API_KEY")}
InstToken =

[Directories]
AbstractRetrieval = ./pybliometrics/abstract_retrieval
AffiliationRetrieval = ./pybliometrics/affiliation_retrieval
AuthorRetrieval = ./pybliometrics/author_retrieval
CitationOverview = ./pybliometrics/citation_overview
ScopusSearch = ./pybliometrics/scopus_search
SerialTitle = ./pybliometrics/serial_title
SubjectClassifications = ./pybliometrics/subject_classifications
DownloadFolder = ./pybliometrics/download
""")

# Create _data dir
os.makedirs("_data", exist_ok=True)

# Fetch author info
author = AuthorRetrieval(AUTHOR_ID)

data = {
    "name": author.indexed_name,
    "affiliation": author.affiliation_current[0].name if author.affiliation_current else "N/A",
    "h_index": author.h_index,
    "citation_count": author.citation_count,
    "document_count": author.document_count,
    "profile_url": f"https://www.scopus.com/authid/detail.uri?authorId={AUTHOR_ID}"
}

with open("_data/scopus.json", "w") as f:
    json.dump(data, f, indent=2)

print("✅ Scopus metrics saved to _data/scopus.json")

# Fetch top 5 publications
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

print("✅ Publications saved to _data/publications.json")
