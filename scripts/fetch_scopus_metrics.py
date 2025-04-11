from scholarly import scholarly
import json
import os
import time

def get_author_data(author_id):
    try:
        # Search for the author with all available sections
        author = scholarly.search_author_id(author_id)
        author_filled = scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
        
        # Debug: Print full response to check available data
        print("Full author data:", json.dumps(author_filled, indent=2)[:500] + "...")  # Print first 500 chars
        
        # Extract metrics - now checking multiple possible locations
        h_index = (
            author_filled.get("hindex") or                  # Try direct field
            author_filled.get("indices", {}).get("hindex")  # Try indices section
        )
        
        i10_index = (
            author_filled.get("i10index") or                # Try direct field
            author_filled.get("indices", {}).get("i10index") # Try indices section
        )
        
        profile = {
            "name": author_filled.get("name", "N/A"),
            "affiliation": author_filled.get("affiliation", "N/A"),
            "h_index": h_index if h_index is not None else 0,
            "citations": author_filled.get("citedby", 0),
            "i10_index": i10_index if i10_index is not None else 0,
            "scholar_id": author_id,
            "url": f"https://scholar.google.com/citations?user={author_id}"
        }
        
        return profile, author_filled.get("publications", [])
    except Exception as e:
        print(f"Error fetching author data: {str(e)}")
        return None, []


def get_publication_data(publications, max_publications=5):
    pub_data = []
    for pub in sorted(publications, key=lambda p: p.get("num_citations", 0), reverse=True)[:max_publications]:
        try:
            # Add delay to avoid rate limiting
            time.sleep(1)
            
            filled_pub = scholarly.fill(pub)
            pub_data.append({
                "title": filled_pub["bib"].get("title", "N/A"),
                "year": filled_pub["bib"].get("pub_year", "N/A"),
                "citations": filled_pub.get("num_citations", 0),
                "venue": filled_pub["bib"].get("venue", "N/A"),
                "url": filled_pub.get("pub_url", "")
            })
        except Exception as e:
            print(f"Error processing publication: {e}")
            continue
            
    return pub_data

def save_to_json(data, filename):
    os.makedirs("_data", exist_ok=True)
    with open(f"_data/{filename}", "w") as f:
        json.dump(data, f, indent=2)

def main():
    author_id = "qOhxqbkAAAAJ"
    
    # Get author data
    profile, publications = get_author_data(author_id)
    if not profile:
        print("Failed to fetch author profile")
        return
    
    # Get publication data
    pub_data = get_publication_data(publications)
    
    # Save data
    save_to_json(profile, "scholar.json")
    save_to_json(pub_data, "scholar_publications.json")
    
    print("✅ Google Scholar data saved successfully.")
    print(f"• Profile: {profile['name']}")
    print(f"• Publications processed: {len(pub_data)}")

if __name__ == "__main__":
    main()
