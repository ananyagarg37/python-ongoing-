import phonenumbers
from opencage.geocoder import OpenCageGeocoder

# Replace with your OpenCage API key
API_KEY = 'YOUR_OPENCAGE_API_KEY'
geocoder = OpenCageGeocoder(API_KEY)

def get_location(phone_number):
    parsed_number = phonenumbers.parse(phone_number)
    country_code = phonenumbers.region_code_for_number(parsed_number)
    geocode_result = geocoder.geocode(country_code)
    if geocode_result:
        return geocode_result[0]['geometry']['lat'], geocode_result[0]['geometry']['lng']
    return None

phone_number = input("Enter phone number: ")
location = get_location(phone_number)

if location:
    print(f"Latitude: {location[0]}, Longitude: {location[1]}")
else:
    print("Location could not be determined.")
