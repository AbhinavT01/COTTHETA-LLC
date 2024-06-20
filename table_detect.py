import os
from google.cloud import vision
from google.cloud.vision_v1 import types

def detect_table(image_path):
    """Detects tables in an image using the Vision API."""
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

    if not annotations:
        print('No document text detected.')
        return

    # Extract text blocks and look for table structures
    print('Detected document text:')
    for page in annotations.pages:
        for block in page.blocks:
            block_type = 'UNKNOWN'
            if block.block_type == 1:  # Table type
                block_type = 'TABLE'
            elif block.block_type == 2:  # Paragraph type
                block_type = 'PARAGRAPH'
            print(f'\nBlock Type: {block_type}')
            print('Block Confidence: {}'.format(block.confidence))
            for paragraph in block.paragraphs:
                print('Paragraph Confidence: {}'.format(paragraph.confidence))
                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    print('Word text: {} (confidence: {})'.format(
                        word_text, word.confidence))
                print('\n')

    if response.error.message:
        raise Exception(f'{response.error.message}')

if __name__ == "__main__":
    # Set the path to your service account key
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'myservicegapi.json'
    
    # Path to the image file
    image_path = './images.png'
    
    # Detect tables in the image
    detect_table(image_path)
