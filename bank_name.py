
import os
import re
from google.cloud import vision
from google.cloud import language_v1
# from google.cloud.language_v1 import enums
vision_client = vision.ImageAnnotatorClient()
nlp_client = language_v1.LanguageServiceClient()

# Set Google Cloud credentials environment variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'myservicegapi.json'

def analyze_entities(text):
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    response = nlp_client.analyze_entities(document=document, encoding_type='UTF8')
    
    entities = response.entities
    bank_names = []
    for entity in entities:
        if language_v1.Entity.Type(entity.type_).name == "ORGANIZATION":
            bank_names.append(entity.name)
    return bank_names

# # Example usage
# text = "KEIRA CHRISTINA KNIGHTLEY 10405 SW 112TH ST MIAMI was the 44th president of the United States. Elon Musk founded SpaceX and co-founded Tesla. John Doe the Driver was on duty. Jane Alice Smith Brown is a scientist."
# # person_name = extract_person_names(text)

# print("Person with highest salience score:", person_name)
