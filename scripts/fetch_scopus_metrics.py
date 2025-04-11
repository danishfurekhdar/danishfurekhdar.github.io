import os
import requests
import json

API_KEY = os.getenv("SCOPUS_API_KEY")
if not API_KEY:
    print("❌ Error: SCOPUS_API_KEY environment variable not set")
    exit(1)

AUTHOR_ID = "57219532607"

# Alternative endpoint (try this if the first one fails)
url = f"https://api.elsevier.com/content/author/author_id/{AUTHOR_ID}?apiKey={API_KEY}&httpAccept=application/json"

headers = {
    "Accept": "application/json",
    "X-ELS-APIKey": API_KEY,  # Some APIs require this instead of URL param
}

try:
    response = requests.get(url, headers=headers)
    print("Status Code:", response.status_code)
    
    if response.status_code != 200:
        print("❌ Error: Failed to fetch data from Scopus API")
        print("Raw response:", response.text)
        exit(1)

    data = response.json()
    print("API Response:", json.dumps(data, indent=2))  # Debug: Print full response

    # Extract data (adjust based on actual response structure)
    author_data = data.get("author-retrieval-response", [{}])[0]
    preferred_name = author_data.get("preferred-name", {})
    
    output = {
        "name": f"{preferred_name.get('surname', '')}, {preferred_name.get('given-name', '')}",
        "affiliation": author_data.get("affiliation-current", {}).get("affiliation-name", "N/A"),
        "h_index": author_data.get("h-index", "N/A"),
        "citation_count": author_data.get("citation-count", "N/A"),
        "document_count": author_data.get("document-count", "N/A"),
        "profile_url": f"https://www.scopus.com/authid/detail.uri?authorId={AUTHOR_ID}",
    }

    os.makedirs('_data', exist_ok=True)
    with open('_data/scopus.json', 'w') as f:
        json.dump(output, f, indent=2)

    print("✅ Scopus data saved to _data/scopus.json")

except Exception as e:
    print("❌ Failed to process Scopus response")
    print("Error:", e)
    if 'response' in locals():
        print("Raw response:", response.text)
    exit(1)
