import folium
map = folium.Map(location=[51.753501, -1.256884], zoom_start=100, tiles="Stamen Terrain")
features = folium.FeatureGroup(name="My Map1")

features.add_child(folium.Marker(location=[51.753501, -1.256884], popup="Jesus College", icon=folium.Icon(color="red")))

map.add_child(features)
map.save("Map1.html")
