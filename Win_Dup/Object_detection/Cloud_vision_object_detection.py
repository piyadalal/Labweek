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



def main(image_path):
    # Step 1: Detect clothing in the image
    clothing_labels = detect_clothing_in_image(image_path)
    return clothing_labels

if __name__ == '__main__':
    # Provide the path to your image file

    image_path = r'C:\Users\PRDA5207\Desktop\CloudVision\Image_search\image_object_to_be_detected.jpg'
    main(image_path)





