from bing_visual_search import BingVisualSearch

# Initialize BingVisualSearch with your API key
bing_search = BingVisualSearch('your_bing_search_api_key')

# Call the search function with the path to your image
image_path = '/path/to/image.jpg'
shopping_results = bing_search.search_product_with_image(image_path)

# Print the shopping results
if shopping_results:
    for item in shopping_results:
        print(item)
else:
    print("No shopping items found.")
