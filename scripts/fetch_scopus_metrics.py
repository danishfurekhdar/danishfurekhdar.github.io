import os
import requests
import json

API_KEY = os.getenv("SCOPUS_API_KEY")
if not API_KEY:
    print("Error: SCOPUS_API_KEY environment variable not set")
    exit(1)

AUTHOR_ID = "57219532607"

url = f"https://api.elsevier.com/content/search/author?query=AU-ID({AUTHOR_ID})&apiKey={API_KEY}&httpAccept=application/json"
response = requests.get(url)

print("Status Code:", response.status_code)
if response.status_code != 200:
    print("Error: Failed to fetch data from Scopus API")
    print("Raw response:", response.text)
    exit(1)

try:
    data = response.json()
    if not data.get('search-results', {}).get('entry'):
        print("Error: No author data found in response")
        exit(1)
        
    entry = data['search-results']['entry'][0]
    
    output = {
        "name": entry.get('preferred-name', {}).get('surname', '') + 
               ", " + entry.get('preferred-name', {}).get('given-name', ''),
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
    print("❌ Failed to process Scopus response")
    print("Error:", e)
    print("Raw response:", response.text)
    exit(1)
