import os
import requests
import json

API_KEY = os.getenv("SCOPUS_API_KEY")
AUTHOR_ID = "57219532607"

url = f"https://api.elsevier.com/content/search/author?query=AU-ID({AUTHOR_ID})&apiKey={API_KEY}&httpAccept=application/json"
response = requests.get(url)

print("Status Code:", response.status_code)
print("Raw response:")
print(response.text)  # Print raw in case something still goes wrong

try:
    data = response.json()
    entry = data['search-results']['entry'][0]

    output = {
        "name": entry['preferred-name']['surname'] + ", " + entry['preferred-name'].get('given-name', ''),
        "affiliation": entry.get('affiliation-current', {}).get('affiliation-name', 'N/A'),
        "h_index": entry.get('h-index', 'N/A'),
        "citation_count": entry.get('citation-count', 'N/A'),
        "document_count": entry.get('document-count', 'N/A'),
        "last_updated": entry.get('prism:coverDate', 'N/A'),
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
