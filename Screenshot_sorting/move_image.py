import os
import shutil
from datetime import datetime

def get_latest_screenshot(src_dir):
    # Get all files in the source directory
    files = [f for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]
    
    # Filter out the screenshots by file extension (assuming they are images like .png, .jpg)
    screenshots = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

    # Sort the files by modification time
    screenshots.sort(key=lambda f: os.path.getmtime(os.path.join(src_dir, f)), reverse=True)

    # Return the most recent screenshot file
    return screenshots[0] if screenshots else None

def rename_and_move_screenshot(src_dir, dst_dir, new_name):
    # Get the latest screenshot
    latest_screenshot = get_latest_screenshot(src_dir)

    if latest_screenshot:
        # Define the full path for the latest screenshot
        old_file_path = os.path.join(src_dir, latest_screenshot)
        
        # Get the extension of the file to preserve it
        file_extension = os.path.splitext(latest_screenshot)[1]
        
        # Create the new file name with the extension
        new_file_name = new_name + file_extension
        
        # Define the new file path in the destination directory
        new_file_path = os.path.join(dst_dir, new_file_name)
        
        # Move and rename the screenshot
        shutil.move(old_file_path, new_file_path)
        
        print(f"Moved and renamed {latest_screenshot} to {new_file_path}")
    else:
        print("No screenshots found in the source directory.")

# Example usage
source_directory = '/path/to/source/directory'  # Replace with the actual source directory where screenshots are saved
destination_directory = '/path/to/destination/directory'  # Replace with the actual destination directory
new_filename = 'renamed_screenshot_' + datetime.now().strftime('%Y%m%d_%H%M%S')  # Generates a timestamped filename

rename_and_move_screenshot(source_directory, destination_directory, new_filename)
