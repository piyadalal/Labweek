import os
import io
import requests
from google.cloud import vision
from google.oauth2 import service_account  # Import this for loading the key
from PIL import Image, ImageDraw

# Bing Search API key
BING_SEARCH_API_KEY = 'your_bing_search_api_key'
BING_SEARCH_ENDPOINT = 'https://api.bing.microsoft.com/v7.0/images/search'

# Provide the path to your Google Cloud Vision JSON key file
GOOGLE_APPLICATION_CREDENTIALS_JSON = '/Users/PRDA5207/Desktop/Cloudvision.json'
GOOGLE_API_KEY = os.getenv('GOOGLE_CUSTOM_SEARCH_API_KEY')
cx = os.getenv('cx')

def detect_clothing_in_image(image_path):
    """Detect clothes or fashion-related items in an image using Google Cloud Vision API."""

    # Load the credentials from the JSON key file
    credentials = service_account.Credentials.from_service_account_file(GOOGLE_APPLICATION_CREDENTIALS_JSON)

    # Initialize Google Cloud Vision client with credentials
    client = vision.ImageAnnotatorClient(credentials=credentials)

    # Load image from file
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Perform label detection
    response = client.label_detection(image=image)
    labels = response.label_annotations

    clothing_labels = []
    print("Detected labels:")

    for label in labels:
        # Filter out clothing-related labels
        if 'clothing' in label.description.lower() or 'apparel' in label.description.lower() or 'fashion' in label.description.lower():
            clothing_labels.append(label.description)
            print(f"Clothing detected: {label.description}, score: {label.score}")

    if not clothing_labels:
        print("No clothing detected.")
        return None

    return clothing_labels


def search_clothing_on_bing(clothing_labels):
    """Search for clothing items on Bing based on detected labels."""
    results = {}

    for label in clothing_labels:
        search_query = label
        headers = {"Ocp-Apim-Subscription-Key": BING_SEARCH_API_KEY}
        params = {"q": search_query, "license": "public", "imageType": "photo"}

        response = requests.get(BING_SEARCH_ENDPOINT, headers=headers, params=params)
        response.raise_for_status()

        search_results = response.json()

        # Collect the image URLs from search results
        if 'value' in search_results:
            image_urls = [img['contentUrl'] for img in search_results['value']]
            results[label] = image_urls
        else:
            results[label] = []

    return results
def search_google_images(search_query, api_key, cx):
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
    clothing_labels = detect_clothing_in_image(image_path)

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

def main_1(image_path):
    # Step 1: Detect clothing in the image
    clothing_labels = detect_clothing_in_image(image_path)

    if clothing_labels:
        print("\nSearching for clothing on Bing...")

        # Step 2: Search for detected clothing labels using Bing Image Search
        search_results = search_clothing_on_bing(clothing_labels)

        # Step 3: Display results
        for label, urls in search_results.items():
            print(f"\nResults for '{label}':")
            if urls:
                for i, url in enumerate(urls[:5]):  # Show top 5 images
                    print(f"{i + 1}: {url}")
                display_images(urls[:5])
            else:
                print(f"No results found for '{label}'")


if __name__ == '__main__':
    # Provide the path to your image file
    image_path = '/Users/PRDA5207/Desktop/search_image.jpeg'
    main(image_path)





