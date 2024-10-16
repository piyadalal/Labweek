import keyboard
import subprocess
import sys

# Function to trigger the Python script
def trigger_script():
    print("Key pressed! Triggering the backend script...")
    
    # Use the same Python executable to run the script
    subprocess.run([sys.executable, 'backend_script.py'])  # Replace 'backend_script.py' with your script name

# Main loop to listen for key presses indefinitely
def listen_for_key_presses():
    print("Listening for key presses...")
    print("Press 't' to trigger the backend script or 'q' to quit.")

    while True:
        # Use keyboard.is_pressed to check for key presses without waiting
        if keyboard.is_pressed('t'):
            trigger_script()
        elif keyboard.is_pressed('q'):
            print("Exiting...")
            break  # Exit the loop and end the program

if __name__ == "__main__":
    listen_for_key_presses()
