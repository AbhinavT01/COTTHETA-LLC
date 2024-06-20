import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
from autocorrect import Speller
import spacy


# Download NLTK resources (if not already downloaded)
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Process text
texts = ['Florida', 'Snzaaline Stut e', 'DRIVER LICENSE CLASS E', 'L252-783-49-172-0', 'Angelina Jolie', 'LICENSE', '2900 APALACHEE PKWY', 'TALLAHASSEE FL 32399-6552', 'DOB: 05-12-1949', 'SEX:M', 'ISSUED 12-22-2006 HGT 6-10', 'EXPIRES: 05-12-2012', 'rest', 'EndoRSE:', 
        'Sjmaks', 'replaceD  01-04-2010', 'SAFE DRIER', 'Opotation 0i & Inolor Vbhe( constkines consetl (O',
          'MIy ~obrlaty Iert roquired by Lan;'] 






# for line in text:
#     textvalue = textvalue + " "+line
#     # Initialize the spell checker
spell_checker = Speller(lang='en')

# Example text with spelling errors


# Perform spell checking and correction
# corrected_text = spell_checker(textvalue)

# Print the corrected text

# print("Original Text:", textvalue)
# print("Corrected Text:", corrected_text)

# ////////////////////////////////////////////////////
# from textblob import TextBlob



# # Create a TextBlob object
# blob = TextBlob(corrected_text)

# # Perform spell correction
# corrected_text = blob.correct()

# # Print the original and corrected text
# print("Original Text:", textvalue)
# print("Corrected Text:", corrected_text)



# Initialize an empty list to store names
names = []

# Loop over each text string in the array

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Sample array of text strings

# Initialize an empty list to store names
names = []

# Process each text string in the array
for text in texts:
    # Process the text with spaCy NER
    doc = nlp(text)
    
    # Extract person names from named entities
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            # Append the recognized person name to the list
            names.append(ent.text.strip())

print(names)

for line in  names:
    # blob = TextBlob(line)
    print( spell_checker(line))
