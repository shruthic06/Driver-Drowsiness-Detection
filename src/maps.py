#GEOCODE FORMULA
import geopy

def location():
    from geopy import Nominatim
    geolocator= Nominatim(user_agent=input('enter your name'))
    location = geolocator.geocode(input('enter your location'))
    return location.latitude, location.longitude
print('latitude','longitude',location())


