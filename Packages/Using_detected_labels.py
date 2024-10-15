from my_clothing_detector import ClothingDetector, BingSearch

# Initialize clothing detector with Google Vision credentials
detector = ClothingDetector('/path/to/your/Cloudvision.json')

# Path to the image you want to process
image_path = '/path/to/screenshot.jpg'

# Detect clothing items in the image
clothing_labels = detector.detect_clothing_in_image(image_path)

if clothing_labels:
    print(f"Detected clothing items: {clothing_labels}")

    # Initialize Bing Search with API key
    bing_search = BingSearch('your_bing_search_api_key')

    # Search for each detected clothing item on Bing
    for label in clothing_labels:
        print(f"Searching for: {label}")
        results = bing_search.search_images(label)
        
        # Display the top 3 results
        for result in results[:3]:
            print(f"Image URL: {result['contentUrl']}")
else:
    print("No clothing items detected.")
