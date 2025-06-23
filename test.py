import requests
import cv2

def test_image(file_path):
    url = 'http://localhost:5000/detect'
    with open(file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files)
        return response.json()

# Test with sample images
print("Testing real image:")
print(test_image('test_images/real.jpg'))

print("\nTesting fake image:")
print(test_image('test_images/fake.jpg'))