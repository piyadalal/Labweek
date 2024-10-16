import requests
import json
import os


class BingVisualSearch:
    def __init__(self, subscription_key):
        """Initialize the Bing Visual Search API client with a subscription key."""
        self.subscription_key = subscription_key
        self.endpoint = 'https://api.bing.microsoft.com/v7.0/images/visualsearch'

    def search_product_with_image(self, image_path):
        """Send an image to Bing Visual Search and return shopping-related results."""

        # Open the image file in binary mode
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()

        # Set up the headers for the request
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key,
            'Content-Type': 'multipart/form-data'
        }

        # Send the request to Bing Visual Search API
        response = requests.post(
            self.endpoint,
            headers={'Ocp-Apim-Subscription-Key': self.subscription_key},
            files={"image": image_data}
        )

        # Check if the request was successful
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
            # If request fails, print the error code and message
            print(f"Error: {response.status_code}, {response.text}")
            return None


# Example usage of the class
if __name__ == "__main__":
    # Initialize the BingVisualSearch class with your subscription key

    BING_SEARCH_API_KEY = os.getenv('BING_IMAGE_SEARCH_KEY')
    if BING_SEARCH_API_KEY:
        print("API Key found:", BING_SEARCH_API_KEY)
    else:
        print("API Key not found! Please check if it's set correctly.")

    subscription_key = 'your_bing_search_api_key'
    bing_search = BingVisualSearch(BING_SEARCH_API_KEY)

    # Path to the image you want to search
    image_path = r'C:\Users\PRDA5207\Desktop\CloudVision\Image_search\skirt.jpg'

    # Call the method to search for products using the image
    shopping_results = bing_search.search_product_with_image(image_path)

    # Print results
    if shopping_results:
        print(f"Found {len(shopping_results)} shopping items!")
        for item in shopping_results:
            print(json.dumps(item, indent=2))
    else:
        print("No shopping items found.")
