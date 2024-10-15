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

        # Filter out clothing-related labels
        clothing_labels = [
            label.description for label in labels
            if 'clothing' in label.description.lower() or
               'apparel' in label.description.lower() or
               'fashion' in label.description.lower()
        ]

        if not clothing_labels:
            print("No clothing detected.")
            return None

        return clothing_labels
