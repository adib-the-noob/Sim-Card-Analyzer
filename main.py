import phonenumbers
from number import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

# location
phone_number = phonenumbers.parse(number)
location = geocoder.description_for_number(phone_number, "en")
print(location)

# service_name
service_name = phonenumbers.parse(number)
print(carrier.name_for_number(service_name, "en"))

# geolocation
geocoder = OpenCageGeocode(key="#Log in to opencage and give the key here")

query = str(location)
result = geocoder.geocode(query)
# print(result)

# setting up location
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat, lng)

# map
myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

# save map in html file
myMap.save("location.html")
