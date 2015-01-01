# mapitem.py
# general class for how MapPLZ represents points, lines, polygons
# FreeBSD license - by Nick Doiron (@mapmeld)

class MapItem(dict):
    def __init__(self, db=None, **kwargs):
        self.db = db
        for key, value in kwargs.iteritems():
            if key in ["lat", "lng"]:
                self[key] = float(value)
            else:
                self[key] = value

    def properties(self):
        # TODO: remove lat, lng, other non-attribute properties from dict
        return self

    def type(self):
        return self["type"]

    def lat(self):
        return self["lat"]

    def lng(self):
        return self["lng"]

    def path(self):
        return self["path"]
