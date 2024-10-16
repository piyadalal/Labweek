import requests

# Set your RapidAPI endpoint and API key
RAPIDAPI_HOST = "rapidapi.com"  # Replace with the actual host
RAPIDAPI_KEY = "c576b27fabmsh1b36bfc5a30d9fdp1fb317jsn5bf116cdb3a6"  # Replace with your RapidAPI key

def reverse_image_search(image_path):
    # Open the image file
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    # Set up the headers for the request
    headers = {
        "Content-Type": "application/octet-stream",
        "x-rapidapi-host": RAPIDAPI_HOST,
        "x-rapidapi-key": RAPIDAPI_KEY
    }

    # Send the request to the reverse image search API
    response = requests.post(
        f"https://{RAPIDAPI_HOST}/reverse-image-search",
        headers=headers,
        data=image_data
    )

    # Check the response
    if response.status_code == 200:
        search_results = response.json()
        return search_results
    else:
        print(f"Error: {response.status_code} ")
        return None

# Example usage
image_path = r'C:\Users\PRDA5207\Desktop\skirt.jpg'  # Path to your image
results = reverse_image_search(image_path)

# Print the results
if results:
    print("Search Results:")
    for result in results.get("results", []):  # Adjust based on the actual structure of the response
        print(f"Title: {result.get('title')}")
        print(f"Link: {result.get('link')}")
        print(f"Thumbnail: {result.get('thumbnail')}")
        print()
