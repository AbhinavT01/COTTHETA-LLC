import usaddress

def parse_address(address_string):
    parsed_address = usaddress.parse(address_string)
    
    building_number = ''
    street = ''
    street_type = ''
    direction = ''
    city = ''
    state = ''
    zip_code = ''

    for component, component_type in parsed_address:
        if component_type == 'AddressNumber':
            building_number = component
        elif component_type == 'StreetName':
            street = component
        elif component_type == 'StreetNamePostType':
            street_type = component
        elif component_type == 'StreetNamePostDirectional':
            direction = component
        elif component_type == 'PlaceName':
            city = component
        elif component_type == 'StateName':
            state = component
        elif component_type == 'ZipCode':
            zip_code = component

    # Concatenate the street components
    street_full = ' '.join(filter(None, [building_number, street, street_type, direction]))

    return {
        "building_number": building_number.strip(),
        "street": street.strip(),
        "street_type": street_type.strip(),
        "direction": direction.strip(),
        "city": city.strip(),
        "state": state,
        "zip_code": zip_code,
        "street_full": street_full.strip()
    }

# if __name__ == "__main__":
    # address_string = "SAMPLEColonel Hugh B. McCallDirector of Public SafetyDRIVER LICENSEALABAMANO.1234567CLASS DD.O.B. 01-05-1948 EXP 01-05-2014CONNORSAMPLE1 WONDERFUL DRIVEMONTGOMERY AL 36104-1234ENDORSEMENTSISS 01-05-2010RESTRICTIONS ASEX M HT 5-05 EYES BLUWT 120 HAIR BLNConnor Sample SAMPLE Colonel Hugh B. McCall Director of Public Safety DRIVER LICENSE ALABAMA NO.1234567 CLASS D D.O.B. 01-05-1948 EXP 01-05-2014 CONNOR 1 WONDERFUL DRIVE MONTGOMERY AL 36104-1234 ENDORSEMENTS ISS 01-05-2010 RESTRICTIONS A SEX M HT 5-05 EYES BLU WT 120 HAIR BLN Connor Sample"
    # parsed_address = parse_address(address_string)
    
    # print("Street:", parsed_address["street"])
    # print("City:", parsed_address["city"])
    # print("State:", parsed_address["state"])
    # print("Zip Code:", parsed_address["zip_code"])
