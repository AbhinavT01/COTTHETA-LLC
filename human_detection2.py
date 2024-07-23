 from nameparser import HumanName

# Function to parse a person's name and return as a single full name without suffix and prefix
def extract_person_names1(name_string):
    parsed_name = HumanName(name_string)
    name_parts = [parsed_name.first, parsed_name.middle, parsed_name.last]
    full_name = " ".join(part for part in name_parts if part)
    return full_name

# Example name string
# name_string = "Dr. John Q. Public III, Ph.D."

# # Parse the name string and get the full name without suffix and prefix
# full_name = parse_person_name(name_string)

# # Print the full name without suffix and prefix
# print("Full Name (without suffix and prefix):", full_name)

