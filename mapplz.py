# mapplz.py
# base class for MapPLZ-Python
# FreeBSD license - by Nick Doiron (@mapmeld)

import sys
import geojson

from mapitem import MapItem

class MapPLZ:
    def __init__(self, db = None):
        self.db = db

    def add(self, *args, **kwargs):
        if len(args) == 0:
            try:
                # (lat=LAT, lng=LNG, prop=PROP)
                lat = float(kwargs["lat"])
                lng = float(kwargs["lng"])
                madeItem = MapItem(db=self.db, lat=lat, lng=lng)
                for key, value in kwargs.iteritems():
                    if key not in ["lat", "lng"]:
                        madeItem[key] = value
                return madeItem
            except:
                k = 1
        elif len(args) == 1:
            try:
                # (lat, lng)
                latlng = args[0]
                lat = float(latlng[0])
                lng = float(latlng[1])
                return MapItem(db=self.db, lat=lat, lng=lng)
            except:
                try:
                    # ([lat, lng])
                    latlng = args[0]
                    lat = float(latlng["lat"])
                    lng = float(latlng["lng"])
                    madeItem = MapItem(db=self.db, lat=lat, lng=lng)
                    for key, value in latlng.iteritems():
                        if key not in ["lat", "lng"]:
                            madeItem[key] = value
                    return madeItem
                except:
                    try:
                        # ({ "type": "Feature", "geometry": { GEOJSON } })
                        # or str() of that
                        gj = args[0]
                        if gj == str(gj):
                            gj = geojson.loads(gj)
                        if gj["type"] == "FeatureCollection":
                            mapitems = []
                            for feature in gj["features"]:
                                mapitems.append(self.add(feature))
                            return mapitems
                        elif gj["type"] == "Feature":
                            madeItem = MapItem(db=self.db)
                            if gj["geometry"]["type"] == "Point":
                                madeItem["lat"] = float(gj["geometry"]["coordinates"][1])
                                madeItem["lng"] = float(gj["geometry"]["coordinates"][0])
                            else:
                                madeItem["path"] = self.reverse_path(gj["geometry"]["coordinates"])
                            return madeItem
                    except:
                        k = 1
        elif len(args) == 2:
            try:
                lat = float(args[0])
                lng = float(args[1])
                return MapItem(db=self.db, lat=lat, lng=lng)
            except:
                k = 1

    def count(self, **conditions):
        k = 1

    def query(self, **conditions):
        k = 1

    def nearest(self, **conditions):
        k = 1

    def within(self, **conditions):
        k = 1

    def reverse_path(self, coords):
        index = 0
        for point in path:
            try:
                lat = float(point[1])
                lng = float(point[0])
                point[index][0] = lat
                point[index][1] = lng
            except:
                path[index] = reverse_path(point)
            return path
