import cv2
from pyzbar.pyzbar import decode
import subprocess

# Function to scan the QR code
def scan_qr_code():
    # Start the webcam video capture
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if ret:
            # Decode the QR code in the frame
            qr_codes = decode(frame)
            
            # Check if any QR code is detected
            for qr_code in qr_codes:
                # Decode the QR code data to a string
                qr_data = qr_code.data.decode('utf-8')
                print(f"QR Code detected: {qr_data}")

                # If QR code data matches, trigger the backend script
                if qr_data == 'trigger_script':  # Change this condition as needed
                    print("Triggering the backend script...")
                    
                    # Call the backend script using subprocess
                    subprocess.run(['python3', 'backend_script.py'])

                # Draw a rectangle around the QR code
                pts = qr_code.polygon
                if len(pts) > 4:
                    pts = pts[:4]
                pts = [(point.x, point.y) for point in pts]
                for i in range(len(pts)):
                    cv2.line(frame, pts[i], pts[(i + 1) % 4], (0, 255, 0), 3)

        # Display the frame with the QR code detection
        cv2.imshow('QR Code Scanner', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_qr_code()
