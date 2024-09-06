import cv2  # For image capture
import requests  # For HTTP requests to send data
import time

# Configuration
RPI_IP = '192.168.1.100'  # Replace with your Raspberry Pi's IP address
RPI_PORT = '5000'  # Port on which the Raspberry Pi server is listening
IMAGE_CAPTURE_INTERVAL = 10  # Time interval to capture images in seconds
DRONE_ID = 'Drone01'  # Unique ID for the drone

# Image Capture Setup
camera = cv2.VideoCapture(0)  # Assuming the drone has a camera at /dev/video0

def capture_image():
    ret, frame = camera.read()
    if not ret:
        print("Failed to capture image")
        return None
    return frame

def send_image(image):
    # Encode the image as JPEG
    _, img_encoded = cv2.imencode('.jpg', image)

    # Prepare the payload to send to the Raspberry Pi
    files = {'image': ('drone_image.jpg', img_encoded.tobytes(), 'image/jpeg')}
    data = {'drone_id': DRONE_ID}
    
    try:
        # Send a POST request with the image to the Raspberry Pi server
        response = requests.post(f'http://{RPI_IP}:{RPI_PORT}/upload', files=files, data=data)
        if response.status_code == 200:
            print("Image sent successfully")
        else:
            print(f"Failed to send image, status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending image: {e}")

def main():
    while True:
        # Capture image at regular intervals
        image = capture_image()
        if image is not None:
            send_image(image)
        
        # Wait for the next capture interval
        time.sleep(IMAGE_CAPTURE_INTERVAL)

if __name__ == '__main__':
    main()