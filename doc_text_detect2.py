import os
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'myservicegapi.json'

def detect_document_text(image_path):
    """Detects document text in an image."""
    # Initialize the client
    client = vision.ImageAnnotatorClient()

    # Read the image file
    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    # Construct the image
    image = vision.Image(content=content)

    # Perform document text detection
    response = client.document_text_detection(image=image)
    annotations = response.full_text_annotation

    if annotations:
        # Return the raw detected text
        formatted_text = annotations.text

        print('Detected document text:')
        print(formatted_text)
        return formatted_text
    else:
        return 'No document text detected.'

    if response.error.message:
        raise Exception(f'{response.error.message}')

# if __name__ == "__main__":

#     # Path to the image file
#     image_path = './images1.jpg'
    
#     # Detect document text
#     detect_document_text(image_path)
