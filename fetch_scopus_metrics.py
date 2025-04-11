import requests
import json

API_KEY = "6fc8a5d266579194ab41ae7e4ca81afe"
AUTHOR_ID = "57219532607"

url = f"https://api.elsevier.com/content/author?author_id={AUTHOR_ID}&apiKey={API_KEY}&httpAccept=application/json"

response = requests.get(url)
data = response.json()

entry = data['author-retrieval-response'][0]

output = {
    "name": entry['author-profile']['preferred-name']['indexed-name'],
    "affiliation": entry['author-profile']['affiliation-current']['affiliation-name'],
    "h_index": entry['h-index'],
    "citation_count": entry['coredata']['citation-count'],
    "document_count": entry['coredata']['document-count'],
    "last_updated": entry['coredata'].get('prism:coverDate', 'N/A'),
    "profile_url": f"https://www.scopus.com/authid/detail.uri?authorId={AUTHOR_ID}"
}

with open('_data/scopus.json', 'w') as f:
    json.dump(output, f, indent=2)
