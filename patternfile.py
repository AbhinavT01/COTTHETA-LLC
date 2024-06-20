patterns= {
   # Pattern for name
  # Pattern for name
    'DOB': (
    r'(?i)'  # Case insensitive
    r'(?:D\.?O\.?B\.?|D[0O]B|Date\s*of\s*Birth)\s*[:\s]*'  # Matches D.O.B, DOB, Date of Birth with optional colon and spaces
    r'('
    r'\d{2}[-/.\s]{0,3}\d{2}[-/.\s]{0,3}\d{2,4}|'  # Matches dates like 12/31/2024, 12-31-24, 12.31-2024, etc.
    r'\d{4}[-/.\s]{0,3}\d{2}[-/.\s]{0,3}\d{2}|'  # Matches ISO dates like 2024-12-31
    r'\d{2}[-/.\s]{0,3}(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-/.\s]{0,3}\d{2,4}|'  # Matches dates like 31 Dec 2024, 31-Dec-24, etc.
    r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-/.\s]{0,3}\d{2}[-/.\s]{0,3},?[-/.\s]{0,3}\d{2,4}'  # Matches dates like Dec 31, 2024, Dec-31-24, etc.
    r')'
),  # Pattern for date of birth
 # Pattern for date of birth
 # Pattern for street address
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
'Issue Date':(
    r'(?i)'  # Case insensitive
    r'(?:ISSU[EA]D|ISS)[:;\s]*'  # Handles ISSUED, ISSUE DATE, ISSUED, ISS with optional colon and spaces
    r'('
    r'(\d{2}[-/.\s]{0,3}\d{2}[-/.\s]{0,3}\d{2,4})|'  # Matches dates like 12/31/2024, 12-31-24, 12.31.2024, etc.
    r'(\d{4}[-/.\s]{0,3}\d{2}[-/.\s]{0,3}\d{2})|'  # Matches ISO dates like 2024-12-31
    r'(\d{2}[-/.\s]{0,3}(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-/.\s]{0,3}\d{2,4})|'  # Matches dates like 31 Dec 2024, 31-Dec-24, etc.
    r'((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-/.\s]{0,3}\d{2}[-/.\s]{0,3},?[-/.\s]{0,3}\d{2,4})'  # Matches dates like Dec 31, 2024, Dec-31-24, etc.
    r')'
),
 'Street Address': (
    r'(?i)'  # Case insensitive
    r'^\d+\s+'  # Matches digits followed by whitespace
    r'(?!safe\s+dr)'  # Excludes "safe dr"
    r'(?:[\w\.\s-]+)\s+'  # Matches any word characters, dots, spaces, or hyphens followed by whitespace
    r'(?:st\s*|street\s*|ave\s*|avenue\s*|rd\s*|road\s*|blvd\s*|boulevard\s*|dr\s*|drive\s*|ln\s*|lane\s*|ct\s*|court\s*|cir\s*|circle\s*|pkwy\s*|parkway\s*|hwy\s*|highway\s*|pl\s*|place\s*|ter\s*|terrace\s*|plz\s*|plaza\s*|way\s*|route\s*|rte\s*|ln\s*|lane\s*|run\s*|cres\s*|crescent\s*|trl\s*|trail\s*|cswy\s*|causeway\s*|row\s*|alley\s*|mnr\s*|manor\s*|sq\s*|square\s*|pass\s*|crossing\s*|park\s*|garden\s*|grn\s*|green\s*|walk\s*|walkway\s*|wharf\s*|track\s*|track\s*|turn\s*|tun\s*|viaduct\s*|vista\s*|gln\s*|glen\s*|crk\s*|creek\s*|ridge\s*|mews\s*|jct\s*|junction\s*|fwy\s*|freeway\s*|expwy\s*|expressway\s*|plaza\s*|plz\s*|cir\s*|circle\s*|cross\s*|creek\s*|park\s*|parks\s*|pike\s*|pine\s*|pinelnd\s*|way\s*|ter\s*|terr\s*|terrace\s*|trail\s*|walk\s*|wal\s*|wall\s*|water\s*|way\s*|wds\s*|wood\s*|woods\s*)'  # Matches common street suffixes
    r'\.?'  # Matches optional period at the end
),
  # Pattern for expiry date
    'Sex':r'(?i)\b(?:SEX)\b\s*[:\s]*(M(?:ALE)?|F(?:EMALE)?)'

,  # Pattern for sex
    'Height': (
    r'(?i)\b'  # Word boundary to ensure the match is standalone
    r'('
    r'(\d{1,2})\'\s*-\s*(\d{1,2})\"|'  # Matches heights like 5'-04"
    r'(\d+)\s*(?:cm)|'  # Matches heights in centimeters like 15cm
    r'(\d+)\s*(?:inches?)' 
    r"'(\d{1,2})\s*in\s*'" # Matches heights in inches like 12in or 12inches
    r')'
),
  # Pattern for height
   'Weight':  r'(?i)'  # Case insensitive
    r'(\d{1,3}(?:\.\d{1,2})?\s*(?:kg|lbs?|pounds?))'
,

  # Pattern for weight

  # Pattern for license number
