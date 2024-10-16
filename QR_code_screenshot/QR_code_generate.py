import qrcode

# Function to generate a QR code
def generate_qr_code(data, file_name):
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code (this could be a URL or text)
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')

    # Save the image to a file
    img.save(file_name)
    print(f"QR Code generated and saved as {file_name}")

# Main
if __name__ == "__main__":
    # URL or text that the QR code will represent
    qr_data = "http://127.0.0.1:5000/trigger"
    file_name = "qr_code_trigger.png"
    
    # Generate and save the QR code
    generate_qr_code(qr_data, file_name)
