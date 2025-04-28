from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

geolocator = Nominatim(user_agent="my_app")
location = geolocator.reverse((40.748817, -73.985428))
print(location.address)
print()




############ Paris Location #############
location = geolocator.reverse((48.858370, 2.294481))
print(location.address)
print()

## Reverse example

# Very important: give a real identifiable user_agent (e.g., your email or project name)
geolocator = Nominatim(user_agent="your_real_app_name_or_email@example.com")

def do_geocode(address):
    try:
        location = geolocator.geocode(address, timeout=10)
        if location:
            print("Address found:")
            print(location.address)
            print("Coordinates:", (location.latitude, location.longitude))
        else:
            print("Address not found.")
    except GeocoderTimedOut:
        print("Error: geocoding service timed out. Try again later.")
    except GeocoderServiceError as e:
        print(f"Service error: {e}")

# Your address
address = "Champ de Mars, Allée Thomy Thierry, Quartier du Gros-Caillou, Paris 7e Arrondissement, Paris, France métropolitaine, 75007, France"
do_geocode(address)
print(Nominatim)
print()


