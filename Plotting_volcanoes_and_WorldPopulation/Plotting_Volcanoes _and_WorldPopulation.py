import folium as fp 
import pandas as pd
import json
#volcanoes.csv code
df1=pd.read_csv("Volcanoes.csv")
lat1=list(df1["LAT"])
lon1=list(df1["LON"])
elev1=list(df1["ELEV"])
name1=list(df1["NAME"])

fgv1=fp.FeatureGroup(name="Volcano Map")
map=fp.Map(location=[48.58,-121.09],tiles="Stamen Terrain",zoom_start=6)
#function that gives icon a color based on elevation
def color_producer(elevation):
    if elevation <1000:
        return 'green'
    elif 1000 <= elevation < 2000:
        return 'orange'
    else:
        return 'red'
    
for lt, ln, el,nm in zip(lat1,lon1,elev1, name1):       #zip function adds two lists together in one for loop
    disp_name_elev=" ".join([nm,str(el)+"m"])        #to display name and elevation in same pop up icon
    fgv1.add_child(fp.CircleMarker(location=[lt,ln],radius=6,popup=disp_name_elev,fill_color=color_producer(el),color='black',fill_opacity=0.7,parse_html=True))

#world.json code
fgp1=fp.FeatureGroup(name="Population Map")
fgp1.add_child(fp.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 20000000 else 'green' 
if 20000000 <= x['properties']['POP2005'] < 50000000 else 'orange' if 50000000 <= x['properties']['POP2005'] < 100000000
else 'red'})) #style functions expects a lambda function


map.add_child(fgv1)
map.add_child(fgp1)
map.add_child(fp.LayerControl()) #it looks to objects at child
map.save("Volcanoes America and world population.html")
