# mapitem.py
# general class for how MapPLZ represents points, lines, polygons
# FreeBSD license - by Nick Doiron (@mapmeld)

import geojson


class MapItem(dict):
    def __init__(self, db=None, **kwargs):
        self.db = db
        self["properties"] = {}
        for key, value in kwargs.iteritems():
            if key in ["lat", "lng"]:
                self[key] = float(value)
            elif key == "path":
                self["path"] = value
            else:
                self["properties"][key] = value

    def type(self):
        if "lat" in self.keys() and "lng" in self.keys():
            return "point"
        else:
            try:
                if self["path"][0][0] == float(self["path"][0][0]):
                    return "line"
            except:
                return "polygon"

    def delete(self):
        db.delete(self)

    def toGeoJson(self):
        if self.type() == "point":
            return geojson.point(lat(), lng())

    def properties(self):
        return self["properties"]

    def lat(self):
        return self["lat"]

    def lng(self):
        return self["lng"]

    def path(self):
        return self["path"]
