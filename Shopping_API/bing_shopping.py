import requests
import json

# Your Bing Search API key
SUBSCRIPTION_KEY = 'your_bing_search_api_key'

# Bing Visual Search endpoint
VISUAL_SEARCH_ENDPOINT = 'https://api.bing.microsoft.com/v7.0/images/visualsearch'

def search_product_with_image(image_path):
    """Send an image to Bing Visual Search and return shopping-related results."""
    
    # Open the image file in binary mode
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    headers = {
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
        'Content-Type': 'multipart/form-data'
    }

    # API request to Bing Visual Search
    response = requests.post(
        VISUAL_SEARCH_ENDPOINT, 
        headers={'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}, 
        files={"image": image_data}
    )

    # Check for successful request
    if response.status_code == 200:
        results = response.json()

        # Filter for shopping-related results
        shopping_items = []
        for item in results.get('tags', []):
            for action in item.get('actions', []):
                if action['actionType'] == 'VisualSearchShopping':
                    shopping_items.append(action['data'])

        return shopping_items

    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None


# Example usage
image_path = 'path_to_your_image.jpg'
shopping_results = search_product_with_image(image_path)

# Print results
if shopping_results:
    print(f"Found {len(shopping_results)} shopping items!")
    for item in shopping_results:
        print(json.dumps(item, indent=2))
else:
    print("No shopping items found.")
