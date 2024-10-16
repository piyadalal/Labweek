import cv2
from pyzbar.pyzbar import decode
import subprocess

# Function to scan the QR code
def scan_qr_code():
    # Start the video capture (webcam)
    cap = cv2.VideoCapture(0)
    
    while True:
        # Read frame from the webcam
        ret, frame = cap.read()
        
        # If the frame is captured successfully
        if ret:
            # Decode QR codes in the frame
            qr_codes = decode(frame)
            
            # Loop through detected QR codes
            for qr_code in qr_codes:
                # Convert QR code data to string
                qr_data = qr_code.data.decode('utf-8')
                print(f"QR Code detected: {qr_data}")
                
                # Trigger another script based on QR data
                if qr_data == 'trigger_script':  # You can customize the condition here
                    print("Triggering backend script...")
                    subprocess.run(['python3', 'backend_script.py'])  # Replace with your script path
                
                # Draw rectangle around the QR code
                pts = qr_code.polygon
                if len(pts) > 4:
                    pts = pts[:4]
                pts = [(point.x, point.y) for point in pts]
                pts = pts[:4]
                
                for i in range(len(pts)):
                    cv2.line(frame, pts[i], pts[(i + 1) % 4], (0, 255, 0), 3)
        
            # Show the webcam feed with the QR code detected
            cv2.imshow('QR Code Scanner', frame)
        
        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Run the QR code scanner
if __name__ == "__main__":
    scan_qr_code()
