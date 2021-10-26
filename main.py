# pip install folium
import folium

map = folium.Map(
    location = [],
    titles = '',
    zoom_start = 15
)

folium.Market(
    [],
    popup = '<i>Name</i>',
    tooltip = ''
).add_to(map)

map.save('E:\Documents')