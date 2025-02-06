# import phonenumbers
# from opencage.geocoder import OpenCageGeocoder

# # Replace with your OpenCage API key
# API_KEY = 'YOUR_OPENCAGE_API_KEY'
# geocoder = OpenCageGeocoder(API_KEY)

# def get_location(phone_number):
#     parsed_number = phonenumbers.parse(phone_number)
#     country_code = phonenumbers.region_code_for_number(parsed_number)
#     geocode_result = geocoder.geocode(country_code)
#     if geocode_result:
#         return geocode_result[0]['geometry']['lat'], geocode_result[0]['geometry']['lng']
#     return None

# phone_number = input("Enter phone number: ")
# location = get_location(phone_number)

# if location:
#     print(f"Latitude: {location[0]}, Longitude: {location[1]}")
# else:

#     print("Location could not be determined.")

import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder as phone_geocoder
from opencage.geocoder import OpenCageGeocode

# Replace with your OpenCage API key
API_KEY = '1671668ae39f44aa8f86ab5e518f9352'
geocoder = OpenCageGeocode(API_KEY)

def get_location(phone_number, default_region):
    try:
        parsed_number = phonenumbers.parse(phone_number, default_region)
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        print(f"Formatted Number: {formatted_number}")  # Debugging
        location_description = phone_geocoder.description_for_number(parsed_number, "en")
        carrier_name = carrier.name_for_number(parsed_number, "en")
        print(f"Carrier: {carrier_name}, Location Description: {location_description}")  # Debugging
        
        geocode_result = geocoder.geocode(location_description)
        if geocode_result:
            components = geocode_result[0]['components']
            country = components.get('country', 'Country not found')
            state = components.get('state', 'State not found')
            latitude = geocode_result[0]['geometry']['lat']
            longitude = geocode_result[0]['geometry']['lng']
            return country, state, latitude, longitude, carrier_name
        else:
            print("No geocode result found")  # Debugging
    except Exception as e:
        print(f"Error: {e}")  # Debugging
    return None

phone_number = input("Enter phone number: ")
default_region = input("Enter default region (e.g., IN for India): ")
location = get_location(phone_number, default_region)

if location:
    country, state, latitude, longitude, carrier_name = location
    print(f"Country: {country}, State: {state}, Latitude: {latitude}, Longitude: {longitude}, Carrier: {carrier_name}")
else:
    print("Location could not be determined.")
