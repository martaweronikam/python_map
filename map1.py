import folium
import pandas

## here we read in the file with the universities and prepare our lists
data = pandas.read_csv("unis.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
country = list(data["COUNTRY"])

## here i decided to play a bit with the colours - in the original project the instructor divided the volcanoes
## by elevation, but that obviously was not going to work here
def color_play(country_name):
    if country_name == "UK":
        return "blue"
    elif country_name == "China":
        return "green"
    elif country_name == "Singapore":
        return "purple"
    else:
        return "red"

## here we create the map
map = folium.Map(location=[51.753501, -1.256884], zoom_start=3, tiles="OpenStreetMap")

## taking care of all the features of the university layer
features_universities = folium.FeatureGroup(name="Universities")
for lt, ln, nm, ct in zip(lat, lon, name, country):
    features_universities.add_child(folium.Marker(location=[lt, ln], popup=nm, icon=folium.Icon(color_play(ct))))

features_population = folium.FeatureGroup(name="Population")
## taking care of all the features of the population layer
## reading in the json file
features_population.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
style_function = lambda x: {"fillColor" : "green" if x["properties"]["POP2005"] < 10000000 else "orange" if 10000000 <= x["properties"]["POP2005"] < 100000000 else "red"}))

## here we update the map to look as we want to
map.add_child(features_universities)
map.add_child(features_population)

## adding layer control
map.add_child(folium.LayerControl())

map.save("Map1.html")
