
import os
import re
from google.cloud import vision
import cv2
import pytesseract as tes
import re
from PIL import Image
import os
import imquality.brisque as brisque
from skimage import io, img_as_float
from human_detection import extract_person_names
from bank_name import analyze_entities

# regex_patterns.py

# regex_patterns.py

# Pattern for card numbers (allowing spaces or hyphens between digits)
card_number_pattern = r'\b(?:\d[ -]*?){13,16}\b'

# Pattern for expiry dates
expiry_date_pattern = r'\b\d{2}/\d{2}\b'

# Expanded pattern for bank names with optional spaces and case insensitivity
bank_name_pattern = r'(?i)\b(?:my\s*best\s*buy|PSECU|OpenSky|Bank\s*of\s*America|Chase|Wells\s*Fargo|Citi|Capital\s*One|U\.S\.\s*Bank|Discover|American\s*Express|PNC|TD\s*Bank|BB&T|SunTrust|HSBC|Fifth\s*Third\s*Bank|Ally\s*Bank|Charles\s*Schwab|Regions|KeyBank|Huntington|Citizens\s*Bank|BMO\s*Harris|Synchrony\s*Bank|Barclays|Santander|M&T\s*Bank|First\s*National\s*Bank|First\s*Republic|Silicon\s*Valley\s*Bank|Signature\s*Bank|Comerica|USAA|New\s*York\s*Community\s*Bank|First\s*Citizens|Western\s*Alliance|City\s*National|Popular\s*Bank|CIBC|Zions|Bank\s*of\s*the\s*West|Associated\s*Bank|BOK\s*Financial|MidFirst\s*Bank|Pacific\s*Western\s*Bank|East\s*West\s*Bank|Valley\s*National\s*Bank|UMB\s*Financial|Cathay\s*Bank|First\s*Hawaiian\s*Bank|Webster\s*Bank|Wintrust\s*Financial|Simmons\s*Bank|BancorpSouth|South\s*State\s*Bank|Old\s*National\s*Bank|United\s*Bank|First\s*Interstate\s*Bank|Columbia\s*Bank|Flagstar\s*Bank|Seacoast\s*National\s*Bank|Commerce\s*Bank|Investors\s*Bank|Glacier\s*Bank|Independent\s*Bank|Banner\s*Bank|BancFirst|Peoples\s*United\s*Bank|Old\s*Second\s*Bank|Peapack-Gladstone\s*Bank|First\s*Midwest\s*Bank|Renasant\s*Bank|First\s*Merchants\s*Bank|NBT\s*Bank|Provident\s*Bank|Southside\s*Bank|OceanFirst\s*Bank|Trustmark\s*Bank|First\s*Horizon\s*Bank|FirstBank|United\s*Community\s*Bank|TIAA\s*Bank|BankUnited|First\s*Commonwealth\s*Bank|Great\s*Southern\s*Bank|Carter\s*Bank|Union\s*Bank|Midland\s*States\s*Bank|Hanmi\s*Bank|City\s*National\s*Bank|Ameris\s*Bank|Prosperity\s*Bank|Valley\s*Bank|Vantage\s*Bank|PlainsCapital\s*Bank|First\s*Foundation\s*Bank|Nicolet\s*National\s*Bank|BankFirst\s*Financial\s*Services|Veritex\s*Community\s*Bank|Columbia\s*State\s*Bank|Heartland\s*Bank|Bankers\s*Trust|Republic\s*Bank|Bryn\s*Mawr\s*Trust|IncredibleBank|Origin\s*Bank|MidwestOne\s*Bank|First\s*National\s*Bank\s*of\s*Omaha|First\s*State\s*Bank|First\s*Federal\s*Bank|Cadence\s*Bank|Central\s*Bank|Texas\s*Capital\s*Bank|Amerant\s*Bank|Third\s*Coast\s*Bank|Summit\s*State\s*Bank|Legacy\s*Texas\s*Bank|FNB\s*Community\s*Bank|Central\s*Pacific\s*Bank|Eastern\s*Bank|Liberty\s*Bank|Stockman\s*Bank|Pinnacle\s*Bank|Fidelity\s*Bank|Great\s*Western\s*Bank|Merchants\s*Bank|Union\s*Savings\s*Bank|Stearns\s*Bank|Intrust\s*Bank|National\s*Bank|Pacific\s*Premier\s*Bank|Zions\s*Bank|Farmers\s*State\s*Bank|Luther\s*Burbank\s*Savings|First\s*City\s*Bank|CNB\s*Bank|Citizens\s*National\s*Bank|HomeStreet\s*Bank|Amalgamated\s*Bank|Amalgamated\s*Bank)\b'

# Pattern for card types with optional spaces and case insensitivity
card_type_pattern = r'(?i)\b(?:VISA|Master\s*Card|MasterCard|Debit|Credit|American\s*Express|Discover|JCB|Diners\s*Club|Union\s*Pay)\b'

# Pattern for card holder names, excluding common phrases like "valid thru" or "good thru"
card_holder_name_pattern = r'\b(?!valid\s*thru|good\s*thru)[A-Z]{2,}(?:\s[A-Z]{2,})*\b'




os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './myservicegapi.json'
client = vision.ImageAnnotatorClient()

# Function to perform OCR using Google Vision API
def extract_text_from_image(image_path):
    with open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    if response.error.message:
        raise Exception(f'{response.error.message}')
    return texts[0].description if texts else ""

# Function to extract information using regex
def extract_info(text):
    info = {}

    # Extracting information
    info['Card Number'] = re.findall(card_number_pattern, text)
    info['Expiry Date'] = re.findall(expiry_date_pattern, text)
    # info['Bank Name'] = re.findall(bank_name_pattern, text)
    info['Bank Name'] = analyze_entities(text)
    info['Card Type'] = re.findall(card_type_pattern, text)
    info['Card Holder Name'] =extract_person_names(text) 

    return info

# Paths to the uploaded images
image_paths ='./Bank-Cards-Reader/card2.png'

# Extracting information from each image

text = extract_text_from_image(image_paths)
info = extract_info(text)
print(f"Information extracted from {image_paths}:")
print(info)
print("\n")