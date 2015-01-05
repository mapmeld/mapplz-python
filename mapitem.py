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
        g = None
        if self.type() == "point":
            g = geojson.Point((self.lng(), self.lat()))
        elif self.type() == "line":
            linepts = []
            for pt in self.path():
                linepts.append((pt[1], pt[0]))
            g = geojson.LineString(linepts)
        elif self.type() == "polygon":
            linepts = []
            for ring in self.path():
                ringpts = []
                for pt in ring:
                    ringpts.append((pt[1], pt[0]))
                linepts.append(ringpts)
            g = geojson.Polygon(linepts)
        if g is not None:
            feature = geojson.Feature(geometry=g, properties=self.properties())
            return geojson.dumps(feature, sort_keys=True)

    def properties(self):
        return self["properties"]

    def lat(self):
        return self["lat"]

    def lng(self):
        return self["lng"]

    def path(self):
        return self["path"]
