import re

# Sample text from the bank card
text ="barclaycard MasterCard Business 5476 7678 9876 5432 5476 01/14 VALID COMPANY NAME M STEPHENS THRU MONTH YEAR 01/18"

# Define the regex pattern
pattern = r"(?P<bank_name>BBVA)\s+(?P<card_type_description>BUSINESS)\s+(?P<card_number>\d{4} \d{4} \d{4} \d{4})\s+GOOD THRU\s+(?P<expiry_date>\d{2}/\d{2})\s+(?P<cardholder_name>[A-Z ]+)\s+(?P<card_type>DEBIT)\s+(?P<card_logo>VISA)"

# Perform the regex search
match = re.search(pattern, text)

# Check if a match was found
if match:
    # Extract and print the captured groups
    bank_name = match.group("bank_name")
    card_type_description = match.group("card_type_description")
    card_number = match.group("card_number")
    expiry_date = match.group("expiry_date")
    cardholder_name = match.group("cardholder_name")
    card_type = match.group("card_type")
    card_logo = match.group("card_logo")
    
    print(f"Bank Name: {bank_name}")
    print(f"Card Type Description: {card_type_description}")
    print(f"Card Number: {card_number}")
    print(f"Expiry Date: {expiry_date}")
    print(f"Cardholder Name: {cardholder_name}")
    print(f"Card Type: {card_type}")
    print(f"Card Logo: {card_logo}")
else:
    print("No match found.")
