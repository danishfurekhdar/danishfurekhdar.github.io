from pybliometrics.scopus import AuthorRetrieval, ScopusSearch
import os, json

# Your Scopus Author ID
AUTHOR_ID = "57219532607"
API_KEY = os.getenv("SCOPUS_API_KEY")

# Manually create the config.ini file
home_dir = os.path.expanduser("~")
config_dir = os.path.join(home_dir, ".pybliometrics")
os.makedirs(config_dir, exist_ok=True)

config_path = os.path.join(config_dir, "config.ini")
with open(config_path, "w") as f:
    f.write(f"""[Authentication]
APIKey = {API_KEY}
InstToken =

[Directories]
AbstractRetrieval = {config_dir}/abstract_retrieval
AffiliationRetrieval = {config_dir}/affiliation_retrieval
AuthorRetrieval = {config_dir}/author_retrieval
CitationOverview = {config_dir}/citation_overview
ScopusSearch = {config_dir}/scopus_search
SerialTitle = {config_dir}/serial_title
SubjectClassifications = {config_dir}/subject_classifications
DownloadFolder = {config_dir}/download
""")

# Create _data folder
os.makedirs("_data", exist_ok=True)

# Fetch author info
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

print("✅ Top publications saved to _data/publications.json")
