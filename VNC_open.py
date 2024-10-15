import subprocess

# Replace with your STB IP
ip_stb = '192.168.1.10'  # Replace this with your STB's actual IP address
port = '5800'

# Create the VNC command to connect to STB
vnc_command = f'{ip_stb}:{port}'

# Run the VNC command using subprocess to open VNC viewer
try:
    # This assumes VNC viewer is installed and available in PATH
    subprocess.run(['vncviewer', vnc_command], check=True)
    print(f"Successfully connected to {vnc_command}")
except subprocess.CalledProcessError as e:
    print(f"Failed to connect to {vnc_command}: {e}")
except FileNotFoundError:
    print("VNC Viewer not found. Please make sure VNC Viewer is installed and added to PATH.")
