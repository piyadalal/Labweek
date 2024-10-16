import keyboard
import subprocess
import sys
import time


# Function to trigger the Python script
def trigger_script():
    print("Key pressed! Triggering the backend script...")
    process =subprocess.Popen([sys.executable,'C://Users//PRDA5207//Desktop//CloudVision//Image_search//Image_search_bing.py'])

    #subprocess.run([sys.executable,'C://Users//PRDA5207//Desktop//CloudVision//Image_search//Image_search_bing.py'])  # Replace 'backend_script.py' with your script name
    #return process

# Main loop to listen for key presses indefinitely
def listen_for_key_presses():
    print("Listening for key presses...")
    print("Press 't' to trigger the backend script or 'q' to quit.")

    while True:  # Keep looping to listen for key presses
        if keyboard.is_pressed('t'):
            trigger_script()  # Call to trigger the backend script
            # Wait until the key is released to avoid multiple triggers
            keyboard.wait('t', suppress=True)  # This waits for the 't' key to be released

        elif keyboard.is_pressed('q'):
            print("Exiting...")
            break  # Exit the loop and end the program


if __name__ == "__main__":
    listen_for_key_presses()
    #sys.exit()