import os
import io
import sys
import requests
from PIL import Image
from Object_detection.Object_detection_package import ClothingDetector

class ClothingSearch:
    def __init__(self, google_credentials_path, bing_api_key):
        self.google_credentials_path = google_credentials_path
        self.bing_api_key = bing_api_key
        self.bing_visual_search_endpoint = "https://api.bing.microsoft.com/v7.0/images/visualsearch"
        self.clothing_detector = ClothingDetector(google_credentials_path)

    def search_clothing_on_bing(self, image_path):
        """Search for clothing items on Bing based on both image and detected labels."""
        clothing_labels = self.clothing_detector.detect_clothing_in_image(image_path)
        if clothing_labels:
            print("\nSearching for clothing on Bing...")
            return self.search_image_on_bing(image_path)
        else:
            print("No clothing detected in the image.")
            return {}

    def search_image_on_bing(self, image_path):
        """Search for an image on Bing using the Visual Search API."""
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()

        headers = {
            "Ocp-Apim-Subscription-Key": self.bing_api_key,
        }

        response = requests.post(
            self.bing_visual_search_endpoint,
            headers=headers,
            files={"image": image_data}
        )

        if response.status_code == 200:
            search_results = response.json()
            print(search_results)
            return search_results
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return {}

    def display_images(self, image_urls):
        """Display matched images using Pillow."""
        for url in image_urls:
            try:
                response = requests.get(url)
                image = Image.open(io.BytesIO(response.content))
                image.show()
            except Exception as e:
                print(f"Could not open image: {e}")

def main(image_path):
    google_credentials_path = r'C:\Users\PRDA5207\Desktop\MyLens_GCP_cloud_vision.json'
    bing_api_key = os.getenv('BING_IMAGE_SEARCH_KEY')

    if not bing_api_key:
        print("Bing API Key not found! Please check if it's set correctly.")
        return

    clothing_search = ClothingSearch(google_credentials_path, bing_api_key)
    search_results = clothing_search.search_clothing_on_bing(image_path)

    # Optionally display the results
    if 'value' in search_results:
        image_urls = [img['contentUrl'] for img in search_results['value']]
        clothing_search.display_images(image_urls[:5])  # Display the top 5 images

if __name__ == '__main__':
    image_path = r'C:\Users\PRDA5207\Desktop\CloudVision\Image_search\image_object_to_be_detected.jpg'
    main(image_path)
    sys.exit()
