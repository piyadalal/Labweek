import requests
import os
# API endpoint and subscription key
url = "https://api.bing.microsoft.com/v7.0/images/visualsearch"
BING_IMAGE_SEARCH_KEY = os.getenv('BING_IMAGE_SEARCH_KEY')


# Define headers
headers = {
    "Ocp-Apim-Subscription-Key": BING_IMAGE_SEARCH_KEY,
    "Content-Type": "multipart/form-data"
}

# Open and read the image file (replace with the path to your local image)
with open("image.jpg", "rb") as image_file:
    image_data = image_file.read()

# Make the POST request with image data
response = requests.post(url, headers=headers, data=image_data)

# Check if request was successful
if response.status_code == 200:
    # Print the search results
    search_results = response.json()
    print(search_results)
else:
    print(f"Error: {response.status_code}, {response.text}")
