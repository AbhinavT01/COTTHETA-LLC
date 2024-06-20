import cv2
import pytesseract
import pandas as pd

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path

def preprocess_image(image_path):
    # Load image in grayscale mode
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply binary thresholding
    _, thresh = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes around contours
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    return image

def extract_table_from_image(image_path, output_excel):
    # Preprocess image
    processed_image = preprocess_image(image_path)

    # Extract text using Tesseract OCR
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(processed_image, config=custom_config)

    # Split text into lines
    lines = text.split('\n')

    # Parse lines into table format
    table_data = []
    for line in lines:
        if line.strip():  # Ignore empty lines
            row_data = line.split()
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
