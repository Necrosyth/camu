import cv2
import numpy as np

def scan_it(qr):
    # Read the image
    image = cv2.imread(qr)
    
    if image is None:
        print("Error: Could not read image")
        return None
        
    # Initialize QR Code detector
    qr_detector = cv2.QRCodeDetector()
    
    # Detect and decode
    try:
        data, bbox, _ = qr_detector.detectAndDecode(image)
        if data:
            return data
        return None
    except Exception as e:
        print(f"Error scanning QR code: {e}")
        return None