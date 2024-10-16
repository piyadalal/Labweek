from flask import Flask, jsonify, render_template
from Image_search.image_search_bing_package import ClothingSearch # Import the function from your external script
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_data', methods=['GET'])
def get_data_route():
    google_credentials_path = r'C:\Users\PRDA5207\Desktop\MyLens_GCP_cloud_vision.json'
    bing_api_key = os.getenv('BING_IMAGE_SEARCH_KEY')
    image_path = r'C:\Users\PRDA5207\Desktop\CloudVision\Image_search\image_object_to_be_detected.jpg'
    cs = ClothingSearch(google_credentials_path,bing_api_key)
    data = cs.search_image_on_bing(image_path)  # Call the function to get the data
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


