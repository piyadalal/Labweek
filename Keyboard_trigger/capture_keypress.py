import keyboard
import subprocess

# Function to trigger the Python script
def trigger_script():
    print("Key pressed! Triggering the backend script...")
    subprocess.run(['python3', 'backend_script.py'])  # Replace 'backend_script.py' with your script name

# Listening for key press
def detect_key_press():
    print("Press 't' to trigger the backend script or 'q' to quit.")
    
    # Detect 't' key press to trigger the script
    keyboard.add_hotkey('t', trigger_script)
    
    # Detect 'q' key press to quit the program
    keyboard.add_hotkey('q', lambda: exit("Exiting..."))

    # Block the script and keep listening for key press events
    keyboard.wait()

if __name__ == "__main__":
    detect_key_press()
