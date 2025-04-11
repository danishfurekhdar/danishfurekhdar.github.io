import os
import requests
import json

API_KEY = os.getenv("SCOPUS_API_KEY")
AUTHOR_ID = "57219532607"

url = f"https://api.elsevier.com/content/author?author_id={AUTHOR_ID}&apiKey={API_KEY}&httpAccept=application/json"
response = requests.get(url)

print("Status Code:", response.status_code)
print("Raw response:")
print(response.text)  # 👈 shows you the real issue if it's an error message

try:
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

    os.makedirs('_data', exist_ok=True)
    with open('_data/scopus.json', 'w') as f:
        json.dump(output, f, indent=2)

    print("✅ Scopus data saved to _data/scopus.json")

except Exception as e:
    print("❌ Failed to parse Scopus response")
    print(e)
    exit(1)
