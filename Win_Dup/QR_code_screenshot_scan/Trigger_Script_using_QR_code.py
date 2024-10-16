from flask import Flask
import subprocess

app = Flask(__name__)

# Route to trigger the backend script
@app.route('/trigger')
def trigger_script():
    # Call the backend script using subprocess
    subprocess.run(['python', r"C:\Users\PRDA5207\Desktop\CloudVision\Image_search\Image_search_bing.py"])
    return "Backend script triggered!"

# Main block to run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
