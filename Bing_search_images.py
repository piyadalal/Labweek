import requests

# API endpoint and subscription key
url = "https://api.bing.microsoft.com/v7.0/images/visualsearch"
subscription_key = "YOUR_BING_API_KEY"

# Define headers
headers = {
    "Ocp-Apim-Subscription-Key": subscription_key,
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
