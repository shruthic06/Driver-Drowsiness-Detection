#GEOCODE FORMULA
import geopy

def location():
    from geopy import Nominatim
    geolocator= Nominatim(user_agent=input('enter your name'))
    location = geolocator.geocode(input('enter your location'))
    return location.latitude, location.longitude


#HAVERSINE FORMULA
import math

lat1,long1,lat2,long2=2.8,4.5,3.6,8.9
def distance():
    global lat1,long1,lat2,long2
    lat1,long1=location()
    lat2,long2=location()
    radius=6371 #km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(long2-long1)

    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1))* math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

print(distance(),"km")

# import gmplot package
import gmplot
#Set different latitude and longitude points
lat, long = zip(*[
   (lat1,long1),(lat2,long2)])
#declare the center of the map, and how much we want the map zoomed in
gmap3 = gmplot.GoogleMapPlotter(lat1,long1, 13)
# Scatter map
gmap3.scatter( lat, long, '#FF0000',size = 50, marker = False )
# Plot method Draw a line in between given coordinates
gmap3.plot(lat, long , 'cornflowerblue', edge_width = 3.0)
# save it to html
gmap3.draw(r"c:\users\Shruthi\desktop\map.html")





