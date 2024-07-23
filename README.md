# COTTHETA LLC OCR System

## **COTTHETA LLC OCR System**

This repository houses an advanced OCR system developed during my internship at CotTheta LLC. The system excels in detecting and extracting text, autofilling extracted information into specified fields, and accurately identifying documents with paragraphs and handwritten content. It also robustly detects tabular data, whether handwritten or digital, enhancing its versatility in document processing." The results are then displayed on a Flask web server.

### Table of Contents

- **Requirements**
- **Installation**
- **Usage**
- **File Structure**
- **Detailed Description**
- **Acknowledgements**

### Requirements

- Python 3.10.11

### Installation

- **Clone the repository:**
  ```sh
  git clone https://github.com/AbhinavT01/COTTHETA-LLC.git
  cd COTTHETA-LLC



- **Install the required Python packages:**
   ```sh
  pip install -r requirements.txt

- **Set up Google Cloud Vision API credentials:**

  Download your service account key from the Google Cloud Console.
  Set the path to your service account key in the environment variable GOOGLE_APPLICATION_CREDENTIALS:

      export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service/account/key.json"

 -  **Start the Flask web application:**
      ```sh
        python app.py
-  Open your web browser and navigate to http://127.0.0.1:5000/.
-  Upload a document to be processed and view the results on the result page.

**File Structure**

COTTHETA-LLC/
│
├── Address.py                  
├── README.md                     
├── app.py                        
├── autocrop.py                  
├── autorotate.py                
├── bank_name.py                 
├── card_detect.py                
├── cropimage.py               
├── doc_text_detect.py           
├── human_detection.py           
├── human_detection2.py                               
├── main.py                                              
├── patternfile.py                
├── person name detect.py        
├── pp.py                       
├── regextest.py                
├── requirements.txt             
├── rotated_image.jpg                               
├── visionapi_testing.py        
├── sample_data/                
├── templates/                    
│   ├── index.html
│   ├── result.html
├── static/
│   ├── styles.css





# Project Overview

## Files and Modules

- **Address.py**: Identifies the type of address (street, city, zip, state) from the extracted text.
- **README.md**: Documentation file.
- **app.py**: Contains the Flask web application.
- **autocrop.py**: Contains the `crop_image` function for auto-cropping images.
- **autorotate.py**: Experimental file for auto-rotating documents.
- **bank_name.py**: Extracts relevant information from bank cards, including bank name.
- **card_detect.py**: Extracts relevant information from bank cards, such as card number, expiry date, CVV, and card type using regex patterns.
- **cropimage.py**: Uses OpenCV to find the largest rectangle or square bounding box in the image and crops that box to get the relevant part of the document.
- **doc_text_detect.py**: Detects and extracts text from documents, including multiple paragraphs and handwritten paragraphs, using the Google Cloud Vision API.
- **human_detection.py**: Detects human names using Google Natural Language Processing Toolkit.
- **human_detection2.py**: An alternate human detection script.
- **main.py**: Contains the main logic for the OCR system.
- **patternfile.py**: Contains a large set of regex patterns that match the extracted text.
- **person name detect.py**: Detects person names using patterns and models.
- **pp.py**: Bank data testing script.
- **regextest.py**: Tests regex patterns.
- **requirements.txt**: Lists the required Python packages.
- **visionapi_testing.py**: Google Vision API testing script.

## Directories

- **sample_data/**: Contains sample data files.
- **templates/**: Contains HTML templates for the web application.
  - **index.html**: Starting page of the web server.
  - **result.html**: Displays the OCR results.
  - **bank.html**:Displays the  bank card image uploadation page.
  - **doc.html**:Display the doc image uploadation page.
  - **table.html**: Display the table image uploadation page.
  - **resultbank.html**: Display the bankcard processed result.
  - **resulttable.html**:Display the option to download csv file for tabular data processed image.
  - **resultdoc.htmL**: Display he doc processed result.
  - 
- **static/**: Contains static files such as CSS for styling the web application.
  - **styles.css**: CSS file for styling the web application.
-**uploads/outputcsv**: Csv file generated from tabular data  is saved in outputcsv folder and  using its path url download option allow to download the file.


# Detailed Description

## app.py

The Flask application is designed to handle the upload and processing of various types of images, specifically ID cards, documents, bank details, and table images. It saves uploaded images in the 'uploads' directory, creating it if it doesn't exist, and stores output CSV files in 'uploads/outputcsv'. The application has several routes: the homepage ('/') renders the main index page; '/bank', '/doc', and '/table' render pages for uploading images of bank details, documents, and tables respectively. The '/uploadid' route handles ID card image uploads, saves the file, processes it with the main_file function, and renders the result on 'result.html'. The '/uploaddoc' route processes document images using detect_document_text and displays the result on 'resultdoc.html'. The '/uploadbank' route processes bank detail images using extract_info and shows the result on 'resultbank.html'. The '/uploadtable' route processes table images with extract_text_and_generate_csv, generates a CSV file, and provides a download link on 'resulttable.html'. The '/uploads/outputcsv/<filename>' route allows users to download the generated CSV files. This comprehensive setup enables the application to handle various image processing tasks and present the results to the user efficiently.

## main.py

The script processes an image to detect and extract text, specifically for use cases involving document analysis and identification. It starts by importing necessary modules and setting up the Google Cloud Vision API client with the required credentials. The main function main_file(image_path) reads the input image, optionally rotates it for correct orientation, and crops it to focus on the relevant region using the crop_image function. The image is then encoded to bytes and sent to the Google Cloud Vision API for text detection. The detected text is extracted, cleaned, and processed to remove unwanted characters and patterns.

The cleaned text is further analyzed to extract specific information such as person names using extract_person_names, address details using parse_address, and other license-related data using regex_detect. The script uses regular expressions extensively to clean the text and extract meaningful information. The extracted data, including names, address, and other fields, is stored in a dictionary license_data, which is then returned as the output. This function is designed to handle various text patterns and ensure accurate extraction of key details from the input image, making it useful for applications like license card detection and information extraction.

## patternfile.py

Contains a large set of regex patterns that match the extracted text. Each pattern checks whether the text is a required field or not. These patterns are imported and used in `main.py`.
This script defines a crop_image function that processes an input image to find and crop a specific region based on detected contours. The function first resizes the image and rotates it if necessary to ensure consistency. It converts the image to grayscale, applies Gaussian blur to reduce noise, and uses adaptive thresholding to create a binary image. Morphological operations enhance contours, which are then filtered based on area and aspect ratio to find significant contours. The function identifies the largest contour, crops the image to this contour, and returns the cropped image. If no contours are found, it returns the original image.

This script is set up to demonstrate the function with commented-out code for reading, processing, displaying, and saving images, but it’s not actively executing those steps.

## cropimage.py

Uses OpenCV to find the largest rectangle or square bounding box in the image and crops that box to get the relevant part of the document. This function is imported and used in `main.py`.

## address.py

Identifies the type of address (street, city, zip, state) from the extracted text. This module is imported and used in `main.py`.
This script uses the usaddress library to parse and extract address components from a given address string. It defines a function, parse_address, which takes an address string and parses it into various components such as building number, street, street type, direction, city, state, and zip code. The function constructs a full street address by combining the relevant components and returns a dictionary with all parsed elements. The script is set up to demonstrate how the function works with an example address, which is commented out but shows how to call the function and print the parsed results.

## human_detection.py

Detects human names using the Google Natural Language Processing Toolkit. This module is imported and used in `main.py`.
This script uses Google Cloud's Natural Language API to extract the most relevant person names from a given text. It initializes the API client, sends the text for entity analysis, and iterates through the detected entities to find those classified as persons. The script prioritizes names based on salience score and filters out irrelevant terms. If a person's name consists of more than three words, only the first three words are returned. The highest-salience person name is then returned.

## card_detect.py

Extracts relevant information from bank cards, such as card number, expiry date, CVV, and card type using regex patterns. This module is imported and used in `main.py`.

This script is designed to extract and analyze text from images of bank cards, utilizing both Google Cloud Vision API for OCR (Optical Character Recognition) and custom regular expressions to identify specific details. Here's an explanation of the script's key components and workflow:

  -Importing Libraries and Setting Up Environment: The script begins by importing necessary libraries such as os, re, cv2, pytesseract, and google.cloud.vision. It also sets the environment variable for Google Cloud credentials to authenticate the Vision API client.

  -Defining Regular Expressions: Several regular expressions are defined to match patterns typically found on bank cards, including card numbers, expiry dates, bank names, card types, and card holder names. These patterns allow for flexible matching, accounting for variations in spacing and case sensitivity.

  -Google Cloud Vision API Client Initialization: The Vision API client is initialized to perform OCR on the uploaded images.

  -Function to Extract Text Using Google Vision API: The extract_text_from_image function reads an image file, converts it to bytes, and sends it to the Google Vision API for text detection. It returns the detected text or raises an error if the API response contains an error message.

  -Function to Extract Information Using Regular Expressions: The extract_info function takes the detected text as input and applies the defined regular expressions to extract specific information, such as card numbers, expiry dates, bank names, card types, and card holder names. The analyze_entities function is used for a more comprehensive analysis of bank names.

  -Processing Uploaded Images: The script specifies a path to an image file and uses the above functions to extract text and then analyze it for specific information. The extracted details are printed to the console.

## bank_name.py

Detects bank names from the text using NLP models. This module is imported and used in `main.py`.
This script provides a function to extract bank names from a given text using Google Cloud's Natural Language API. It initializes clients for the Vision and Natural Language APIs and sets up the credentials environment variable. The analyze_entities function takes text as input, creates a document for entity analysis, and extracts entities identified as organizations (likely banks). It collects and returns these entities as bank names. The commented-out code provides an example of how to use the function but is not actively executed.

## document_detection.py

The Python script detect_document_text(image_path) uses Google Cloud Vision API to detect text in a document image. The script initializes the Vision client, reads the image file, and constructs a Vision Image object. It then performs document text detection using the document_text_detection method and prints the detected text if found. If no text is detected, it prints an appropriate message. The script also handles any errors returned by the API.

## pp.py

A testing script for bank data. This script is used to test the functionality of extracting and processing data from bank documents.

## visionapi_testing.py

A testing script for the Google Vision API. This script is used to test the capabilities and functionality of the Google Vision API in processing and extracting text from images.

## autorotate.py
The Python function auto_rotate(image) processes an image to ensure its width is greater than its height by rotating it if necessary. The function starts by checking the image dimensions and resizing it for consistency. It converts the image to grayscale, applies Gaussian blur to reduce noise, and uses adaptive thresholding to obtain a binary image. Morphological operations enhance contours, and contours are found using OpenCV's findContours method. Contours are filtered based on area, aspect ratio, and solidity to detect valid regions. The function then defines a nested function rotate_image_to_horizontal(image, rect) that rotates the image based on the minimum area rectangle around the largest detected contour. If no suitable contour is found, the entire image is used for rotation. The function finally returns the rotated image.

## Table_OCR.py
The Python script processes an image to detect text within table cells and generates a CSV file with the extracted text using OpenCV and Google Cloud Vision API. It sets up Google Cloud Vision API credentials and initializes the client, loads the image using OpenCV, and converts it to grayscale. Adaptive thresholding is applied to obtain a binary image where text and lines are white, and the background is black. Horizontal and vertical lines are detected using morphological operations, combined to create a mask representing the table grid. Contours of the grid cells are found using OpenCV's findContours method, and small contours are filtered out. For each detected cell, the corresponding image region is extracted, encoded to a byte array, and sent to Google Cloud Vision API for text detection. The detected text is extracted and stored along with the cell's coordinates. The extracted text data is sorted by the y-coordinate (row-wise) and then by the x-coordinate (column-wise) and written to a CSV file, with each row in the CSV representing a row in the table. The CSV file is saved in the outputcsv folder within the image's directory. The script can be run with an example image path to generate a CSV file containing the extracted text from the image's table cells, encapsulated in the function extract_text_and_generate_csv(image_path), which takes an image path as input and returns the path of the generated CSV file.

## Experimental files
- human_detection2.py : alternate method to detect human names used name parser library(python) to detect names.
- auto_rotate.py: to auto align the document in right position.Not works for all documents.
- pp.py: sample  file  to check bank_data  algorithm
- doc_text_detect2:  testing for  structured document data as present in file . but sometimes data  is very dioriented.

## Acknowledgements

Special thanks to Ashish K. Dash and Mallesham katnam from CotTheta LLC for mentoring and guidance throughout this project.

This updated README provides a comprehensive overview of your project, including installation instructions, usage, and detailed descriptions of each file's functionality, specifically highlighting the license and bank card recognition features, as well as the document detection capabilities, including handling multiple paragraphs and handwritten paragraphs using the Google Cloud Vision API. The additions also include descriptions for the testing scripts and the experimental auto-rotation script.
