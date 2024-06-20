import re
from patternfile import patterns
# Sample text for testing
# Pattern with non-capturing group for 'SEX' and capturing group for 'M', 'MALE', 'F', 'FEMALE'
# Find all matches in the text
license_data = {
        'Name': '',
        'DOB': '',
        'Issue Date': '',
        'Expiry Date': '',
        'Sex': '',
        'Height': '',
        'Weight': '',
        'License Number': '',
        'Class': '',
        'Rest': '',
        'Replaced': '',
        'Street Address':'',
        'City':'',
        'Full Address':'',
        'State and ZIP':'',  
        'All Text': ''
    }
# # text = "SEX: M  SEX : F  SEX : FEMALE"
# for key in pattern:
# # Pattern to find all matches
#     patterns= re.compile(pattern[key])

#     # Find all matches in the text
#     matches = patterns.finditer(text)

#     matfound = []
#     # Print all matches
#     for match in matches:
#        matfound.append(match.group(1))
#        break
# print(matfound)


# for key in pattern:
#     # Search for matches in the text using the pattern
#     patterns = pattern[key]
#     print(patterns)
#     print('\n')
#     patterns= re.compile(patterns)
#     matches = patterns.finditer(text)
#     for match in matches:
#         # Update the corresponding value in the license_date dictionary
#          print(match.group(1))

# # Print the updated license_data dictionary

# # print(license_data)
# # Display the captured groupsprint(text)
# for pattern_name, pattern_code in pattern.items():
#     # Search for the pattern in the text
#     for value in test:
#         matches = re.findall(pattern_code, value)

#         # Print the matches
#         if matches:
#             print(f'Matches found for {pattern_name}:')
#             for match in matches:
#                 print(match)
#                 print('\n')
        

# def regex_detect(test):
#     for line in test:

#             for key, pattern_type in patterns.items():
#                 matches = re.search(pattern_type,line)
#                 if matches :
                   
                    
#                     #  print(f'Matches found for {key}:')
#                     if matches.group(1)!=None:
#                      license_data[key] += matches.group(1)
#                     #  print(matches.group(1))
#     return  license_data
# 

# 

def regex_detect(test):
   

    for key, pattern_type in patterns.items():
        matches = re.search(pattern_type,test)
        if matches :
                   
                    
                    #  print(f'Matches found for {key}:')
            if matches.group(1)!=None:
                     license_data[key] = matches.group(1)
                    #  print(matches.group(1))
    return  license_data 

# test = ' DISTRICT OF COLUMBIA DRIVER LICENSE 4d.DLN 1234567 1.FAMILY NAME SAMPLECARD 2.GIVEN NAMES THOMAS ALEXANDER 8.ADDRESS 4b.EXP 02/21/2021 (8 DL USA 1234 COMMODORE JOSHUA BARNEY DRIVE, NE #1234 WASHINGTON, DC 00000-0000 1234567 02211984 15.SEX 16.HGT 17.WGT 18.EYES M 6-04 200 BRO 3.DOB 02/21/1984 9.CLASS 4a.ISS 12/03/2013 TA SAMPLECARD D 9a.ENDORSEMENTS Thomas Samplecard NONE 5.DD 12.RESTRICTIONS 12348757475974 1 DONOR VETERAN'

# licenses = regex_detect(test)
# print(licenses)









# 



# test = ['The', 'Florida shine State',
#          'DRIVER LICENSE CLASS E', 'W426-545-30-761-0', 'JOSEPH A', 'SAMPLE', '3456 SOMEWHERE AVE', 'TALLAHASSEE, FL 32399', 'DOB: 08-16-1980 SEX: M', 'Joe Sample', 'ORGAN DONOR', 'ADA', 'ISSUED: 08-16-2003 HGT: 5-08', 'EXPIRES: 08-16-2007', 'REST: BF', 'ENDORSE: X', 'V', 'REPLACED: 08-16-2003', 'SAFE DRIVER', 'MOTORCYCLE ONLY'
#         , '943.0435, F.S.', 'Operation of a motor vehicle constitutes consent to any sobriety test required by law.']
# print(regex_detect(test))
# print(license_data)
