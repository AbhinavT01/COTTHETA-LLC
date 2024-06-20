import io
import pandas as pd
from google.cloud import vision

# Function to extract table from image using Google Cloud Vision API
def extract_table_from_image(image_path, output_excel):
    # Authenticate using service account key
    client = vision.ImageAnnotatorClient.from_service_account_json('./myservicegapi.json')

    # Read image file
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    # Perform OCR on the image
    image = vision.Image(content=content)
    response = client.document_text_detection(image=image)
    document = response.full_text_annotation

    # Extract text and structure into tabular format
    table_data = []
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                row_data = []
                for word in paragraph.words:
                    word_text = ''.join([symbol.text for symbol in word.symbols])
                    row_data.append(word_text)
                table_data.append(row_data)

    # Convert table data to pandas DataFrame
    df = pd.DataFrame(table_data)

    # Export DataFrame to Excel
    df.to_excel(output_excel, index=False, header=False)

    print(f"Table extracted and saved to {output_excel}")

# Example usage:
if __name__ == "__main__":
    image_path = './images.png'
    output_excel = 'output_table.xlsx'
    extract_table_from_image(image_path, output_excel)
