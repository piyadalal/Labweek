import keyboard
import subprocess
import sys
import time

# Function to trigger the Python script
def trigger_script():
    print("Key pressed! Triggering the backend script...")
    
    # Use the same Python executable to run the script
    process = subprocess.Popen([sys.executable, 'backend_script.py'])  # Start the backend script
    return process  # Return the process handle

# Main loop to listen for key presses indefinitely
def listen_for_key_presses():
    print("Listening for key presses...")
    print("Press 't' to trigger the backend script or 'q' to quit.")

    process = None  # Process handle for the triggered script

    while True:
        # Use keyboard.is_pressed to check for key presses without waiting
        if keyboard.is_pressed('t'):
            if process is None or process.poll() is not None:  # Check if the script is not running
                process = trigger_script()  # Call to trigger the backend script
            else:
                print("Backend script is already running.")

        elif keyboard.is_pressed('q'):
            if process is not None:  # If the script is running, terminate it
                process.terminate()  # Terminate the backend script
                print("Backend script terminated.")
            print("Exiting main script...")
            break  # Exit the loop and end the program

if __name__ == "__main__":
    listen_for_key_presses()
