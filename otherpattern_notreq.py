patterns = {
 'Name': (
    r'(?i)'  # Case insensitive
    r'\b(?=[A-Za-z\'"\s]{6,}\b)'  # Ensure at least 6 characters without digits
    r'(?<!\d)(\d*?[A-Za-z\'"\s]{3,})\s+([A-Za-z\'"\s]{3,}\d*?)(?!\d)\b'  # Match two words with at least 3 characters each, excluding digits
    r'|'  # OR
    r'\b(\d*?[A-Za-z\'"\s]{3,})\s*([A-Za-z\'"\s]{3,}\d*?)\d*\b'  # Match two words with at least 3 characters each, allowing optional digits before and after
)
,  # Pattern for name
  # Pattern for name
    'State and ZIP': r"(?i)\bFL\s+\d{5}\b",  # Pattern for state and ZIP code
    'DOB': (
    r'(?i)'  # Case insensitive
    r'(?:D[O0][B8]?)\.?:?\s*'  # Matches DOB, D0B, D8B, D.O.B, etc., with optional colon and spaces
    r'('
    r'\d{2}[-/.\s]{0,3}\d{2}[-/.\s]{0,3}\d{2,4}|'  # Matches dates like 12/31/2024, 12-31-24, 12.31-2024, etc.
    r'\d{4}[-/.\s]{0,3}\d{2}[-/.\s]{0,3}\d{2}|'  # Matches ISO dates like 2024-12-31
    r'\d{2}[-/.\s]{0,3}(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-/.\s]{0,3}\d{2,4}|'  # Matches dates like 31 Dec 2024, 31-Dec-24, etc.
    r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-/.\s]{0,3}\d{2}[-/.\s]{0,3},?[-/.\s]{0,3}\d{2,4}'  # Matches dates like Dec 31, 2024, Dec-31-24, etc.
    r')'
    r'|'  # Separator for variations
    r'(?:D\.O\.B)\b'  # Matches "D.O.B" as a separate word
    r'|'  # Separator for variations
    r'(?:DOB)',  # Matches "DOB" as a separate word (non-capturing)
),  # Pattern for date of birth
 # Pattern for date of birth
