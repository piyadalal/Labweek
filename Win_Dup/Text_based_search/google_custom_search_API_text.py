import os
import io
import requests
from google.cloud import vision
from google.oauth2 import service_account  # Import this for loading the key
from PIL import Image, ImageDraw

import os

BING_SEARCH_API_KEY = os.getenv('BING_IMAGE_SEARCH_KEY')
if BING_SEARCH_API_KEY:
    print("API Key found:", BING_SEARCH_API_KEY)
else:
    print("API Key not found! Please check if it's set correctly.")


BING_VISUAL_SEARCH_ENDPOINT = "https://api.bing.microsoft.com/v7.0/images/visualsearch"
#BING_VISUAL_SEARCH_ENDPOINT = 'https://api.bing.microsoft.com/bing/v7.0/search'


# Provide the path to your Google Cloud Vision JSON key file
GOOGLE_APPLICATION_CREDENTIALS_JSON = r'C:\Users\PRDA5207\Desktop\MyLens_GCP_cloud_vision.json'
GOOGLE_API_KEY = os.getenv('GOOGLE_CUSTOM_SEARCH_API_KEY')
print(GOOGLE_API_KEY)
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

    # Perform label detection on the image file
    response = client.label_detection(image=image)

    # Get label annotations (list of labels)
    labels = response.label_annotations

    clothing_labels = []
    print("Detected labels:")

    for label in labels:
        # Filter out clothing-related labels
            clothing_labels.append(label.description)
            print(f"Label detected: {label.description}, score: {label.score}")

    # Check for errors in the API response
    if response.error.message:
        raise Exception(f"API Error: {response.error.message}")

    return clothing_labels





def search_clothing_on_bing(image_path, clothing_labels):
    """Search for clothing items on Bing based on both image and detected labels."""

    # Open the image file
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    # Prepare headers for the API request
    headers = {
        "Ocp-Apim-Subscription-Key": BING_SEARCH_API_KEY,
        "Content-Type": "multipart/form-data"
    }

    # Prepare the request with image data
    multipart_form_data = {
        "image": ("skirt.jpg", image_data, "image/jpeg")
    }

    results = {}

    # Perform the initial visual search with the image
    response = requests.post(BING_VISUAL_SEARCH_ENDPOINT, headers=headers, files=multipart_form_data)
    response.raise_for_status()
    visual_search_results = response.json()

    # Process each clothing label and refine search with both image and label
    '''for label in clothing_labels:
        # Refine search with detected labels (inverse search)
        search_query = label
        params = {
            "q": search_query,  # Add label as part of the search query
            "license": "public",
            "imageType": "photo"
        }

        # Perform another search with the label combined with image search results
        refined_response = requests.get(BING_VISUAL_SEARCH_ENDPOINT, headers=headers, params=params)
        refined_response.raise_for_status()
        refined_search_results = refined_response.json()

        # Collect the image URLs from refined search results
    if 'value' in visual_search_results:
        image_urls = [img['contentUrl'] for img in visual_search_results['value']]
        results[label] = image_urls
    else:
        results[label] = []  # No results for this label'''

    return visual_search_results

#Google custom search API :: text search query
#Bing Search API :
def search_image_on_bing(image_path, ):
    #RESULT_LIMIT = 5
    # Path to your local image file


    # Open the image file and prepare to send it to Bing
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
    print('Bing visual search endpoint {}'.format(BING_VISUAL_SEARCH_ENDPOINT))
    print('Bing visual search key {}'.format(BING_SEARCH_API_KEY))
    # Prepare the headers for the request
    headers = {
        "Ocp-Apim-Subscription-Key": BING_SEARCH_API_KEY,
    }

    # Send a POST request with the image data to Bing Visual Search API
    response = requests.post(
        BING_VISUAL_SEARCH_ENDPOINT,
        headers=headers,
        files={"image":  image_data}
    )

    # Check the response
    if response.status_code == 200:
        search_results = response.json()
        print(search_results)  # Process the search results
        '''
        # Initialize a list to hold limited search results
        limited_results = []

        # Limit the results to 10
        if 'tags' in search_results:
            for tag in search_results['tags']:
                for action in tag.get('actions', []):
                    if len(limited_results) >= RESULT_LIMIT:
                        break  # Stop when we reach the limit

                    if 'displayName' in action and action['displayName'] == "Visual Search":
                        for result in action.get('data', []):
                            if 'thumbnailUrl' in result:
                                limited_results.append(result['thumbnailUrl'])

                    # If we've reached the limit, stop adding more results
                    if len(limited_results) >= RESULT_LIMIT:
                        break

        # Print or return the limited results
        print(limited_results)  # This will print up to 10 image URLs
    '''
    else:
        print(f"Error: {response.status_code} - {response.text}")



def search_google_images(search_query, GOOGLE_API_KEY, cx):
    "Searching based on query string"
    """Search for images on Google using Custom Search API based on detected labels."""
    search_url = "https://www.googleapis.com/customsearch/v1"
    #search_url = "https://cse.google.com/cse?cx=7490c5af6dba240a9"

    params = {
        'q': search_query,
        'cx': cx,  # Custom Search Engine ID
        'key': GOOGLE_API_KEY,
        'searchType': 'image',  # To retrieve images
        'num': 1  # Number of results
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

def main1(image_path):
    clothing_labels = detect_clothing_in_image(image_path)

    if clothing_labels:
        print("\nSearching for clothing on bing visual Search...")

        # Step 2: Search for detected clothing labels using Bing Image Search
        search_results = search_image_on_bing(image_path)
        #search_results = search_clothing_on_bing(image_path,clothing_labels)


        # Step 3: Display results
        for label, urls in search_results.items():
            print(f"\nResults for '{label}':")
            if urls:
                for i, url in enumerate(urls[:5]):  # Show top 5 images
                    print(f"{i + 1}: {url}")
                display_images(urls[:5])
            else:
                print(f"No results found for '{label}'")
        '''
        # Limit the results by slicing the 'tags' section
        if 'tags' in search_results:
            limited_results = search_results['tags'][:RESULT_LIMIT]
            print(limited_results)  # Process or display limited results
        else:
            print("No tags found in the search results.")
        '''

if __name__ == '__main__':
    # Provide the path to your image file
    image_path = r'C:\Users\PRDA5207\Desktop\Red_car.jpg'
    main1(image_path)





