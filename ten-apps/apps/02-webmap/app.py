import folium
import pandas


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation < 3000:
        return 'orange'
    else:
        return 'red'


def main():
    data = pandas.read_csv('Volcanoes.txt')
    lat = list(data['LAT'])
    lon = list(data['LON'])
    elev = list(data['ELEV'])

    map_f = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles='Mapbox Bright')
    fgv = folium.FeatureGroup(name='Volcanoes')
    fgp = folium.FeatureGroup(name='Population')

    for lt, ln, el in zip(lat, lon, elev):
        popup = str(el) + ' meters'
        # popup = folium.Popup(str(el), parse_htmp=True)) se tivesse aspas simples na string
        # fg.add_child(folium.Marker(location=[lt, ln], popup=popup, icon=folium.Icon(color=color_producer(el))))
        fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=popup, fill_color=color_producer(el), color='grey', fill=True, fill_opacity=0.7))

    fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                                style_function=lambda pol: {'fillColor': 'green' if pol['properties']['POP2005'] < 10000000
                                else 'orange' if pol['properties']['POP2005'] < 20000000 else 'red'}))

    map_f.add_child(fgv)
    map_f.add_child(fgp)
    map_f.add_child(folium.LayerControl())
    map_f.save('Map1.html')


main()