'Street Address': (
    r'(?i)'  # Case insensitive
    r'\b(?:(?!direct\s+address)\b[\w\s.-]+\b)\b'  # Match any word characters, spaces, dots, or hyphens, excluding "direct address"
    r'|'  # Separator for variations
    r'\b(?:Address)\b'  # Matches "Address" as a separate word
    r'|'  # Separator for variations
    r'\d+\s+'  # Matches digits followed by whitespace
    r'(?:[A-Za-z]+\s+)?'  # Matches optional directional prefixes (e.g., NW, SE)
    r'(?:[\w\.\s-]+)\s+'  # Matches any word characters, dots, spaces, or hyphens followed by whitespace
    r'(?:st|street|ave|avenue|rd|road|blvd|boulevard|dr|drive|ln|lane|ct|court|cir|circle|pkwy|parkway|hwy|highway|pl|place|ter|terrace|plz|plaza|way|route|rte|run|cres|crescent|trl|trail|cswy|causeway|row|alley|mnr|manor|sq|square|pass|crossing|park|garden|grn|green|walk|walkway|wharf|track|turn|viaduct|vista|gln|glen|crk|creek|ridge|mews|jct|junction|fwy|freeway|expwy|expressway|plaza|plz|cir|circle|cross|creek|pike|pine|pinelnd|way|ter|terr|terrace|trail|walk|wal|wall|water|way|wds|wood|woods)\b'  # Matches common street suffixes
),  # Pattern for street address


    'City': r"(?i)^(?:miami|orlando|tampa|jacksonville|tallahassee|st\.?\s?petersburg|fort\s?lauderdale|sarasota|gainesville|pensacola|naples|boca\s?raton|palm\s?beach|hialeah|hollywood|key\s?west|clearwater|daytona\s?beach|lakeland|ocala|melbourne|fort\s?myers|coral\s?gables|cape\s?coral)",  # Pattern for city
    'Issue Date':(
    r'(?i)'  # Case insensitive
    r'(?:ISSU[EA]D|ISS)[:;\s]*'  # Handles ISSUED, ISSUE DATE, ISSUED, ISS with optional colon and spaces
    r'('
    r'(\d{2}[-/.\s]{0,3}\d{2}[-/.\s]{0,3}\d{2,4})|'  # Matches dates like 12/31/2024, 12-31-24, 12.31.2024, etc.
    r'(\d{4}[-/.\s]{0,3}\d{2}[-/.\s]{0,3}\d{2})|'  # Matches ISO dates like 2024-12-31
    r'(\d{2}[-/.\s]{0,3}(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-/.\s]{0,3}\d{2,4})|'  # Matches dates like 31 Dec 2024, 31-Dec-24, etc.
    r'((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-/.\s]{0,3}\d{2}[-/.\s]{0,3},?[-/.\s]{0,3}\d{2,4})'  # Matches dates like Dec 31, 2024, Dec-31-24, etc.
    r')'
)
,  # Pattern for issue date
   'Expiry Date': (
    r'(?i)(?:4b\s)?'
    r'(?:EXP(?:IR(?:ES|Y DATE)?|IRY DATE|IRE[SD])?)[:\s]*'
    r'('
    r'(\d{2}[-/.\s]{0,3}\d{2}[-/.\s]{0,3}\d{2,4})|'  # Matches dates like 12/31/2024, 12-31-24, 12.31.2024, etc.
    r'(\d{4}[-/.\s]{0,3}\d{2}[-/.\s]{0,3}\d{2})|'  # Matches ISO dates like 2024-12-31
    r'(\d{2}[-/.\s]{0,3}(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-/.\s]{0,3}\d{2,4})|'  # Matches dates like 31 Dec 2024, 31-Dec-24, etc.
    r'((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-/.\s]{0,3}\d{2}[-/.\s]{0,3},?[-/.\s]{0,3}\d{2,4})'  # Matches dates like Dec 31, 2024, Dec-31-24, etc.
    r')'
),  # Pattern for expiry date

  # Pattern for expiry date
    'Sex': r'(?i)\bSEX\b\s*[:\s]*(?:M(?:ALE)?|F(?:EMALE)?)',  # Pattern for sex
    'Height':(
    r'(?i)'  # Case insensitive
    r'(H(?:GT|EIGHT)?)[:\s]*'  # Handles HGT, HEIGHT, with optional colon and spaces
    r'('
    r'(\d+)[\'\"]\s*(?:[.-]?)\s*(\d+)?'  # Matches heights like 4'-07, 4' .07, etc.
    r'|'
    r'(\d{1,2})[-.\s]*([1-9]|1[0-2])\s*(?:ft|feet|foot|\'\')?'  # Matches heights like 5-10 ft, 6.2 feet, etc.
    r'|'
    r'(\d{1,2})[-.\s]*(\d{1,2})\s*(?:in|inch|"|\'\')?'  # Matches heights like 5-10 in, 6.2 inches, etc.
    r'|'
    r'(\d{1,2})\'\s*-\s*(\d{1,2})\"'  # Matches heights like 4' - 07", etc.
    r')'
),  # Pattern for height
    'Weight': (
    r'(?i)'  # Case insensitive
    r'(W(?:T|EIGHT|G)?)\s*[:\s]*'  # Handles WT, WEIGHT, WGT, with optional colon and spaces
    r'('
    r'(\d{1,3}(?:\.\d{1,2})?)\s*([lI1*o0]bs|kg)|'  # Matches weights like 150 lbs, 72.5 kg, etc.
    r'(\d{1,3}(?:\.\d{1,2})?)\s*(?:[lI1*o0]bs|kg)?'  # Matches weights like 150, 72.5, etc., with flexible matching for "lbs"
    r')'
    r'|'  # Separator for variations
    r'(WGT?)\s*[:\s]*(\d{1,3}(?:\.\d{1,2})?)\s*([lI1*o0]bs|kg)?'  # Handles variations like WGT: 150 lbs, WGT: 72.5 kg, etc.
),  # Pattern for weight
    'License Number': (
    r'(?i)(?:\b(?:DL|DL\sNO\.?|DLN|DIN|AIN|No\.?|N0\.|Lic\.\sNo\.)\b\s*)?[A-Z]\d{3}-\d{3}-\d{2}-\d{3}-\d{1}'
    r'|'
    r'(?:4d\s)?\b[A-Z]\d{3}-\d{4}-\d{4}\b'  # Matches license numbers like P142-4558-7924
    r'|'
    r'\b\d{9}\b'  # Matches 9-digit numbers
),  # Pattern for license number
# Pattern for license number
  # Pattern for license number
    'Class': (
    r'(?:CLASSIFICATION)\b\s*'  # Non-capturing match for "Classification"
    r'|'  # Separator for variations
    r'(?i)'  # Case insensitive
    r'(?:CLASS)\s*\s*([A-Z0-9]+|CHILD)'  # Matches any combination of uppercase letters and digits, or "CHILD" after "CLASS" with optional spacing
),  # Pattern for class
  # Pattern for class
    'Rest': r'(?i)REST:?\s*([A-Z]+)',  # Pattern for restrictions
    'Replaced': (
    r'(?i)'  # Case insensitive
    r'(REPLAC[EA]D)[:\s]*'  # Handles REPLACED, REPLACE DATE, REPLACD, etc., with optional colon and spaces
    r'('
    r'(\d{2}[-/.\s]{0,3}\d{2}[-/.\s]{0,3}\d{2,4})|'  # Matches dates like 12/31/2024, 12-31-24, 12.31.2024, etc.
    r'(\d{4}[-/.\s]{0,3}\d{2}[-/.\s]{0,3}\d{2})|'  # Matches ISO dates like 2024-12-31
    r'(\d{2}[-/.\s]{0,3}(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-/.\s]{0,3}\d{2,4})|'  # Matches dates like 31 Dec 2024, 31-Dec-24, etc.
    r'((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-/.\s]{0,3}\d{2}[-/.\s]{0,3},?[-/.\s]{0,3}\d{2,4})'  # Matches dates like Dec 31, 2024, Dec-31-24, etc.
    r')'
)
,  # Pattern for replaced date with variations  # Pattern for name + date of birth
  # Pattern for expiry date
     'Sex': r'(?i)\bSEX\b\s*[:\s]*(?:M(?:ALE)?|F(?:EMALE)?)',  # Pattern for sex
    'Height':(
    r'(?i)'  # Case insensitive
    r'(H(?:[GT]|EIGHT)?)[:\s]*'  # Handles HGT, HEIGHT, with optional colon and spaces
    r'('
    r'(\d+)[\'\"]\s*(?:[.-]?)\s*(\d+)?'  # Matches heights like 4'-07, 4' .07, etc.
    r'|'
    r'(\d{1,2})[-.\s]*([1-9]|1[0-2])\s*(?:ft|feet|foot|\'\')?'  # Matches heights like 5-10 ft, 6.2 feet, etc.
    r'|'
    r'(\d{1,2})[-.\s]*(\d{1,2})\s*(?:in|inch|"|\'\')?'  # Matches heights like 5-10 in, 6.2 inches, etc.
    r'|'
    r'(\d{1,2})\'\s*-\s*(\d{1,2})\"'  # Matches heights like 4' - 07", etc.
    r')'
),  # Pattern for height
    'Weight': (
    r'(?i)'  # Case insensitive
    r'(W(?:T|EIGHT|G)?)\s*[:\s]*'  # Handles WT, WEIGHT, WGT, with optional colon and spaces
    r'('
    r'(\d{1,3}(?:\.\d{1,2})?)\s*([lI1*o0]bs|kg)|'  # Matches weights like 150 lbs, 72.5 kg, etc.
    r'(\d{1,3}(?:\.\d{1,2})?)\s*(?:[lI1*o0]bs|kg)?'  # Matches weights like 150, 72.5, etc., with flexible matching for "lbs"
    r')'
    r'|'  # Separator for variations
    r'(WGT?)\s*[:\s]*(\d{1,3}(?:\.\d{1,2})?)\s*([lI1*o0]bs|kg)?'  # Handles variations like WGT: 150 lbs, WGT: 72.5 kg, etc.
),  # Pattern for weight
    'License Number': r'(?i)(?:\b(?:DLN|DIN|AIN)\b\s*)?[A-Z]\d{3}-\d{3}-\d{2}-\d{3}-\d{1}',  # Pattern for license number
    'Class': (
    r'(?i)'  # Case insensitive
    r'CLASS\s*\s*([A-Z0-9]+|CHILD)'  # Matches any combination of uppercase letters and digits, or "CHILD" after "CLASS" with optional spacing
),  # Pattern for class
    'Rest': r'(?i)REST:?\s*([A-Z]+)',  # Pattern for restrictions
    'Replaced': (
    r'(?i)'  # Case insensitive
    r'(REPLAC[EA]D)[:\s]*'  # Handles REPLACED, REPLACE DATE, REPLACD, etc., with optional colon and spaces
    r'('
    r'(\d{2}[-/.\s]{0,3}\d{2}[-/.\s]{0,3}\d{2,4})|'  # Matches dates like 12/31/2024, 12-31-24, 12.31.2024, etc.
    r'(\d{4}[-/.\s]{0,3}\d{2}[-/.\s]{0,3}\d{2})|'  # Matches ISO dates like 2024-12-31
    r'(\d{2}[-/.\s]{0,3}(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-/.\s]{0,3}\d{2,4})|'  # Matches dates like 31 Dec 2024, 31-Dec-24, etc.
    r'((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-/.\s]{0,3}\d{2}[-/.\s]{0,3},?[-/.\s]{0,3}\d{2,4})'  # Matches dates like Dec 31, 2024, Dec-31-24, etc.
    r')'
)
 # Pattern for replaced date with variations
    # 'NameDOB': r'(?i)^[A-Z]+\s[A-Z]+\s[A-Z]+(?<!\s)(?:DOB|D[O0][B8]):?\s*(\d{2}[-.]\d{2}[-.]\d{4})',  # Pattern for name + date of birth
}
