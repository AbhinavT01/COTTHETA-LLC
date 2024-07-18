# COTTHETA-LLC
COTTHETA LLC OCR System
This repository contains the OCR system developed during my internship at CotTheta LLC. The system is designed to detect and extract text from various documents, clean the text, and rectify OCR errors. The extracted information is processed to identify patterns, crop relevant parts of the image, and categorize addresses and human names. The results are then displayed on a Flask web server.

Table of Contents
Requirements
Installation
Usage
File Structure
Detailed Description
Acknowledgements
Requirements
Python 3.10.11
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/AbhinavT01/COTTHETA-LLC.git
cd COTTHETA-LLC
Install the required Python packages:
bash
Copy code
pip install -r requirements.txt
Set up Google Cloud Vision API credentials:

Download your service account key from the Google Cloud Console.
Set the path to your service account key in the environment variable GOOGLE_APPLICATION_CREDENTIALS:
bash
Copy code
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service/account/key.json"
Usage
Start the Flask web application:
bash
Copy code
python app.py
Open your web browser and navigate to http://127.0.0.1:5000/.

Upload a document to be processed and view the results on the result page.

File Structure
graphql
Copy code
COTTHETA-LLC/
│
├── Address.py                    # Add files via upload (last month)
├── README.md                     # Initial commit (last month)
├── app.py                        # Add files via upload (last month)
├── autocrop.py                   # Add files via upload (last month)
├── autorotate.py                 # Experimental file for auto-rotation of documents (last month)
├── bank_name.py                  # Add files via upload (last month)
├── card_detect.py                # Add files via upload (last month)
├── cropimage.py                  # Add files via upload (last month)
├── doc_text_detect.py            # Add files via upload (last month)
├── human_detection.py            # Add files via upload (last month)
├── human_detection2.py           # Add files via upload (last month)
├── images.png                    # Add files via upload (last month)
├── img.jpg                       # Add files via upload (last month)
├── main.py                       # Add files via upload (last month)
├── ocr.py                        # Add files via upload (last month)
├── patternfile.py                # Add files via upload (last month)
├── person name detect.py         # Add files via upload (last month)
├── pp.py                         # Bank data testing script (last month)
├── regextest.py                  # Add files via upload (last month)
├── requirements.txt              # Add files via upload (last month)
├── rotated_image.jpg             # Add files via upload (last month)
├── runtime.txt                   # Add files via upload (last month)
├── visionapi_testing.py          # Google Vision API testing script (last month)
├── sample_data/                  # Add files via upload (last month)
├── templates/                    # Add files via upload (last month)
│   ├── index.html
│   ├── result.html
├── static/
│   ├── styles.css
Address.py: Identifies the type of address (street, city, zip, state) from the extracted text.
README.md: Documentation file.
app.py: Contains the Flask web application.
autocrop.py: Contains the crop_image function for auto-cropping images.
autorotate.py: Experimental file for auto-rotating documents.
bank_name.py: Extracts relevant information from bank cards, including bank name.
card_detect.py: Extracts relevant information from bank cards, such as card number, expiry date, CVV, and card type using regex patterns.
cropimage.py: Uses OpenCV to find the largest rectangle or square bounding box in the image and crops that box to get the relevant part of the document.
doc_text_detect.py: Detects and extracts text from documents, including multiple paragraphs and handwritten paragraphs, using the Google Cloud Vision API.
human_detection.py: Detects human names using Google Natural Language Processing Toolkit.
human_detection2.py: An alternate human detection script.
images.png & img.jpg: Sample images for testing.
main.py: Contains the main logic for the OCR system.
ocr.py: General OCR processing.
patternfile.py: Contains a large set of regex patterns that match the extracted text.
person name detect.py: Detects person names using patterns and models.
pp.py: Bank data testing script.
regextest.py: Tests regex patterns.
requirements.txt: Lists the required Python packages.
rotated_image.jpg: Rotated sample image.
runtime.txt: Runtime configuration file.
visionapi_testing.py: Google Vision API testing script.
sample_data/: Contains sample data files.
templates/: Contains HTML templates for the web application.
index.html: Starting page of the web server.
result.html: Displays the OCR results.
static/: Contains static files such as CSS for styling the web application.
Detailed Description
app.py
This file contains the Flask web application. It serves the starting page and displays the results of the OCR processing. It includes routes for uploading documents and displaying processed results.

main.py
The core of the OCR system. It performs the following tasks:

Detects text from documents.
Cleans the text to remove unwanted characters and rectifies OCR errors.
Passes cleaned text to other modules for further processing.
patternfile.py
Contains a large set of regex patterns that match the extracted text. Each pattern checks whether the text is a required field or not. These patterns are imported and used in main.py.

cropimage.py
Uses OpenCV to find the largest rectangle or square bounding box in the image and crops that box to get the relevant part of the document. This function is imported and used in main.py.

address.py
Identifies the type of address (street, city, zip, state) from the extracted text. This module is imported and used in main.py.

human_detection.py
Detects human names using the Google Natural Language Processing Toolkit. This module is imported and used in main.py.

card_detect.py
Extracts relevant information from bank cards, such as card number, expiry date, CVV, and card type using regex patterns. This module is imported and used in main.py.

analyze_entities.py
Detects bank names from the text using NLP models. This module is imported and used in main.py.

document_detection.py
Detects and extracts text from documents, including multiple paragraphs and handwritten paragraphs, using the Google Cloud Vision API. The detect_document_text function initializes the Vision API client, reads the image file, and performs document text detection. If text is detected, it is processed and displayed, capable of handling both printed and handwritten text.

pp.py
A testing script for bank data. This script is used to test the functionality of extracting and processing data from bank documents.

visionapi_testing.py
A testing script for the Google Vision API. This script is used to test the capabilities and functionality of the Google Vision API in processing and extracting text from images.

autorotate.py
An experimental file used for testing the auto-rotation of documents. This script explores methods for correctly orienting scanned or photographed documents to facilitate accurate text extraction.

templates/
Contains HTML files:

index.html: Starting page of the web server.
result.html: Displays the OCR results.
static/
Contains static files such as CSS for styling the web application.

Acknowledgements
Special thanks to Ashish K. Dash from CotTheta LLC for mentoring and guidance throughout this project.

This updated README provides a comprehensive overview of your project, including installation instructions, usage, and detailed descriptions of each file's functionality, specifically highlighting the license and bank card recognition features, as well as the document detection capabilities, including handling multiple paragraphs and handwritten paragraphs using the Google Cloud Vision API. The additions also include descriptions for the testing scripts and the experimental auto-rotation script.
