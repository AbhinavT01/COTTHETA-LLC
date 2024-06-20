
import re
from google.cloud import vision
import os
from regextest import regex_detect
from human_detection import extract_person_names
from human_detection2 import extract_person_names1
from Address import parse_address
# Set Google Cloud credentials environment variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'myservicegapi.json'
# from visionapi import detect_text
import cv2
from patternfile import patterns
from cropimage import crop_image
import os
# import numpy as np
# from PIL import Image

# Initialize easyocr reader
# reader = easyocr.Reader(['en'],gpu=True)

def main_file(image_path):

    image = cv2.imread(image_path)
    # image = auto_rotate(image)

    # cv2.imshow("rotae",image)

    image = crop_image(image)
    # Convert image to bytes
    _, buffer = cv2.imencode('.jpg', image)
    content = buffer.tobytes()

    client = vision.ImageAnnotatorClient()

    image = vision.Image(content=content)

    # Perform text detection
    response = client.text_detection(image=image)
    texts = response.text_annotations
    # Store detected text as a single string
    detected_text = texts[0].description.strip()

    # Split the detected text into lines
    descriptions = detected_text.split('\n')
  
    words = []
    detected_value = ''
    for text in texts:
        if text.description not in words:
            words.append(text.description)

    # Join all words into a single string
    for each in descriptions:
        detected_value  = detected_value + " "+each
# jjjjjjjjjjjjjjfsaldhkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk//////////////////////////////////////////////////
    clean_text = ''
    
    # Remove leading and trailing whitespace
    
    print('detecetvelaue',detected_value)
    print('\n')
    # Remove leading and trailing whitespace
    cleaned_text = detected_value.strip()
    
    # Remove newline characters
    # Remove newline characters
    
    
    # Remove newline characters
    cleaned_text = cleaned_text.replace('\n', ' ')

    # Remove double numbers with both sides having spaces
    cleaned_text = re.sub(r'(?<=\s)\d{2}\s\d{2}(?=\s)', '', cleaned_text)
    
    # Remove single digits surrounded by spaces or non-space characters with length not equal to one
    cleaned_text = re.sub(r'(?<!\S)\d(?!\S)|(?<!\S)\d{1}(?!\S)', '', cleaned_text)
    
    # Remove single words with one digit and one small alphabetic character with spacing on both sides
    cleaned_text = re.sub(r'(?<=\s)[a-z]\d\s(?=\s)|(?<=\s)\d[a-z]\s(?=\s)', '', cleaned_text)
    
    # Remove two-letter words consisting of digits with spacing on both sides
    cleaned_text = re.sub(r'(?<=\s)\d{2}\s(?=\s)|(?<=\s)\s\d{2}(?=\s)', '', cleaned_text)
    
    # Remove "4a" and "4b" from the text
    cleaned_text = re.sub(r'\b(?:4a|4b)\b', '', cleaned_text)
    
    # Transform the digit 1 to the letter I if it is between two alphabetical characters
    cleaned_text = re.sub(r'(?<=[a-zA-Z])1(?=[a-zA-Z])', 'I', cleaned_text)
    
    # Remove non-alphanumeric characters except spaces, slashes, hyphens, colons, periods, quotes, and hashtags
    cleaned_text = re.sub(r'[^\w\s/:,\-\'".#]', '', cleaned_text)
    
    # Remove extra spaces
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    # Ignore sequences starting with "DD" followed by a long number sequence larger than 10 characters
    cleaned_text = re.sub(r'\bDD\d{10,}\b', '', cleaned_text)

    # Remove texts like "4a" or "a4" with spacing on both sides
    cleaned_text = re.sub(r'(?<=\s)(?:4[a-z]|[a-z]4)(?=\s)', '', cleaned_text, flags=re.IGNORECASE)
    
    
    
    

    print('CLEANEDTEXT',cleaned_text)
    print('\n')
    print("descriptions",descriptions)
    print('\n')
    persons = extract_person_names(cleaned_text)
    print(persons)
    address = parse_address(cleaned_text)
    license_data = regex_detect(cleaned_text)
    # print(address)
    # print(persons)
    # Load the image
    # image_path = './uploads/corrected_image.jpg'  # Replace with your image path
    n = len(descriptions)
    # for i in range(n-1):
    #     license_data['All Text'].append(descriptions[i])
    #     arr =descriptions[i]+" "+descriptions[i+1]
    #     descriptions.append(arr)
    #     arr ="" 
    # Initialize a dictionary to store the data
    # Define patterns for extracting information
    params = ['Name','State and ZIP','DOB','Street Address','City','Issue Date','Expiry Date','Sex','Height','Weight','License Number',
                                                                  'Class','Rest','Replaced']
    # Process the extracted detected_text
    # Process each text string in the array
    # for text in descriptions:
    #     # Process the text with spaCy NER
    #     doc = nlp(text)
        # Extract person names from named entities
        # for ent in doc.ents:
        #     if ent.label_ == 'PERSON':
        #         # Append the recognized person name to the list
        #         names.append(ent.text.strip())
    # print(names)
   
    # for line in descriptions:
    #     matched = False
        # for key, pattern in patterns.items():
        #     match = re.search(pattern, line)
        #     if match :
        #         license_data[key] = match.group(1) 
        #         matched = True
    print(address)
    # match =  re.search(r'(?:\D*\d){3}',address['street_full'])
    # if match and len(match.groups())>1:license_data['Street Address'] =match.group(1)
    
    license_data['Name'] = persons
    license_data['Street Address']=address['street_full']
    license_data['City']=address['city']
    license_data['State and ZIP']  = address['state']+" "+address['zip_code']

    # match =  re.search( ( r'^(?!.*\b(?:\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})\b).*$',     re.IGNORECASE)
    #                    ,address['zip_code'])

    # if match and len(match.groups())>1:license_data['State and ZIP'] =match.group(1)
    
    license_data['All Text']= detected_value
    # Output the extracted data
    print(license_data,'\n')
    return license_data
# imgpath='./sample data/idcad8.jpg'
# img = main_file(imgpath)
