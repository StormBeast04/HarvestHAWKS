from flask import Flask, request
import os

app = Flask(__name__)

# Create a directory to save uploaded images
if not os.path.exists('uploads'):
    os.makedirs('uploads')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files and not request.data:
        return "No file part", 400

    # Saving the uploaded image
    img_data = request.data
    if img_data:
        with open(os.path.join('uploads', 'image.jpg'), 'wb') as f:
            f.write(img_data)
        return "Image uploaded successfully", 200
    else:
        return "No image data", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
