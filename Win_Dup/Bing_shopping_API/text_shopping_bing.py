import json
import requests
import os
def search_product_with_text(query):
    """Search for products using Bing Entity Search API based on text."""

    # Bing Entity Search endpoint
    ENTITY_SEARCH_ENDPOINT = 'https://api.bing.microsoft.com/v7.0/entities'
    BING_SEARCH_API_KEY = os.getenv('BING_IMAGE_SEARCH_KEY')
    if BING_SEARCH_API_KEY:
        print("API Key found:", BING_SEARCH_API_KEY)
    else:
        print("API Key not found! Please check if it's set correctly.")
    headers = {
        'Ocp-Apim-Subscription-Key': BING_SEARCH_API_KEY
    }

    params = {
        'q': query,
        'mkt': 'en-US'
    }

    response = requests.get(ENTITY_SEARCH_ENDPOINT, headers=headers, params=params)

    if response.status_code == 200:
        results = response.json()
        return results
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None


# Example usage
query = ' jacket'
product_results = search_product_with_text(query)

if product_results:
    print(json.dumps(product_results, indent=2))
else:
    print("No products found.")

