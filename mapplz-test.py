# mapplz-test.py
# base testing class for MapPLZ-Python
# FreeBSD license - by Nick Doiron (@mapmeld)

import unittest
from mapplz import MapPLZ

class TestWithoutDB(unittest.TestCase):
    def setUp(self):
        self.mapstore = MapPLZ()

    def test_add_pt_lat_lng(self):
        pt = self.mapstore.add(40, -70)
        self.assertTrue(pt.lat() == 40)
        self.assertTrue(pt.lng() == -70)
        self.assertTrue(pt["lat"] == 40)
        self.assertTrue(pt["lng"] == -70)

    def test_add_pt_latlng(self):
        pt = self.mapstore.add([40, -70])
        self.assertTrue(pt.lat() == 40)
        self.assertTrue(pt.lng() == -70)

    def test_add_pt_latlng_dict(self):
        pt = self.mapstore.add({ "lat": 40, "lng": -70 })
        self.assertTrue(pt.lat() == 40)
        self.assertTrue(pt.lng() == -70)

    def test_add_pt_by_geojson_dict(self):
        pt = self.mapstore.add({ "type": "Feature", "geometry": { "type": "Point", "coordinates": [-70, 40] } })
        self.assertTrue(pt.lat() == 40)
        self.assertTrue(pt.lng() == -70)

    def test_add_pt_by_geojson_string(self):
        pt = self.mapstore.add('{ "type": "Feature", "geometry": { "type": "Point", "coordinates": [-70, 40] } }')
        self.assertTrue(pt.lat() == 40)
        self.assertTrue(pt.lng() == -70)

    def test_add_pt_latlng_kwargs(self):
        pt = self.mapstore.add(lat=40, lng=-70)
        self.assertTrue(pt.lat() == 40)
        self.assertTrue(pt.lng() == -70)

if __name__ == "__main__":
    unittest.main()
