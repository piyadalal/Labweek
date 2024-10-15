import requests
import base64
import json
import os

# Load API key from environment variable or set it directly
GOOGLE_API_KEY = os.getenv('GOOGLE_CUSTOM_SEARCH_API_KEY')  # Replace with your API key

def detect_clothing_in_image(image_path):
    """Detect clothes or fashion-related items in an image using Google Cloud Vision API."""

    # Cloud Vision API URL
    url = f"https://vision.googleapis.com/v1/images:annotate?key={GOOGLE_API_KEY}"

    # Read the image and convert it to base64
    with open(image_path, "rb") as image_file:
        image_content = base64.b64encode(image_file.read()).decode("utf-8")

    # Create the payload for the Cloud Vision API request
    payload = {
        "requests": [
            {
                "image": {
                    "content": image_content
                },
                "features": [
                    {
                        "type": "LABEL_DETECTION",
                        "maxResults": 10
                    }
                ]
            }
        ]
    }

    # Make the POST request to Cloud Vision API
    response = requests.post(url, data=json.dumps(payload), headers={"Content-Type": "application/json"})

    # Parse the response
    if response.status_code == 200:
        labels = response.json()["responses"][0]["labelAnnotations"]
        for label in labels:
            print(f"Detected label: {label['description']} (score: {label['score']})")
    else:
        print(f"Error: {response.status_code} - {response.text}")

# Example usage
detect_clothing_in_image('/Users/PRDA5207/Desktop/search_image.jpeg')