# Pattern for license number
  # Pattern for license number
   'Class': (
    r'(?:CLASSIFICATION)\b\s*'  # Non-capturing match for "Classification"
    r'|'  # Separator for variations
    r'(?i)'  # Case insensitive
    r'(?:CLASS)\s*\s*([A-Z0-9]+|CHILD)'  # Matches any combination of uppercase letters and digits, or "CHILD" after "CLASS" with optional spacing
),   # Pattern for class
    'Rest': (
   r'(?i)'
    r'(?:REST(?:R(?:ICTIONS)?)?:?)\s*'  # Matches REST, RESTR, RESTRICTIONS, etc.
    r'([A-Z0-9]{1,4}|(?i)none)' 
  # Matches REST or RESTRICTIONS followed by optional colon and spaces, capturing the restrictions
)
,  # Pattern for restrictions
    'Replaced': (
    r'(?i)'  # Case insensitive
    r'(?:REPLAC[EA]D)[:\s]*'  # Handles REPLACED, REPLACE DATE, REPLACD, etc., with optional colon and spaces
    r'('
    r'(\d{2}[-/.\s]{0,3}\d{2}[-/.\s]{0,3}\d{2,4})|'  # Matches dates like 12/31/2024, 12-31-24, 12.31.2024, etc.
    r'(\d{4}[-/.\s]{0,3}\d{2}[-/.\s]{0,3}\d{2})|'  # Matches ISO dates like 2024-12-31
    r'(\d{2}[-/.\s]{0,3}(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-/.\s]{0,3}\d{2,4})|'  # Matches dates like 31 Dec 2024, 31-Dec-24, etc.
    r'((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-/.\s]{0,3}\d{2}[-/.\s]{0,3},?[-/.\s]{0,3}\d{2,4})'  # Matches dates like Dec 31, 2024, Dec-31-24, etc.
    r')'
)
,  # Pattern for replaced date with variations  # Pattern for name + date of birth
  # Pattern for expiry date
       # Pattern for sex
     # Pattern for weight
   'License Number':  (r'(?i)('
    r'Lic\s*[#:.\-]?\s*\d{9}\s*|'  # LIC 123456789
    r'(?:DLN|DIN|AIN)?\s*[A-Z]\d{3}[\s.\-]?\d{3}[\s.\-]?\d{2}[\s.\-]?\d{3}[\s.\-]?\d|'  # DLN A123-456-78-901-2
    r'NO[.\s]*\s*?0?\d{7}\s*|'  # NO. 1234567 (or with OCR error as NO. O1234567)
    r'4[da]\s*0?\d{7}\s*|'  # 4d 7158184 (or OCR error as 4d 0158184)
    r'DLN\s*[A-Z0-9]+\s*|'  # DLN D08954796
    r'DL\s*[I1O0]\d{7}\s*|'  # DL I1234568 (or OCR errors as DL 01234568 or DL L1234568)
    r'LIC\s*[#:;.\-]?\s*0?\d{6,9}\s*|'  # LIC#: 787878787 (or OCR error as LIC: 078787878)
    r'DL\s*NO[.\s]*\s*\d{8,12}\s*|'  # DL NO. 98765438
    r'S\s*?\d{3}[\s.\-]?\d{3}[\s.\-]?\d{2}[\s.\-]?\d{3}[\s.\-]?\d\s*|'  # S514-172-80-844-0
    r'DL\s*NO[.\s]*\s*0?\d{9}\s*|'  # DL NO. 999999999 (or OCR error as DL NO. 099999999)
    r'LIC\s*NO[.\s]*\s*[A-Z0-9]{3}[\s.\-]?\d{4}[\s.\-]?\d{4}\s*|'  # LIC NO: P142-4558-7924
    r'4[da]\s*DLN\s*\d{4}[\s.\-]?\d{2}[\s.\-]?\d{4}\s*|'  # 4d DLN 1234-56-7890
    r'DLN\s*\d{4}[\s.\-]?\d{2}[\s.\-]?\d{3}\s*|'  # DLN 1234-56-890
    r'DLN\s*\d{3}XX\d{4}\s*|'  # DLN 123XX6789
    r'LIC\s*\.?#?\s*NO[.\s]*\s*[A-Z0-9]{3}[\s.\-]?\d{2}[\s.\-]?\d{4}\s*|'  # LIC. NO. K01-75-4269
    r'4[da]\s*DLN\s*[A-Z0-9]{3}[\s.\-]?\d{3}[\s.\-]?\d{3}\s*|'  # 4d DLN S00-000-001
    r'DL\s*NO[.\s]*\s*0?\d{7}\s*|'  # DL NO. 1234567 (or OCR error as DL NO. 01234567)
    r'S[\s.\-]?\d{3}[\s.\-]?\d{3}[\s.\-]?\d{3}[\s.\-]?\d{3}\s*|'  # CUSTOMER IDENTIFIER S-000-000-000-000
    r'NUMBER\s*[A-Z0-9]+\s*|'  # NUMBER S99988801
    r'DL#?\s*[A-Z]\d{3}[\s.\-]?\d{3}[\s.\-]?\d{3}[\s.\-]?\d{3}\s*|'  # DL# A123-456-789-123
    r'DL\s*NO[.\s]*\s*\d{12}\s*|'  # DL NO. 123456789123
    r'LICENSE\s*#?[.\s]*\s*\d{9}\s*'  # LICENSE #123456789
    r')'
)

}
