from google.cloud import vision
import os
import io

# Set Google Cloud credentials environment variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'myservicegapi.json'

def detect_text(image_path):
    client = vision.ImageAnnotatorClient()

    # Read image file
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Perform text detection
    response = client.text_detection(image=image)
    texts = response.text_annotations

    # Store detected text as a single string
    detected_text = texts[0].description.strip()

    # Split the text into words
    words = detected_text.split('\n')

    return words

# Example usage
# image_path = './uploads/img.jpeg'  # Replace with your image path
# detected_words = detect_text(image_path)
# print("Detected Words:")
# for word in detected_words:
#     print(word)
