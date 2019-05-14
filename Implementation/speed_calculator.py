import fiona
import sys
import time
import pandas as pd
import geopy.distance as ds
import geopandas as gpd


with fiona.open('./shapefiles/Como_dataset.shp') as np:
    meta = np.meta
    timezones = []
    print("Recupero time_zones...")
    for feature in np:
        # aggiungo colonna speed
        feature['properties']['speed'] = 'float'
        #recupero tutti i timezone e li salvo in una lista
        timezone = feature['properties']['time_zone']
        if timezone not in timezones:
            timezones.append(timezone)

    print("Stampo i path...")
    paths = []
    n = 0
    for tz in timezones:
        print("Percorso " + str(n))
        n+=1
        path = filter(lambda f: f['properties']['time_zone'] == tz, np)
        path = list(path)
        # print(path[0])
        # esempio struttura
        # {'type': 'Feature', 'id': '0', 'properties': OrderedDict([('ts', 1460114897392.0), ('time_zone', '2016-04-08 11:28:14.000000'), ('location', 'Como'), ('latitude', 45.80360806110678), ('longitude', 9.094291062725679), ('tr_point', '0101000020E61000007B6C0DEB46302240B7A002A1DCE64640')]), 'geometry': {'type': 'Point', 'coordinates': (9.094291062725679, 45.80360806110678)}}
        prev_geom = None
        prev_time = 0.0
        for i in range(len(path)):
            curr_geom = path[i]['geometry']['coordinates']
            curr_time = path[i]['properties']['ts']
            distance = 0.0
            speed = 0.0
            if i > 0:
                distance = ds.distance(curr_geom, prev_geom).meters
                speed = distance / ((curr_time - prev_time) / 1000)
            path[i]['properties']['speed'] = speed

            # print('')
            # print("Distanza: " + str(distance) + ' m')
            # print("Tempo: " + str(curr_time) + ' ms')
            # print("Delta Tempo: " + str((curr_time - prev_time) / 1000) + ' s')
            # print("Velocità: " + str(path[i]['properties']['speed']) + ' m/s')
            prev_geom = curr_geom
            prev_time = curr_time
            paths.append(path[i])
        # break

print(paths)
# gdf = gpd.GeoDataFrame(paths)
# gdf.to_file(driver = 'ESRI Shapefile', filename = './shapefiles/speedy_Como_dataset.shp')



    # with fiona.open('./shapefiles/speedy_Como_dataset.shp', 'w', **meta) as  output:
    #     pass
