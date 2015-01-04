# mapplz.py
# base class for MapPLZ-Python
# FreeBSD license - by Nick Doiron (@mapmeld)

import sys
import json
import geojson

from mapitem import MapItem


class MapPLZ:
    def __init__(self, db=None):
        self.db = db

    def add(self, *args, **kwargs):
        if len(args) == 0:
            try:
                # (lat=LAT, lng=LNG, PROPS)
                lat = float(kwargs["lat"])
                lng = float(kwargs["lng"])
                madeItem = MapItem(db=self.db, lat=lat, lng=lng)
                for key, value in kwargs.iteritems():
                    if key not in ["lat", "lng"]:
                        madeItem["properties"][key] = value
                return madeItem
            except:
                raise MapPLZUnparsedException()

        elif len(args) == 1:
            try:
                # [lat, lng]
                latlng = args[0]
                lat = float(latlng[0])
                lng = float(latlng[1])
                return self.add(lat, lng, *args[0][2:])
            except:
                try:
                    # ({ lat, lng, props })
                    latlng = args[0]
                    lat = float(latlng["lat"])
                    lng = float(latlng["lng"])
                    return self.add(lat, lng, latlng)
                except:
                    try:
                        # ({ "type": "Feature", "geometry": { GEOJSON } })
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
                            geom = gj["geometry"]
                            if geom["type"] == "Point":
                                lat = float(geom["coordinates"][1])
                                lng = float(geom["coordinates"][0])
                                madeItem["lat"] = lat
                                madeItem["lng"] = lng
                            else:
                                path = self.reverse_path(geom["coordinates"])
                                madeItem["path"] = path
                            return madeItem
                    except:
                        try:
                            # ([[lat1, lng1], [lat2, lng2]])
                            line = args[0]
                            path = []
                            for pt in line:
                                path.append([float(pt[0]), float(pt[1])])
                            return MapItem(db=self.db, path=path)
                        except:
                            try:
                                line = args[0]
                                path = []
                                for pt in line:
                                    lat = float(pt["lat"])
                                    lng = float(pt["lng"])
                                    path.append([lat, lng])
                                return self.add(path)
                            except:
                                try:
                                    path = args[0]["path"]
                                    madeItem = self.add(path)
                                    for key, value in args[0].iteritems():
                                        if key not in ["lat", "lng", "path"]:
                                            madeItem["properties"][key] = value
                                    return madeItem
                                except:
                                    raise MapPLZUnparsedException()
        elif len(args) == 2:
            try:
                # (lat, lng)
                lat = float(args[0])
                lng = float(args[1])
                return MapItem(db=self.db, lat=lat, lng=lng)
            except:
                try:
                    # ([lat, lng], PROPS)
                    latlng = args[0]
                    lat = float(latlng[0])
                    lng = float(latlng[1])
                    return self.add(lat, lng, *args[1:])
                except:
                    try:
                        # ({lat: LAT, lng: LNG}, PROPS)
                        latlng = args[0]
                        lat = float(latlng["lat"])
                        lng = float(latlng["lng"])
                        return self.add(lat, lng, args[1:])
                    except:
                        try:
                            # (path, props)
                            props["path"] = args[0]
                            return self.add(props)
                        except:
                            raise MapPLZUnparsedException()
        elif len(args) == 3:
            try:
                lat = float(args[0])
                lng = float(args[1])
                madeItem = MapItem(db=self.db, lat=lat, lng=lng)
                props = args[2]
                try:
                    # (lat, lng, { json })
                    for key, value in props.iteritems():
                        if key not in ["lat", "lng"]:
                            madeItem["properties"][key] = value
                    return madeItem
                except:
                    try:
                        # (lat, lng, '{ json }')
                        props = json.loads(args[2])
                        for key, value in props.iteritems():
                            if key not in ["lat", "lng"]:
                                madeItem["properties"][key] = value
                        return madeItem
                    except:
                        # (lat, lng, key_prop)
                        madeItem["properties"]["property"] = args[2]
                        return madeItem
            except:
                raise MapPLZUnparsedException()

    def count(self, **conditions):
        raise MapPLZUnparsedException()

    def query(self, **conditions):
        raise MapPLZUnparsedException()

    def nearest(self, **conditions):
        raise MapPLZUnparsedException()

    def within(self, **conditions):
        raise MapPLZUnparsedException()

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


class MapPLZUnparsedException(Exception):
    def __init__(self):
        k = 2
