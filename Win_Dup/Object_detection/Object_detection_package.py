import os
import io
from google.cloud import vision
from google.oauth2 import service_account

class ClothingDetector:
    def __init__(self, credentials_path):
        """Initialize the detector with Google Cloud credentials."""
        self.credentials = service_account.Credentials.from_service_account_file(credentials_path)
        self.client = vision.ImageAnnotatorClient(credentials=self.credentials)

    def detect_clothing_in_image(self, image_path):
        """Detect clothing-related items in the image using Google Cloud Vision API."""
        # Load image from file
        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        # Perform label detection
        response = self.client.label_detection(image=image)
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
    GOOGLE_APPLICATION_CREDENTIALS_JSON = r'C:\Users\PRDA5207\Desktop\MyLens_GCP_cloud_vision.json'
    object_clothing_detector = ClothingDetector(GOOGLE_APPLICATION_CREDENTIALS_JSON)
    clothing_labels = object_clothing_detector.detect_clothing_in_image(image_path)
    return clothing_labels

if __name__ == '__main__':
    # Provide the path to your image file

    image_path = r'C:\Users\PRDA5207\Desktop\CloudVision\Image_search\image_object_to_be_detected.jpg'
    main(image_path)
