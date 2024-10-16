import os
import io
import requests
from google.cloud import vision
from google.oauth2 import service_account  # Import this for loading the key
from PIL import Image, ImageDraw

import os

# Provide the path to your Google Cloud Vision JSON key file
GOOGLE_APPLICATION_CREDENTIALS_JSON = r'C:\Users\PRDA5207\Desktop\MyLens_GCP_cloud_vision.json'
GOOGLE_API_KEY = os.getenv('GOOGLE_CUSTOM_SEARCH_API_KEY')
cx = os.getenv('cx')


def search_google_images(search_query, GOOGLE_API_KEY, cx):
    "Searching based on query string"
    """Search for images on Google using Custom Search API based on detected labels."""
    #search_url = "https://www.googleapis.com/customsearch/v1"
    search_url = "https://cse.google.com/cse?cx=7490c5af6dba240a9"

    params = {
        'q': search_query,
        'cx': cx,  # Custom Search Engine ID
        'key': GOOGLE_API_KEY,
        'searchType': 'image',  # To retrieve images
        'num': 5  # Number of results
    }

    response = requests.get(search_url, params=params)
    response.raise_for_status()

    search_results = response.json()

    # Collect the image URLs from search results
    image_urls = [item['link'] for item in search_results.get('items', [])]
    return image_urls





def display_images(image_urls):
    """Display matched images using Pillow."""
    for url in image_urls:
        try:
            response = requests.get(url)
            image = Image.open(io.BytesIO(response.content))
            image.show()
        except Exception as e:
            print(f"Could not open image: {e}")


def main(image_path):
    # Step 1: Detect clothing in the image using Google Vision API

    if clothing_labels:
        print("\nSearching for clothing on Google Custom Search...")

        # Step 2: Search for detected clothing labels using Google Custom Search API
        for label in clothing_labels:
            print(f"\nSearching for '{label}'...")
            image_urls = search_google_images(label, GOOGLE_API_KEY, cx)

            if image_urls:
                print(f"Found {len(image_urls)} images for '{label}':")
                for i, url in enumerate(image_urls):
                    print(f"{i + 1}: {url}")
                # Optionally, display the images
                display_images(image_urls)
            else:
                print(f"No images found for '{label}'")


if __name__ == '__main__':
    # Provide the path to your image file
    image_path = r'C:\Users\PRDA5207\Desktop\CloudVision\Image_search\image_object_to_be_detected.jpg'
    main(image_path)





