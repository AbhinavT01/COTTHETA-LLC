from google.cloud import language_v1
import os

# Set Google Cloud credentials environment variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'myservicegapi.json'

def extract_person_names(text):
    client = language_v1.LanguageServiceClient()

    document = language_v1.Document(
        content=text,
        type_=language_v1.Document.Type.PLAIN_TEXT
    )

    response = client.analyze_entities(document=document)

    person_names = "any_name"
    salience_score = 0

    # Iterate through entities and extract person names
    for entity in response.entities:
        if language_v1.Entity.Type(entity.type_) == language_v1.Entity.Type.PERSON:
            # Check if the entity name is not 'DRIVER' or 'SAFE' and has a higher salience score
            if entity.salience > salience_score and entity.name.lower() not in ['driver', 'safe']:
                name_words = entity.name.split()
                # Check if the name has more than three words
                if len(name_words) > 3:
                    # Truncate the name to the first three words
                    truncated_name = ' '.join(name_words[:3])
                    person_names = truncated_name
                elif len(name_words)>1:
                    person_names = entity.name


                salience_score = entity.salience
                

    return person_names

# # Example usage
# text = "KEIRA CHRISTINA KNIGHTLEY 10405 SW 112TH ST MIAMI was the 44th president of the United States. Elon Musk founded SpaceX and co-founded Tesla. John Doe the Driver was on duty. Jane Alice Smith Brown is a scientist."
# # person_name = extract_person_names(text)

# print("Person with highest salience score:", person_name)
