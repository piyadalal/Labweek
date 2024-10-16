import sys

import keyboard
import subprocess


# Function to trigger the Python script
def trigger_script():
    print("Key pressed! Triggering the backend script...")
    subprocess.run([sys.executable, 'C://Users//PRDA5207//Desktop//CloudVision//Image_search//Image_search_bing.py'])  # Replace 'backend_script.py' with your script name

def listen_for_key_presses():
    print("Listening for key presses...")
    print("Press 't' to trigger the backend script or 'q' to quit.")

    while True:
        # Use keyboard.is_pressed to check for key presses without waiting
        if keyboard.is_pressed('t'):
            trigger_script()
            break
        elif keyboard.is_pressed('q'):
            print("Exiting...")
            break  # Exit the loop and end the program



if __name__ == "__main__":
    listen_for_key_presses()